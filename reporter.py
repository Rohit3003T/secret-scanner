import json

def print_report(findings):
    if not findings:
        print("✅ No secrets found.")
        return

    print("\n🚨 Secrets Detected:\n")
    for f in findings:
        print(f"File : {f['file']}")
        print(f"Line : {f['line']}")
        print(f"Type : {f['type']}")
        print(f"Value: {f['value']}")
        print("Action: Rotate/remove this secret immediately\n")

def save_json(findings, filename="scan-report.json"):
    with open(filename, "w") as f:
        json.dump(findings, f, indent=2)
