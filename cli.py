import click
from pathlib import Path
from scanner import scan_directory
from reporter import print_report, save_json

@click.command()
@click.argument("path", type=click.Path(exists=True))
def scan(path):
    """Scan a local directory for exposed secrets."""
    path = Path(path)
    print(f"🔍 Scanning: {path}\n")
    findings = scan_directory(path)
    print_report(findings)
    save_json(findings)
    print("📄 Report saved as scan-report.json")

if __name__ == "__main__":
    scan()
