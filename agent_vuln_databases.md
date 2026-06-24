# Vulnerability Database Research — Agent Task File

**Objective:** Research and document ALL significant vulnerability database operators — government, commercial, open-source, academic, and gray/offensive (exploit brokers, underground markets). Global scope. Flag geopolitical context where relevant.

**Started:** 2026-06-17
**Last Updated:** 2026-06-23
**Status:** COMPLETE (initial pass)

**Source note:** The majority of this document is synthesised from `/home/fmf/Projects/cve-analysis/` — a prior 1,288+ database research project with 20-parameter scoring across 80+ databases. Web searches were conducted to supplement with 2025–2026 current-state information not yet in that project, particularly for gray/offensive actors, geopolitical databases, and emerging categories. No duplication of prior research work — only augmentation and cross-referencing.

---

## Task List

### Tier 1 — Core Public/Government:
- [DONE] NVD (NIST/CISA)
- [DONE] CVE Program (MITRE)
- [DONE] CISA KEV
- [DONE] OVAL (MITRE)
- [DONE] JVN / JVNDB (Japan)
- [DONE] CNVD (China) [GEOPOLITICAL FLAG]
- [DONE] CNNVD (China, MSS-linked) [GEOPOLITICAL FLAG]
- [DONE] FSTEC BDU (Russia) [GEOPOLITICAL FLAG]
- [DONE] KVD (Korea)

### Tier 2 — Community / Open Source:
- [DONE] Exploit-DB (OffSec)
- [DONE] Packet Storm Security
- [DONE] Full Disclosure mailing list
- [DONE] SecurityFocus / BugTraq (historical)
- [DONE] GitHub Advisory Database (GHSA)
- [DONE] OSV (Google)
- [DONE] VulDB (Swiss)
- [DONE] Vulners (Russian origin)
- [DONE] Sploitus
- [DONE] OpenCVE
- [DONE] InTheWild.io
- [DONE] VulnCheck
- [DONE] Nuclei Templates (ProjectDiscovery)

### Tier 3 — Commercial:
- [DONE] Zero Day Initiative (ZDI — Trend Micro)
- [DONE] Tenable Research / Nessus plugin DB
- [DONE] Rapid7 Metasploit modules DB
- [DONE] Qualys VMDR
- [DONE] CrowdStrike vulnerability intel
- [DONE] Recorded Future vulnerability intel
- [DONE] Flashpoint vulnerability intel
- [DONE] VARIoT (IoT — EU funded)
- [DONE] Claroty Research (OT/ICS)
- [DONE] Dragos vulnerability intel (ICS)
- [DONE] Nozomi Networks Research (ICS)

### Tier 4 — Gray/Offensive:
- [DONE] Zerodium (exploit broker)
- [DONE] Crowdfense (UAE) [GEOPOLITICAL FLAG]
- [DONE] Vupen Security (historical, dissolved)
- [DONE] Dark web exploit markets
- [DONE] Canvas exploit framework (Immunity / Fortra)
- [DONE] CORE Impact (Fortra)

### Tier 5 — Vendor Advisory Programs:
- [DONE] MSRC (Microsoft)
- [DONE] Google Project Zero
- [DONE] Apple PSRT
- [DONE] Cisco PSIRT
- [DONE] Oracle CPU
- [DONE] Red Hat RHSA
- [DONE] Ubuntu/Canonical USN
- [DONE] Siemens ProductCERT (ICS)
- [DONE] Schneider Electric PSIRT (ICS)

### Tier 6 — Bug Bounty Platforms:
- [DONE] HackerOne
- [DONE] Bugcrowd
- [DONE] Intigriti (Belgium)
- [DONE] Synack
- [DONE] YesWeHack (France)

### Tier 7 — ICS/SCADA Specific:
- [DONE] CISA ICS-CERT Advisories

### Additional:
- [DONE] ENISA EUVD (new 2025/2026)
- [DONE] Cloud vulnerability databases (AWS, Azure, GCP)
- [DONE] AI/ML model vulnerability databases (MITRE ATLAS, AVID)
- [DONE] Supply chain / SBOM-linked vulnerability databases
- [DONE] GCVE / CVE Foundation (governance alternatives)
- [DONE] VARIoT, CIRCL ecosystem

---

## CRITICAL 2025–2026 CONTEXT

Before the database entries, four structural crises define the current landscape:

### 1. NVD Enrichment Collapse (April 2026)
NIST formally adopted a risk-based triage model on April 15, 2026. Under this model, NVD only enriches CVEs that appear in the CISA KEV catalog, affect US federal government software, or are designated critical under EO 14028. The remaining ~80–85% of new CVEs are categorised as **"Not Scheduled"** indefinitely. The backlog of unenriched CVEs stood at ~27,000 by end-2025, with ~29,000 additionally reclassified. OIG audit OIG-26-020-I (May 26, 2026) found NVD severity scores match independent evaluators only **12% of the time** (88% error rate) — the most severe quality finding in NVD's 21-year history. This makes NVD unreliable as a sole enrichment source.

### 2. CVE Program Governance Crisis (April 2025)
On April 15–16, 2025, DHS allowed MITRE's contract to lapse for ~24 hours, nearly shutting down the CVE program entirely — which would have disabled every vulnerability scanner, advisory feed, and risk scoring system globally. CISA issued an 11-month emergency extension. The 11-month extension expired in March 2026; the program continues under further emergency arrangements. Community responses include: the **CVE Foundation** (formed to advocate for multi-stakeholder governance) and **GCVE** (CIRCL-launched decentralised CVE allocation system, January 2026). CNA count: 484 organisations as of January 2026, with 365 active in 2025.

### 3. Exploitation Velocity Acceleration
Mean time-to-exploit hit negative 7 days in 2025 — exploitation precedes public disclosure in 42% of cases. VulnCheck tracked 14,000+ exploits for 10,000+ CVEs in 2025. CISA KEV median lag from exploitation to catalog entry: ~42 days. 56.4% of ransomware CVEs in 2025 were zero-days at time of exploitation.

### 4. Supply Chain Non-CVE Threat Explosion
Mondoo 2026 report: 192,742 malicious open-source packages without CVE identifiers — approximately 4x the CVE volume published in all of 2025. This threat surface is entirely invisible to CVE-centric tools.

---

## Findings

---

## TIER 1 — CORE PUBLIC/GOVERNMENT DATABASES

### NVD — National Vulnerability Database
- **Operator:** NIST (National Institute of Standards and Technology), US Department of Commerce
- **Website:** https://nvd.nist.gov / API: https://services.nvd.nist.gov/rest/json/cves/2.0
- **What it holds:** CVE entries enriched with CVSS severity scores (v2, v3.1, limited v4), CPE product applicability mappings, CWE weakness classifications. The de-facto global vulnerability reference for all downstream scanners, SIEMs, and VM platforms. As of August 20, 2025, legacy JSON bulk feeds permanently retired; API 2.0 is the only official data source.
- **Coverage:** Universal CVE scope — covers all products, vendors, and platforms for which CVEs exist. 308,920 cumulative CVEs by end-2025; ~48,185 new in 2025.
- **Access model:** Free, no authentication required for basic queries; API key recommended for higher rate limits. CC0 public domain.
- **Who uses it:** Virtually every security tool globally — scanners (Tenable, Qualys, Rapid7), SIEM platforms, developers, academics, all national CERTs.
- **2025–2026 crisis status:**
  - April 2026 triage policy: Only ~15–20% of new CVEs receive full enrichment going forward
  - CPE coverage at publication time for Jan 2025 CVEs: only 8% (full-year 2024: 41.35%)
  - CVSS score accuracy: 12% correct per OIG-26-020-I audit (88% error rate)
  - 55% of CWE classifications map to invalid/placeholder types
  - ~29,000 backlog CVEs reclassified as "Not Scheduled"
  - NVD remains the universal identifier index (P1=5) but enrichment quality has collapsed (P2=2)
- **Exploit availability:** None — NVD does not track exploit status
- **Geopolitical flags:** US government operated; concerns about centralization risk exposed by April 2025 CVE funding crisis. DoC OIG audit documented governance failures at institutional level.
- **Recommended supplement:** VulnCheck NVD++ (free community tier fills CPE/CVSS for unenriched CVEs), CISA Vulnrichment (GitHub, ADP containers)

---

### CVE Program (MITRE)
- **Operator:** MITRE Corporation under DHS/CISA contract; now also supported by the newly formed CVE Foundation
- **Website:** https://cve.mitre.org / Raw feed: https://github.com/CVEProject/cvelistV5
- **What it holds:** Universal naming system for publicly disclosed vulnerabilities. Assigns globally unique CVE-YYYY-NNNNN identifiers. JSON 5.0 schema (cvelistV5 on GitHub). Does NOT provide CVSS scores, CPE mappings, exploit data, or any enrichment — it is a naming registry, not a database.
- **Coverage:** Publicly disclosed issues submitted through the CNA (CVE Numbering Authority) ecosystem. 484 CNAs registered as of January 2026; 365 active in 2025. Top CNA by 2025 volume: Patchstack (7,007 CVEs for WordPress vulnerabilities).
- **Access model:** Completely free, CC0 public domain. Bulk JSON download via GitHub. API available via services.nvd.nist.gov.
- **Who uses it:** Every security tool globally uses CVE IDs as the primary key for vulnerability tracking.
- **April 2025 governance crisis:** DHS allowed MITRE's contract to lapse on April 15–16, 2025, creating a ~24-hour period of near-shutdown. CISA issued an emergency 11-month extension. The crisis exposed systemic governance risk in having a critical global infrastructure operated under a single government contract. Community response:
  - **CVE Foundation:** Formed to advocate for independent, multi-stakeholder governance of the CVE program
  - **GCVE (Global CVE):** Launched by CIRCL (Luxembourg) in January 2026 as a distributed, federated CVE allocation alternative. Operates independently of US government funding.
- **Exploit availability:** None — identifiers only
- **Geopolitical flags:** US government-funded; single point of failure exposed. GCVE and CVE Foundation represent international hedges against US funding instability.

---

### CISA KEV — Known Exploited Vulnerabilities Catalog
- **Operator:** Cybersecurity and Infrastructure Security Agency (CISA), US DHS
- **Website:** https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- **Raw feed:** https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- **What it holds:** Curated catalog of CVEs with confirmed active exploitation in the wild. Each entry includes: CVE ID, vendor, product, short description, date CISA added it, required action, and mandatory remediation deadline (for US federal agencies under BOD 22-01).
- **Coverage:** Intentionally narrow — only confirmed-exploitation CVEs with assigned CVE IDs. 1,484 entries as of late 2025. Does NOT cover zero-days without CVE IDs, vulnerabilities without confirmed exploitation evidence, or non-US-focused threats (some regional bias).
- **Access model:** Completely free. Machine-readable JSON and CSV. No authentication required. Updated on a rolling basis (avg. ~4.7 additions per week in 2025).
- **Who uses it:** Mandatory for US federal civilian agencies (BOD 22-01); widely adopted globally as a prioritization anchor by all VM programs. Integrated into Tenable VPR, Qualys TruRisk, Rapid7, CrowdStrike, and virtually all commercial VM platforms.
- **Key metric:** Median lag from confirmed exploitation to KEV catalog addition: ~42 days (with mean time-to-exploit now at negative 7 days, this means KEV often lags exploitation by 5–7 weeks).
- **Exploit availability:** Yes — KEV is itself a confirmed-exploitation signal; the highest-quality free exploitation status indicator available.
- **Limitations:** Only 1,484 entries vs. 308,920 total CVEs; no dark web or pre-disclosure signals; regional US bias; no CVSS scores or CPE mappings of its own.
- **Comparison:** VulnCheck's expanded KEV catalog carries 3,600+ entries (173% more than CISA KEV), tracking exploitation evidence from 500+ data sources. Flashpoint VulnDB KEV: 5,100+ exploited CVEs.

---

### OVAL — Open Vulnerability and Assessment Language (MITRE)
- **Operator:** MITRE Corporation (specification); vendors publish their own OVAL feeds
- **Website:** https://oval.mitre.org / CIS OVAL repository: https://oval.cisecurity.org
- **What it holds:** XML/JSON-format machine-readable definitions for detecting the presence of vulnerabilities or configuration issues on specific systems. OVAL definitions are consumed by OpenSCAP, SCAP-Workbench, Nessus, and enterprise compliance scanners. Each definition maps a CVE or configuration check to specific product/version/registry/file conditions.
- **Coverage:** Vendor-specific; major OVAL publishers include Red Hat, Microsoft, Debian, Ubuntu, Oracle, Cisco, and others. Not all CVEs have OVAL definitions.
- **Access model:** Free; vendor-published OVAL feeds are publicly available. CIS hosts a consolidated OVAL repository.
- **Who uses it:** Compliance-driven environments (FedRAMP, FISMA, DoD STIG); automated configuration and vulnerability assessment tools.
- **Exploit availability:** None — detection/assessment language only, not exploit tracking

---

### JVN / JVNDB — Japan Vulnerability Notes
- **Operator:** IPA (Information-technology Promotion Agency) and JPCERT/CC, Japanese government-affiliated
- **Website:** JVN portal: https://jvn.jp (individual advisories); JVNDB: https://jvndb.jvn.jp (aggregated database)
- **What it holds:**
  - **JVN:** Japan-origin vulnerability advisories with JVN#XXXXXXXX identifiers. Primary disclosure coordination and publication channel for Japan-origin vulnerabilities and coordinated multi-vendor issues in Japan.
  - **JVNDB (JVN iPedia):** Comprehensive Japanese-language CVE/NVD mirror with Japanese descriptions, CVSS scores, and CWE mappings. 277,000+ entries. REST API available. Aggregates global CVE data plus Japan-origin disclosures.
  - **JPCERT/CC:** Publishes independent advisories, weekly digest, and participates in APCERT and FIRST.
- **Coverage:** Strong for Japanese software vendors; JVNDB provides near-NVD coverage in Japanese. Distinct from NVD for Japan-origin issues that may not reach MITRE CNAs.
- **Access model:** Free, public access. REST API available for JVNDB.
- **Who uses it:** Japanese government agencies, enterprises, and researchers; Asia-Pacific security teams tracking Japan-origin threat activity.
- **Exploit availability:** Low — primarily disclosure-oriented, limited exploit tracking
- **Geopolitical flags:** Japan-aligned; coordinates with Five Eyes partners; no known manipulation concerns

---

### CNVD — China National Vulnerability Database
- **Operator:** CNCERT/CC (China National Computer Network Emergency Response Technical Team), under MIIT (Ministry of Industry and Information Technology)
- **Website:** https://www.cnvd.org.cn
- **What it holds:** China's primary government vulnerability database. Assigns CNVD-YYYY-NNNNN identifiers to vulnerabilities, including many affecting Chinese software and hardware products that may not have CVE IDs. Required disclosure channel for Chinese critical information infrastructure operators under the 2021 Cybersecurity Law and Data Security Law.
- **Coverage:** ~200,000+ entries. Strong coverage of Chinese domestic software/hardware (Huawei, Hikvision, Dahua, domestic routers, etc.). Many CNVD entries for Chinese products never receive CVE IDs.
- **Access model:** Free web search portal; limited data exports. API access restricted.
- **Who uses it:** Chinese government agencies, domestic enterprises, researchers tracking China-origin software vulnerabilities.
- **Exploit availability:** Minimal — largely disclosure-only
- **GEOPOLITICAL FLAG (HIGH):**
  - Operated under MIIT (China's industrial and telecom ministry); government-mandated disclosure channel
  - Documented: 267+ CNVD entries with retroactively altered publication dates (Recorded Future research) — a pattern of backdating that may be used to obscure when China became aware of vulnerabilities before public disclosure
  - Some CNVD identifiers for Chinese product vulnerabilities have no Western equivalent, creating a coverage gap for organizations assessing Chinese-made hardware (IoT, telecom, ICS equipment)
  - CNVD-2021-27290 (Hikvision RCE) appeared in CNVD months before US researchers documented it via NVD
  - Western organizations should treat CNVD as a supplemental source for Chinese vendor products, but should not rely on its timestamps or completeness for strategic threat assessment
  - Data from CNVD should be correlated against Western sources to detect manipulation patterns

---

### CNNVD — China National Information Security Vulnerability Database
- **Operator:** NLCSRC (National Laboratory for Information Security Risk Assessment), under the **Ministry of State Security (MSS)** — China's primary foreign intelligence agency
- **Website:** https://www.cnnvd.org.cn
- **What it holds:** China's second official government vulnerability database. Assigns CNNVD-YYYYMM-NNNNN identifiers. Overlaps with CNVD but operated by a different ministry (MSS vs. MIIT). Publishes vulnerability entries with timestamps, descriptions, and CVSS scores.
- **Coverage:** ~196,000+ entries. Covers global CVEs plus China-origin vulnerabilities.
- **Access model:** Free web portal; limited API
- **Who uses it:** Chinese government intelligence community; Chinese enterprises; researchers tracking Chinese state vulnerability awareness
- **Exploit availability:** None published — but exploitation timing is the intelligence concern
- **GEOPOLITICAL FLAG (CRITICAL):**
  - **MSS direct operation:** CNNVD is operated by CNITSEC (China Information Technology Security Evaluation Center), the 13th Bureau of China's foreign intelligence service (MSS). Vulnerabilities submitted for registration are evaluated for potential intelligence exploitation value before publication.
  - **Retroactive timestamp manipulation:** Recorded Future documented that CNNVD backdated publication dates for at least 267 vulnerabilities identified as statistical outliers — a pattern consistent with retroactive cover-up of delayed publication that might reveal advance knowledge.
  - **Pre-CVE publication timing:** Multiple studies document cases where CNNVD published vulnerability details days or weeks before the corresponding CVE entry was made public in the US, raising questions about whether China's intelligence services had advance access to vulnerability information from CNAs or other sources.
  - **Atlantic Council analysis ("Sleight of Hand"):** Documents how China uses its vulnerability disclosure regulations to create a pipeline from public CVEs to potential PLA/MSS offensive cyber operations.
  - **Western assessment:** CNNVD data should be treated as potentially manipulated intelligence product, not as a neutral vulnerability reference. Do NOT use CNNVD timestamps as authoritative disclosure dates. Cross-reference all CNNVD entries against CNVD, NVD, and vendor advisories.
  - **2025 update:** Post-VulnCon 2025, CNNVD has reportedly reduced publication of non-CVE vulnerabilities, possibly reflecting regulatory adjustments under China's 2021 Regulations on the Management of Network Product Security Vulnerabilities (RVDM).

---

### FSTEC BDU — Russian Federation Data Security Threats Database
- **Operator:** FSTEC of Russia (Federal Service for Technical and Export Control), Russian Ministry of Defence-affiliated military agency
- **Website:** https://bdu.fstec.ru (Russian-language)
- **What it holds:** Russia's national vulnerability database (BDU = Банк данных угроз безопасности информации). Assigns BDU:YYYY-NNNNN identifiers. Contains vulnerability descriptions, CVSS scores (Russian assessment), and threat modeling data. Focused on vulnerabilities affecting Russian state information systems and critical infrastructure.
- **Coverage:** Only ~10% of global CVEs are published (~11,036 of 107,901+ CVEs). Publishes ~50 days after NVD for vulnerabilities it does cover. Highly selective — focuses on hardware/software used by Russian government agencies.
- **Access model:** Free, Russian-language web portal. Limited machine-readable access.
- **Who uses it:** Russian government agencies, Russian critical infrastructure operators; international researchers tracking Russia's vulnerability awareness
- **Exploit availability:** None published
- **GEOPOLITICAL FLAG (HIGH):**
  - FSTEC is a military agency under the Russian Ministry of Defence, responsible for both export control of weapons/dual-use technology and Russian military information security. Its vulnerability database is effectively a national-security-controlled intelligence product.
  - **Selective publication:** FSTEC has published 61% of vulnerabilities exploited by Russian state-sponsored threat groups. The high correlation between what FSTEC covers and what Russian threat actors use is statistically significant.
  - **Incomplete and delayed coverage:** Publishing only 10% of global CVEs, ~50 days late, with minimal enrichment — makes BDU useless as a neutral vulnerability reference for non-Russian organizations.
  - **Researcher assessment (Dark Reading, Bleeping Computer, The Register):** BDU is described as "sparse and slow" with a focus on Russian government software rather than global coverage. Multiple researchers have noted that BDU coverage decisions appear to prioritize Russian state interests.
  - **Western use cases:** BDU is primarily valuable to researchers studying which vulnerabilities Russia's government is officially tracking (which may indicate offensive interest) and for understanding Russia's internal cybersecurity regulatory posture.
  - **Sanctions context (2022+):** Following Russia's 2022 invasion of Ukraine and subsequent sanctions, BDU has become more isolated from Western vulnerability intelligence sharing. International CERT coordination with Russia is effectively suspended.

---

### KVD — Korea Vulnerability Database (KISA)
- **Operator:** KISA (Korea Internet & Security Agency), under South Korea's Ministry of Science and ICT
- **Website:** https://knvd.krcert.or.kr (Korean-language); international: https://www.krcert.or.kr
- **What it holds:** South Korea's national vulnerability database (formally KrCERT/CC vulnerability coordination). Publishes CVE-referenced advisories, vulnerability countermeasures information, and KVD-assigned identifiers for Korean software. KISA is the Korean CVE Numbering Authority partner.
- **Coverage:** Strong coverage of Korean domestic software (Hancom Office, Korean-language CMS platforms, Korean enterprise software). Global CVE cross-referencing. Korean-language primary.
- **Access model:** Free; Korean-language primary; some English advisory content available
- **Who uses it:** Korean government agencies, Korean enterprises, researchers tracking Korea-origin software vulnerabilities
- **Exploit availability:** Minimal — primarily advisory-focused
- **Geopolitical flags:** South Korea-aligned; no known data manipulation concerns; coordinates with US and Five Eyes partners

---

## TIER 2 — COMMUNITY / OPEN SOURCE DATABASES

### Exploit-DB
- **Operator:** OffSec (Offensive Security), the creators of Kali Linux and OSCP certification
- **Website:** https://www.exploit-db.com
- **What it holds:** Archive of public proof-of-concept exploit code, aggregated from mailing lists (Full Disclosure, oss-security), direct researcher submissions, and CVE-correlated disclosures. Each entry is mapped to a CVE ID where one exists. Powers the `searchsploit` CLI tool for offline searching. Also includes Google Hacking Database (GHDB) dorking queries.
- **Coverage:** 50,000+ exploits. Covers all major platforms and technologies. Many entries predate CVE assignment. Not a complete vulnerability database — only covers publicly released exploit code.
- **Access model:** Free, open, CC BY-SA 4.0. Full offline download available. No API authentication required.
- **Who uses it:** Penetration testers, red teams, security researchers, scanner developers (for weaponization signal)
- **Exploit availability:** This IS an exploit database — PoC/weaponization signal is the entire point. High-quality for confirmed public exploits; not monitored for dark-web or private exploits.
- **Comparison matrix score:** P4=5 (exploit intelligence, best-in-class for free), but P1=2 (incomplete vulnerability coverage), P2=2 (minimal enrichment)

---

### Packet Storm Security
- **Website:** https://packetstormsecurity.com
- **What it holds:** Long-running (since 1998) security advisory and exploit archive. Aggregates vulnerability disclosures, exploit code, security tools, and PoC material from mailing lists and researcher submissions. Covers vulnerabilities not always in structured databases. CVE-searchable.
- **Coverage:** Historical depth (25+ years). Complements Exploit-DB with material the latter does not index, including many vendor advisories and non-CVE security papers.
- **Access model:** Free, no authentication required
- **Who uses it:** Researchers, penetration testers, historical vulnerability researchers
- **Exploit availability:** Yes — exploit code archives, PoC material

---

### Full Disclosure Mailing List / BugTraq Archive
- **Full Disclosure:** https://seclists.org/fulldisclosure (archived at SecLists)
- **BugTraq:** https://seclists.org/bugtraq (archived at SecurityFocus / Broadcom)
- **What they hold:** Full Disclosure is a public mailing list where researchers publish vulnerability details, often before CVE assignment or NVD publication. Critical source for zero-day timeline analysis. BugTraq is the historical predecessor (mid-1990s onward), largely static, but heavily referenced in historical CVE research.
- **Who uses them:** Researchers analyzing disclosure timelines, zero-day researchers, historical CVE attribution work
- **Exploit availability:** Frequently yes — Full Disclosure is intentionally aggressive on technical detail and PoC sharing

---

### GitHub Advisory Database (GHSA)
- **Operator:** GitHub Security Lab (Microsoft subsidiary) with community contributions via pull request
- **Website:** https://github.com/advisories / Bulk download: https://github.com/github/advisory-database
- **What it holds:** CVE and GHSA-prefixed advisories for open-source packages, maintained by GitHub Security Lab and community PRs. Directly integrated with Dependabot and GitHub's dependency graph. Data: CVSS v3.1 and v4.0 scores, affected version ranges (purl-based), CWE classifications, EPSS daily sync (added 2025), KEV status flags, and VEX integration planning.
- **Coverage:** 25,000+ reviewed advisories covering npm, PyPI, Maven, Go, Ruby, Rust, NuGet, Pub, and more.
- **Access model:** Free, CC BY 4.0. REST API, GraphQL API, bulk GitHub download. No authentication for read access.
- **Who uses it:** GitHub Dependabot (auto-generates PRs for vulnerable deps), SCA tools, OSV aggregates from it
- **2025–2026 updates:** Empirical mean listing time after disclosure: 2.4 days (second-fastest free DB). Daily EPSS sync. Growing CVSS v4.0 adoption (1,153 CVEs scored v4 as of 2025). Comparison matrix score: P2=5, P3=5 (upgraded in 2026 re-analysis).
- **Exploit availability:** Low — focused on disclosure/remediation, not weaponization

---

### OSV — Open Source Vulnerabilities (Google)
- **Operator:** Google, with contributions from the open-source ecosystem
- **Website:** https://osv.dev / API: https://api.osv.dev
- **What it holds:** Structured open-source vulnerability database with precise version ranges (package URL / purl-based). Aggregates from 28+ ecosystem advisory feeds: Go, Rust (RustSec), Python (PyPA), npm (GHSA), Maven, Ruby, Alpine, Debian, Ubuntu, and more. JSON schema published as OSV format (becoming a de-facto standard).
- **Coverage:** 84,520+ vulnerabilities across 28+ ecosystems as of 2025. Best-in-class for open-source software component vulnerabilities.
- **Access model:** Free, CC0. REST API (/v1/querybatch for bulk SBOM matching), bulk JSON download. No authentication.
- **Who uses it:** Syft, Grype, Trivy, Dependency-Track, academic researchers, SBOM-based vulnerability matching workflows
- **2025 empirical data:** Mean listing time after disclosure: 1.8 days — fastest free vulnerability database measured in 2025 study (NVD: 6.2 days). Comparison matrix score: P3=5, P7=5 (best purl/SBOM matching).
- **Exploit availability:** Minimal — focused on OSS component disclosure and remediation
- **Note:** OSV schema has been adopted across ecosystems (Hex/Erlang, Haskell/Hackage, Dart/Flutter/Pub, CRAN/R), making osv.dev the de-facto aggregator for the full open-source vulnerability universe.

---

### VulDB
- **Operator:** Independent commercial research CNA; Swiss/German origin
- **Website:** https://vuldb.com
- **What it holds:** Independent vulnerability database with 250,000+ entries. Provides CVSS v3.1 and v4.0 (including Temporal scores), exploitation timeline data, patch status tracking, and countermeasure guidance. Research team independently scores vulnerabilities rather than relying solely on NVD assessments.
- **Coverage:** Global; covers commercial and open-source software. Notable for systematic publication of CVSS v4.0 scores — VulDB accounts for approximately **49% of all CVSS v4 scores published globally** as of 2026 (Mondoo data), making it the single most significant contributor to the new scoring standard.
- **Access model:** Freemium. Free web browsing with limited lookups; API and bulk export require paid subscription.
- **Who uses it:** Security researchers, VM platforms needing CVSS v4 data, threat intelligence teams
- **Exploit availability:** Includes exploitation timeline and likelihood scoring; tracks whether exploits are available
- **Comparison matrix score:** P6=5 (risk scoring — upgraded 2026 based on 49% global CVSS v4 share and systematic Temporal scoring)

---

### Vulners
- **Operator:** Vulners.com (Russian-origin commercial company; current operational status post-2022 sanctions uncertain)
- **Website:** https://vulners.com
- **What it holds:** Vulnerability intelligence search engine and API aggregating CVEs, security advisories, exploit code, and patch bulletins from 200+ sources (NVD, vendor advisories, Exploit-DB, Packet Storm, BugTraq) into a unified searchable index. SBOM scanning endpoints on commercial tier.
- **Coverage:** Broad aggregation; one of the most comprehensive free-tier search engines for cross-source vulnerability lookup.
- **Access model:** Freemium. Free web browsing and limited queries; commercial API subscriptions for bulk export, higher rate limits, and SBOM scanning.
- **Who uses it:** Penetration testers, researchers, SIEM integrators, automated enrichment pipelines
- **Exploit availability:** Yes — aggregates exploit code from multiple sources, surfaced alongside CVE data
- **GEOPOLITICAL FLAG (MODERATE):**
  - Russian-origin company; founded by Kir Ermakov and team based in Russia
  - Post-2022 Ukraine invasion: operational status and data handling practices under Russian law (including SORM/FSB access requirements) are uncertain for Western users
  - Russian data localization laws potentially expose user query data and vulnerability research activity to Russian state access
  - **Recommendation for Western users:** Treat as a useful aggregation tool for technical research, but avoid submitting sensitive vulnerability research or organizational data. Consider EU/US-hosted alternatives (CIRCL Vulnerability Lookup, OpenCVE) for environments with data residency requirements.

---

### Sploitus
- **Website:** https://sploitus.com
- **What it holds:** Open exploit and PoC search engine aggregating Exploit-DB, GitHub repositories, Packet Storm, and other community sources. Searchable by CVE ID or keyword. Surfaces newly published PoC code within hours of public release.
- **Access model:** Free, no authentication required
- **Who uses it:** Penetration testers needing quick PoC availability checks; researchers tracking public exploit release timing
- **Exploit availability:** This IS an exploit aggregator — its entire purpose is surfacing PoC/exploit code
- **Comparison matrix score:** P4=4, but low scores overall (Total: 42/100) due to minimal enrichment and governance

---

### OpenCVE
- **Website:** https://www.opencve.io (SaaS) or self-hosted: https://github.com/opencve/opencve
- **What it holds:** Open-source CVE monitoring and alerting platform. Subscribes to MITRE CVE feed and NVD enrichment; provides dashboard, vendor/product subscription model, webhook/email alerting for new and modified CVEs, and REST API. Self-hostable for full data privacy.
- **Coverage:** Full CVE/NVD coverage through feed subscription. EPSS and KEV integration available.
- **Access model:** Freemium (SaaS: free tier with limits; paid for higher-volume alerting). Self-hosted: fully free and unlimited.
- **Who uses it:** Security teams needing CVE monitoring dashboards; organizations wanting alerting on specific vendor/product CVE activity without commercial VM platform costs
- **Exploit availability:** No — alerting tool that surfaces CVEs from NVD; not an exploit database

---

### InTheWild.io
- **Website:** https://inthewild.io
- **What it holds:** Community-contributed and research-aggregated database tracking CVEs with confirmed or suspected in-the-wild exploitation evidence. Cross-references CISA KEV, researcher reports, vendor advisories, and threat intelligence to flag CVEs with exploitation evidence broader than KEV alone.
- **Coverage:** Targets the gap between KEV (confirmed exploitation, 1,484 entries) and the full CVE universe. Community-curated exploitation evidence.
- **Access model:** Free web access; API available
- **Who uses it:** Threat intelligence analysts, VM prioritization workflows wanting broader exploitation coverage than CISA KEV alone
- **Exploit availability:** Yes — exploitation evidence tracking is its core function

---

### VulnCheck
- **Operator:** VulnCheck (founded 2022, led by ex-NVD team members including Patrick Garrity)
- **Website:** https://vulncheck.com
- **Funding:** $25M Series B financing (February 2026, reported by BusinessWire)
- **What it holds:**
  - **NVD++:** Free community service providing NVD enrichment for CVEs that NIST has deprioritized. CPE coverage: 76.95% of 2024 CVEs vs. NVD's 41.35%. Critical supplement post-April 2026 NVD triage policy.
  - **VulnCheck KEV:** Expanded Known Exploited Vulnerabilities catalog — 3,600+ entries as of 2025 (173% more than CISA KEV). Tracked 884 new exploited CVEs in 2025 alone (3.6x CISA's 245 additions in the same period).
  - **Exploit Intelligence:** Tracked 14,000+ distinct exploits for 10,000+ unique CVEs in 2025 (500+ data sources). 2026 Exploit Intelligence Report published.
  - **Exploitation Timeline Data:** Best-in-class tracking of when exploitation begins relative to CVE disclosure.
- **Coverage:** 10,000+ CVEs with exploitation intelligence; NVD++ covering 76.95% of the CPE gap
- **Access model:** Freemium. Community tier free (NVD++, limited KEV). Commercial API subscriptions for full exploit intelligence, bulk feeds, and integrations.
- **Who uses it:** Enterprise SOC teams, VM platforms, researchers filling the NVD enrichment gap, threat intelligence teams
- **Exploit availability:** Excellent — characterises weaponization level, active exploitation status, and exploit availability per CVE
- **Comparison matrix score:** Total 77/100 (upgraded 2026: P1 to 4 based on coverage breadth, P4=5 for exploit intelligence)

---

### Nuclei Templates (ProjectDiscovery)
- **Operator:** ProjectDiscovery (community-led, open-source)
- **Website:** https://github.com/projectdiscovery/nuclei-templates
- **What it holds:** Community-maintained YAML-format network and web vulnerability detection templates, the majority keyed to specific CVE IDs. Each template can verify exploitability (active detection, not just banner-based). Over 9,000+ templates contributed by thousands of researchers.
- **Coverage:** Best-in-class for detection template availability. A Nuclei template existing for a CVE is a strong signal of real-world exploitability.
- **Access model:** Completely free, MIT license. GitHub-hosted, can be run offline.
- **Who uses it:** Penetration testers, bug bounty hunters, red teams, vulnerability verification workflows
- **Exploit availability:** Nuclei templates ARE weaponization indicators — each template constitutes a working verification/exploitation proof
- **Note:** CVEMap (ProjectDiscovery) is a companion CLI tool querying NVD + OSV enriched with CISA KEV status, EPSS scores, and Nuclei template availability — creating a free triage pipeline from a single command.

---

## TIER 3 — COMMERCIAL DATABASES

### Zero Day Initiative (ZDI) — Trend Micro
- **Operator:** Trend Micro (acquired from HP TippingPoint in 2016); now branded as "TrendAI ZDI"
- **Website:** https://www.zerodayinitiative.com
- **What it holds:** World's largest vendor-agnostic bug bounty program and vulnerability intelligence database. Acquires zero-day vulnerabilities from independent researchers, coordinates disclosure with affected vendors under a 120-day deadline policy, and publishes advisories (ZDI-YY-NNNNN) after patch or deadline. 15,000+ vulnerabilities disclosed over 20 years. 1,000+ unique vulnerabilities published in 2023 (most recent public figure).
- **Research scale:** 450+ dedicated researchers across 14 global threat centers; 19,000+ independent researcher community
- **Coverage:** Broad — enterprise software, network devices, industrial control systems, mobile. Particularly strong for ICS/SCADA (Pwn2Own ICS track), browsers, and enterprise applications.
- **Access model:** Freemium. Free advisories on website (with pre-patch notification to Trend Micro customers). Subscription tier for earlier access and TippingPoint virtual patching signatures (filters). Average 90+ days of protection ahead of vendor patches for TippingPoint customers.
- **Who uses it:** Enterprise customers needing pre-patch detection; penetration testers; researchers tracking 0-day disclosures; all parties monitoring Pwn2Own results
- **Exploit availability:** Yes — ZDI advisories include technical details and sometimes PoC code post-patch. Pre-patch detection via TippingPoint digital vaccine signatures.
- **Comparison matrix score:** Total 67/100; P4=5 (unique 0-day pre-patch intelligence)

---

### Tenable Research / Nessus Plugin Database
- **Operator:** Tenable, Inc. (NASDAQ: TENB)
- **Website:** https://www.tenable.com/plugins
- **What it holds:**
  - 334,320+ Nessus plugins covering 119,000+ CVEs (2025 figures)
  - **VPR (Vulnerability Priority Rating):** Predictive risk score using 150+ factors including CVSS, EPSS, exploit code maturity, threat intelligence signals, KEV status, and active threat activity. Updated continuously — not static.
  - **AI-enhanced VPR** launched 2025
  - **IoT plugin families:** Dedicated Nessus Network Monitor (NNM) plugin families for VxWorks, IP phones, smart devices, industrial equipment
  - Lumin Exposure View for contextual organizational risk scoring
- **Coverage:** Broadest plugin coverage in the commercial VM market. FedRAMP authorized.
- **Access model:** Commercial. Per-asset licensing or subscription. Plugins are bundled with Nessus and Tenable.sc products.
- **Who uses it:** Enterprise security teams, managed security service providers, US federal agencies (FedRAMP)
- **Exploit availability:** VPR incorporates exploit availability and weaponization status as scoring factors
- **Comparison matrix score:** Total 73/100; P6=5 (VPR is one of the top risk scoring systems), P14=3 (IoT plugin families)

---

### Rapid7 InsightVM / Metasploit Modules Database
- **Operator:** Rapid7, Inc. (NASDAQ: RPD)
- **Website:** https://www.rapid7.com/products/insightvm / https://www.metasploit.com
- **What it holds:**
  - **InsightVM/Nexpose:** Vulnerability knowledge base with "Active Risk" composite score (EPSS+KEV+contextual weighting). Threat Feed flags active exploitation including zero-days before CVSS scores exist.
  - **Metasploit Framework:** Open-source exploitation framework with 2,300+ CVE-mapped exploit and auxiliary modules. Community-maintained; module presence is a well-established weaponization signal. Module database on GitHub (BSD license).
  - **RealRisk score:** Draws on exploit kit availability, malware association data, Rapid7 honeypot telemetry (Project Heisenberg), and community signals.
  - **IntSights acquisition (2021):** Added dark web and criminal forum CVE monitoring to Rapid7's intelligence stack.
  - **AttackerKB integration:** Community-assessed exploitability ratings complement EPSS.
- **Coverage:** Full NVD CVE scope plus Rapid7's extended research. AttackerKB provides practitioner-level exploitability assessment.
- **Access model:** Commercial for InsightVM. Metasploit Framework: free, open-source (BSD). AttackerKB: free community platform.
- **Who uses it:** Enterprise red teams, SOC teams, penetration testers globally
- **Exploit availability:** Excellent — Metasploit is a weaponized exploit framework; module presence = weaponization confirmation
- **Comparison matrix score:** Total 74/100; P4=5 (Metasploit), P6=5 (Active Risk scoring)

---

### Qualys VMDR / Threat Protection
- **Operator:** Qualys, Inc. (NASDAQ: QLYS)
- **Website:** https://www.qualys.com/apps/threat-protection
- **What it holds:**
  - 25,000+ vulnerability signatures in KnowledgeBase
  - **TruRisk 2.0:** Risk scoring combining CVSS v4, EPSS, KEV, asset criticality, business context, and Qualys RTI (Real-Time Threat Indicators)
  - **RTIs:** Active exploitation, malware association, wormability, exploit kit presence, public exploit code, denial of service risk — continuously updated
  - **Asset Criticality Rating (ACR):** Contextual scoring per organizational asset
  - Daily security alerts with structured remediation references
- **Coverage:** Full NVD CVE scope; OT/ICS coverage growing; FedRAMP authorized
- **Access model:** Commercial SaaS; per-asset licensing. Part of Qualys Cloud Platform suite.
- **Who uses it:** Enterprise VM programs, US federal agencies, managed service providers
- **Exploit availability:** RTIs track active exploitation, malware, and exploit kit presence per CVE in real time
- **Comparison matrix score:** Total 74/100; P7=5 (asset matching), P6=5 (TruRisk 2.0)

---

### CrowdStrike Falcon Spotlight
- **Operator:** CrowdStrike Holdings, Inc. (NASDAQ: CRWD)
- **Website:** https://www.crowdstrike.com/products/exposure-management/falcon-spotlight-vulnerability-management/
- **What it holds:** Agentless VM module within Falcon platform. Delivers real-time CVE exposure from the same sensor used for EDR — no separate scanning agent. **ExPRT.AI** risk scores correlate CVE exposure with CrowdStrike's named adversary intelligence (Bears, Pandas, Kittens) to surface CVEs being actively targeted by specific threat actors.
- **Coverage:** Real-time exposure data across endpoints; integrates CrowdStrike's adversary attribution (one of the deepest threat actor databases in the industry).
- **Access model:** Commercial; requires Falcon platform subscription
- **Who uses it:** CrowdStrike customers wanting integrated EDR+VM with adversary context
- **Exploit availability:** ExPRT.AI incorporates exploitation signals; CrowdStrike adversary intelligence flags which CVEs specific named actors are exploiting
- **Comparison matrix score:** Total 69/100; P3=5 (fastest weaponization detection), P5=5 (adversary attribution)

---

### Recorded Future Vulnerability Intelligence
- **Operator:** Recorded Future (Nasdaq: RDDT parent: Mastercard acquired 2024 for ~$2.65B)
- **Website:** https://www.recordedfuture.com/solutions/vulnerability-management
- **What it holds:** SaaS platform monitoring dark web criminal forums, technical communities, paste sites, and code repositories across 10+ languages for CVE-specific exploitation activity. ML-generated risk scores incorporating when CVEs are gaining underground attention. STIX export. Temporal risk scoring that updates as threat context changes.
- **Key 2025 data:** 53% of H1 2025 exploitation attributed to state-sponsored actors (Recorded Future data).
- **Coverage:** Global; particularly strong for state-sponsored threat actor attribution and dark web exploitation signals. Pre-KEV exploitation detection capability.
- **Access model:** Commercial. High six-figure USD pricing for small teams (AWS Marketplace multi-year packages documented in the $100k–$200k+ range).
- **Who uses it:** Enterprise SOC teams, threat intelligence programs, government agencies
- **Exploit availability:** Excellent — dark web forum monitoring, exploit sales tracking, pre-disclosure signals
- **Comparison matrix score:** Total 76/100; P5=5 (threat context), P4=5 (exploit intelligence), P6=5 (temporal risk scoring)

---

### Flashpoint VulnDB
- **Operator:** Flashpoint (formed from Flashpoint acquisition of Risk Based Security in 2022)
- **Website:** https://flashpoint.io/vulndb
- **What it holds:** Most comprehensive commercial vulnerability database by raw entry count: 400,000+ vulnerability entries, including 100,000+ not in NVD. Features: curated CVSS conflict resolution, CNVD/CNNVD/JVN cross-mapping, dark web intelligence integration, editorial enrichment, ransomware prediction, and **Flashpoint KEV** (5,100+ confirmed-exploited CVEs — 3x+ CISA KEV).
- **Lineage:** Risk Based Security (RBS) pioneered commercial CVE enrichment beyond NVD scope; merged into Flashpoint 2022.
- **Coverage:** Widest scope of any commercial database — covers non-CVE vulnerabilities, China/Russia/Japan-origin IDs, dark web chatter-linked CVEs.
- **Access model:** Commercial. Enterprise licensing. REST API, ServiceNow integration.
- **Who uses it:** Enterprise SOC teams, vulnerability management programs, organizations with complex international supply chains needing CNVD/CNNVD coverage
- **Exploit availability:** Excellent — dark web intelligence, weaponization indicators, ransomware prediction, Flashpoint KEV (5,100+ exploited)
- **Comparison matrix score:** Total 78/100 (highest-scoring database in the comparison matrix)

---

### VARIoT — Vulnerability and Exploit Database for IoT
- **Operator:** CIRCL (Computer Incident Response Center Luxembourg) under EU Horizon 2020 funding
- **Website:** https://www.variot.eu
- **What it holds:** IoT-specific vulnerability and exploit database aggregating CVEs, exploit data, and vendor advisories for embedded systems, routers, smart devices, and industrial IoT hardware not well-covered by NVD. Structured JSON API.
- **Coverage:** IoT-focused; fills gaps where NVD CPE mappings for embedded devices are incomplete or absent.
- **Access model:** Free. REST API available.
- **Who uses it:** IoT security researchers, CERT teams, embedded security engineers, EU-funded security projects
- **Exploit availability:** Includes exploit data for IoT-specific vulnerabilities
- **Comparison matrix score:** P14=5 (IoT-specific coverage is best-in-class free source with CISA ICS-CERT)

---

### Claroty Research / xDome (OT/ICS)
- **Operator:** Claroty (commercial)
- **Website:** https://www.claroty.com
- **What it holds:** Industrial and healthcare IoT vulnerability intelligence within the Claroty Platform (which acquired Medigate). Tracks CVEs for OT devices, medical devices, and building management systems. Scores findings with OT-specific risk context (network reachability within Purdue Model segments, safety impact). CISA ICS-CERT advisory cross-references. Zone/Conduit-aware risk scoring. ISA/IEC 62443 compliance reporting.
- **Research arm:** **Team82** — Claroty's OT, IoT, and medical device security research team. Publishes original CVE discoveries, exploitation analysis, and protocol vulnerability research. Free research output.
- **Coverage:** Deep OT/ICS/medical device coverage. First Gartner MQ for CPS Protection Platforms (February 2025).
- **Access model:** Commercial platform. Team82 research: free public reports.
- **Who uses it:** Critical infrastructure operators, hospital networks, manufacturing enterprises
- **Exploit availability:** OT-specific exploitation context; physical safety impact assessment
- **Comparison matrix score:** Total 69/100; P14=5 (IoT/OT specific)

---

### Dragos Vulnerability Intelligence (ICS)
- **Operator:** Dragos, Inc. (commercial)
- **Website:** https://www.dragos.com
- **What it holds:** ICS/OT-specific vulnerability intelligence for PLCs, DCS, HMI, and SCADA components (Siemens, Rockwell, Schneider Electric, Honeywell). Dragos scores vulnerabilities for OT impact (safety, reliability, process disruption) and correlates with ICS threat groups tracked by Dragos WorldView. Tracks named OT threat actors including VOLTZITE, KAMACITE, SYLVANITE (new 2025), and other ICS-targeting groups.
- **Key findings (2025):** 508 CISA ICS advisories in 2025 (record year); 82% rated High/Critical; 25% of NVD CVSS scores for ICS CVEs are incorrect per Dragos analysis.
- **Coverage:** Best-in-class for OT/ICS environments. "Now/Next/Never" prioritization framework unique to industrial settings.
- **Access model:** Commercial. Dragos WorldView for threat intelligence subscription.
- **Who uses it:** Electric utilities, oil and gas, manufacturing, critical infrastructure operators
- **Exploit availability:** ICS-specific exploitation context; threat actor exploitation correlation via Dragos WorldView
- **Comparison matrix score:** Total 69/100; P14=5, P5=5 (OT threat groups)

---

### Nozomi Networks Research (ICS)
- **Operator:** Nozomi Networks (commercial; Advent International-backed)
- **Website:** https://www.nozominetworks.com
- **What it holds:** OT and IoT vulnerability management within Guardian and Vantage platforms. Continuously monitors ICS environments for CVE exposure, correlates with Nozomi Threat Intelligence feeds. CVE-to-device mapping, patch availability tracking, compensating control recommendations for unpatchable OT systems.
- **Coverage:** Deep ICS/OT passive network discovery; broad ICS protocol support (Modbus, DNP3, IEC 61850, etc.)
- **Access model:** Commercial
- **Who uses it:** Industrial operators, utility companies, manufacturing enterprises
- **Exploit availability:** OT-specific exploitation context
- **Comparison matrix score:** Total 69/100; P14=5

---

## TIER 4 — GRAY/OFFENSIVE OPERATORS

### Zerodium
- **Operator:** Zerodium LLC; founder: Chaouki Bekrar (French national; formerly VUPEN CEO)
- **Website:** https://zerodium.com
- **Jurisdiction:** Originally registered in Washington DC, USA; operational team in France/Europe
- **Employee count (April 2026):** 3 employees (Tracxn data)
- **What it holds:** The world's most prominent commercial zero-day exploit broker. Acquires unpatched ("0-day") vulnerabilities from independent researchers and sells the resulting intelligence — plus technical documentation and sometimes weaponized exploit code — to government, military, and intelligence agency clients via subscription-based ZERODIUM Security Research Feed (Z-SRF). Does NOT disclose vulnerabilities to vendors.
- **Data held:** Proprietary catalog of unpatched zero-day exploits across mobile OS (iOS, Android), browsers, enterprise software, messaging apps (WhatsApp, Signal, iMessage), and network infrastructure. Clients receive technical briefings plus pre-patch exploitation capability.
- **Price schedule (current):**
  - iOS full-chain remote jailbreak (zero-click): up to $2.5 million
  - Android full-chain remote code execution (zero-click): up to $2.5 million
  - WhatsApp/Signal/iMessage zero-click RCE: up to $1.5–2 million
  - General mobile RCE: up to $2 million
  - Estimated monthly spending on acquisitions: $1–3 million
  - Prices inflating at ~44% annually per market analysts
- **Coverage:** Mobile OS, browsers, messaging platforms, enterprise software, VPN/router firmware
- **Access model:** Government/intelligence agencies only via Z-SRF subscription. Researchers submit via zerodium.com/program. No public database.
- **Who uses it:** US, European, and allied government intelligence and military agencies. Historically also sold to non-Western governments (controversial).
- **Exploit availability:** This IS an offensive exploitation capability broker — the entire business is weaponized exploits
- **GEOPOLITICAL FLAG (CRITICAL — WESTERN GRAY ZONE):**
  - Operates legally in Western jurisdictions but sells offensive exploitation capability for use by intelligence agencies
  - 2021 controversy: Zerodium publicly stated it was no longer purchasing Tor Browser exploits because there were "too many" — interpreted as evidence of large existing Tor exploit stockpile
  - No vendor disclosure; purchased zero-days are NOT disclosed to affected vendors, creating a stockpiling dynamic that extends exploitation windows
  - Historically sold to clients beyond Five Eyes allies — including reports of sales to countries with questionable human rights records
  - Distinct from ZDI (which requires vendor disclosure within 120 days) — Zerodium has no mandatory disclosure commitment
  - Under US ITAR/EAR export control scrutiny; export of offensive cyber tools classified as munitions in many jurisdictions

---

### Crowdfense
- **Operator:** Crowdfense Ltd (Abu Dhabi, UAE); currently under potential acquisition by EDGE Group (UAE defense conglomerate)
- **Website:** https://www.crowdfense.com
- **What it holds:** UAE-based zero-day exploit acquisition and brokering platform. Operates the Exploit Acquisition Program (EAP) — a $30 million program (2024 expansion). Also operates the **Crowdfense N-Day Vulnerability Feed** (strategic partnership with NDAY Security announced March 2026).
- **Price schedule (published 2024):**
  - iOS zero-click full-chain RCE: up to $7 million
  - Android zero-click full-chain RCE: up to $5 million
  - Scope expanded to Enterprise Software, WiFi/Baseband, and Messengers
  - $30M total EAP budget
- **Coverage:** Mobile OS (iOS, Android), enterprise software, messaging apps, WiFi/baseband firmware
- **Access model:** Government/intelligence clients only. Researchers submit via crowdfense.com/exploit-acquisition-program.
- **Who uses it:** UAE government intelligence (likely direct buyer given EDGE Group interest); other Gulf state and international intelligence agencies.
- **Exploit availability:** Full offensive exploitation capability — weaponized zero-days with no mandatory vendor disclosure
- **GEOPOLITICAL FLAG (CRITICAL — UAE/GULF REGION):**
  - **UAE EDGE Group acquisition interest:** Tactical Report documented that UAE defense company EDGE Group (Abu Dhabi-based, operates within the UAE defense-industrial complex) is actively pursuing Crowdfense acquisition. EDGE Group is linked to UAE military and intelligence community and has been associated with offensive cyber programs (including Project Raven/DarkMatter controversies).
  - **No US/EU regulatory framework:** Unlike Zerodium (US-registered), Crowdfense operates outside US ITAR/EAR jurisdiction and EU dual-use export controls. UAE has no equivalent export control framework for offensive cyber tools.
  - **Human rights risk:** UAE has used offensive cyber capabilities (Pegasus/DarkMatter) against dissidents, journalists, and activists. Crowdfense's UAE base and potential EDGE Group acquisition raises serious concerns about the end-use of acquired zero-days.
  - **Intelligence community caution:** Western security researchers are advised to understand that zero-days sold to Crowdfense may ultimately be deployed by UAE intelligence against targets that include Western-ally activists, journalists, and potentially US/EU persons.
  - **Operational security note:** Any researcher interacting with Crowdfense's platform should assume their identity and research interests are visible to UAE intelligence.
  - **NDAY Security partnership (2026):** Crowdfense now also supplies N-day (known, unpatched) vulnerability intelligence to NDAY Security's commercial platform — a shift from pure zero-day brokering toward commoditized n-day intelligence.

---

### Vupen Security (Historical — Dissolved)
- **Operator:** VUPEN Security; founder: Chaouki Bekrar (France); dissolved ~2015
- **What it was:** French exploit brokering company that sold zero-day exploits and offensive tools to Western government agencies (primarily NATO members) before dissolving and reconstituting as Zerodium in 2015.
- **Historical significance:** First major public-facing commercial zero-day broker to openly operate in the Western market. Won Pwn2Own competitions and retained the exploits (refusing to disclose to vendors), demonstrating the broker model publicly. Dissolved after French export control scrutiny and reconstituted as Zerodium (US-registered) — partly to operate under US rather than French export control jurisdiction.
- **Current status:** Defunct. Bekrar's current operation is Zerodium.

---

### Dark Web Exploit Markets
- **Operators:** Anonymous/pseudonymous; primarily Russian-language but increasingly multinational
- **Active markets (2025–2026):** TorZon, Nemesis Market, STYX Market, Russian Market (dominant for credentials/stealer logs), XSS forum, Exploit.in forum, RaidForums successors
- **What they hold:**
  - **CVE exploit kits:** Weaponized exploit code for known CVEs, sold as standalone modules or bundled into crimeware kits
  - **Zero-day exploits:** Rarely but significantly — some zero-days appear on criminal forums before public disclosure
  - **Initial access listings:** Network access to organizations exploited via specific CVEs, sold by Initial Access Brokers (IABs)
  - **Ransomware-as-a-Service (RaaS) kits:** Include exploit components for initial access vulnerabilities
  - **Stealer logs:** Credentials harvested via malware exploiting CVEs; sold on Russian Market and similar
- **Market size (2025):** Darknet market crypto flows reached ~$2.6 billion in 2025 (Chainalysis estimate). Dark web marketplaces grew 28% in 2025 despite law enforcement operations.
- **Pricing examples:** CVE exploit modules typically $500–$50,000 depending on recency, reliability, and unpatched-status. Zero-day capabilities on criminal forums: $50,000–$500,000+.
- **Who uses them:** Ransomware groups, nation-state-affiliated cybercriminals, Initial Access Brokers, espionage actors
- **Who monitors them:** Cybersixgill (DVE Score), Recorded Future, Flashpoint, Intel 471, DarkOwl, Kela Cyber, Flare Systems — all commercial platforms monitoring dark web CVE exploitation chatter
- **GEOPOLITICAL FLAG (HIGH):**
  - Russian-language forums (XSS, Exploit.in) are the primary market infrastructure; operating under de-facto Russian state tolerance
  - Dark web exploitation intelligence is 100% commercially gated — minimum ~$50,000/year for quality platforms (Cybersixgill, Recorded Future)
  - Law enforcement operations (Operation Endgame, etc.) periodically disrupt market infrastructure but new markets consistently emerge

---

### Canvas Exploit Framework (Immunity / Fortra)
- **Operator:** Originally Immunity Inc. (Dave Aitel); now operated by Fortra (formerly HelpSystems)
- **Website:** https://www.immunitysec.com / Fortra: https://www.fortra.com
- **What it holds:** Commercial penetration testing and exploit development platform with 370+ exploits. Less expensive than CORE Impact or commercial Metasploit. Includes exploit development and testing framework. SILICA (WiFi) and D2 Elliot Web exploitation framework variants also exist.
- **Coverage:** Network exploits, web application, WiFi — primarily classic enterprise infrastructure
- **Access model:** Commercial license. Primarily sold to security consultants, government red teams, and defense contractors.
- **Who uses it:** Penetration testers, offensive security teams, government red teams
- **Exploit availability:** Commercial weaponized exploitation framework — exploits are the core product

---

### CORE Impact (Core Security / Fortra)
- **Operator:** Core Security (founded 1996, Buenos Aires/Boston origins); acquired by Fortra (formerly HelpSystems). Research now conducted by Fortra Intelligence & Research Experts (FIRE) group.
- **Website:** https://www.coresecurity.com/products/core-impact
- **What it holds:** Enterprise-grade penetration testing platform with a certified exploit library (formerly Core Labs, now FIRE team). Library is continuously updated with verified, high-impact, reliable exploits matching current threat-actor techniques. H2 2025 update blog published. Custom pricing; quote-based licensing.
- **Coverage:** Network infrastructure, web applications, endpoints, social engineering modules; ICS/SCADA modules available
- **Access model:** Commercial. Enterprise licensing via Fortra.
- **Who uses it:** Enterprise security teams, government agencies, large consulting firms
- **Exploit availability:** Certified weaponized exploit library — quality-controlled commercial exploitation framework
- **Note:** Distinct from the CISA ICS-CERT's use of "CORE" acronym — this is the Core Security commercial product

---

## TIER 5 — VENDOR ADVISORY PROGRAMS

### MSRC — Microsoft Security Response Center
- **Website:** https://msrc.microsoft.com / CVSS API and CSAF feeds available
- **What it holds:** Authoritative advisory database for all Microsoft products (Windows, Azure, M365, etc.). CVSS v4.0 with Exploitability Index; CSAF 2.0 machine-readable advisories; Patch Tuesday (second Tuesday of each month) coordination. MSRC Exploitability Index provides analyst-calibrated exploitability ratings distinct from CVSS.
- **Coverage:** All Microsoft products and services globally
- **Access model:** Free, public
- **Comparison matrix score:** Total 75/100; gold standard for CVSS v4 adoption and CSAF 2.0 machine-readable output

---

### Google Project Zero
- **Website:** https://project zero.googleblog.com / Issue tracker: https://bugs.chromium.org/p/project-zero
- **What it holds:** Elite zero-day research team. Discovers vulnerabilities in third-party products; publishes full technical details under 90-day disclosure policy (regardless of patch availability). Bug tracker is public and provides the most detailed technical record of discovered flaws, often months before NVD enrichment.
- **Coverage:** Major platforms — Windows, iOS/macOS, Android, browsers, chipsets, cloud infrastructure
- **Access model:** Free, completely public
- **Exploit availability:** Technical details and PoC published — intentionally detailed to pressure vendor response

---

### Apple PSRT — Product Security Response Team
- **Website:** https://support.apple.com/en-us/111900 (HT-series security content articles)
- **What it holds:** HT-series articles documenting CVEs fixed in macOS, iOS/iPadOS, watchOS, tvOS, visionOS, and Safari. Per-CVE descriptions, credit, and fix details.
- **Coverage:** Apple product ecosystem
- **Access model:** Free, public
- **Note:** Apple's security advisory culture is historically closed (minimal technical detail, no pre-patch disclosure); improving post-iPhone "Blastdoor" era

---

### Cisco PSIRT
- **Website:** https://sec.cloudapps.cisco.com/security/center
- **What it holds:** CVSS v4.0 with Cisco-specific environmental scores; CSAF 2.0 machine-readable advisories; Security Impact Rating (SIR) overlay providing Cisco's own severity assessment distinct from NVD; active exploitation flags.
- **Coverage:** All Cisco products: IOS, IOS XE, NX-OS, ASA, FTD, UCS, collaboration, etc.
- **Access model:** Free, public. CSAF feeds available for automated ingestion.
- **Comparison matrix score:** Total 72/100; best vendor PSIRT data quality in the comparison matrix; P18=5 (patch tracking)

---

### Oracle CPU — Critical Patch Update
- **Website:** https://www.oracle.com/security-alerts
- **What it holds:** Quarterly bulk patch releases (January, April, July, October) addressing CVEs across all Oracle products (Database, Java, MySQL, WebLogic, E-Business Suite, Fusion Middleware, cloud services).
- **Coverage:** Oracle product ecosystem — extremely broad including many enterprise and legacy systems
- **Access model:** Free, public. CPU advisories are machine-readable. Risk Matrix published with CVSS scores.
- **Note:** Quarterly release cycle creates known remediation gaps; Oracle tends to publish minimal technical detail until patches ship

---

### Red Hat RHSA — Security Advisories
- **Website:** https://access.redhat.com/security/security-updates/#/security-advisories / API: access.redhat.com/hydra/rest/securitydata
- **What it holds:** Security advisories for RHEL, Fedora, RHCOS (OpenShift), and related products. Includes Red Hat's independently validated CVSS scores that often differ from NVD — Red Hat publishes both its score and NVD's score side-by-side with documented justification for divergence. Machine-readable via REST API and OVAL.
- **Coverage:** Red Hat product ecosystem (RHEL, Fedora, OpenShift, JBoss, Satellite)
- **Access model:** Free, public API (access.redhat.com/hydra/rest/securitydata)
- **2026 significance:** With NVD accuracy at 12% per OIG audit, Red Hat's independently validated, context-adjusted CVSS scores have become the most reliable free source of quality risk scoring for Linux infrastructure.
- **Comparison matrix score:** Total 74/100; P6=5 (upgraded 2026 — independent contextual CVSS with documented justification is best-in-class for free Linux risk scoring)

---

### Ubuntu / Canonical USN — Ubuntu Security Notices
- **Website:** https://ubuntu.com/security/notices / CVE tracker: ubuntu.com/security/cve
- **What it holds:** Security notices for Ubuntu LTS and current releases. Per-package, per-release CVE fix status. Machine-readable exports. Launchpad-hosted CVE tracker (launchpad.net/ubuntu-cve-tracker).
- **Coverage:** Ubuntu/Canonical product ecosystem
- **Access model:** Free, public

---

### Siemens ProductCERT
- **Website:** https://cert.siemens.com / CSAF feeds published
- **What it holds:** Best-in-class ICS vendor PSIRT globally (per comparison matrix). CVSS v4.0 with OT-specific environmental scores; CSAF 2.0 machine-readable advisories; ISA/IEC 62443 alignment; comprehensive affected-version trees for all Siemens industrial products.
- **Coverage:** Siemens industrial product portfolio: SIMATIC, SIPROTEC, SINEMA, RUGGEDCOM, Totally Integrated Automation, building systems
- **Access model:** Free, public. CSAF feeds machine-readable.
- **Comparison matrix score:** Total 71/100; P14=5 (ICS/OT specific); gold standard for ICS vendor PSIRT output quality

---

### Schneider Electric PSIRT
- **Website:** https://www.se.com/ww/en/work/support/cybersecurity/overview.jsp
- **What it holds:** Security advisories for Schneider Electric industrial products (EcoStruxure, Modicon PLCs, SCADA systems, building management, energy management). CVSS scores with ICS context.
- **Coverage:** Schneider Electric industrial product ecosystem
- **Access model:** Free, public

---

## TIER 6 — BUG BOUNTY PLATFORMS

### HackerOne
- **Website:** https://hackerone.com
- **What it holds:** World's largest bug bounty and vulnerability disclosure platform by researcher count. Connects organizations with 580,000+ validated vulnerability reports (as of 2025). Tracks disclosed reports, coordinates disclosure timelines, and maintains a record of validated vulnerabilities.
- **2025 statistics (HackerOne Hacker-Powered Security Report 2025):**
  - $81 million in payouts in 2025
  - AI vulnerability reports up 210%
  - Prompt injection vulnerabilities up 540%
  - Programs with AI in scope grew 270%
  - $3 billion in breach losses avoided (by HackerOne's own RoM methodology)
- **Market share:** ~38% of bug bounty market by practitioner mind share
- **Coverage:** All software categories; particularly strong for web applications, APIs, and now AI/ML systems
- **Access model:** Free for researchers to participate. Organizations pay program fees. Disclosed reports (with researcher permission) are public.
- **Who uses it:** Global enterprises, tech companies, US government (DoD), critical infrastructure
- **Exploit availability:** Disclosed reports often include PoC details — highly valuable for understanding real-world exploitation techniques for specific CVEs

---

### Bugcrowd
- **Website:** https://bugcrowd.com
- **What it holds:** Bug bounty and vulnerability disclosure platform. Second-largest by market share (~32%). Specialises in managed programs with dedicated program management.
- **2025 statistics:**
  - Broken access control critical vulnerabilities rose 36%
  - API vulnerabilities rose 10%
  - Network vulnerabilities doubled
  - Hardware vulnerabilities rose 88% — signal of growing IoT/embedded security research
- **Access model:** Free for researchers. Organizations pay program fees.
- **Who uses it:** Enterprises, government agencies, fintech, healthcare
- **Exploit availability:** Disclosed reports include technical details for validated findings

---

### Intigriti
- **Headquarters:** Belgium (EU-based)
- **Website:** https://intigriti.com
- **What it holds:** European-focused bug bounty and vulnerability disclosure platform with 50,000+ ethical hackers. European alternative to HackerOne/Bugcrowd with GDPR-native data handling and EU data residency.
- **2025–2026 highlights:** Nvidia launched a major enterprise-scale bug bounty program on Intigriti in 2025, signaling platform maturity for high-profile enterprise programs.
- **Access model:** Free for researchers. Organizations pay program fees.
- **Who uses it:** EU enterprises and government agencies; organizations with EU data residency requirements; companies requiring GDPR-compliant bug bounty management
- **Geopolitical note:** EU-based platform; relevant for EU organizations concerned about non-EU data handling in cybersecurity workflows

---

### Synack
- **Website:** https://synack.com
- **What it holds:** Managed crowd-sourced security testing platform with a vetted "Red Team" of researchers (background-checked, government-cleared options). Provides structured penetration test reports with CVE-mapped findings. Used by US federal agencies including DoD.
- **Access model:** Commercial managed service. Not a public bug bounty platform.
- **Who uses it:** US government agencies (DoD, DHS), regulated industries requiring vetted researchers with clearances
- **Exploit availability:** Detailed technical reports with PoC code for enterprise clients

---

### YesWeHack
- **Headquarters:** France (EU-based)
- **Website:** https://yeswehack.com
- **What it holds:** European-founded bug bounty platform with strong presence in EMEA and APAC. European Commission (EC OSPO) partner for EU open-source security programs (e.g., Jenkins bug bounty program 2025). French, German, and Swiss corporate focus.
- **2025 statistics (YesWeHack Bug Bounty Report 2025):** Published; details on European enterprise vulnerability trends.
- **Access model:** Free for researchers. Organizations pay program fees.
- **Who uses it:** European enterprises, EU public administration, French government agencies
- **Geopolitical note:** EU-origin platform; data processed under GDPR; European Commission partnership provides additional institutional credibility for EU-regulated organizations

---

## TIER 7 — ICS/SCADA SPECIFIC

### CISA ICS-CERT Advisories
- **Website:** https://www.cisa.gov/ics-advisories
- **What it holds:** US government advisories specifically targeting industrial control systems, operational technology, and critical infrastructure. Includes affected product lists, CVSS scores, mitigations, vendor responses, and ICS-specific exploitation context. Coordinated with Siemens ProductCERT, Claroty, Dragos, Nozomi, and other ICS vendors.
- **2025 statistics:** 508 advisories in 2025 (record year); 82% rated High/Critical; 2,155 CVEs covered; 26% with no patch or mitigation available; 25% with incorrect CVSS scores (per Dragos analysis).
- **Coverage:** PLCs, DCS, HMI, SCADA, building automation, energy management, water/wastewater, manufacturing. All major ICS vendors.
- **Access model:** Completely free, public. JSON feed available via ICS Advisory Project (GitHub) — community-reformatted machine-readable version.
- **Who uses it:** Critical infrastructure operators, ICS security teams, OT security researchers, all CISA-regulated sectors
- **Exploit availability:** ICS-specific exploitation context; limited PoC details for safety reasons
- **Comparison matrix score:** P14=5 (best free ICS-specific source alongside VARIoT)

---

## ADDITIONAL / EMERGING CATEGORIES

### ENISA EUVD — European Vulnerability Database
- **Operator:** ENISA (European Union Agency for Cybersecurity); EU institutional authority
- **Website:** https://euvd.enisa.europa.eu
- **Launched:** May 13, 2025
- **What it holds:** EU's sovereign NVD alternative. Aggregates NVD CVE data, EU CERT advisories, and voluntary vendor disclosures. Machine-readable API. Distinct from the CRA Single Reporting Platform (SRP) — EUVD is the NIS2-mandated vulnerability reference database; SRP is the forthcoming mandatory CRA reporting portal (pilot Q1 2026, full operation before September 2026).
- **Coverage:** Global CVE scope via NVD aggregation; EU CERT advisory integration adds EU-origin context
- **Access model:** Completely free, public. EU public institution.
- **Key regulatory context:**
  - NIS2 Directive (Article 12) mandates ENISA maintain a European vulnerability database
  - EU Cyber Resilience Act (CRA): Manufacturers must notify ENISA's CSIRT of actively exploited vulnerabilities; mandatory CRA reporting begins September 11, 2026
  - GDPR-native: EU institutional governance, Athens-hosted servers, full data residency for EU-regulated organizations
  - ENISA became a CVE Root CNA (November 2025) — can now assign CVEs directly for EU-origin disclosures
- **Who uses it:** EU-regulated entities (NIS2, CRA, DORA), EU government agencies, organizations with EU data residency requirements, EU critical infrastructure operators
- **Comparison matrix score:** Total 62/100 (new 2026 addition); P13=5 (highest EU regulatory compliance score); P11=5 (EU institutional governance); P20=5 (GDPR-native)
- **VulnCheck assessment:** VulnCheck published a technical evaluation of EUVD ("Does ENISA EUVD live up to all the hype?") noting it aggregates NVD data with EU CERT enrichment but does not yet provide independent CVE scoring or exploit intelligence at commercial platform quality.

---

### GCVE — Global CVE (Distributed Alternative)
- **Operator:** CIRCL (Computer Incident Response Center Luxembourg); open community
- **Website:** https://gcve.eu (launched January 2026)
- **What it holds:** Federated, distributed alternative to the MITRE CVE program. Provides a CVE-equivalent identifier allocation system that does not depend on US government funding or MITRE's centralized infrastructure. Launched as a direct response to the April 2025 CVE program near-shutdown.
- **Coverage:** Emerging — primarily covering EU/CIRCL-allocated identifiers initially; designed for global adoption
- **Access model:** Free, open, federated model
- **Who uses it:** European CERTs, researchers wanting CVE program independence from US political risk; early adopters hedging against future US funding instability
- **Geopolitical significance:** Represents the EU/European CERT community's assertion that critical security infrastructure should not be controlled by a single government or contract. Part of a broader trend toward CVE program sovereignty.

---

### Cloud Vulnerability Databases (AWS / Azure / GCP)
- **AWS Security Bulletins:** https://aws.amazon.com/security/security-bulletins — ALAS (Amazon Linux Security Advisories), EC2 instance metadata vulnerabilities, service-level security bulletins
- **Google Cloud Security Bulletins:** https://cloud.google.com/support/bulletins — GKE (Kubernetes Engine) security bulletins, GCP platform advisories, Container-Optimized OS (COS) advisories
- **Microsoft Azure / MSRC:** Security updates for Azure services surfaced through MSRC; Microsoft Defender for Cloud release notes (learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes)
- **Coverage statistics (May 2025 IEEE DataPort dataset):** AWS: 122 unique CVE entries; Azure: 319 entries; GCP: 264 entries — demonstrating that cloud-native CVE coverage is thin compared to traditional software
- **Cloud Vulnerabilities DB:** https://www.cloudvulndb.org — open project cataloguing cloud service provider security issues; community GitHub project at github.com/hashishrajan/cloud-security-vulnerabilities
- **Key gap:** Cloud-native vulnerabilities (IAM misconfigurations, cross-tenant privilege escalation, metadata service exploits) often don't receive CVE IDs because they affect the provider's infrastructure rather than discrete software versions. NVD and CVE are structurally inadequate for cloud-native vulnerability tracking.
- **Commercial coverage:** Wiz (cloud CNAPP, Total 68/100 in matrix), Orca Security, Palo Alto Prisma Cloud, CrowdStrike Falcon CSPM — all provide cloud-native vulnerability correlation with runtime context.

---

### AI/ML Model Vulnerability Databases
- **MITRE ATLAS:** https://atlas.mitre.org — Adversarial Threat Landscape for AI Systems. v5.4.0 (February 2026): 16 tactics, 84 techniques, 56 sub-techniques targeting AI/ML systems. Added 14 new techniques in 2025 for AI agents (prompt injection, memory manipulation, tool poisoning). February 2026 additions: "Publish Poisoned AI Agent Tool" and "Escape to Host." Not a CVE database — a tactics/techniques framework analogous to ATT&CK.
- **AVID (AI Vulnerability and Incidents Database):** https://avidml.org/database — Open database of failure modes in general-purpose AI systems. Maps to CVSS risk scores and MITRE ATLAS. The closest analogue to an AI-specific CVE database.
- **CVE coverage for AI/ML (2025–2026):** EchoLeak (CVE-2025-32711) — zero-click prompt injection in Microsoft 365 Copilot (Aim Security, June 2025). 30+ CVEs filed against MCP (Model Context Protocol) implementations in early 2026, CVSS up to 9.6. LiteLLM supply chain attack (March 2026) — ML software dependency compromise.
- **Gap assessment:** AI/ML vulnerability tracking is pre-paradigm. CVSS is not designed for prompt injection or model-extraction attacks. No authoritative CVE numbering practice exists for AI model vulnerabilities as distinct from the software running them. MITRE ATLAS provides the TTP framework but no CVE-equivalent identifier system. This is a critical emerging gap.

---

### Supply Chain / SBOM-Linked Vulnerability Databases
- **OSV schema:** The de-facto standard for SBOM-linked vulnerability tracking. CycloneDX v1.7 (October 2025) and SPDX v3.0 both map directly to OSV/NVD/GHSA vulnerability identifiers via purl (package URL). ECMA-427 (purl formal specification) published December 2025.
- **OWASP Dependency-Track:** Open-source SBOM management platform continuously correlating SBOMs against NVD, OSV, GHSA, Sonatype OSS Index, and VEX documents. Re-evaluates every stored SBOM as new CVEs publish.
- **Key statistics:**
  - 95% of vulnerabilities in transitive (indirect) dependencies — unreachable via direct dependency scanning
  - CPE-only pipeline false positive rate: 68.37% (vs. up to 80% reduction with purl-primary approach per Grype)
  - 81,000 EOL package versions with CVEs and no patch path
  - 192,742 malicious packages in 2025 with NO CVE identifiers (Mondoo data) — supply chain threat is larger than CVE-tracked surface
  - Sonatype documented 167,286 false negatives from their own database in 2025
- **Firmware SBOM tools:** Espressif esp-idf-sbom (ESP32), Finite State, Binarly — all generate SBOMs from firmware binaries to enable CVE mapping at component level
- **Regulatory drivers:** NTIA SBOM guidelines, FDA Section 524B (medical devices), EU Cyber Resilience Act (September 2026 for manufacturers) — all mandate SBOM generation for connected devices

---

## COMPARISON MATRIX SCORES (Selected Databases)

From `/home/fmf/Projects/cve-analysis/cve_db_comparison_matrix.md` — 20-parameter scoring (1–5 scale, max 100):

| Rank | Database | Total | Cost | Key Strengths |
|------|----------|-------|------|---------------|
| 1 | Flashpoint VulnDB | 78 | Commercial | Coverage (400k+ entries, 100k+ beyond NVD), dark web intel, Flashpoint KEV (5,100+), CNVD/CNNVD/JVN cross-mapping |
| 2 | Google Threat Intelligence | 77 | Commercial | APT attribution, Project Zero integration, VirusTotal malware correlation |
| 3 | VulnCheck | 77 | Freemium | NVD++ (76.95% CPE), KEV+173%, 14,000+ exploits tracked 2025, free community tier |
| 4 | Recorded Future VI | 76 | Commercial | Dark web, temporal risk, threat actor linkage, STIX export |
| 5 | Mandiant VI | 75 | Commercial | Incident-grounded exploitation evidence, M-Trends data, attacker TTP |
| 6 | Microsoft MSRC | 75 | Free | CVSS v4 gold standard, CSAF 2.0, Patch Tuesday precision, zero cost |
| 7 | Rapid7 InsightVM | 74 | Commercial | Active Risk, Metasploit linkage, AttackerKB |
| 8 | Qualys ThreatProtect | 74 | Commercial | TruRisk 2.0, RTI scoring, FedRAMP |
| 9 | Red Hat CVE DB | 74 | Free | Independent contextual CVSS (best free Linux risk scoring amid NVD crisis) |
| 10 | OSV (osv.dev) | 74 | Free | 1.8-day mean listing, 28+ ecosystems, best purl/SBOM matching |
| 11 | GHSA | 70 | Free | 2.4-day mean listing, EPSS daily sync, CVSS v4, 25k+ reviewed advisories |
| 12 | CISA KEV | 72 | Free | Authoritative confirmed-exploitation, mandatory deadlines, JSON feed |
| 13 | Tenable VPR | 73 | Commercial | VPR 150+ factors, 334k+ plugins, IoT families, FedRAMP |
| 14 | Cisco PSIRT | 72 | Free | Best vendor PSIRT quality, CVSS v4 + environmental, CSAF 2.0 |
| 15 | Siemens ProductCERT | 71 | Free | Best ICS vendor PSIRT globally, ISA/IEC 62443, OT scores |
| — | CNVD | 33 | Free | Chinese domestic products only; geopolitically compromised |
| — | CNNVD | 34 | Free | MSS-operated; backdated timestamps; do not use as authoritative source |
| — | FSTEC BDU | 32 | Free | 10% CVE coverage; Russian military operated; selective publication |
| — | ENISA EUVD | 62 | Free | EU CRA compliance (P13=5); GDPR-native (P20=5); launched May 2025 |
| — | VulDB | 67 | Freemium | 49% of all CVSS v4 scores globally; systematic Temporal scoring |

---

## RECOMMENDED STACKS

### Minimum Viable Free Stack (post-April 2026 NVD crisis)
1. **NIST NVD API 2.0** — baseline CVE identifiers and enrichment for priority tier
2. **VulnCheck NVD++** (free community tier) — fills CPE/CVSS for the 80% NVD no longer enriches
3. **CISA KEV** — confirmed exploitation signal (JSON feed)
4. **EPSS** (FIRST.org daily CSV) — exploitation probability for everything KEV doesn't cover
5. **OSV** (osv.dev API) — open-source component vulnerabilities, SBOM matching
6. **CISA Vulnrichment** (GitHub) — ADP containers filling enrichment gaps
7. **OpenCVE** (self-hosted) — monitoring, alerting, vendor/product watchlists
8. **GHSA** — GitHub/OSS ecosystem, EPSS-synced, 2.4-day mean listing time
9. **ENISA EUVD** — mandatory for EU CRA compliance from September 2026

### IoT / OT / Embedded Stack
Above + CISA ICS-CERT + Siemens/Schneider CSAF feeds + VARIoT + Dragos or Claroty (commercial for large OT) + MITRE ATT&CK for ICS + MITRE EMB3D v2.0

### Enterprise SOC Stack
Above free stack + VulnCheck (full commercial) + Recorded Future or Flashpoint (dark web, threat actor) + Tenable or Qualys (VM platform) + Shadowserver + GreyNoise (exploitation telemetry)

---

## SOURCES (Web Research)

- [Zerodium platform](https://zerodium.com/)
- [Crowdfense Exploit Acquisition Program](https://www.crowdfense.com/exploit-acquisition-program/)
- [Crowdfense $30M program - Security Affairs](https://securityaffairs.com/161584/hacking/crowdfense-30m-exploit-acquisition-program.html)
- [UAE EDGE eyeing Crowdfense - Tactical Report](https://www.tacticalreport.com/daily/63154-uaes-edge-advances-cyber-acquisition-with-crowdfense-and-plans-further-expansion)
- [China's CNNVD as MSS tool - CyberScoop](https://cyberscoop.com/china-national-vulnerability-database-mss-recorded-future/)
- [China altered public data - Recorded Future](https://www.recordedfuture.com/blog/chinese-vulnerability-data-altered)
- [Sleight of hand China - Atlantic Council](https://www.atlanticcouncil.org/in-depth-research-reports/report/sleight-of-hand-how-china-weaponizes-software-vulnerability/)
- [Russia BDU database - Dark Reading](https://www.darkreading.com/cyberattacks-data-breaches/russian-national-vulnerability-database-operation-raises-suspicions)
- [Russia publishes only 10% of CVEs - Infosecurity Magazine](https://www.infosecurity-magazine.com/news/russia-publishes-only-10-of-cves/)
- [CVE program averts shutdown - CSO Online](https://www.csoonline.com/article/3963190/cve-program-faces-swift-end-after-dhs-fails-to-renew-contract-leaving-security-flaw-tracking-in-limbo.html)
- [Dark web markets 2025 - darknet.org.uk](https://www.darknet.org.uk/2025/10/inside-dark-web-exploit-markets-in-2025-pricing-access-active-sellers/)
- [VulnCheck 2026 Exploit Intelligence Report](https://www.vulncheck.com/blog/2026-vulncheck-exploit-intelligence-report)
- [VulnCheck $25M Series B](https://www.businesswire.com/news/home/20260217872039/en/VulnCheck-Raises-$25M-Series-B-Financing-to-Address-Surging-Demand-for-its-Exploit-Intelligence-Solutions)
- [ENISA EUVD launch](https://www.enisa.europa.eu/news/consult-the-european-vulnerability-database-to-enhance-your-digital-security)
- [ENISA becomes CVE Root CNA](https://www.enisa.europa.eu/news/stepping-up-our-role-in-vulnerability-management-enisa-becomes-cve-root)
- [VulnCheck EUVD assessment](https://www.vulncheck.com/blog/enisa-euvd)
- [MITRE ATLAS framework 2026](https://www.practical-devsecops.com/mitre-atlas-framework-guide-securing-ai-systems/)
- [AVID database](https://avidml.org/database/)
- [NVD OIG audit 88% error - TechTimes](https://www.techtimes.com/articles/317594/20260602/nist-national-vulnerability-database-severity-scores-wrong-88-time-inspector-generator-finds.htm)
- [NVD "Not Scheduled" policy - Help Net Security](https://www.helpnetsecurity.com/2026/04/16/nist-national-vulnerability-database-nvd-enrichment/)
- [NIST NVD operations update - NIST.gov](https://www.nist.gov/news-events/news/2026/04/nist-updates-nvd-operations-address-record-cve-growth)
- [HackerOne 210% AI spike press release](https://www.hackerone.com/press-release/hackerone-report-finds-210-spike-ai-vulnerability-reports-amid-rise-ai-autonomy)
- [ZDI about page](https://www.zerodayinitiative.com/about/)
- [Intigriti platform](https://www.intigriti.com/)
- [YesWeHack Bug Bounty Report 2025](https://www.yeswehack.com/news/yeswehack-bug-bounty-report-2025)
- [CORE Impact H2 2025 chronicle](https://www.coresecurity.com/blog/core-impact-chronicle-exploits-and-updates-h2-2025)
- [Cloud Vulnerabilities DB](https://www.cloudvulndb.org/)
- [Cloud CVE dataset IEEE DataPort](https://ieee-dataport.org/documents/aws-azure-google-cloud-platform-vulnerability-datasets-gethered-2025-may)

**Prior research project:** `/home/fmf/Projects/cve-analysis/` — 1,288+ database master list, 20-parameter evaluation framework, comparison matrix (80+ databases), gap analysis report, intelligence analysis POV. All scores and detailed data for entries not individually expanded above are sourced from that project.
