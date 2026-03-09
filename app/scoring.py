def calculate_score(headers_score: int, robots_result: dict, tls_result: dict, fingerprint_result: dict) -> dict:
    total = headers_score
    issues = []

    if not tls_result.get("tls_supported"):
        total -= 20
        issues.append("TLS not available or handshake failed")

    if robots_result.get("exists") is False:
        total -= 3
        issues.append("robots.txt not found")

    for item in fingerprint_result.get("indicators", []):
        if item["type"] == "x_powered_by":
            total -= 5
            issues.append("X-Powered-By header exposed")
        if item["type"] == "server_header":
            total -= 3
            issues.append("Server header exposed")

    total = max(total, 0)

    if total >= 85:
        level = "low"
    elif total >= 60:
        level = "medium"
    else:
        level = "high"

    return {
        "score": total,
        "risk_level": level,
        "issues": issues,
    }