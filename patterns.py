import re

PATTERNS = {
    "AWS Access Key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "AWS Secret Key": re.compile(r"(?i)aws_secret_access_key\s*[:=]\s*['\"][A-Za-z0-9/+=]{40}['\"]"),
    "Azure Storage Key": re.compile(r"(?i)azure_storage_account_key\s*[:=]\s*['\"][A-Za-z0-9+/=]{88}['\"]"),
    "Azure Client Secret": re.compile(r"(?i)azure_client_secret\s*[:=]\s*['\"][A-Za-z0-9~!@#$%^&*()_+=]{20,}['\"]"),
    "GCP Service Account Key": re.compile(r"\"type\":\s*\"service_account\""),
    "JWT Token": re.compile(r"eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+"),
    "Generic API Key": re.compile(r"(?i)api[_-]?key\s*[:=]\s*['\"][A-Za-z0-9\-_=]{16,}['\"]"),
    "Generic Secret": re.compile(r"(?i)secret\s*[:=]\s*['\"][^'\"]{8,}['\"]"),
    "Password": re.compile(r"(?i)password\s*[:=]\s*['\"][^'\"]{6,}['\"]"),
    "Stripe Key": re.compile(r"(?i)sk_live_[0-9a-zA-Z]{24}"),
    "Slack Token": re.compile(r"xox[baprs]-[0-9a-zA-Z]{10,48}"),
    "Twilio SID": re.compile(r"AC[0-9a-fA-F]{32}"),
    "Twilio Token": re.compile(r"[0-9a-fA-F]{32}"),
    "SSH Private Key": re.compile(r"-----BEGIN PRIVATE KEY-----"),
    "RSA Private Key": re.compile(r"-----BEGIN RSA PRIVATE KEY-----"),
    "High-Entropy String": re.compile(r"[A-Za-z0-9+/]{40,}={0,2}")
}
