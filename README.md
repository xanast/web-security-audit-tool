# Web Security Audit Tool

A defensive Python tool that performs lightweight security audits on websites you **own or are explicitly authorized to test**.

The tool analyzes common web security configurations and generates structured **JSON** and **HTML reports** that summarize potential risk indicators and security findings.

---

# Features

* HTTP security headers analysis
* robots.txt analysis
* passive server fingerprinting
* TLS / HTTPS inspection
* vulnerability indicators
* JSON report export
* HTML report export
* CLI interface for scanning domains

---

# Tech Stack

* Python 3
* requests
* jinja2
* argparse

---

# Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/web-security-audit-tool.git
cd web-security-audit-tool
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Usage

Run a scan from the terminal:

```bash
python -m app.main example.com
```

Example:

```bash
python -m app.main youtube.com
```

After the scan completes, the tool generates:

```
report.json
report.html
```

---

# Example Output

Example JSON structure:

```json
{
  "target": "https://example.com",
  "summary": {
    "score": 82,
    "risk_level": "medium"
  }
}
```

Example terminal output:

```
Scan complete.
JSON report: ./report.json
HTML report: ./report.html
```

---

# Project Structure

```
web-security-audit-tool
│
├── app
│   ├── main.py
│   ├── scanner.py
│   ├── headers_audit.py
│   ├── robots_audit.py
│   ├── fingerprint.py
│   ├── tls_checks.py
│   ├── scoring.py
│   └── utils.py
│
├── templates
│   └── report.html.j2
│
├── samples
│   └── sample_report.json
│
├── tests
│   ├── test_headers.py
│   └── test_scoring.py
│
├── report.json
├── report.html
├── requirements.txt
├── LICENSE
└── README.md
```

---

# What This Tool Checks

The audit currently evaluates:

### HTTP Security Headers

The tool checks for common security headers such as:

* Content-Security-Policy
* Strict-Transport-Security
* X-Frame-Options
* X-Content-Type-Options
* Referrer-Policy
* Permissions-Policy

These headers help mitigate risks like **XSS**, **clickjacking**, and **MIME sniffing**.

---

### robots.txt Analysis

The tool checks:

* whether a robots.txt file exists
* disallowed paths
* sitemap references

Note:
`robots.txt` is **not a security control**, but misconfigurations may expose sensitive paths.

---

### Passive Server Fingerprinting

The scanner looks for indicators such as:

* Server headers
* X-Powered-By headers
* technology hints inside HTML

This helps identify potential **information disclosure**.

---

### TLS / HTTPS Inspection

The tool inspects:

* TLS version
* certificate metadata
* HTTPS support

---

# Security / Legal Notice

This tool is intended **only for systems you own or have explicit authorization to test**.

Unauthorized scanning of third-party systems may violate:

* laws
* service terms
* acceptable use policies

Use responsibly.

---

# Future Improvements

Planned features include:

* cookie security analysis
* CSP policy parsing
* redirect chain analysis
* sitemap crawling
* multi-domain scanning
* CLI configuration flags
* security scoring improvements
* advanced HTML reporting dashboard

---

# Author

Computer Science student focused on **software engineering, web security, and backend systems**.

This project is part of a personal portfolio aimed at demonstrating practical development and security analysis skills.

---

# License

MIT License
