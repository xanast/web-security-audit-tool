def passive_fingerprint(headers: dict, html: str) -> dict:
    indicators = []

    server = headers.get("Server")
    powered_by = headers.get("X-Powered-By")

    if server:
        indicators.append({"type": "server_header", "value": server})

    if powered_by:
        indicators.append({"type": "x_powered_by", "value": powered_by})

    html_lower = html.lower()
    if "wp-content" in html_lower or "wordpress" in html_lower:
        indicators.append({"type": "technology_hint", "value": "Possible WordPress"})
    if "csrf-token" in html_lower:
        indicators.append({"type": "security_hint", "value": "CSRF token present"})
    if "bootstrap" in html_lower:
        indicators.append({"type": "frontend_hint", "value": "Bootstrap detected"})

    return {
        "indicators": indicators
    }