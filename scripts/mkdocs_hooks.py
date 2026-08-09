"""MkDocs hooks for local development and governance.

Ensures cross-platform reliability for live reloading on macOS by configuring
watchdog to use PollingObserver during `mkdocs serve`. Also filters tech-blog
posts so that only articles with frontmatter `status: approved` are published,
and maps `pubDate` to `date` dynamically for MkDocs Material blog compatibility.
"""

from __future__ import annotations

import os
import re
import yaml
import platform
import watchdog.observers
import watchdog.observers.polling
from mkdocs.structure.files import Files, InclusionLevel
import material.plugins.blog.structure as blog_struct
import material.plugins.blog.plugin as blog_plugin_mod

# Patch Material for MkDocs Post.__init__ so pubDate is dynamically mapped to date
_orig_post_init = blog_struct.Post.__init__


def _patched_post_init(self, file, config):
    _orig_yaml_load = yaml.load

    def _yaml_load_with_pubdate(stream, Loader):
        res = _orig_yaml_load(stream, Loader)
        if isinstance(res, dict) and "pubDate" in res and "date" not in res:
            res["date"] = res["pubDate"]
        return res

    yaml.load = _yaml_load_with_pubdate
    try:
        _orig_post_init(self, file, config)
    finally:
        yaml.load = _orig_yaml_load


blog_struct.Post.__init__ = _patched_post_init

# Patch Material for MkDocs BlogPlugin._resolve_posts so blog posts maintain NOT_IN_NAV inclusion level
_orig_resolve_posts = blog_plugin_mod.BlogPlugin._resolve_posts


def _patched_resolve_posts(self, files, config):
    for post in _orig_resolve_posts(self, files, config):
        post.file.inclusion = InclusionLevel.NOT_IN_NAV
        yield post


blog_plugin_mod.BlogPlugin._resolve_posts = _patched_resolve_posts


# On macOS (Darwin), FSEventsObserver can stall or miss events in subshells
# or IDE terminals. Fallback to PollingObserver to guarantee reliable file watching.
if platform.system() == "Darwin":
    watchdog.observers.Observer = watchdog.observers.polling.PollingObserver


def on_files(files: Files, config: dict) -> Files:
    """Filter out tech-blog markdown files that do not have status: approved in frontmatter."""
    filtered_files = []
    docs_dir = config.get("docs_dir", "docs")

    for file in files:
        # Only inspect markdown files inside tech-blog directory (excluding index.md)
        if file.src_path.startswith("tech-blog/") and not file.src_path.endswith("index.md") and file.src_path.endswith(".md"):
            full_path = os.path.join(docs_dir, file.src_path)
            if os.path.exists(full_path):
                with open(full_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
                if match:
                    try:
                        frontmatter = yaml.safe_load(match.group(1)) or {}
                        status = str(frontmatter.get("status", "")).strip().lower()
                        if status == "approved":
                            filtered_files.append(file)
                            continue
                    except Exception:
                        pass
                # If missing frontmatter or status is not 'approved', exclude from build files
                continue

        filtered_files.append(file)

    return Files(filtered_files)


def on_page_read_source(page, config: dict) -> str | None:
    """Dynamically inject date: <pubDate> into in-memory markdown source if date is missing."""
    docs_dir = config.get("docs_dir", "docs")
    full_path = os.path.join(docs_dir, page.file.src_path)

    if page.file.src_path.startswith("tech-blog/") and os.path.exists(full_path):
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()

        match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
        if match:
            try:
                frontmatter = yaml.safe_load(match.group(1)) or {}
                if "pubDate" in frontmatter and "date" not in frontmatter:
                    frontmatter["date"] = frontmatter["pubDate"]
                    new_yaml = yaml.dump(frontmatter, sort_keys=False)
                    return f"---\n{new_yaml}---\n{content[match.end():]}"
            except Exception:
                pass
        return content

    return None
