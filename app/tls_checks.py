import socket
import ssl
from app.utils import get_hostname

def check_tls(url: str) -> dict:
    hostname = get_hostname(url)

    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                version = ssock.version()

        return {
            "tls_supported": True,
            "tls_version": version,
            "certificate_subject": dict(x[0] for x in cert.get("subject", [])),
            "certificate_issuer": dict(x[0] for x in cert.get("issuer", [])),
        }
    except Exception as exc:
        return {
            "tls_supported": False,
            "error": str(exc),
        }