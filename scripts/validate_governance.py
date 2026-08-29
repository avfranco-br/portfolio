import os
import re
import yaml
import sys
import argparse

def validate_terminology(policy_path, docs_dir):
    with open(policy_path, 'r') as f:
        policy = yaml.safe_load(f)
    
    canonical_terms = policy.get('canonical_terms', {})
    
    findings = []
    
    for root, _, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Strip fenced code blocks to avoid false positives in code.
                content = re.sub(r'```.*?```', lambda m: '\n' * m.group(0).count('\n'), content, flags=re.DOTALL)
                content = re.sub(r'~~~.*?~~~', lambda m: '\n' * m.group(0).count('\n'), content, flags=re.DOTALL)
                content = re.sub(r'`.*?`', '', content)
                
                # Strip markdown link targets to avoid false positives in URLs
                content = re.sub(r'(\[.*?\])\(.*?\)', r'\1()', content)
                    
                for canonical, details in canonical_terms.items():
                    rejected_variants = details.get('reject', [])
                    for variant in rejected_variants:
                        pattern = r'\b' + re.escape(variant) + r'\b'
                        matches = list(re.finditer(pattern, content, re.IGNORECASE))
                        if matches:
                            for match in matches:
                                line_no = content.count('\n', 0, match.start()) + 1
                                findings.append({
                                    'file': os.path.relpath(file_path, docs_dir),
                                    'line': line_no,
                                    'found': match.group(),
                                    'preferred': canonical
                                })
    
    return findings

def validate_frontmatter_status(tech_blog_dir):
    findings = []
    if not os.path.exists(tech_blog_dir):
        return findings

    valid_statuses = {'approved', 'draft', 'review'}

    for root, _, files in os.walk(tech_blog_dir):
        for file in files:
            if file.endswith('.md') and file != 'index.md':
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
                if not match:
                    findings.append({
                        'file': os.path.relpath(file_path, tech_blog_dir),
                        'issue': "Missing YAML frontmatter block"
                    })
                    continue

                try:
                    frontmatter = yaml.safe_load(match.group(1)) or {}
                except Exception as e:
                    findings.append({
                        'file': os.path.relpath(file_path, tech_blog_dir),
                        'issue': f"Invalid YAML frontmatter: {e}"
                    })
                    continue

                status = frontmatter.get('status')
                if not status:
                    findings.append({
                        'file': os.path.relpath(file_path, tech_blog_dir),
                        'issue': "Missing required 'status' attribute in frontmatter (defaulting to draft)"
                    })
                elif status not in valid_statuses:
                    findings.append({
                        'file': os.path.relpath(file_path, tech_blog_dir),
                        'issue': f"Invalid status '{status}' (must be one of: {', '.join(sorted(valid_statuses))})"
                    })

    return findings

def get_canonical_banner(rel_path):
    """Return the canonical banner string for a given relative path under docs/."""
    rel_path_str = rel_path.replace("\\", "/")
    if rel_path_str.startswith("sop/") or rel_path_str.startswith("narratives/cas"):
        return "> [!IMPORTANT]\n> **Classification Level**: `RESTRICTED / HIGHLY CONFIDENTIAL` — Alexandre Franco Enterprise Architecture Portfolio."
    elif rel_path_str.startswith("narratives/"):
        return "> [!NOTE]\n> **Classification Level**: `CONFIDENTIAL - CLIENT CASE STUDY` — Alexandre Franco Enterprise Architecture Portfolio."
    elif rel_path_str.startswith("tech-blog/"):
        return "> [!NOTE]\n> **Classification Level**: `PUBLIC - THOUGHT LEADERSHIP` — Alexandre Franco Enterprise Architecture Portfolio."
    else:
        return "> [!NOTE]\n> **Classification Level**: `PUBLIC` — Alexandre Franco Enterprise Architecture Portfolio."

def get_canonical_footer():
    return "*© 2026 Alexandre Franco. Ideas-to-Life. All rights reserved.*"

def validate_ip_governance(docs_dir, fix=False):
    findings = []
    if not os.path.exists(docs_dir):
        return findings

    copyright_regex = re.compile(r'(©|\bCopyright\b|Alexandre Franco.*Ideas.*Life|All rights reserved)', re.IGNORECASE)
    classification_banner_regex = re.compile(r'>\s*\[!(NOTE|IMPORTANT|WARNING|TIP|CAUTION)\]\s*\n>\s*\*\*Classification Level\*\*:\s*`?[A-Za-z0-9 _/\-]+`?', re.IGNORECASE)

    for root, _, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, docs_dir).replace("\\", "/")

                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Separate frontmatter if present
                fm_match = re.match(r'^(---\s*\n.*?\n---\s*\n?)', content, re.DOTALL)
                if fm_match:
                    frontmatter = fm_match.group(1)
                    body = content[len(frontmatter):]
                else:
                    frontmatter = ""
                    body = content

                has_banner = bool(classification_banner_regex.search(body[:500]) or classification_banner_regex.search(content[:500]))
                has_footer = bool(copyright_regex.search(body[-500:]) or copyright_regex.search(content[-500:]))

                file_modified = False

                if not has_banner:
                    if fix:
                        canonical_banner = get_canonical_banner(rel_path)
                        body = canonical_banner + "\n\n" + body.lstrip()
                        file_modified = True
                    else:
                        findings.append({
                            'file': rel_path,
                            'issue': "Missing required IP classification banner"
                        })

                if not has_footer:
                    if fix:
                        canonical_footer = get_canonical_footer()
                        body = body.rstrip() + "\n\n---\n\n" + canonical_footer + "\n"
                        file_modified = True
                    else:
                        findings.append({
                            'file': rel_path,
                            'issue': "Missing required IP copyright footer"
                        })

                if fix and file_modified:
                    new_content = frontmatter + body
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)

    return findings

def main():
    parser = argparse.ArgumentParser(description="Portfolio Governance & IP Validator")
    parser.add_argument("--fix-ip", action="store_true", help="Automatically inject missing IP classification banners and copyright footers")
    args, _ = parser.parse_known_args()

    policy_path = 'governance/terminology.yaml'
    docs_dir = 'docs'
    tech_blog_dir = 'docs/tech-blog'
    
    print("--- Portfolio Governance: Terminology Check ---")
    if not os.path.exists(policy_path):
        print(f"Error: Policy file not found at {policy_path}")
        sys.exit(1)
        
    findings = validate_terminology(policy_path, docs_dir)
    
    if findings:
        print(f"Found {len(findings)} terminology inconsistencies:")
        for f in findings:
            print(f"  [GUIDANCE] {f['file']}:{f['line']} - Found '{f['found']}', prefer '{f['preferred']}'")
        print("\nNote: These are informational warnings. Build will proceed.")
    else:
        print("No terminology inconsistencies found. Well done!")
    
    print("\n--- Portfolio Governance: Frontmatter Status Check ---")
    status_findings = validate_frontmatter_status(tech_blog_dir)
    if status_findings:
        print(f"Found {len(status_findings)} frontmatter status issues:")
        for sf in status_findings:
            print(f"  [STATUS WARNING] {sf['file']}: {sf['issue']}")
    else:
        print("All technical blog articles have valid frontmatter status metadata.")

    print("\n--- Portfolio Governance: IP & Content Safeguards Check ---")
    if args.fix_ip:
        print("Auto-fix mode active (--fix-ip): Injecting/repairing missing IP banners and footers...")
    ip_findings = validate_ip_governance(docs_dir, fix=args.fix_ip)
    if ip_findings:
        print(f"Found {len(ip_findings)} IP governance issues:")
        for ipf in ip_findings:
            print(f"  [IP WARNING] {ipf['file']}: {ipf['issue']}")
        print("\nTip: Run `python scripts/validate_governance.py --fix-ip` to auto-annotate missing metadata.")
    else:
        print("All documentation pages meet IP classification and copyright footer standards.")

    print("\n--- Portfolio Governance: Structural Integrity ---")
    print("Note: Navigation and link integrity are handled by 'mkdocs build --strict'.")

if __name__ == "__main__":
    main()
