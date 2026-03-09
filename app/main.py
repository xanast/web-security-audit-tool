import argparse
from app.scanner import run_scan

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Defensive Web Security Audit Tool"
    )
    parser.add_argument(
        "target",
        help="Target URL to audit (authorized systems only)"
    )

    args = parser.parse_args()

    result = run_scan(args.target)

    print("\nScan complete.")
    print(f"JSON report: {result['json_report_path']}")
    print(f"HTML report: {result['html_report_path']}")

if __name__ == "__main__":
    main()