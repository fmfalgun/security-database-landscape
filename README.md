# Security Database Landscape

A comprehensive reference catalog of **414+ security database operators** across 7 categories, covering commercial, free/open, government, academic, and gray/dark market sources. Research current as of July 2026.

---

## What This Is

No single security database covers the full threat landscape. This project catalogs every significant operator — who owns the data, what they hold, how to access it, and where geopolitical risks apply. The goal is a reference that reflects what both security professionals and offensive researchers actually use in practice.

Global scope. Geopolitical flags (Chinese, Russian, state-affiliated operators) are documented where relevant.

---

## Repository Structure

```
security-database-landscape/
├── agent_breach_leaks.md          # Breach & credential leak databases (38 operators)
├── agent_internet_scanning.md     # Internet scanning & asset discovery (42 operators)
├── agent_threat_intel.md          # Threat intelligence & IOC feeds (89 operators)
├── agent_osint_dns.md             # OSINT, passive DNS, WHOIS history (70 operators)
├── agent_malware_repos.md         # Malware sample repositories & sandboxes (49 operators)
├── agent_vuln_databases.md        # Vulnerability databases (55+ operators)
├── agent_darkweb_monitoring.md    # Dark web monitoring (71 operators)
├── extract_operators.py           # Script to extract & categorize operator names
└── extracted/                     # Generated output from extract_operators.py
    └── operators.md               # Extracted names (markdown, default)
    └── operators.csv              # Extracted names (CSV, optional)
    └── operators.json             # Extracted names (JSON, optional)
    └── operators.txt              # Extracted names (plain text, optional)
```

---

## Extract Operator Names

The `extract_operators.py` script parses all 7 research files and outputs a clean list of operator names, deduplicated and categorized — including a **multi-category section** that identifies operators appearing in more than one category and groups them by combination.

### Usage

```bash
# Default: markdown output → extracted/operators.md
python3 extract_operators.py

# Choose format
python3 extract_operators.py --format csv
python3 extract_operators.py --format json
python3 extract_operators.py --format txt

# Custom output directory
python3 extract_operators.py --output-dir results

# Run from a different directory
python3 extract_operators.py --repo-dir /path/to/security-database-landscape
```

### Output Structure

**Single-category sections** — operators unique to one category, alphabetically sorted.

**Multi-category section** — operators appearing in 2+ categories, grouped by their combination:

```
## Multi-Category Operators (N operators)

### Threat Intelligence + Malware Repositories (4)
- VirusTotal
- ...

### Threat Intelligence + OSINT / Passive DNS (3)
- Shodan
- ...
```

### Requirements

Python 3.10+ (no external dependencies — standard library only).

---

## Categories

### 1. Breach & Credential Leak Databases — 38 operators
Databases that collect, index, and expose data from public cybersecurity breaches and credential dumps.

**Includes:** HaveIBeenPwned, DeHashed, SpyCloud, LeakCheck, Snusbase, IntelligenceX, BreachDirectory, Constella Intelligence, Hudson Rock, Flashpoint, Flare Systems, Breachsense, Genesis Market, Russian Market, 2easy.shop, and 23 more.

---

### 2. Internet Scanning & Asset Discovery — 42 operators
Organizations that continuously scan the entire internet's IP space to index exposed services, devices, banners, certificates, and configurations.

**Includes:** Shodan, Censys, FOFA ⚠️, ZoomEye ⚠️, GreyNoise, LeakIX, Netlas, Onyphe, IVRE, Microsoft Defender EASM, Shadowserver, CAIDA, Rapid7 Project Sonar, Criminal IP, Cortex Xpanse, runZero, CyCognito, 360 Quake ⚠️, Hunt.io, and 23 more.

---

### 3. Threat Intelligence & IOC Feeds — 89 operators
Organizations that collect, correlate, and distribute intelligence about malicious IPs, domains, URLs, file hashes, C2 infrastructure, and threat actor TTPs.

**Includes:** VirusTotal/GTI, Recorded Future, Mandiant, CrowdStrike, IBM X-Force, Cisco Talos, AlienVault OTX, abuse.ch, MISP, Spamhaus, Team Cymru, Shadowserver, FS-ISAC, Kaspersky ⚠️, Group-IB ⚠️, Positive Technologies ⚠️, Qihoo 360 ⚠️, and 72 more.

---

### 4. OSINT / Passive DNS / WHOIS History — 70 operators
Databases built from historical DNS resolution data, WHOIS records, certificate transparency logs, BGP routing data, and related internet infrastructure telemetry.

**Includes:** PassiveTotal/RiskIQ (retiring Aug 2026), Farsight DNSDB, DomainTools, SecurityTrails, Shodan, CIRCL, Netcraft, CT ecosystem (crt.sh, Google CT, Cloudflare CT), ZoomEye ⚠️, FOFA ⚠️, Robtex, Hurricane Electric, RIPE NCC, Maltego, Censys, Criminal IP, Netlas, ONYPHE, WhoisXML API, PassiveDNS.cn ⚠️, and 49 more.

---

### 5. Malware Sample Repositories & Sandboxes — 49 operators
Organizations that collect, store, analyze, and share malware samples, behavioral reports, and related indicators.

**Includes:** VirusTotal, MalwareBazaar, ANY.RUN, Hybrid Analysis, Joe Sandbox, Cuckoo/CAPE, Triage (Recorded Future), Intezer, VXUnderground, VirusShare, Malshare, ReversingLabs, PolySwarm, Kaspersky ⚠️ (US-banned Sept 2024), Qihoo 360 ⚠️, CISA MAR, NSA CNMF disclosures, and 32 more.

---

### 6. Vulnerability Databases — 55+ operators
Databases that catalog, score, and distribute information about software vulnerabilities, exploits, CVEs, and security advisories.

**Includes:** NVD (enrichment crisis 2024–2025), MITRE CVE (near-shutdown April 2025), CISA KEV, Exploit-DB, GitHub GHSA, OSV, VulDB, VulnCheck, ZDI, Zerodium, Crowdfense ⚠️, CNVD ⚠️, CNNVD ⚠️ (MSS-operated), FSTEC BDU ⚠️, ENISA EUVD (launched May 2025), HackerOne, Bugcrowd, CISA ICS-CERT, Claroty, Dragos, and 35+ more.

---

### 7. Dark Web Monitoring — 71 operators
Organizations that crawl Tor, I2P, Telegram, paste sites, and closed forums to collect intelligence on criminal activity, data leaks, threat actor communications, and underground markets.

**Includes:** Recorded Future/Insikt, Flashpoint, ReliaQuest, ZeroFox, DarkOwl, Cybersixgill/Bitsight, Intel 471, KELA, Searchlight Cyber, Cyble, Flare Systems, FBI (full seizure timeline), Europol EC3, INTERPOL, BreachForums (v1–v4 history), RaidForums, XSS.is ⚠️ (admin arrested July 2025), Exploit.in ⚠️, Russian Market ⚠️, Hydra ⚠️, active ransomware group leak sites, and 49 more.

---

## What Each Entry Covers

For every operator documented:

- **Organization / company name**
- **Product / database name**
- **Website / URL**
- **Data held** — what's in the database
- **Scale** — record counts, coverage where known
- **Access model** — free, paid, API, researcher-only, government-only, dark web
- **Who uses it** — defenders, red teamers, law enforcement, researchers, etc.
- **Geopolitical flags** — operators subject to Chinese or Russian state intelligence laws, US sanctions, or known state-affiliated use
- **Notable events** — acquisitions, shutdowns, law enforcement actions, legal controversies

---

## Geopolitical Flags

Operators flagged ⚠️ are subject to one or more of:

- **Chinese state access** — subject to PRC National Intelligence Law / Data Security Law (FOFA, ZoomEye, Qihoo 360, PassiveDNS.cn, ThreatBook, NSFocus, Antiy Labs)
- **Russian state access / sanctions** — US Treasury sanctioned or Sberbank/state-telecom owned (Kaspersky — US-banned Sept 2024, Positive Technologies — sanctioned April 2021, BI.ZONE, Solar/Rostelecom)
- **Complex geopolitical status** — company relocated due to founder arrest by home government (Group-IB — founder imprisoned by Russian FSB 2021, now UAE/Singapore)
- **UAE intelligence context** — exploit broker with state end-use risk (Crowdfense — acquired by EDGE Group)

---

## Notable 2025–2026 Findings

- **Kaspersky fully banned in the US** — effective September 29, 2024; ~1M US users force-migrated to UltraAV
- **XSS.is admin arrested** — July 2025 by Ukrainian/European authorities; Exploit.in absorbed displaced users
- **BreachForums v4** — still cycling through seizures and relaunches as of 2026
- **BinaryEdge shutdown** — March 31, 2025 (absorbed into Coalition cyber insurance)
- **BGPView shutdown** — November 2025; BGP.tools is the recommended replacement
- **Microsoft MDTI retiring** — August 1, 2026 (formerly PassiveTotal/RiskIQ)
- **IBM X-Force Exchange EOL** — 2026
- **Cybersixgill acquired by Bitsight** — November 2024 ($115M)
- **Recorded Future acquired by Mastercard** — December 2024 ($2.65B)
- **Cyberint acquired by Check Point** — October 2024 ($200M)
- **ENISA EUVD launched** — May 2025; EU's sovereign NVD alternative; CRA mandatory reporting starts September 2026
- **CVE program near-shutdown** — April 2025 funding crisis; CISA emergency extension saved it
- **NVD enrichment crisis** — OIG audit found 88% error rate; NIST now enriches only risk-prioritized subset

---

## Related Work

This research complements [`cve-database-analysis`](https://github.com/fmfalgun/cve-database-analysis) — a systematic evaluation of 1,288+ CVE/vulnerability databases across 20 parameters with a focus on IoT/OT security programs.

---

*Last updated: July 2026*
