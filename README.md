# Secret Scan CLI

A local command-line tool to scan codebases for exposed secrets like API keys and tokens.

## Usage
```bash
python cli.py ./your-project
# Secret Scanner CLI

A **Python CLI tool** to scan local codebases for exposed secrets such as cloud tokens, API keys, passwords, and other sensitive credentials.  

This tool helps developers catch accidental leaks **before pushing code to GitHub or other repositories**. It can also be integrated into **CI/CD pipelines** for automated checks.

---

## Features

- Detects:
  - Cloud credentials (AWS, Azure, GCP)
  - Temporary session tokens
  - API keys and JWT tokens
  - Passwords and database credentials
  - High-entropy secrets hidden in code

- Works **locally**, no secrets are uploaded anywhere
- **Masks sensitive values** in output to prevent exposure
- Can be integrated into **CI/CD pipelines**
- Ignores common files like `.gitignore` and `.env` to reduce false positives

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/secret-scanner.git
cd secret-scanner
pip install -r requirements.txt
secret-scan /path/to/your/project
