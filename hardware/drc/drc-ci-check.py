#!/usr/bin/env python3
"""
KiCad Headless DRC/ERC Report Parser & CI Gatekeeper
Astro at Baylor - High Power Rocketry Avionics
"""

import argparse
import json
import os
import sys

def parse_report(report_path, report_type="DRC"):
    if not os.path.exists(report_path):
        print(f"[{report_type}] Notice: Report file not found at {report_path} (Skipping).")
        return {"errors": 0, "warnings": 0, "unconnected": 0}

    try:
        with open(report_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"[{report_type}] Failed to parse JSON report: {e}")
        return {"errors": 1, "warnings": 0, "unconnected": 0}

    errors = 0
    warnings = 0
    unconnected = 0

    # KiCad 8 JSON format inspection
    violations = data.get("violations", [])
    for v in violations:
        severity = v.get("severity", "error").lower()
        desc = v.get("description", "Unknown violation")
        if severity == "error":
            errors += 1
            print(f"[{report_type} ERROR] {desc}")
        elif severity == "warning":
            warnings += 1
            print(f"[{report_type} WARN] {desc}")

    unconnected_items = data.get("unconnected_items", [])
    unconnected += len(unconnected_items)
    for u in unconnected_items:
        print(f"[{report_type} UNCONNECTED] {u.get('description', 'Unconnected net item')}")

    print(f"[{report_type} SUMMARY] Errors: {errors}, Warnings: {warnings}, Unconnected: {unconnected}")
    return {"errors": errors, "warnings": warnings, "unconnected": unconnected}

def main():
    parser = argparse.ArgumentParser(description="KiCad DRC/ERC CI Check")
    parser.add_argument("--drc", default=None, help="Path to KiCad DRC JSON report")
    parser.add_argument("--erc", default=None, help="Path to KiCad ERC JSON report")
    parser.add_argument("--strict", action="store_true", help="Fail on any errors or unconnected nets")
    args = parser.parse_args()

    total_errors = 0
    total_unconnected = 0

    if args.erc:
        erc_res = parse_report(args.erc, report_type="ERC")
        total_errors += erc_res["errors"]
        total_unconnected += erc_res["unconnected"]

    if args.drc:
        drc_res = parse_report(args.drc, report_type="DRC")
        total_errors += drc_res["errors"]
        total_unconnected += drc_res["unconnected"]

    if args.strict and (total_errors > 0 or total_unconnected > 0):
        print("\n❌ CI Check FAILED: DRC/ERC violations or unconnected pins detected!")
        sys.exit(1)
    else:
        print("\n✅ DRC/ERC Check PASSED (No blocking violations).")
        sys.exit(0)

if __name__ == "__main__":
    main()
