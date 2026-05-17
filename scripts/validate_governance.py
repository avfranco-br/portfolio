import os
import re
import yaml
import sys

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
                
                # Strip code blocks to avoid false positives in code
                content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
                content = re.sub(r'`.*?`', '', content)
                
                # Strip markdown link targets to avoid false positives in URLs
                # [text](target) -> [text]()
                content = re.sub(r'(\[.*?\])\(.*?\)', r'\1()', content)
                    
                for canonical, details in canonical_terms.items():
                    rejected_variants = details.get('reject', [])
                    for variant in rejected_variants:
                        # Use word boundaries for precise matching
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

def main():
    policy_path = 'governance/terminology.yaml'
    docs_dir = 'docs'
    
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
    
    print("\n--- Portfolio Governance: Structural Integrity ---")
    print("Note: Navigation and link integrity are handled by 'mkdocs build --strict'.")

if __name__ == "__main__":
    main()
