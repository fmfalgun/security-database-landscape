#!/usr/bin/env python3
"""
extract_operators.py — Extract security database operator names from research files.

Usage:
    python3 extract_operators.py [--format {markdown,txt,csv,json}] [--output-dir DIR] [--repo-dir DIR]

Defaults:
    --format    markdown
    --output-dir  extracted/
    --repo-dir    . (current directory)

Examples:
    python3 extract_operators.py
    python3 extract_operators.py --format csv
    python3 extract_operators.py --format json --output-dir results
    python3 extract_operators.py --repo-dir /home/fmf/security-db-research
"""

import re
import os
import json
import csv
import argparse
from collections import defaultdict

# Category display names mapped to filenames
CATEGORIES = {
    "agent_breach_leaks.md":        "Breach & Credential Leaks",
    "agent_internet_scanning.md":   "Internet Scanning & Asset Discovery",
    "agent_threat_intel.md":        "Threat Intelligence & IOC Feeds",
    "agent_osint_dns.md":           "OSINT / Passive DNS / WHOIS",
    "agent_malware_repos.md":       "Malware Repositories & Sandboxes",
    "agent_vuln_databases.md":      "Vulnerability Databases",
    "agent_darkweb_monitoring.md":  "Dark Web Monitoring",
}

# Headings that indicate we are NOT in a findings section (skip these)
NON_ENTRY_PREFIXES = re.compile(
    r'^(Finding|Updated|Note|Status|Progress|Batch|Tier|Section|Task|Summary|'
    r'Research|Objective|Overview|Background|Context|Introduction|Additional|'
    r'Supplemental|Deprecated|Shutdown|Defunct|Commercial|Government|Community|'
    r'Academic|Underground|Gray|Dark|Open)',
    re.IGNORECASE
)

# Suffixes / noise to strip from raw heading text
STRIP_PATTERNS = [
    (r'\s*\[(?:DONE|x|IN PROGRESS|✓)\]', ''),   # [DONE], [x], [✓]
    (r'\s*→.*$', ''),                             # → and everything after
    (r'\s*—.*$', ''),                             # — and everything after
    (r'\s*\(SHUTDOWN[^)]*\)', ''),                # (SHUTDOWN ...)
    (r'\s*\(Defunct[^)]*\)', ''),                 # (Defunct)
    (r'\s*\(defunct[^)]*\)', ''),                 # (defunct)
    (r'\s*\(acquired[^)]*\)', ''),                # (acquired ...)
    (r'\s*\(historical[^)]*\)', ''),              # (historical)
    (r'⚠.*$', ''),                               # ⚠ and everything after
    (r'\s*—\s*Retirement Note.*$', ''),           # retirement notes
    (r'\s*\(Overview\)', ''),                     # (Overview)
    (r'\s*\(overview\)', ''),                     # (overview)
]


def clean_name(raw: str) -> str:
    """Strip noise from a raw heading string to get a clean operator name."""
    name = raw.strip()
    for pattern, replacement in STRIP_PATTERNS:
        name = re.sub(pattern, replacement, name, flags=re.IGNORECASE)
    name = name.strip().rstrip('-').rstrip('.').strip()
    return name


def extract_operators_from_file(filepath: str) -> list[str]:
    """
    Extract unique operator names from a research markdown file.
    Uses numbered headings (## N. / ### N.) as the primary signal.
    Deduplicates within the file via a seen-set (after cleaning).
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match: ## 1. Name   or   ### 1. Name   (2–4 hash levels, any numbered entry)
    heading_pattern = re.compile(
        r'^#{2,4}\s+\d+\.\s+(.+)$',
        re.MULTILINE
    )

    seen: set[str] = set()
    operators: list[str] = []

    for match in heading_pattern.finditer(content):
        raw = match.group(1).strip()
        name = clean_name(raw)

        if not name or len(name) < 3:
            continue
        if NON_ENTRY_PREFIXES.match(name):
            continue
        # Skip pure-digit or pure-symbol names
        if re.match(r'^[\d\W]+$', name):
            continue

        key = name.lower()
        if key not in seen:
            seen.add(key)
            operators.append(name)

    return operators


def build_operator_map(repo_dir: str) -> dict:
    """
    Build a map: normalized_name → {display_name, categories: [...]}
    Scans all category files in the repo.
    """
    op_map: dict[str, dict] = {}

    for filename, category in CATEGORIES.items():
        filepath = os.path.join(repo_dir, filename)
        if not os.path.exists(filepath):
            print(f"  [warn] {filename} not found — skipping.")
            continue

        operators = extract_operators_from_file(filepath)
        print(f"  {filename}: {len(operators)} operators extracted")

        for op in operators:
            key = op.lower().strip()
            if key not in op_map:
                op_map[key] = {"name": op, "categories": []}
            if category not in op_map[key]["categories"]:
                op_map[key]["categories"].append(category)

    return op_map


def categorize(op_map: dict) -> tuple[dict, list, list]:
    """
    Split operators into:
      - by_category: category → [names] (unique to that category only)
      - sorted_combos: [(combo_label, [names])] sorted by count desc
      - multi_category: [{name, categories}]
    """
    by_category: dict[str, list] = defaultdict(list)
    multi_category: list[dict] = []

    for key, data in op_map.items():
        cats = data["categories"]
        name = data["name"]
        if len(cats) == 1:
            by_category[cats[0]].append(name)
        else:
            multi_category.append({"name": name, "categories": cats})

    # Sort each category list alphabetically
    for cat in by_category:
        by_category[cat].sort(key=str.lower)

    # Group multi-category operators by their category combination
    combo_groups: dict[str, list] = defaultdict(list)
    for item in multi_category:
        # Use canonical category order (CATEGORIES dict order)
        ordered_cats = [c for c in CATEGORIES.values() if c in item["categories"]]
        combo_key = " + ".join(ordered_cats)
        combo_groups[combo_key].append(item["name"])

    # Sort combinations by operator count descending
    sorted_combos = sorted(combo_groups.items(), key=lambda x: -len(x[1]))

    return dict(by_category), sorted_combos, multi_category


def short_cat(category: str) -> str:
    """Return a shortened category label for compact display."""
    return category.split("/")[0].split("&")[0].strip().rstrip()


# ── Output writers ──────────────────────────────────────────────────────────

def write_markdown(by_category, sorted_combos, multi_category, output_path):
    single_total = sum(len(v) for v in by_category.values())
    grand_total = single_total + len(multi_category)

    lines = [
        "# Security Database Operators — Extracted Names",
        "",
        f"> **{grand_total} unique operators** across 7 categories  ",
        f"> {single_total} appear in exactly one category · "
        f"{len(multi_category)} appear in multiple categories",
        "",
        "---",
        "",
    ]

    # Per-category sections (unique operators only)
    for category in CATEGORIES.values():
        ops = by_category.get(category, [])
        lines.append(f"## {category} ({len(ops)} unique)\n")
        if ops:
            for op in ops:
                lines.append(f"- {op}")
        else:
            lines.append("*No operators unique to this category.*")
        lines.append("")

    # Multi-category section
    lines += [
        "---",
        "",
        f"## Multi-Category Operators ({len(multi_category)} operators)",
        "",
        "Operators listed here appear in more than one category.",
        "",
    ]

    for combo, names in sorted_combos:
        cats = combo.split(" + ")
        short = " + ".join(short_cat(c) for c in cats)
        lines.append(f"### {short} ({len(names)})")
        lines.append("")
        lines.append(f"*Full categories: {combo}*")
        lines.append("")
        for name in sorted(names, key=str.lower):
            lines.append(f"- {name}")
        lines.append("")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f"\n[markdown] Written to {output_path}")


def write_txt(by_category, sorted_combos, multi_category, output_path):
    single_total = sum(len(v) for v in by_category.values())
    grand_total = single_total + len(multi_category)

    lines = [
        "SECURITY DATABASE OPERATORS",
        "=" * 50,
        f"Total unique: {grand_total} "
        f"({single_total} single-category, {len(multi_category)} multi-category)",
        "",
    ]

    for category in CATEGORIES.values():
        ops = by_category.get(category, [])
        lines.append(f"[{category.upper()}] — {len(ops)} operators")
        for op in ops:
            lines.append(f"  {op}")
        lines.append("")

    lines += [
        "=" * 50,
        f"MULTI-CATEGORY ({len(multi_category)} operators)",
        "",
    ]
    for combo, names in sorted_combos:
        cats = combo.split(" + ")
        short = " + ".join(short_cat(c) for c in cats)
        lines.append(f"  [{short}] ({len(names)})")
        for name in sorted(names, key=str.lower):
            lines.append(f"    {name}")
        lines.append("")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f"\n[txt] Written to {output_path}")


def write_csv(by_category, sorted_combos, multi_category, output_path):
    rows = []

    for category, ops in by_category.items():
        for op in ops:
            rows.append({
                "name": op,
                "categories": category,
                "multi_category": "No",
                "category_count": 1,
            })

    for item in multi_category:
        rows.append({
            "name": item["name"],
            "categories": " | ".join(item["categories"]),
            "multi_category": "Yes",
            "category_count": len(item["categories"]),
        })

    rows.sort(key=lambda x: x["name"].lower())

    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(
            f, fieldnames=["name", "categories", "multi_category", "category_count"]
        )
        writer.writeheader()
        writer.writerows(rows)
    print(f"\n[csv] Written to {output_path}")


def write_json(by_category, sorted_combos, multi_category, output_path):
    single_total = sum(len(v) for v in by_category.values())

    data = {
        "meta": {
            "total_unique": single_total + len(multi_category),
            "single_category_count": single_total,
            "multi_category_count": len(multi_category),
            "categories": len(CATEGORIES),
        },
        "by_category": {},
        "multi_category": {
            "total": len(multi_category),
            "combinations": [],
        },
    }

    for category in CATEGORIES.values():
        ops = by_category.get(category, [])
        data["by_category"][category] = {
            "count": len(ops),
            "operators": sorted(ops, key=str.lower),
        }

    for combo, names in sorted_combos:
        data["multi_category"]["combinations"].append({
            "categories": combo.split(" + "),
            "count": len(names),
            "operators": sorted(names, key=str.lower),
        })

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\n[json] Written to {output_path}")


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Extract security database operator names from research markdown files.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--format", "-f",
        choices=["markdown", "txt", "csv", "json"],
        default="markdown",
        help="Output format (default: markdown)",
    )
    parser.add_argument(
        "--output-dir", "-o",
        default="extracted",
        help="Output directory relative to --repo-dir (default: extracted/)",
    )
    parser.add_argument(
        "--repo-dir", "-r",
        default=".",
        help="Path to repo directory containing agent_*.md files (default: .)",
    )
    args = parser.parse_args()

    repo_dir = os.path.abspath(args.repo_dir)
    output_dir = os.path.join(repo_dir, args.output_dir)
    os.makedirs(output_dir, exist_ok=True)

    print(f"Repo dir  : {repo_dir}")
    print(f"Output dir: {output_dir}")
    print(f"Format    : {args.format}")
    print()

    print("Extracting operators...")
    op_map = build_operator_map(repo_dir)

    print("\nCategorizing...")
    by_category, sorted_combos, multi_category = categorize(op_map)

    single_total = sum(len(v) for v in by_category.values())
    grand_total = single_total + len(multi_category)
    print(f"  {grand_total} unique operators total")
    print(f"  {single_total} single-category")
    print(f"  {len(multi_category)} multi-category ({len(sorted_combos)} unique combinations)")

    ext_map = {"markdown": "md", "txt": "txt", "csv": "csv", "json": "json"}
    output_filename = f"operators.{ext_map[args.format]}"
    output_path = os.path.join(output_dir, output_filename)

    writers = {
        "markdown": write_markdown,
        "txt":      write_txt,
        "csv":      write_csv,
        "json":     write_json,
    }
    writers[args.format](by_category, sorted_combos, multi_category, output_path)

    print(f"\nDone → {output_path}")


if __name__ == "__main__":
    main()
