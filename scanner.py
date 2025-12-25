from pathlib import Path
from patterns import PATTERNS

IGNORE_FILES = [".gitignore", ".env"]

def mask_secret(secret: str) -> str:
    if len(secret) <= 6:
        return "***"
    return secret[:3] + "***" + secret[-3:]

def scan_file(file_path: Path):
    findings = []
    if file_path.name in IGNORE_FILES:
        return findings
    try:
        with file_path.open(errors="ignore") as f:
            for lineno, line in enumerate(f, start=1):
                for name, pattern in PATTERNS.items():
                    match = pattern.search(line)
                    if match:
                        findings.append({
                            "file": str(file_path),
                            "line": lineno,
                            "type": name,
                            "value": mask_secret(match.group())
                        })
    except Exception:
        pass
    return findings

def scan_directory(path: Path):
    all_findings = []
    for file in path.rglob("*"):
        if file.is_file():
            all_findings.extend(scan_file(file))
    return all_findings
