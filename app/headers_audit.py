EXPECTED_HEADERS = {
    "Content-Security-Policy": "Helps reduce XSS/injection impact",
    "Strict-Transport-Security": "Forces HTTPS on supported browsers",
    "X-Content-Type-Options": "Prevents MIME sniffing",
    "X-Frame-Options": "Helps mitigate clickjacking",
    "Referrer-Policy": "Controls referrer leakage",
    "Permissions-Policy": "Restricts browser features",
}

def audit_headers(headers: dict) -> dict:
    findings = []
    score = 100

    for header, description in EXPECTED_HEADERS.items():
        if header in headers:
            findings.append({
                "header": header,
                "status": "present",
                "details": headers.get(header),
                "description": description,
            })
        else:
            findings.append({
                "header": header,
                "status": "missing",
                "details": None,
                "description": description,
            })
            score -= 8

    return {
        "score": max(score, 0),
        "findings": findings,
    }