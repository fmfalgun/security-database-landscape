# OSINT / Passive DNS / WHOIS History / Internet Infrastructure Intelligence Research

**Objective:** Document ALL significant operators of OSINT, passive DNS, WHOIS history, and internet infrastructure intelligence databases — commercial, free/open, government, academic, and gray market. Global scope.

**Agent:** claude-sonnet-4-6  
**Started:** 2026-06-17  
**File path:** /home/fmf/security-db-research/agent_osint_dns.md

---

## Entry Index (70 entries — all complete)

1. [DONE] PassiveTotal / RiskIQ → Microsoft Defender Threat Intelligence
2. [DONE] Farsight Security DNSDB → DomainTools
3. [DONE] DomainTools
4. [DONE] SecurityTrails (→ Recorded Future)
5. [DONE] Shodan
6. [DONE] VirusTotal (Google / Alphabet)
7. [DONE] CIRCL Passive DNS (Luxembourg)
8. [DONE] BinaryEdge → Coalition (SHUTDOWN March 2025)
9. [DONE] Netcraft
10. [DONE] Certificate Transparency (CT) Ecosystem (crt.sh, Google CT, Cloudflare CT, ISRG)
11. [DONE] ZoomEye (Knownsec, China) ⚠ GEOPOLITICAL FLAG
12. [DONE] FOFA (Baimaohui, China) ⚠ GEOPOLITICAL FLAG
13. [DONE] CT Aggregators (Facebook CT Monitor, certspotter/SSLMate)
14. [DONE] Robtex
15. [DONE] Hurricane Electric BGP Toolkit
16. [DONE] BGPView (SHUTDOWN November 2025)
17. [DONE] RIPE NCC and RIPEstat
18. [DONE] Regional Internet Registries: ARIN, APNIC, LACNIC, AFRINIC
19. [DONE] Spyse (Defunct)
20. [DONE] Maltego
21. [DONE] Recon-ng
22. [DONE] OWASP Amass
23. [DONE] theHarvester
24. [DONE] Hacker Target
25. [DONE] DNSdumpster
26. [DONE] Yandex (Russian context) ⚠ GEOPOLITICAL FLAG
27. [DONE] Censys
28. [DONE] GreyNoise
29. [DONE] Criminal IP (AI Spera, Korea)
30. [DONE] Netlas.io
31. [DONE] ONYPHE (France)
32. [DONE] Recorded Future → Mastercard
33. [DONE] Intel471
34. [DONE] Google Threat Intelligence (Mandiant + VirusTotal)
35. [DONE] IBM X-Force Exchange (EOL 2026)
36. [DONE] AlienVault OTX (AT&T / LevelBlue)
37. [DONE] Pulsedive
38. [DONE] Team Cymru
39. [DONE] BGP.tools
40. [DONE] CAIDA (UC San Diego / NSF)
41. [DONE] OpenINTEL (Netherlands)
42. [DONE] BuiltWith
43. [DONE] Spamhaus
44. [DONE] WhoisXML API
45. [DONE] Hunter.io
46. [DONE] Wayback Machine / Internet Archive
47. [DONE] IPinfo.io
48. [DONE] MaxMind GeoIP
49. [DONE] PublicWWW
50. [DONE] Common Crawl
51. [DONE] FullHunt
52. [DONE] LeakIX
53. [DONE] Rapid7 Open Data / Project Sonar — FDNS & DNSGrep
54. [DONE] ProjectDiscovery / Subfinder
55. [DONE] Cloudflare Radar
56. [DONE] Cisco Umbrella Investigate
57. [DONE] PassiveDNS.cn / Qihoo 360 PassiveDNS ⚠ GEOPOLITICAL FLAG
58. [DONE] Qihoo 360 Quake ⚠ GEOPOLITICAL FLAG
59. [DONE] Shadowserver Foundation
60. [DONE] ThreatBook (微步在线, China) ⚠ GEOPOLITICAL FLAG
61. [DONE] NSA XKEYSCORE / Five Eyes SIGINT (publicly known context)
62. [DONE] Dark Web / Underground OSINT Aggregators (overview)
63. [DONE] Russian Internet Infrastructure / Runet OSINT Context ⚠ GEOPOLITICAL FLAG
64. [DONE] Microsoft Defender Threat Intelligence (MDTI) — Retirement Note (August 2026)
65. [DONE] ODIN (Cyble)
66. [DONE] Intelligence X (intelx.io)
67. [DONE] Hudson Rock
68. [DONE] PeeringDB
69. [DONE] IVRE (Instrument de Veille sur les Réseaux Extérieurs)
70. [DONE] ProjectDiscovery Chaos

---

## Progress Log

- **Batch 1:** Researched PassiveTotal/RiskIQ, Farsight/DomainTools, SecurityTrails, Shodan, VirusTotal, CIRCL, BinaryEdge, Netcraft, ZoomEye, FOFA, Certificate Transparency
- **Batch 2:** Robtex, Hurricane Electric, BGPView, RIPE NCC, RIRs (ARIN/APNIC/LACNIC/AFRINIC), Spyse, Maltego, Recon-ng, Amass, theHarvester, Hacker Target, DNSdumpster, ViewDNS.info, Yandex
- **Batch 3:** (in progress) Tier 2 items: Censys, GreyNoise, Criminal IP, Netlas, ONYPHE, Recorded Future, Intel471, AlienVault OTX, Pulsedive, Team Cymru, BGP.tools, CAIDA, OpenINTEL, BuiltWith, Spamhaus, RIPEstat, WhoisXML API, Hunter.io, Wayback Machine, and more

---

## Findings

---

### 1. PassiveTotal / RiskIQ → Microsoft Defender Threat Intelligence

- **Organization:** RiskIQ (founded 2009) → acquired by Microsoft (July 2021)
- **Product:** Microsoft Defender Threat Intelligence (MDTI), formerly PassiveTotal
- **Website:** https://www.riskiq.com / https://ti.defender.microsoft.com
- **Data held:**
  - Passive DNS (400 million unique records/day ingested from geographically dispersed sensor + partner network)
  - WHOIS history (current + historical)
  - SSL/TLS certificates
  - Web page content / crawl history
  - Subdomain enumeration
  - IP-to-domain resolution history
  - Threat actor infrastructure tracking
  - Threat intelligence indicators
- **Data retention:** Multi-year historical archive
- **Scale:** 400M+ unique passive DNS records/day; petabyte-scale historical archive
- **Access model:**
  - Free tier: PassiveTotal community access
  - Enterprise: Microsoft Defender Threat Intelligence portal
  - API access for enterprise; integrated with Microsoft Sentinel SIEM
  - SOAR integrations (Palo Alto XSOAR, etc.)
- **Users:** SOC analysts, threat hunters, pen testers, incident responders, law enforcement, government agencies
- **Geopolitical notes:** Microsoft (US); post-acquisition, data integrated into US government-adjacent infrastructure

---

### 2. Farsight Security DNSDB → DomainTools

- **Organization:** Farsight Security (founded by Paul Vixie) → acquired by DomainTools (November 2021)
- **Product:** DNSDB (Passive DNS Database)
- **Website:** https://www.farsightsecurity.com / https://www.domaintools.com
- **Data held:**
  - Passive DNS (largest DNS intelligence database in the world)
  - Historical DNS resolution records (A, AAAA, MX, NS, CNAME, PTR, SOA, etc.)
  - Real-time DNS telemetry
  - Sensor network data globally distributed
- **Data retention:** Multi-decade archive (founded 2013, but Vixie-era data goes back earlier)
- **Scale:** 100+ billion domain resolution records; 300,000+ unique DNS resolutions per second
- **Access model:**
  - Commercial API (paid tiers)
  - Researcher/academic access program
  - Integrated into DomainTools Iris platform
  - DNSDB Scout (browser-based UI)
  - DNSDB API (programmatic)
- **Users:** Threat intelligence analysts, IR teams, law enforcement, academic researchers
- **Geopolitical notes:** US company; DomainTools is a key vendor to US government/IC community

---

### 3. DomainTools

- **Organization:** DomainTools LLC
- **Website:** https://www.domaintools.com
- **Data held:**
  - Active DNS (daily DNS crawls across all TLDs)
  - Passive DNS (via DNSDB acquisition)
  - WHOIS history (since ~2001 — one of the longest archives)
  - Domain registration history
  - Reverse IP / hosting history
  - SSL certificate data
  - Iris investigation graph
  - Newly observed domains (NOD feed)
  - Domain risk scoring
- **Data retention:** WHOIS history to ~2001; DNS history varies by record type
- **Scale:** 400M+ active domains monitored; ~10B+ WHOIS records
- **Access model:**
  - Commercial SaaS (DomainTools Iris)
  - API (paid tiers, enterprise licensing)
  - Researcher program
- **Users:** Threat intel teams, fraud investigators, law enforcement, brand protection, corporate legal teams
- **Geopolitical notes:** US company; primary vendor to US IC; WHOIS data used in court proceedings

---

### 4. SecurityTrails

- **Organization:** SecurityTrails (independent) → acquired by Recorded Future
- **Website:** https://securitytrails.com
- **Data held:**
  - Historical DNS records (A, MX, NS, SOA, TXT, CNAME)
  - WHOIS history (~3 billion historical + current WHOIS records)
  - Subdomain enumeration (2.6+ billion tracked hostnames)
  - Reverse DNS lookup
  - IP intelligence
  - Certificate history
- **Data retention:** Multi-year DNS and WHOIS history
- **Scale:** 3B+ WHOIS records; 2.6B+ hostnames; 203M+ domain database
- **Access model:**
  - Free community tier (limited queries)
  - Paid API tiers (RESTful, JSON output)
  - Enterprise/bulk access
- **Users:** Security researchers, pen testers, threat hunters, bug bounty hunters, red teamers
- **Geopolitical notes:** Now part of Recorded Future, which was acquired by Mastercard (2024)

---

### 5. Shodan

- **Organization:** Shodan (independent, founded by John Matherly, 2009)
- **Website:** https://www.shodan.io
- **Data held:**
  - Internet device/service banner data (TCP/UDP across all IPv4 and partial IPv6)
  - SSL/TLS certificates and history
  - Passive DNS and historical DNS
  - BGP/ASN data
  - Vulnerability data (CVEs mapped to services)
  - Open port enumeration
  - Geolocation
  - Organization/ASN attribution
  - Historical snapshots (Shodan Monitor)
  - Honeypot detection
- **Data retention:** Ongoing real-time; historical data varies by plan
- **Scale:** Billions of device records; continuous full IPv4 sweeps; 400M+ indexed hosts
- **Access model:**
  - Free (50 results/search, limited features)
  - Membership ($49/lifetime for basic; monthly enterprise plans)
  - API access (tiered)
  - Bulk data / data streams (enterprise)
  - Developer API for integration
- **Users:** Pen testers, security researchers, IT asset managers, threat hunters, red teamers, defenders
- **Geopolitical notes:** US company; data is open to all including adversary states; used by nation-state actors for recon

---

### 6. VirusTotal (Google / Alphabet)

- **Organization:** VirusTotal (founded 2004, Spain) → acquired by Google (2012) → Google Chronicle / Alphabet
- **Website:** https://www.virustotal.com
- **Data held:**
  - Passive DNS (historical IP-domain resolution records from URL submissions, sandboxes, and partner feeds)
  - WHOIS lookups (current)
  - File hashes / malware samples
  - URL/domain reputation history
  - SSL certificate data
  - Sandbox execution results
  - Threat graph / infrastructure relationships
- **Data retention:** Multi-year passive DNS; permanent file hash storage
- **Scale:** Billions of files; hundreds of millions of URLs; global sensor network contributions from 70+ AV engines
- **Access model:**
  - Free (web UI, limited API)
  - VirusTotal Premium / Enterprise (Google Threat Intelligence)
  - API v3 (paid tiers)
  - Chronicle/Google SecOps integration
- **Users:** Malware analysts, SOC teams, IR teams, AV vendors, threat researchers
- **Geopolitical notes:** Google/Alphabet (US); integrated into US IC-adjacent infrastructure; data retention opaque

---

### 7. CIRCL Passive DNS (Computer Incident Response Center Luxembourg)

- **Organization:** CIRCL — Computer Incident Response Center Luxembourg (government-adjacent, for private sector + communes)
- **Website:** https://www.circl.lu / https://www.circl.lu/services/passive-dns/
- **Data held:**
  - Historical DNS records from malware analysis and partner feeds
  - Passive DNS Common Output Format (COF) compliant
  - Also offers Passive SSL (certificate history)
- **Data retention:** Long-term archive (exact retention not publicly stated)
- **Scale:** Not publicly quantified; regional Luxembourg-EU focus but global partner feeds
- **Access model:**
  - Restricted: Access limited to trusted partners (Luxembourg + international)
  - Application required with affiliation and use-case justification
  - REST API (JSON output, COF-compliant)
  - Python library: PyPDNS
  - Version 2.0 released November 2023 (added filtering and pagination)
- **Users:** Incident handlers, security researchers, CERTs, academic researchers
- **Geopolitical notes:** Luxembourg government-backed; EU-oriented; trusted-partner model; no commercial ties to US/CN

---

### 8. BinaryEdge → Coalition (SHUTDOWN March 2025)

- **Organization:** BinaryEdge → acquired by Coalition (cyber insurance, 2020)
- **Website:** https://www.binaryedge.io (defunct as standalone platform)
- **Status:** SHUTDOWN — all accounts terminated March 31, 2025
- **Data held (historical):**
  - Internet-wide scanning data (ports, services, banners)
  - Certificate data
  - ASN/BGP information
  - Vulnerability data
  - Exposed services enumeration
- **Scale:** Large-scale continuous internet scanning
- **Access model:** Was API-based (paid); now integrated internally into Coalition cyber insurance underwriting
- **Users (former):** Security researchers, pen testers, insurance underwriters, IT teams
- **Geopolitical notes:** Absorbed into Coalition (US cyber insurance startup); data now proprietary to Coalition

---

### 9. Netcraft

- **Organization:** Netcraft Ltd. (UK, founded 1994)
- **Website:** https://www.netcraft.com
- **Data held:**
  - Web server technology fingerprinting (since 1994 — longest-running internet survey)
  - Hosting provider history
  - SSL certificate history and monitoring
  - Phishing site detection and takedown
  - Domain infrastructure history
  - Web technology usage statistics
  - ASN and IP infrastructure mapping
  - Cryptocurrency scam tracking
  - Phishing feeds (used by browsers and ISPs)
- **Data retention:** Active since 1994; historical web infrastructure data going back 30 years
- **Scale:** 225M+ malicious sites blocked; 1.3M+ phishing sites disrupted (March 2024–March 2025); 16,000+ impersonated orgs tracked; median takedown time: 33 minutes
- **Access model:**
  - Commercial (enterprise anti-phishing, brand protection)
  - Phishing feed (ISP, browser vendor licensing — powers Firefox, Opera, etc.)
  - Site report (free web lookup at sitereport.netcraft.com)
  - API (commercial)
- **Users:** Banks, ISPs, browser vendors, government agencies, law enforcement, brand protection teams
- **Geopolitical notes:** UK company; feeds used by major browser vendors globally; no known geopolitical concerns

---

### 10. Certificate Transparency (CT) Ecosystem

#### 10a. crt.sh (Sectigo)
- **Organization:** Sectigo (formerly Comodo CA)
- **Website:** https://crt.sh
- **Data held:** Index of all CT logs from major operators; searchable by domain, organization, SAN, wildcard
- **Scale:** 500M+ log entries; thousands of queries/hour
- **Access model:** Free public search; also PostgreSQL database access for researchers
- **Users:** Security researchers, pen testers, subdomain hunters, certificate auditors

#### 10b. Google CT Logs (Google Trust Services)
- **Organization:** Google / Alphabet
- **Website:** https://transparencyreport.google.com/https/certificates
- **Data held:** Argon, Xenon, and other Google-operated CT logs; all publicly issued TLS certificates
- **Scale:** Billions of certificate entries

#### 10c. Cloudflare CT (Nimbus logs)
- **Organization:** Cloudflare
- **Website:** https://radar.cloudflare.com/certificate-transparency
- **Data held:** Nimbus CT logs (2023, 2024, 2025, Elephant2026h1, etc.); real-time CT monitoring
- **Scale:** 369,328+ entries/hour growth rate on active logs

#### 10d. Let's Encrypt / ISRG Oak CT logs
- **Organization:** Internet Security Research Group (ISRG)
- **Data held:** Oak CT log; issues 54.4% of all public SSL/TLS certs (Q1 2026)

**CT ecosystem summary:**
- All publicly issued TLS certificates must be logged in at least 2 approved CT logs
- CT logs are operated by Google, Cloudflare, DigiCert, Sectigo, Let's Encrypt, and others
- No single operator controls the ecosystem
- Data is permanently public by design
- **Users:** Certificate auditors, subdomain hunters, security researchers, brand monitors

---

### 11. ZoomEye

- **Organization:** Knownsec (Beijing Knownsec Information Technology Co., Ltd.) / KnownSec Hong Kong
- **Website:** https://www.zoomeye.ai
- **Data held:**
  - Internet-wide device/service scanning (ports, banners, services)
  - 40,000+ component type identification
  - Web application fingerprinting
  - ICS/OT device enumeration
  - IP geolocation
  - ASN/BGP attribution
  - Vulnerability mapping
- **Data retention:** Ongoing; historical snapshots
- **Scale:** Full IPv4 space scanned in 7–10 days; billions of indexed assets
- **Access model:**
  - Free tier (limited results)
  - Paid API tiers (international access)
  - Chinese researchers may have broader access
- **Users:** Security researchers, pen testers, threat intelligence; APT actors have been observed using it
- **GEOPOLITICAL FLAG — HIGH RISK:**
  - Operated by Knownsec, a Chinese cybersecurity firm with documented close ties to Chinese government and military
  - Leaked internal Knownsec documents reveal integration with "key target database" linking ZoomEye IP intelligence to exploitation targeting
  - Knownsec "Internet Aegis" and "Enterprise Digital Fortress" systems used for PRC domestic surveillance
  - Data queries by Western researchers may be logged and accessible to Chinese intelligence services
  - Knownsec employees appeared in leak showing espionage tradecraft documentation

---

### 12. FOFA

- **Organization:** Beijing Huashun Xin'an Technology Co. Ltd. (白帽汇/BAIMAOHUI)
- **Website:** https://fofa.info
- **Data held:**
  - Internet-wide infrastructure scanning
  - 4+ billion internet asset records
  - Device fingerprinting
  - Service/port enumeration
  - Certificate data
  - Web technology identification
  - ICS/SCADA device discovery
- **Data retention:** Ongoing; historical records maintained
- **Scale:** 4B+ indexed internet assets
- **Access model:**
  - Tiered subscription (free + paid)
  - API access (paid)
  - Chinese language primary interface (English available)
- **Users:** Security researchers, pen testers; notably used by APT41 (PRC-linked) for passive reconnaissance
- **GEOPOLITICAL FLAG — HIGH RISK:**
  - Chinese company; operates under PRC data sovereignty laws
  - APT41 and other Chinese APT groups documented using FOFA for target reconnaissance
  - Data potentially accessible to Chinese state intelligence apparatus
  - Queries by adversary researchers against Western infrastructure indexed here

---

### 13. CT Aggregators / Search Tools (additional)

#### 13a. Facebook CT Monitor (Meta)
- **Website:** https://developers.facebook.com/tools/ct/
- Certificate transparency monitoring for domains; free API for notifications

#### 13b. certspotter (SSLMate)
- **Website:** https://sslmate.com/certspotter/
- Real-time CT log monitoring; API for alerting on new cert issuance for your domains

---

### 14. Robtex

- **Organization:** Robtex (independent, Sweden)
- **Website:** https://www.robtex.com
- **Data held:**
  - Reverse DNS (IP-to-hostname mapping)
  - Forward DNS (hostname-to-IP)
  - WHOIS (domain registration data)
  - BGP routing and ASN data
  - MX and NS records
  - IP and domain reputation
  - Cryptocurrency address/transaction lookups (Bitcoin, Lightning Network)
  - MAC address lookups
- **Data retention:** "Billions of documents of internet data collected over more than a decade"
- **Scale:** Very large; exact scale not publicly stated; one of the longest-running free DNS intelligence tools
- **Access model:**
  - Free public web interface (robtex.com)
  - JSON API (documented; formerly via Mashape/RapidAPI, now direct)
  - Also exposes an MCP Server interface
- **Users:** Security researchers, pen testers, network engineers, OSINT investigators
- **Geopolitical notes:** Swedish company; no known geopolitical concerns; passive reconnaissance tool with no packet-sending to targets

---

### 15. Hurricane Electric BGP Toolkit

- **Organization:** Hurricane Electric LLC (global ISP and network operator, Fremont CA, USA)
- **Website:** https://bgp.he.net / https://he.net
- **Data held:**
  - BGP routing tables (prefixes, peers, upstream/downstream ASN relationships)
  - Internet Exchange Points (IXPs) and peering data
  - IPv4 and IPv6 prefix announcements
  - AS-to-prefix mapping
  - RPKI and ASPA validation status
  - Bogon route detection
  - IPv6 adoption metrics and statistics
  - Geolocation data per prefix
  - Certificate search
  - DNS records
  - Network statistics and host rankings
  - Super Traceroute and Looking Glass tools
- **Data retention:** Updated every 24 hours; ASN must be visible in routing tables for data to be available; historical visibility limited
- **Scale:** Global scope; HE is the largest IPv4 and IPv6 transit network globally by peering count; data sourced from public BGP collectors
- **Access model:**
  - Entirely free, no registration required
  - Web interface only (no public bulk API)
- **Users:** Network engineers, SOC analysts, OSINT investigators, threat intelligence analysts, pen testers
- **Geopolitical notes:** US company; completely open access with no authentication; used by researchers globally and also by threat actors for infrastructure mapping

---

### 16. BGPView

- **Organization:** BGPView (independent open project)
- **Website:** https://bgpview.io
- **Status:** SHUTTING DOWN — announced shutdown on November 26, 2025; recommends bgp.tools as replacement
- **Data held (while operational):**
  - ASN information (peers, prefixes, upstreams, downstreams)
  - IPv4 and IPv6 prefix data
  - BGP routing state
  - IXP membership
  - WHOIS-derived network registration data
  - Geolocation
- **Scale:** Covered global BGP routing table; free and widely used by OSINT practitioners
- **Access model:**
  - Free web interface
  - Free public REST API (JSON)
  - Open source backend (GitHub: BGPView/Backend-API)
- **Users:** Network operators, OSINT analysts, security researchers
- **Replacement:** BGP.Tools (https://bgp.tools) recommended by BGPView team on shutdown
- **Geopolitical notes:** Independent/open project; no known geopolitical concerns

---

### 17. RIPE NCC and RIPEstat

- **Organization:** RIPE NCC (Réseaux IP Européens Network Coordination Centre) — non-profit, Amsterdam, Netherlands
- **Website:** https://www.ripe.net / https://stat.ripe.net
- **Data held:**
  - IP address space allocations (Europe, Middle East, Central Asia)
  - ASN registration and WHOIS data
  - BGP routing data via RIS (Routing Information Service) — global BGP table from remote route collectors (RRCs) at IXPs worldwide
  - Routing history (BGPlay)
  - DNS (RIPE NCC operates k.root-servers.net)
  - Geolocation and abuse contacts
  - Certificate data (RPKI ROAs)
  - NWI (Network Weathermap / infrastructure statistics)
  - BGP update streams (real-time + historical)
- **Data retention:** RIS data archived since 1999; BGP Updates dataset indexed post-January 2024 in newer API
- **Scale:** RIPE NCC manages ~60,000 ASNs and millions of IP prefixes; RIS has 25+ Remote Route Collectors at major IXPs globally
- **Access model:**
  - RIPEstat Data API: free for non-commercial use; commercial users must contact RIPE NCC
  - Web UI at stat.ripe.net (free, no registration)
  - RIPE Whois (public WHOIS server, RDAP also available)
  - BGP data streams (MRT dumps downloadable freely)
- **Users:** Network operators, ISPs, academic researchers, security analysts, RIPE NCC members
- **Geopolitical notes:** European non-profit; independent from US/CN infrastructure; widely trusted; RIPE NCC has faced pressure from Russian government regarding sanctions compliance (2022–2025 context)

---

### 18. Regional Internet Registries (RIRs): ARIN, APNIC, LACNIC, AFRINIC

#### 18a. ARIN (American Registry for Internet Numbers)
- **Region:** North America (USA, Canada, Caribbean, North Atlantic)
- **Website:** https://www.arin.net
- **Data:** IP address allocations, ASN registration, WHOIS (organizations, POCs), RDAP, RPKI
- **Access:** Free public WHOIS and RDAP; bulk data available via ARIN FTP (free)
- **Geopolitical notes:** US nonprofit; data used extensively by US government and IC

#### 18b. APNIC (Asia-Pacific Network Information Centre)
- **Region:** Asia-Pacific
- **Website:** https://www.apnic.net
- **Data:** IP allocations, ASN data, WHOIS, research datasets, DNS measurement data
- **Access:** Free public WHOIS/RDAP; research data for academic use; APNIC Blog publishes internet measurement research
- **Geopolitical notes:** Covers China, India, Japan, Australia, etc.; operates under member governance; maintains independence from government control

#### 18c. LACNIC (Latin America and Caribbean Network Information Centre)
- **Region:** Latin America and Caribbean
- **Website:** https://www.lacnic.net
- **Data:** IP allocations, ASN data, WHOIS/RDAP, RPKI
- **Access:** Free public WHOIS; limited research data

#### 18d. AFRINIC (African Network Information Centre)
- **Region:** Africa
- **Website:** https://www.afrinic.net
- **Data:** IP allocations, ASN data, WHOIS/RDAP, RPKI
- **Access:** Free public WHOIS; faced governance crisis (2021–2023) with court battles; operations resumed
- **Geopolitical notes:** Governance dispute with cloud provider LARUS/Cloud Innovation raised questions about IP block fraud

**RIR ecosystem summary:**
- Together the 5 RIRs (RIPE NCC + 4 above) hold authoritative registration records for all globally allocated IP address space and ASNs
- All support RDAP (Registration Data Access Protocol) as of January 2025 (ICANN mandate)
- WHOIS data (registration, not DNS resolution) is the authoritative source for IP ownership attribution
- Widely queried by law enforcement, intelligence agencies, security researchers, and ISPs globally

---

### 19. Spyse (Defunct)

- **Organization:** Spyse (independent startup, Ukraine-origin)
- **Website:** https://spyse.com (defunct)
- **Status:** PERMANENTLY CLOSED — listed as such on Crunchbase; website may show archived version
- **Data held (while operational):**
  - Internet asset search engine targeting pentesters and security researchers
  - Domain intelligence (WHOIS, DNS records, subdomain enumeration)
  - IP and ASN data
  - SSL/TLS certificate data
  - Port and service enumeration
  - Technology fingerprinting
  - Vulnerability mapping
- **Scale:** Claimed large-scale continuously updated database of internet assets
- **Access model (historical):** Free tier with limited results; paid API tiers; paid subscription plans
- **Users (historical):** Penetration testers, red teamers, security researchers, bug bounty hunters
- **Notes:** Was considered a competitor to Shodan, Censys, and FOFA. Shut down; exact closure date unclear (approx. 2022–2023). No confirmed acquirer.
- **Geopolitical notes:** Ukraine-origin; the Russia-Ukraine conflict context may have been a factor in shutdown; no confirmed geopolitical acquisition

---

### 20. Maltego

- **Organization:** Maltego Technologies GmbH (Germany; founded Cape Town, South Africa)
- **Website:** https://www.maltego.com
- **Data held:** Maltego does NOT own or store data itself; it is a graph-based investigation platform and data aggregation layer
- **What it aggregates (via 100+ Connectors/Transforms):**
  - WHOIS and reverse WHOIS
  - Passive DNS (via DomainTools, SecurityTrails, VirusTotal, CIRCL, etc.)
  - SSL/TLS certificate data
  - BGP/ASN data
  - Social media profiles
  - Email addresses and personal identity data
  - Dark web data
  - Breach/leak data (Have I Been Pwned, etc.)
  - Threat intelligence feeds (Recorded Future, Shodan, etc.)
  - Corporate structure data (OCCRP Aleph, ICIJ Offshore Leaks)
  - Law enforcement-specific data via restricted transforms
- **Scale:** Aggregator accessing petabytes of external data across 100+ third-party providers
- **Access model:**
  - Maltego CE (Community Edition): free, limited transforms
  - Maltego One (Professional): paid subscription; full transform access
  - Maltego Enterprise: organization-wide deployment
  - Maltego Data Pass: licensing model for third-party data inside Maltego
  - Maltego Monitor: real-time change tracking
- **Users:** Threat intelligence analysts, law enforcement, intelligence agencies, fraud investigators, penetration testers, journalists, private investigators
- **Geopolitical notes:** German company (Paterva spin-off origin from South Africa); used by law enforcement and intelligence agencies worldwide including Five Eyes; transforms for law enforcement include restricted access to additional datasets

---

### 21. Recon-ng

- **Organization:** Open-source project (Tim Tomes / lanmaster53)
- **Website:** https://github.com/lanmaster53/recon-ng
- **Data held:** Recon-ng does NOT hold data itself; it is a modular OSINT framework that queries external data sources
- **What it queries (via modules):**
  - Passive DNS (via VirusTotal, SecurityTrails modules)
  - WHOIS data
  - Subdomain enumeration (via certificate transparency, search engines)
  - Email harvesting
  - Social media profiles
  - Shodan, Censys, BinaryEdge integration
  - BGP/ASN lookups
  - Breach data
- **Module count:** ~90+ modules (76 recon, 8 reporting, 2 import, 2 exploitation, 2 discovery)
- **Access model:**
  - Free and open-source (Python)
  - Distributed via Kali Linux, GitHub
  - Many modules require API keys from third-party services
- **Users:** Penetration testers, red teamers, security researchers, OSINT practitioners
- **Geopolitical notes:** Open-source; no data retention; all queries go directly to third-party APIs

---

### 22. OWASP Amass

- **Organization:** OWASP (Open Web Application Security Project) / maintained by Jeff Foley
- **Website:** https://owasp-amass.github.io / https://github.com/owasp-amass/amass
- **Data held:** Amass does NOT hold data; it is a DNS attack surface mapping tool that queries 55+ external passive DNS and OSINT sources
- **Data sources queried:**
  - AlienVault OTX, ArchiveIt, ArchiveToday, Arquivo
  - Baidu, BinaryEdge, Bing
  - BufferOver, Censys, CertSpotter
  - CIRCL Passive DNS, CommonCrawl, crt.sh
  - ViewDNS, VirusTotal, Wayback Machine
  - WhoisXML API, Yahoo, and 30+ more
- **Capabilities:**
  - Passive subdomain enumeration from public data sources
  - Active DNS enumeration (brute force, zone transfer attempts)
  - Certificate transparency log mining
  - Reverse DNS, ASN enumeration
  - DNS zone walking
  - Recursive subdomain discovery
- **Access model:**
  - Free and open-source (Go)
  - Distributed via Kali Linux, GitHub, Homebrew
  - API keys for third-party sources improve coverage significantly
- **Users:** Penetration testers, bug bounty hunters, red teamers, security researchers
- **Geopolitical notes:** Open-source OWASP project; no data retention; widely used in bug bounty programs

---

### 23. theHarvester

- **Organization:** Open-source project (Christian Martorella / laramies), maintained by community
- **Website:** https://github.com/laramies/theHarvester
- **Data held:** Does NOT hold data; passive OSINT aggregation tool querying 54+ external sources
- **Data sources queried:**
  - Search engines: Google, Bing, Yahoo, Baidu, DuckDuckGo
  - SecurityTrails (historical DNS)
  - Shodan, Censys
  - crt.sh (certificate transparency)
  - VirusTotal, Hunter.io
  - GitHub, LinkedIn (limited)
  - THC subdomain finder, SubdomainCenter
- **Data types collected:**
  - Email addresses
  - Subdomain names and IPs
  - Employee names
  - Open ports and banners
  - ASNs
  - URLs
- **Access model:**
  - Free and open-source (Python)
  - Included in Kali Linux by default
  - Many sources require free or paid API keys
- **Users:** Penetration testers, red teamers, OSINT analysts, bug bounty hunters
- **Geopolitical notes:** Open-source; no data held; fast reconnaissance tool for initial external attack surface mapping

---

### 24. Hacker Target

- **Organization:** HackerTarget.com (Australia-based)
- **Website:** https://hackertarget.com
- **Data held:**
  - Passive DNS data (aggregated from Certificate Transparency, scans.io, Shodan, Netcraft, Common Crawl, search engines)
  - Reverse IP (shared hosting enumeration)
  - Reverse DNS
  - WHOIS data
  - ASN and BGP lookups
  - IP geolocation (MaxMind)
  - Port and service banner data
- **Key tools:**
  - Domain Profiler (chained reconnaissance report)
  - Reverse IP Lookup
  - Reverse DNS Lookup
  - ASN Lookup
  - Subdomain Finder
  - DNS Lookup
  - DNSdumpster.com (companion free tool, see entry below)
- **Scale:** Not publicly quantified; aggregator of multiple external sources
- **Access model:**
  - Free web interface (rate-limited)
  - Paid API plans for higher volume
  - All passive tools send no packets to target
- **Users:** Penetration testers, security researchers, network engineers, OSINT analysts
- **Geopolitical notes:** Australian company; no known geopolitical concerns; open access

---

### 25. DNSdumpster

- **Organization:** HackerTarget.com (same operator as Hacker Target, above)
- **Website:** https://dnsdumpster.com
- **Data held:**
  - DNS records enumeration (A, MX, NS, TXT, CNAME)
  - Subdomain enumeration
  - Hosting provider and IP mapping
  - Service banners (TCP 21, 22, 23, 80, 443, 8080)
  - Network topology visualization (graphical map output)
- **Data sources:** Alexa Top 1M, search engines, Common Crawl, Certificate Transparency logs
- **Scale:** Free tool; processes DNS queries for millions of domains
- **Access model:**
  - Free web interface (no registration)
  - No bulk API (sister tool HackerTarget has paid API)
- **Users:** Security researchers, pen testers, attack surface mappers, bug bounty hunters
- **Geopolitical notes:** Australian; completely open access; no authentication required

---

### 26. Yandex (Russian Context)

- **Organization:** Yandex N.V. (Dutch holding) → Russian operations sold to VK/Yandex LLC consortium (April 2024) for ~$5.4B USD
- **Website:** https://yandex.ru / https://yandex.com
- **Data held (OSINT-relevant):**
  - Web crawl index (Russian and CIS internet coverage superior to Google in these regions)
  - Cached page content
  - Image reverse search (Yandex Images — stronger on Slavic face datasets)
  - Email (Yandex Mail — major Russian email provider)
  - Maps and geolocation (Yandex Maps)
  - DNS resolution data (Yandex DNS: 77.88.8.8 — public resolver)
  - Search query data (Russian-language sites indexed before Google)
  - Russian social media, forums, paste sites indexed more comprehensively
- **OSINT use cases:**
  - Searching Russian-language breach data, forums, paste sites
  - Reverse image search for Eastern European/Russian subjects
  - Discovering Russian-language infrastructure leaks
  - Accessing Runet content not well-indexed by Google
- **Data retention:** Web crawler continuously updated; historical cache varies
- **Scale:** Dominant search engine in Russia (~60% market share pre-2022); covers CIS region comprehensively
- **Access model:**
  - Free public search (web, images, maps)
  - Yandex Cloud / API products (commercial)
- **Geopolitical notes — CRITICAL FLAGS:**
  - **State alignment:** Following the 2024 restructuring, Yandex's Russian business operates under Russian law (Federal Law No. 149-FZ on Information, and RKN/Roskomnadzor regulatory authority)
  - **Data sovereign to Russia:** User queries, indexed content, and platform data are subject to Russian state access under SORM-3 (Russia's equivalent of CALEA/PRISM)
  - **DOD supply chain risk (2025):** A Russia-based Yandex employee was found to oversee open-source software approved for US DOD use — flagged by Nextgov/FCW in August 2025
  - **Runet isolation:** Russia is actively building infrastructure to disconnect Runet from the global internet by 2026; Yandex DNS (77.88.8.8) is one of the domestic resolution infrastructure components
  - **Western researcher risk:** Using Yandex services for OSINT research may expose query metadata to Russian intelligence services (FSB)
  - **Geofencing:** Some Yandex services inaccessible from certain Western IP ranges

---

### 27. Censys

- **Organization:** Censys, Inc. (Ann Arbor, Michigan, USA; spun out of University of Michigan research)
- **Website:** https://censys.com / https://search.censys.io
- **Data held:**
  - Internet-wide scan data: hosts, services, and certificates
  - Scans 200+ protocols on all 65,536 ports (probabilistic models for likely service locations)
  - X.509 certificate database: 8 billion certificates (from CT logs + internet scans)
  - Passive DNS (from HTTP(S) scans against names from CT logs, HTTP redirects, third-party passive DNS subscriptions)
  - IPv4 and IPv6 host enumeration
  - ASN and geolocation data
  - Vulnerability data (CVE mapping)
  - Daily snapshots (~2 TB/day compressed)
- **Data retention:** Daily snapshots; append-only certificate store (15–20 TB)
- **Scale:** ~3.3 billion indexed services; billions of certificates; 500+ academic research papers cite Censys data
- **Access model:**
  - Free web search (limited queries)
  - Censys CLI (open-source command-line tool)
  - Search API (paid tiers)
  - Bulk data / enterprise access
  - Academic researcher free access program
  - Censys ASM (Attack Surface Management) product (commercial)
- **Users:** Security researchers, pen testers, academics, threat hunters, enterprise security teams
- **Geopolitical notes:** US company; US academic origin (University of Michigan); provides free researcher access; widely cited in academic literature

---

### 28. GreyNoise

- **Organization:** GreyNoise Intelligence (Washington DC, USA)
- **Website:** https://www.greynoise.io
- **Data held:**
  - Mass internet scanner / background noise intelligence
  - Not passive DNS — instead: IP behavior classification (scanner, crawler, harmless, malicious, unknown)
  - 5,000+ honeypot sensors across 80+ countries
  - Tracks IPs conducting internet-wide scanning, exploitation attempts, credential stuffing
  - Tags: CVE exploitation attempts, service probing, botnet activity, tor exit node, VPN, hosting
  - GreyNoise "Recall" — time-series historical query capability (added 2025)
  - 2026 State of the Edge Report data: 2.97B malicious sessions from 3.8M unique IPs (H2 2025)
- **Scale:** 5,000+ global sensors; analyzes up to 1 billion sessions/day; tracks 50M+ IPs
- **Access model:**
  - Free community tier (limited lookups)
  - Paid API tiers
  - Enterprise data feeds (STIX/TAXII, SIEM integrations: Splunk, Microsoft Sentinel, Google SecOps)
  - MCP Server (launched September 2025 — AI agent-native threat intel queries)
- **Users:** SOC analysts, threat hunters, IR teams, SIEM platform integrators
- **Geopolitical notes:** US company; data collected from global sensor network; no specific geopolitical concerns; often used to de-noise alerts from mass scanners before investigating targeted attacks

---

### 29. Criminal IP

- **Organization:** AI Spera (South Korea; official service launched April 2023)
- **Website:** https://www.criminalip.io
- **Data held:**
  - Internet-wide IP scan: 4.2+ billion IPv4 addresses indexed
  - Device/service fingerprinting (ports, banners, service types)
  - WHOIS, geolocation, ASN attribution
  - Screenshot history for web services
  - IP blacklisting and DNSBL status
  - Malware activity and abuse history
  - Vulnerability mapping (CVEs)
  - Certificate data
  - IoT, ICS/SCADA devices
  - Four search modes: Asset, Domain, Image, Exploit
  - AI-powered threat score (0–100) per IP
- **Scale:** 4.2B+ IPs indexed; checks thousands of ports daily
- **Access model:**
  - Free tier (limited searches)
  - Paid subscription tiers
  - API access
- **Languages:** English, Korean, Japanese, French, Arabic
- **Users:** Security researchers, SOC teams, threat hunters, pen testers
- **Geopolitical notes:** South Korean company; no known PRC/government ties; competes with ZoomEye/FOFA in Asia-Pacific; geopolitically neutral relative to Chinese alternatives

---

### 30. Netlas.io

- **Organization:** Netlas (independent; Russia-origin team — flag for due diligence)
- **Website:** https://netlas.io
- **Data held:**
  - Internet-wide scanning: all IPv4 addresses + all known domain names
  - Protocols: HTTP, FTP, SMTP, POP3, IMAP, SMB/CIFS, SSH, Telnet, SQL and others
  - DNS records (A, AAAA, MX, NS, CNAME, TXT, SOA, etc.)
  - IP WHOIS and Domain WHOIS
  - SSL/TLS certificates
  - Open ports and service banners
  - IP geolocation and ASN attribution
  - Technology fingerprinting (~75% of hosts identified by passive scan)
  - Vulnerability data
- **Scale:** Scans every IPv4 address and all known domains; supports up to 65,536 targets per private scan
- **Access model:**
  - Community tier: 50 free requests/day (no credit card required)
  - Paid API tiers
  - Datastore: some databases purchasable directly
  - RESTful API (JSON)
  - Subfinder integration (non-default source)
- **Users:** Penetration testers, threat intelligence analysts, attack surface management teams
- **Geopolitical notes:** Unclear exact company jurisdiction (Ukraine/Russia-origin team); exercise caution for sensitive use cases; data itself is openly accessible; not known to be state-affiliated

---

### 31. ONYPHE

- **Organization:** ONYPHE SAS (France, founded 2017)
- **Website:** https://www.onyphe.io
- **Data held:**
  - Internet-wide IPv4 and IPv6 scanning
  - Passive DNS: 7 billion DNS queries/month → passive DNS database
  - Service banners and port data
  - SSL/TLS certificates
  - URL scanning: 40 million URLs/day
  - Web page content and headers
  - Historical DNS records and hosting changes
  - ASN, geolocation, WHOIS
  - Threat intelligence (known malicious IPs/domains)
  - Attack Surface Management data
- **Data retention:** Historical passive DNS; multi-year dataset
- **Scale (2025):** Data collection volume grew from 21 TB/month to 125 TB/month in 2025 (500% increase); scans 2,600+ ports weekly; 7B+ DNS queries/month
- **Access model:**
  - Free tier (limited)
  - Paid API tiers (tiered pricing at onyphe.io/pricing)
  - Enterprise ASM/ASD products
  - TheHive/Cortex integration (Strangebee)
  - Horizontally scalable platform
- **Users:** Enterprise security teams, MSSPs, threat intelligence researchers, European government agencies
- **Geopolitical notes:** French company; all data and query logs kept within EU; GDPR-compliant; good alternative to US-centric tools for EU-based organizations; no known government ties but EU-based may be preferable for European customers with data residency requirements

---

### 32. Recorded Future → Mastercard

- **Organization:** Recorded Future → acquired by Mastercard (December 20, 2024) for $2.65 billion
- **Website:** https://www.recordedfuture.com
- **Data held:**
  - Open web, dark web, technical sources (passive DNS, WHOIS, certificates, vulnerability data)
  - SecurityTrails data integrated (acquired January 2022 for $65M) — 3B+ WHOIS records, 2.6B+ hostnames
  - Threat actor tracking and attribution
  - Vulnerability intelligence
  - Brand monitoring
  - Financial crime intelligence
  - Attack surface management (via SecurityTrails)
  - Dark web forum monitoring
  - AI-powered Intelligence Graph
- **Scale:** 1,900+ clients in 75 countries; 45 government clients; 50%+ of Fortune 100; indexes open + dark web + technical sources continuously
- **Access model:**
  - Enterprise subscription (platform + API)
  - Intelligence modules (Attack Surface, Vulnerability, Dark Web, etc.)
  - SIEM/SOAR integrations
  - Analyst UI
- **Users:** Enterprise security teams, government intelligence agencies, financial institutions (Mastercard clients), SOC teams
- **Geopolitical notes:** Now owned by Mastercard (US payment network giant); combination of global transaction data + threat intelligence raises significant data aggregation concerns; 45 government clients including US IC; SecurityTrails data now embedded in Mastercard-owned platform

---

### 33. Intel471

- **Organization:** Intel471 (US-based; internationally staffed with ex-law enforcement and intelligence)
- **Website:** https://www.intel471.com
- **Data held:**
  - Underground cybercrime intelligence (not passive DNS / internet scanning)
  - Closed access: cybercrime forums, messaging platforms (Telegram, Discord), dark web marketplaces
  - Infostealer logs and malware tracking
  - Data breach logs
  - Covert source intelligence (human intelligence from cybercriminal communities)
  - Ransomware-as-a-Service (RaaS) monitoring
  - Threat actor profiles and TTPs
  - Verity471 platform — structured intelligence database
- **Scale:** 2025 findings: extortion activity +63% YoY; major cybercrime forum disruptions; tracks major ransomware operators
- **Access model:**
  - Enterprise subscription only
  - No free tier
  - Analyst portal + API
  - Maltego integration available
- **Users:** Enterprise security teams, law enforcement (primary customer base alongside corporate SOCs), financial institutions, government agencies
- **Geopolitical notes:** US-based; staffed by former law enforcement and intelligence officers from multiple nations; data cannot be published/shared publicly; primarily serves Western government and enterprise customers; not Chinese- or Russian-affiliated

---

### 34. Google Threat Intelligence (Mandiant + VirusTotal)

- **Organization:** Google / Alphabet (acquired Mandiant May 2022; VirusTotal acquired 2012)
- **Website:** https://cloud.google.com/security/products/threat-intelligence
- **Data held:**
  - Passive DNS (historical IP-domain resolutions from VirusTotal submissions + sensor network)
  - WHOIS lookup (current and pivoting by registrant properties)
  - SSL/TLS certificates
  - File hashes and malware samples (VirusTotal)
  - Threat actor profiles (Mandiant — 450,000+ hours of incident investigations/year)
  - Vulnerability intelligence (CVEs + exploitation timeline)
  - Dark web and underground monitoring
  - Google Threat Intelligence Group (GTIG) research
  - Incident response findings
- **Scale:** Combines VirusTotal's global sensor network (70+ AV engines), Mandiant's IR team, and Google's internet infrastructure visibility
- **Access model:**
  - Google Cloud Security subscription
  - API integration
  - Google SecOps / Chronicle SIEM integration
  - Palo Alto Cortex XSOAR integration
- **Users:** Enterprise security teams, government agencies, SOC/IR teams
- **Geopolitical notes:** Google/Alphabet (US); deeply integrated into US government security infrastructure; VirusTotal data submissions from 190+ countries — Google has visibility into global malware telemetry

---

### 35. IBM X-Force Exchange

- **Organization:** IBM Security (US)
- **Website:** https://exchange.xforce.ibmcloud.com
- **Status:** RETIRING — X-Force Exchange Threat Intelligence will reach end-of-life in 2026 (April or August depending on product tier); users directed to migrate to Palo Alto Networks or IBM Security Verify
- **Data held:**
  - IP reputation (risk scores 1–10)
  - Passive DNS (historical IP-domain associations)
  - WHOIS information
  - Vulnerability data
  - Threat indicator sharing (community-contributed)
  - Historical content and categorization
  - Malware file analysis
  - OSINT advisories
- **Access model:**
  - Free community tier (limited queries)
  - Commercial API (retiring)
  - SIEM integrations (IBM QRadar, etc.)
- **Users:** Security teams, IR analysts, SIEM operators
- **Geopolitical notes:** IBM (US); integrates global threat data; no specific geopolitical concerns; platform being retired

---

### 36. AlienVault OTX (Open Threat Exchange) — AT&T Cybersecurity

- **Organization:** AlienVault → acquired by AT&T Cybersecurity (2018)
- **Website:** https://otx.alienvault.com
- **Data held:**
  - Threat indicators (IPs, domains, URLs, file hashes) contributed by 100,000+ community members from 140 countries
  - 19 million+ threat indicators contributed daily (community-sourced "Pulses")
  - Passive DNS component (IP-domain associations reported by community)
  - WHOIS lookups
  - Malware samples and analysis
  - MITRE ATT&CK mapped threat intelligence
- **Scale:** Largest open threat intelligence community; 100% free community tier; 100,000+ participants
- **Access model:**
  - Free community access (web UI + API)
  - OTX DirectConnect (automated feed ingestion for SIEM/SOAR)
  - Integrations with AlienVault OSSIM/USM, Rapid7, Splunk, etc.
- **Users:** Security researchers, SOC analysts, threat hunters, community practitioners
- **Geopolitical notes:** AT&T (US); community contributions come from worldwide; data quality varies (community-sourced); useful for community threat sharing but requires validation

---

### 37. Pulsedive

- **Organization:** Pulsedive (independent)
- **Website:** https://pulsedive.com
- **Data held:**
  - IP, URL, and domain indicators
  - Passive DNS (WHOIS requests + DNS record collection on scan)
  - Active scanning (web browser-based fetch for HTTP headers, SSL certs, redirects)
  - Community-submitted threat feeds and IOCs
  - MITRE ATT&CK enrichment
  - Attribute correlation: ASN, country, WHOIS, HTTP headers, PTR records, metadata
  - 50M+ searchable indicators
- **Access model:**
  - Free (Visitor: search only; User: free account with submissions + exports)
  - Pro: $27.50/month (historical screenshots, full API)
  - Team plans and commercial API/Feed options
  - Browser extensions (Chrome, Firefox, Edge)
- **Users:** Security researchers, OSINT analysts, SOC teams, bug bounty hunters
- **Geopolitical notes:** Independent; no known geopolitical concerns; freemium model makes it accessible; good free alternative to commercial threat intel platforms

---

### 38. Team Cymru

- **Organization:** Team Cymru (US nonprofit → commercial arm: Team Cymru Inc.)
- **Website:** https://www.team-cymru.com
- **Data held:**
  - IP-to-ASN mapping service (widely used; free community service)
  - BGP feeds from 50+ peers (updated every 4 hours)
  - Bogon IP network lists (RFC 1918, IANA reserved, unallocated blocks)
  - Pure Signal Orbit (commercial threat intelligence)
  - Insights Threat Feed (launched March 2025): classifies 40M+ IPs daily, 2,000+ contextual tags
  - CSIRT community services: DDoS mitigation, threat detection, alerting
- **Scale:** 50+ BGP peers; 140 CERTs in 86+ countries served via free community services; 40M IPs/day classified in commercial feed
- **Access model:**
  - IP-to-ASN mapping: free WHOIS-based query (whois.cymru.com)
  - Bogon lists: free bulk download
  - Community CSIRT services: free for qualifying organizations
  - Commercial intelligence products: paid subscription
  - STIX/TAXII delivery for threat feeds
  - SIEM integrations: Google SecOps, Microsoft Sentinel, Splunk
- **Users:** Network operators, ISPs, CERTs, SOC teams, academic researchers
- **Geopolitical notes:** US nonprofit/commercial; long-standing trust in security community; community services genuinely free with no commercial ties; primarily western-alliance oriented

---

### 39. BGP.tools

- **Organization:** Ben Cartwright-Cox (UK, independent operator)
- **Website:** https://bgp.tools
- **Data held:**
  - BGP routing table data (near real-time)
  - ASN information (peers, prefixes, upstreams, downstreams, IXP membership)
  - IPv4 and IPv6 prefix data
  - Geolocation mapping of announced prefixes
  - RPKI validation status
  - BGP looking glass
  - MAC address lookups (via public OUI databases)
- **Status:** Recommended replacement for BGPView (which shut down November 2025)
- **Data retention:** Near real-time; changelog updated regularly (June 2026, April 2026, December 2025, etc.)
- **Scale:** Global BGP table coverage; independently operated
- **Access model:**
  - Entirely free
  - Web interface
  - API available
- **Users:** Network engineers, OSINT analysts, security researchers, ISPs
- **Geopolitical notes:** UK independent operator; completely open; no authentication required; no known geopolitical concerns

---

### 40. CAIDA (Center for Applied Internet Data Analysis)

- **Organization:** CAIDA — Center for Applied Internet Data Analysis (University of California San Diego, USA)
- **Website:** https://www.caida.org
- **Data held:**
  - Passive internet traffic measurement (OC192 monitor at SDSC since 2008; shifted to 100GB link LA-Dallas 2025)
  - BGP routing tables and routing history (AS relationship datasets — quarterly releases)
  - AS topology and relationship mapping (customer-provider, peer-to-peer)
  - Traceroute data (active measurement — Ark monitor infrastructure)
  - IPv4 and IPv6 address space analysis
  - Passive DNS (via partner feeds and measurement infrastructure)
  - Darknet / network telescope data
  - Submarine cable and internet infrastructure topology data
- **Data retention:** Multi-year; BGP relationship datasets go back to late 1990s
- **Scale:** Global measurement vantage points; datasets used in thousands of academic papers
- **Access model:**
  - Public datasets: free with user registration + data use justification form (new authentication framework from 2025)
  - Academic research access
  - Some datasets require non-commercial use agreement
  - Not available for commercial OSINT use without permission
- **Users:** Academic researchers, network operators, policy researchers, government research agencies
- **Geopolitical notes:** US academic institution (UC San Diego); NSF-funded; data shared with US government research programs; no commercial orientation

---

### 41. OpenINTEL

- **Organization:** University of Twente, SURF, SIDN, NLnet Labs (Netherlands academic collaboration)
- **Website:** https://openintel.nl
- **Data held:**
  - Active DNS measurement (not passive — it actively queries)
  - Daily queries for ~65% of the global DNS namespace (zone-based; all .com, .net, .org, .nl, etc.)
  - Record types: A, AAAA, MX, NS, SOA, CNAME, TXT, DNSKEY, DS, etc.
  - Near 3 trillion DNS records collected since 2015
  - Longitudinal dataset enabling trend analysis of the evolving DNS
- **Data retention:** Daily snapshots since 2015 — nearly a decade of DNS history
- **Scale:** 65% of global namespace; 3 trillion+ records; daily updated dataset
- **Access model:**
  - Academic/research access — application required
  - Data shared with researchers via University of Twente and partner institutions
  - Some datasets via SURF research infrastructure
  - Not available for commercial use
- **Users:** Academic researchers, DNS policy researchers, internet governance stakeholders, NLnet Labs / SIDN researchers
- **Geopolitical notes:** Dutch academic consortium; EU/Netherlands based; European research infrastructure; independent of commercial and US/CN government control; awarded Dutch national research data prize (2018)

---

### 42. BuiltWith

- **Organization:** BuiltWith Pty Ltd (Australia)
- **Website:** https://builtwith.com
- **Data held:**
  - Web technology profiling: CMS, frameworks, analytics, hosting, CDN, payment systems, etc.
  - 108,000+ tracked web technologies
  - 26M+ eCommerce websites; 2B+ unique eCommerce products
  - DNS records (A, MX, NS associated with profiled sites)
  - Hosting provider history and changes over time
  - Certificate data
  - Third-party library and tracking pixel presence
  - Employee count, revenue estimates, social media metrics
- **Data retention:** Historical technology changes tracked; temporal profiles of when technologies added/removed
- **Scale:** Billions of URL profiles; hundreds of millions of websites tracked
- **Access model:**
  - Free basic lookups (builtwith.com)
  - Commercial plans (technology lists, competitor analysis, bulk exports)
  - API access (paid)
  - Technology market share reports
- **Users:** Sales intelligence teams, competitor analysts, security researchers (identifying shared technology stacks), pen testers (finding software versions), marketers
- **Geopolitical notes:** Australian company; no known geopolitical concerns; widely used in competitive intelligence and ad tech targeting

---

### 43. Spamhaus

- **Organization:** Spamhaus Technology Ltd. (UK/Switzerland; founded 1998)
- **Website:** https://www.spamhaus.org / https://www.spamhaus.com (commercial arm)
- **Data held:**
  - Spamhaus Blocklist (SBL): 30–40K IP listings for spam senders
  - Exploits Blocklist (XBL): 2M+ listings; 650,000 new entries/day of exploited IPs (malware-infected hosts, open proxies, etc.)
  - Policy Block List (PBL): end-user IP space that should not send email directly
  - Domain Blocklist (DBL): domains associated with phishing, malware, spam
  - Combined Sender Base (CSS): recently seen spam sources
  - Hash Blocklist (HBL): hashes of malware files, cryptowallets, email addresses, URLs
  - Botnet Controller List (BCL): IPs hosting botnet C2 servers
  - DNSBL: all above lists served via real-time DNS query protocol
- **Data retention:** Continuously updated (PBL every 15 minutes; XBL daily new detections)
- **Scale:** 80+ DNSBL mirror servers worldwide; 100+ public mirrors; used by billions of email connections daily
- **Access model:**
  - Free for low-volume email filtering (public DNSBL queries)
  - Commercial Spamhaus DQS (Data Query Service): high-volume commercial licensing
  - IP reputation API
  - Threat intelligence feeds (commercial)
- **Users:** Email server operators, ISPs, web hosting providers, enterprise email security
- **Geopolitical notes:** UK/Swiss nonprofit-aligned; independent; widely trusted; no known geopolitical concerns; used by internet infrastructure globally

---

### 44. WhoisXML API

- **Organization:** WhoisXML API (US/international; major OEM data provider)
- **Website:** https://www.whoisxmlapi.com / https://dns-history.whoisxmlapi.com
- **Data held:**
  - WHOIS database: 28.7 billion records across 7,596+ TLDs
  - Passive DNS / DNS Chronicle: billions of historical DNS records; history back to 2008; 1,091M+ DNS records added weekly
  - DNS Database Download: 4.2+ billion domains and subdomains
  - IP WHOIS and ASN data
  - Domain availability and monitoring
  - Subdomain finder
  - Bulk WHOIS (500K domains simultaneous lookup)
  - DNS Chronicle API (launched October 2024): complete DNS history for domains/IPs
- **Data retention:** DNS history to 2008; WHOIS to early-2000s
- **Scale:** 28.7B WHOIS records; 4.2B+ domains; 52,000+ business customers
- **Users:** Fortune 500 companies, Cyber150 security vendors, government organizations, security researchers, fraud investigators
- **Geopolitical notes:** US-based but globally operated; no known geopolitical concerns; major OEM supplier to other OSINT tools (many tools query WhoisXML API under the hood)

---

### 45. Hunter.io

- **Organization:** Hunter SAS (France; founded 2015)
- **Website:** https://hunter.io
- **Data held:**
  - Email address discovery: indexed from billions of crawled public web pages
  - Domain Search: all publicly visible email addresses for a domain
  - Email Finder: guesses email format based on name + domain
  - Email Verifier: validates email deliverability (91.3% valid rate for standard B2B domains)
  - Not a passive DNS or BGP database — primarily email-focused OSINT
- **Scale:** Billions of indexed web pages; millions of domains covered
- **Access model:**
  - Free: 10 API requests/month; 25 searches/month
  - Starter: $34/month
  - Scale: $209–$299/month (25,000 credits/month)
  - Unified Credits system (launched July 2025)
  - Full REST API
- **Users:** Sales/marketing (primary), security researchers (for email OSINT), social engineering assessors, HR investigations
- **Geopolitical notes:** French company; EU data protection context; GDPR compliance; no infrastructure/routing/DNS data — purely email address discovery

---

### 46. Wayback Machine / Internet Archive

- **Organization:** Internet Archive (US nonprofit, San Francisco; founded 1996 by Brewster Kahle)
- **Website:** https://web.archive.org / https://archive.org
- **Data held:**
  - Crawled web page snapshots since 1996 — 1 trillion+ web pages archived as of 2025
  - 99 petabytes of unique data; 212+ petabytes with backups/redundancy
  - Cached HTML, JavaScript, CSS, images, media
  - Historical DNS infrastructure data (inferred from HTML source, redirect chains)
  - Historical contact information, email addresses, login pages from archived pages
  - Robots.txt history (can reveal hidden paths/directories)
  - PDF, documents, software, video, audio archives
- **Data retention:** Permanent; going back to 1996
- **Scale:** 1 trillion+ pages; 212+ petabytes; pivoting toward decentralized storage (2025 milestone)
- **Access model:**
  - Completely free, public access
  - Wayback Machine API (CDX API for programmatic access; free)
  - Bulk data not easily accessible (petabyte-scale requires contact)
  - Used by Amass, theHarvester, and other OSINT tools as a source
- **Users:** Journalists, legal teams, researchers, historians, OSINT analysts, digital forensics investigators
- **Geopolitical notes:** US nonprofit; operates under US law; broadly trusted; has faced domain-specific takedown requests; some content excluded by robots.txt exclusion requests; legally contested in some jurisdictions for copyright

---

### 47. IPinfo.io

- **Organization:** IPinfo LLC (US-based)
- **Website:** https://ipinfo.io
- **Data held:**
  - IP geolocation (city, region, country, coordinates)
  - ASN data (AS number, organization name, AS type: ISP/hosting/government/education/business, country)
  - IP-to-ASN mapping (IPv4 + IPv6)
  - Carrier/mobile network data
  - Privacy detection (VPN, Tor, datacenter, proxy flags)
  - Abuse contact data
  - IP ranges per ASN
- **Scale:** 44% of world's ASNs reachable within 1ms via active measurement; 500,000+ developer users; active measurement across 140+ countries and 500+ cities
- **Access model:**
  - IPinfo Lite API: free, unlimited country-level + basic ASN data
  - Paid tiers: full geolocation, privacy detection, carrier, ASN details
  - Database download (paid)
  - Snowflake, Splunk, GCP integrations
  - Daily updated ASN database download
- **Users:** Developers, security engineers, fraud detection teams, network operators, OSINT analysts
- **Geopolitical notes:** US company; no known geopolitical concerns; widely used by commercial and open-source tools

---

### 48. MaxMind GeoIP

- **Organization:** MaxMind, Inc. (US; founded 2002)
- **Website:** https://www.maxmind.com
- **Data held:**
  - IP geolocation databases (city, country, ISP, organization, domain, user type)
  - GeoIP2 City Database: city-level accuracy for 99.9999% of IPs in use
  - GeoIP2 ISP Database: ISP and organization attribution
  - GeoLite (free): country + city-level; released since 2002
  - Connection type data (cable, dial-up, mobile, etc.)
  - Domain to IP mapping component
- **Data retention:** Weekly/daily updates; free GeoLite updated weekly (Monday–Friday)
- **Scale:** Covers 99.9999% of IPs in use; 20+ years of IP geolocation data
- **Access model:**
  - GeoLite2: free (requires registration; Creative Commons Attribution-ShareAlike 4.0)
  - GeoIP2 Commercial: paid subscription
  - Local database download (MMDB format) or web service API
  - Used embedded in Apache, Nginx, and most security products
- **Users:** Web developers, content delivery networks, fraud prevention teams, security tools, ISPs, ad networks
- **Geopolitical notes:** US company; widely embedded in global internet infrastructure; de facto standard for IP geolocation in security tools; used by governments and commercial entities worldwide

---

### 49. PublicWWW

- **Organization:** PublicWWW (independent, Russia-origin operator)
- **Website:** https://publicwww.com
- **Data held:**
  - Source code search engine: searches HTML, JavaScript, and CSS of indexed web pages
  - Identifies specific code patterns, analytics tags, ad network snippets, tracking pixels, JavaScript library signatures
  - Useful for finding all sites using a specific ad network ID, analytics tag, or malware JavaScript pattern
  - Not passive DNS — no routing or DNS resolution data; purely source code content
- **Scale:** Indexes billions of web pages
- **Access model:**
  - Free (limited results per search)
  - Paid plans (full result export)
- **Users:** Security researchers (tracking malware infrastructure via shared JS), ad fraud investigators, competitive intelligence analysts
- **Geopolitical notes:** Russia-origin operator; exercise caution for sensitive queries; no specific known intelligence-service ties

---

### 50. Common Crawl

- **Organization:** Common Crawl Foundation (US nonprofit; San Francisco)
- **Website:** https://commoncrawl.org
- **Data held:**
  - Monthly web crawl snapshots since 2008
  - 250+ billion crawled web pages
  - Data formats: WARC (raw), WET (extracted text), WAT (metadata), CDX (index)
  - URL-level index enables querying for specific domains, paths, patterns
  - HTML source, HTTP headers, metadata
  - Not passive DNS but enables DNS enumeration from discovered URLs
- **Data retention:** Monthly crawl archives since 2008; permanently stored on AWS S3 (open access)
- **Scale:** Single monthly archive: 50–100 TB compressed; 10,000+ research papers cite Common Crawl
- **Access model:**
  - Completely free; publicly available on AWS S3 (Registry of Open Data on AWS)
  - No registration required for data download
  - Heavy compute required for full processing
- **Users:** Academic researchers, AI/ML training dataset teams (foundational to GPT, BERT training data), security researchers, SEO analysts
- **Geopolitical notes:** US nonprofit; AWS-hosted; widely used by AI companies globally; some concern about data privacy (crawls public web content without opt-out mechanism by default)

---

### 51. FullHunt

- **Organization:** FullHunt (independent startup)
- **Website:** https://fullhunt.io
- **Data held:**
  - External attack surface management (EASM) database
  - Domain and subdomain enumeration
  - IP and host discovery
  - Port and service enumeration
  - Technology fingerprinting
  - Vulnerability detection and risk assessment
  - Dark web monitoring component
  - Third-party risk management data
  - Global internet space scanning data
- **Access model:**
  - Free community tier
  - Enterprise paid subscription (continuous ASM, dark web monitoring, 3P risk)
  - REST API (paid)
  - Listed as non-default source in Subfinder
- **Users:** Security teams, red teamers, bug bounty hunters, enterprise security programs
- **Geopolitical notes:** Independent; no known geopolitical concerns

---

### 52. LeakIX

- **Organization:** LeakIX (independent; France-based operator)
- **Website:** https://leakix.net
- **Data held:**
  - Internet-wide scan for exposed/misconfigured services
  - Unauthenticated databases: MongoDB, Elasticsearch, Redis, CouchDB, Cassandra, MySQL, PostgreSQL
  - Misconfigured cloud storage: S3 buckets, Azure Blob, GCP Cloud Storage (public listing/access)
  - Exposed web applications and services
  - Leaked credentials and sensitive data leakage from misconfigured hosts
  - Email/password/host-level pivots on exposed data
- **Scale:** Continuously scanning internet; indexes exposed services globally
- **Access model:**
  - Free web interface (leakix.net)
  - Paid subscription for full detail and API
  - Listed as default source in Subfinder
- **Users:** Security researchers, bug bounty hunters, threat intelligence analysts, pen testers, defenders (for exposure monitoring)
- **Geopolitical notes:** France-based; European operator; no known government ties; operates in a legal gray area (scanning and indexing exposed data without targets' consent is controversial)

---

### 53. Rapid7 Open Data / Project Sonar — FDNS & DNSGrep

- **Organization:** Rapid7 (US publicly traded cybersecurity company)
- **Website:** https://opendata.rapid7.com
- **Data held:**
  - Forward DNS (FDNS): DNS responses for all known domain names (ANY queries; A, AAAA, CNAME, TXT records)
  - Reverse DNS: PTR record sweeps across IPv4 space
  - Open port data from Project Sonar internet scanning
  - TLS/SSL certificate data
  - HTTP response data
  - Updated approximately weekly
- **Scale:** Forward DNS covers hundreds of millions of domain names; ~10–50 GB compressed GZIP per snapshot
- **Data access formats:** JSON-lines compressed GZIP; available via Rapid7 API (free researcher account) or direct download; also mirrored on AWS Open Data Registry
- **OSINT tooling:**
  - DNSGrep: binary search tree tool for querying FDNS dataset efficiently; experimental API
  - Used by bug bounty hunters, pen testers for subdomain enumeration without active scanning
- **Access model:**
  - Free for researchers (registration at opendata.rapid7.com)
  - Commercial access for more frequent updates
  - AWS Open Data Registry (free)
- **Users:** Security researchers, bug bounty hunters, pen testers, threat intelligence teams
- **Geopolitical notes:** US commercial company; open data program is genuinely open; commercial product tracks for the data; no specific geopolitical concerns

---

### 54. ProjectDiscovery / Subfinder

- **Organization:** ProjectDiscovery (US-based; open-source security tooling company)
- **Website:** https://projectdiscovery.io / https://github.com/projectdiscovery/subfinder
- **Data held:** Subfinder does NOT hold data; it is a passive subdomain enumeration tool that aggregates 40+ passive DNS and OSINT sources
- **Sources queried (default):**
  - AlienVault, Certspotter, Censys, Chaos (ProjectDiscovery), crt.sh
  - DNSdumpster, FOFA, FullHunt, HackerTarget, LeakIX
  - ONYPHE, Robtex, SecurityTrails, Shodan, VirusTotal
  - WhoisXML API, Zoomeye, and 20+ more
- **Sources queried (non-default/all):**
  - CommonCrawl, DNSDB, GitHub, Netlas, RapidDNS
  - Sitedossier, ThreatBook, Wayback Machine, HudsonRock, and others
- **Architecture:** Go-based; concurrent goroutines for parallel source querying; API key configured via config file
- **Access model:**
  - Free and open-source (GitHub)
  - Kali Linux included
  - API keys needed for most high-value sources
- **Users:** Penetration testers, bug bounty hunters, red teamers, attack surface managers
- **Geopolitical notes:** Open-source; RSAC 2025 Innovation Sandbox finalist; no data retention; queries go to third-party services

---

### 55. Cloudflare Radar

- **Organization:** Cloudflare, Inc. (US; San Francisco)
- **Website:** https://radar.cloudflare.com
- **Data held:**
  - DNS query trends (patterns derived from Cloudflare 1.1.1.1 resolver — 180B+ queries/day)
  - Internet traffic trends (country-level, network-level traffic patterns)
  - BGP routing data and RPKI validation statistics
  - Real-time BGP route visibility (added 2025)
  - Certificate Transparency (Nimbus logs)
  - DDoS attack statistics
  - Internet outage and disruption tracking
  - IPv6 adoption metrics
  - Domain registration trends (newly registered domains)
  - Protocol usage statistics (HTTP/2, HTTP/3, QUIC, post-quantum TLS)
- **Scale:** Cloudflare is one of the largest DNS resolvers globally; processes hundreds of billions of DNS queries daily from global user base; 2025 Year in Review is their sixth annual
- **Access model:**
  - Free public dashboard (radar.cloudflare.com)
  - Cloudflare API: BGP Routes, DNS stats, traffic data (free tier available)
  - No bulk raw data export
- **Users:** Network researchers, security analysts, internet governance stakeholders, journalists, government policy teams
- **Geopolitical notes:** US company; Cloudflare handles significant fraction of global internet traffic — data provides unprecedented visibility into internet behavior; no specific concerns but Cloudflare's scale means data reflects global internet usage patterns and geopolitical internet events in near real-time

---

### 56. Cisco Umbrella Investigate

- **Organization:** Cisco Systems / OpenDNS (acquired by Cisco 2015)
- **Website:** https://umbrella.cisco.com/products/umbrella-investigate
- **Data held:**
  - Passive DNS: 800 billion DNS queries/day analyzed (from Umbrella resolver infrastructure)
  - 5-year historical passive DNS snapshots with security categorization timeline
  - Domain threat categorization history
  - IP-domain relationship mapping
  - SSL/TLS certificate data
  - AS/BGP data
  - Whois information
  - Newly Seen Domains feed
  - AI-enhanced DNS tunneling detection (Black Hat Asia 2025 research)
- **Data retention:** 5 years of passive DNS history; security categorization over time
- **Scale:** 180B+ DNS requests analyzed/day via Umbrella resolvers; 800B queries/day in full passive DNS infrastructure — one of the largest passive DNS datasets in existence
- **Access model:**
  - Enterprise subscription (Cisco Umbrella Investigate product)
  - API integration
  - Cortex XSOAR, Splunk, SIEM integrations
  - Not available as free tool
- **Users:** Enterprise SOC teams, threat hunters, IR teams, Cisco Talos threat researchers
- **Geopolitical notes:** Cisco/US; deeply embedded in enterprise DNS infrastructure globally; Talos threat intelligence team is one of the largest private threat research organizations; data at this scale provides geopolitical insight into DNS traffic patterns

---

### 57. PassiveDNS.cn / Qihoo 360 PassiveDNS

- **Organization:** Qihoo 360 (Beijing, China) — later integrated into Qi Anxin (QAX)
- **Website:** https://passivedns.cn
- **Data held:**
  - Passive DNS: Chinese internet DNS traffic (~10% of China's DNS traffic; ~900,000 queries/second)
  - 5.7 billion DNS resource record sets
  - 17.2 billion resource data entries
  - 4.6 billion unique domains
  - Chinese domestic DNS resolution patterns (significant coverage of Baidu, Alibaba, Tencent CDN infrastructure)
- **Data retention:** Collected since ~2014; multi-year archive
- **Scale:** Largest public passive DNS database in China; first to open to security communities (NSP-SEC, OPS-TRUST)
- **Access model:**
  - Restricted access: application required; available to "qualified individuals" (security researchers, network security admins)
  - No open commercial API
  - No free public access
- **Users:** Chinese and international security researchers, CERTs, APT researchers
- **Geopolitical notes — CRITICAL FLAGS:**
  - Operated by Qihoo 360 (and/or QAX) — Chinese cybersecurity companies with close PRC government ties
  - Data reflects 10% of China's DNS traffic — queries to this service are visible to Chinese intelligence
  - 360 has documented ties to PRC security apparatus; NSO Group-style disclosures have highlighted Chinese firm cooperation with government
  - Western researchers using this service for China-related investigations should assume query logs are accessible to PRC security services
  - Coverage of Chinese domestic internet infrastructure is unmatched by any Western tool

---

### 58. Qihoo 360 Quake (网络空间测绘)

- **Organization:** Qihoo 360 (Beijing, China) — 360 Network Security Research Lab
- **Website:** https://quake.360.net/quake
- **Data held:**
  - Network space mapping ("网络空间测绘"): internet-wide asset scan
  - Billions of indexed network assets
  - Coverage: 1,000+ common and industrial control protocols; 20 categories including communications, ICS, blockchain, IoT, video
  - Device fingerprinting, service banners, port data
  - Passive DNS integrated with 360's broader passive DNS infrastructure (started 2014)
  - WHOIS, certificate data, sandboxes, honeypot data
  - Honeypot detection feature (can check if an IP is a honeypot)
  - Combined with 360 Threat Intelligence Platform for IOC enrichment
- **Scale:** Billions of assets indexed; combined with 360's broader intelligence infrastructure (URLs, certificates, sandbox, passive DNS)
- **Access model:**
  - Chinese language primary (English available)
  - Registration required
  - Free tier for limited queries; commercial tiers
  - Command-line tool (quake_rs) on GitHub
- **Users:** Chinese security researchers, PRC-aligned APT actors, global pen testers
- **Geopolitical notes — CRITICAL FLAGS:**
  - Same geopolitical concerns as ZoomEye and FOFA: PRC government ties, state data access
  - 360 has been sanctioned/blocked by multiple Western governments; 360 Mobile Services blacklisted by UK government
  - Honeypot detection feature suggests tactical offensive use cases beyond pure research
  - Data accessible to PRC intelligence services

---

### 59. Shadowserver Foundation

- **Organization:** Shadowserver Foundation (US nonprofit; founded 2004)
- **Website:** https://www.shadowserver.org
- **Data held:**
  - Malware analysis and botnet tracking via global sinkhole infrastructure
  - Internet-wide scanning: full IPv4 scanned 42 times/day
  - 90+ distinct report types (DNS open resolvers, exposed services, compromised websites, etc.)
  - Passive DNS / network sensor data from honeypots and honeyclients
  - Botnet command-and-control tracking
  - DDoS amplification source enumeration
  - Compromised device feeds (IoT, SOHO routers, medical devices)
  - Law enforcement cooperation data (coordinated takedowns)
  - 2025: Operation Endgame follow-on — 86M+ stolen records from Rhadamanthys infostealer; 525,000+ infections across 226 countries
- **Data retention:** Ongoing; historical data maintained for trend analysis
- **Scale:** 42 full IPv4 scans/day; data sent to 130+ national CERTs and network operators daily; global sinkhole network
- **Access model:**
  - Free for qualifying organizations (CERTs, national computer emergency response teams, network operators)
  - Automated daily email/API reports per ASN or prefix
  - No public bulk download
  - Partners with law enforcement globally
- **Users:** National CERTs, ISPs, network operators, law enforcement, academic researchers
- **Geopolitical notes:** US nonprofit; strong law enforcement partnerships across Five Eyes and beyond; data not publicly accessible but widely disseminated to critical infrastructure operators; considered trusted and neutral by global CSIRT community

---

### 60. ThreatBook (微步在线)

- **Organization:** ThreatBook (微步在线, Beijing-based; Chinese cybersecurity company; founded 2015)
- **Website:** https://threatbook.io (international) / https://www.threatbook.com (Chinese)
- **Data held:**
  - Passive DNS: historical DNS resolutions linking domains and IPs
  - WHOIS data
  - SSL/TLS certificate data
  - Malware indicators and attack history
  - Threat actor tracking (APAC-focused; PRC, North Korea, Southeast Asia actor tracking since 2015)
  - Verdicts, threat labels, MITRE ATT&CK mapping
  - OneDNS: DNS-based security gateway (checks against 100M+ threat indicators)
  - Network Detection and Response (NDR) — Gartner Magic Quadrant for NDR (June 2025): only Chinese company selected
- **Access model:**
  - Community intelligence portal (i.threatbook.io) — free limited access
  - Commercial CTI platform (enterprise subscription)
  - API access (paid)
  - Subfinder integration (non-default ThreatBook source)
- **Users:** Chinese enterprise security teams, APAC regional incident responders, global threat intelligence researchers
- **Geopolitical notes — MODERATE FLAG:**
  - Chinese company; data reflects PRC-centric threat intelligence perspective
  - APAC actor tracking may include data not available in Western threat intel feeds
  - Operates under PRC data sovereignty law — Chinese government can access platform data
  - Growing international presence (Gartner recognition 2025) — used by non-Chinese organizations for APAC threat intelligence
  - Western organizations should be aware of data sovereignty implications when submitting indicators to ThreatBook platform

---

### 61. NSA XKEYSCORE / Five Eyes SIGINT (Publicly Known)

- **Organization:** NSA (US), GCHQ (UK), ASD (Australia), CBNC/CSE (Canada), GCSB (New Zealand) — Five Eyes
- **Context:** Publicly known intelligence programs, NOT commercially accessible
- **Publicly known data collected:**
  - XKEYSCORE: NSA "analytic framework" and data-retrieval system for signals intelligence
  - Indexes: email addresses, file names, IP addresses, port numbers, cookies, webmail/chat usernames, buddy lists, phone numbers, browser metadata including search queries
  - "3-day rolling buffer" of "all unfiltered data" at 150 global sites on 700 database servers (as of 2013 Snowden disclosure)
  - Content: retained 3–5 days; metadata: retained 30 days
  - Passive DNS, BGP routing data, and internet flow data collected separately under other SIGINT programs (PRISM, MUSCULAR, TURMOIL, etc.)
- **Five Eyes sharing:** NSA shares XKeyscore with ASD (Australia), CSE (Canada), GCSB (New Zealand), GCHQ (UK); also shared with German BND, Danish FE, Japan DIA
- **Current status (2026):** Programs presumed active but details beyond Snowden/2013 disclosures not publicly confirmed; no new large-scale leaks confirming scale/scope updates
- **Access:** NOT accessible; government intelligence use only; classified
- **Geopolitical notes:**
  - Most powerful internet surveillance infrastructure in existence (though China's capabilities may be comparable for Chinese internet)
  - Exposed by Edward Snowden in June 2013
  - Western allies (Five Eyes) share raw SIGINT; "14 Eyes" extends to Germany, France, Sweden, etc.
  - Russian equivalent: SORM-3 (FSB-controlled) operates similarly on Russian internet infrastructure
  - Chinese equivalent: The Great Firewall / CNNIC / PRC DPI infrastructure

---

### 62. Dark Web / Underground OSINT Aggregators (Overview)

Key commercial operators providing dark web and underground forum intelligence:

#### 62a. Recorded Future (covered in #32) — dark web indexing integrated
#### 62b. Intel471 (covered in #33) — primary underground cybercrime intelligence vendor
#### 62c. FalconFeeds
- **Website:** https://falconfeeds.io
- Real-time feeds from dark web, deep web, and open sources
- STIX/TAXII feeds for SIEM/SOAR/TIP integration
- Ransomware group tracking; data breach marketplace monitoring

#### 62d. SpyCloud
- **Website:** https://spycloud.com
- Breach data recovery from underground markets
- 2025 Identity Exposure Report: average corporate user has 146 stolen records linked to their identity (12× increase vs. prior estimates)
- Enterprise account takeover prevention; law enforcement cooperation

#### 62e. KELA Cyber Intelligence
- **Website:** https://ke-la.com
- Dark web monitoring focused on cybercrime, ransomware, financial fraud
- Tracks 300K+ underground sources; human intelligence from criminal forums

#### 62f. Constella Intelligence
- **Website:** https://constella.ai
- Breach data, dark web exposure, identity risk scoring

**Dark web OSINT context:**
- Dark web data primarily accessed via Tor/.onion sites and I2P networks
- Commercial vendors maintain long-term access to private forums through cover identities (especially Intel471, which employs ex-law enforcement)
- Law enforcement operations in 2025 (Operation Talent) disrupted major English-speaking forums: Cracked, Nulled, Sellix, StarkRDP — Nulled shut down permanently; Cracked resurfaced under new domain
- OSINT market growth: $12.7B in 2025; projected $133.6B by 2035 at 26.7% CAGR

---

### 63. Russian Internet Infrastructure (Runet OSINT Context)

- **Qrator Labs:** https://qrator.net — Russian DDoS mitigation and BGP routing analytics; publishes research on Russian BGP connectivity; politically neutral commercially but subject to Russian law
- **RU-CERT:** https://www.cert.ru — Russian CERT operated under Coordination Center for TLD .RU; national CSIRT; limited external information sharing post-2022
- **Roskomnadzor (RKN):** Russian internet regulator; controls domain/IP blocklists under SORM/sovereign internet laws; operates Russia's internet filtering infrastructure
- **SORM-3:** Russia's equivalent of NSA PRISM/CALEA; all Russian ISPs required to install FSB-controlled intercept equipment; captures metadata and content for all Russian internet users
- **Russian OSINT/DNS tools (domestic):** Yandex DNS (77.88.8.8), PassiveDNS.cn (360/QAX — Chinese tool also covers Russian internet indirectly), Qrator Radar (BGP monitoring)
- **Sovereign Internet Law (2019):** Russia implements deep packet inspection (DPI) infrastructure managed by RKN; designed to isolate Runet from global internet; October 2025 government decree grants centralized control authority
- **OSINT research risk:** Researching Russian infrastructure using Russian tools (Yandex, RU-CERT) exposes query metadata to FSB/SVR; use neutral Western tools (RIPE NCC, Shodan, Censys) for Russian infrastructure research

---

### 64. Microsoft Defender Threat Intelligence (MDTI) — Retirement Note

- **Organization:** Microsoft (formerly RiskIQ / PassiveTotal)
- **Website:** https://ti.defender.microsoft.com
- **Status:** RETIRING August 1, 2026 as standalone product
- **Transition:** MDTI features being merged into Microsoft Defender XDR and Microsoft Sentinel at no additional cost (included in Microsoft 365 E5 licensing)
- **What changes:** Standalone MDTI portal and separate SKU retire; features accessible via Sentinel and Defender XDR for existing license holders; PassiveTotal community edition access lost
- **Notes:** See Entry #1 (PassiveTotal/RiskIQ) for full data holdings description; this entry documents the August 2026 retirement event
- **OSINT community impact:** Free and community-tier passive DNS access (which previously existed via PassiveTotal community) fully sunset; researchers must use paid Microsoft licensing or migrate to alternatives (DomainTools, SecurityTrails/Recorded Future, WhoisXML API, etc.)

---

### 65. ODIN (Cyble)

- **Organization:** Cyble Inc. (US-based; Alpharetta, Georgia)
- **Website:** https://odin.io / https://search.odin.io
- **Data held:**
  - Internet-wide scan: full IPv4 and IPv6 address space
  - Host, subdomain, and URL discovery
  - Open port and service enumeration
  - Vulnerability scanning and CVE mapping
  - Exposed cloud bucket detection (S3, Azure Blob, GCP)
  - Technology fingerprinting
  - Threat intelligence integration (Cyble Vision platform)
  - 2025 telemetry: used to predict and flag unusual cloud activity ahead of publicly reported breaches
- **Scale:** Full IPv4 + IPv6 continuous scanning; 10 free searches/day for public users
- **Access model:**
  - 10 free searches/day (public)
  - Paid enterprise tiers (Cyble Vision TIP platform)
  - Microsoft Azure Marketplace
  - Recognized: Forrester ETIS Providers Q1 2026; Gartner Peer Insights 2026
- **Users:** Enterprise security teams, SOC/IR teams, attack surface management programs
- **Geopolitical notes:** US-based; no known geopolitical concerns

---

### 66. Intelligence X (Intelx.io)

- **Organization:** Intelligence X (Prague, Czech Republic; independent; founded 2018 by Peter Kleissner)
- **Website:** https://intelx.io
- **Data held:**
  - Dark web indexing (Tor/.onion, I2P sites)
  - Data leak archives (breach dumps, credential leaks, sensitive document dumps)
  - Historical web page archives (dark web + paste sites — Wayback Machine equivalent for dark/deep web)
  - WHOIS data search
  - Government and corporate document leaks
  - Paste site content (Pastebin, Ghostbin, etc.)
  - Telegram channel and group indexed content
  - Search by selectors: email, domain, URL, IP, CIDR, Bitcoin address, IPFS hash
- **Scale:** Large historical dataset spanning dark web, deep web, and leaked data archives
- **Access model:**
  - Free limited searches (public)
  - Paid plans (Professional, Corporate)
  - API access (paid)
  - Non-default source in Subfinder (intelx)
- **Users:** OSINT investigators, journalists (Bellingcat uses intelx), threat intelligence analysts, law enforcement, pen testers
- **Geopolitical notes:** Czech/European company; content includes legally sensitive material (breach data, classified leaks, dark web content); Bellingcat uses intelx.io in investigative workflows; operates in legal gray areas in multiple jurisdictions; content from Russia, China, and other adversary nations indexed here

---

### 67. Hudson Rock

- **Organization:** Hudson Rock (Israel/US; founded 2020 by Roi Carthy and Alon Gal)
- **Website:** https://www.hudsonrock.com / https://cavalier.hudsonrock.com
- **Data held:**
  - Infostealer-infected computer database: 30M+ compromised computers analyzed
  - Compromised credentials, browser cookies, saved passwords, autofill data from infostealer logs
  - 11.6M+ compromised domains identified
  - Corporate credential exposure tracking (employee, customer, partner accounts)
  - APT-linked infostealer activity (e.g., Bitter APT / PTCL breach, 2025)
- **Scale:** 30M+ compromised computers; 11.6M+ compromised domains; 100+ enterprise customers; 4600% ARR growth in 4 years
- **Access model:**
  - Enterprise subscription (Cavalier platform)
  - Free API endpoints for limited lookups
  - Non-default Subfinder source (hudsonrock)
- **Users:** Enterprise security teams, incident responders, government intelligence, fraud teams
- **Geopolitical notes:** Israel-US company; APT attribution via infostealer data is geopolitically relevant (2025 India-Pakistan conflict attribution); increasingly used in nation-state threat intelligence context

---

### 68. PeeringDB

- **Organization:** PeeringDB, Inc. (US nonprofit; San Mateo, California)
- **Website:** https://www.peeringdb.com
- **Data held:**
  - Voluntary registry of ASNs and their peering relationships
  - Internet Exchange Points (IXPs): physical locations, participants, port speeds, contact info
  - Network facility data (colocation facilities where networks interconnect)
  - Peering policies, contact information, IRC channels
  - Not passive DNS — network infrastructure topology and physical location registry
- **Scale:** Global coverage; de facto standard registry for internet peering data; continuously updated by network operators
- **Access model:**
  - Free public access (read; no authentication required)
  - Free REST/JSON API
  - IXP Manager integration
- **Users:** Network operators, ISPs, IXP managers, OSINT investigators (network attribution, physical facility mapping), academic researchers
- **Geopolitical notes:** US nonprofit; data submitted voluntarily; major ISPs, CDNs, cloud providers, and governments listed; physical facility locations can reveal otherwise-undisclosed infrastructure presence

---

### 69. IVRE (Instrument de Veille sur les Réseaux Extérieurs)

- **Organization:** Open-source project (France-origin; Pierre Lalet / CEA — French Alternative Energies and Atomic Energy Commission)
- **Website:** https://ivre.rocks / https://github.com/ivre/ivre
- **Data held:** IVRE does NOT hold data centrally; it is a self-hosted network reconnaissance framework
- **Capabilities:**
  - Active network scanning integration (Nmap, Masscan, ZGrab2, ZDNS)
  - Passive DNS collection via Zeek (logs DNS_ANSWER records from live traffic)
  - Passive network traffic analysis and flow logging
  - Self-hosted alternative to Shodan/Censys — organizations can build sovereign internet scan databases
  - Web interface + CLI + Python API
  - MongoDB and PostgreSQL backends
- **Access model:**
  - Free and open-source (GPLv3)
  - Self-hosted only — no cloud service
  - GitHub: github.com/ivre/ivre
- **Users:** National CERTs, defense/intelligence researchers, academic security teams, organizations needing sovereign (non-US/CN) internet scanning capability
- **Geopolitical notes:** French-origin with CEA affiliation (French defense/nuclear research); enables EU governments and researchers to run internet intelligence operations without depending on US or Chinese commercial platforms; significant for European digital sovereignty efforts

---

### 70. ProjectDiscovery Chaos

- **Organization:** ProjectDiscovery (US-based)
- **Website:** https://chaos.projectdiscovery.io
- **Data held:**
  - Crowdsourced subdomain datasets from public bug bounty programs
  - Live certificate stream ingestion
  - DNS PTR lookups, TLS grabs, HTTP header collection
  - IPv4 scanning on non-default ports
  - Dynamic dataset; weekly updates
- **Scale:** Hundreds of thousands of domains from public bug bounty program attack surfaces; crowdsourced from active security researchers
- **Access model:**
  - Paid API subscription (Chaos)
  - Default Subfinder source (chaos)
  - Limited free access for bug bounty researchers
- **Users:** Bug bounty hunters, security researchers, red teamers, attack surface managers
- **Geopolitical notes:** US company; RSAC 2025 Innovation Sandbox finalist; no geopolitical concerns

---

## Key Status Updates / Deprecations (2024–2026)

| Service | Status | Date |
|---|---|---|
| BinaryEdge (standalone) | SHUTDOWN | March 31, 2025 |
| BGPView | SHUTDOWN | November 26, 2025 |
| Microsoft MDTI (standalone) | RETIRING | August 1, 2026 |
| IBM X-Force Exchange | END OF LIFE | 2026 (April or August) |
| Spyse | PERMANENTLY CLOSED | ~2022–2023 |
| RiskIQ PassiveTotal (community edition) | MERGED into MDTI → retiring | 2021–2026 |
| SecurityTrails (independent) | ACQUIRED by Recorded Future | January 2022 ($65M) |
| Recorded Future (independent) | ACQUIRED by Mastercard | December 2024 ($2.65B) |

---

## Summary: Data Type Coverage Matrix

| Data Type | Top Operators |
|---|---|
| Passive DNS (largest scale) | Cisco Umbrella (800B/day), DNSDB (DomainTools), SecurityTrails, WhoisXML API, MDTI/RiskIQ |
| Internet-wide scanning | Shodan, Censys, FOFA, ZoomEye, Netlas, Criminal IP, Quake (360), ODIN (Cyble), Shadowserver |
| WHOIS history (longest) | DomainTools (~2001), WhoisXML API (28.7B records), SecurityTrails, RIRs (ARIN/RIPE/APNIC/LACNIC/AFRINIC) |
| BGP / ASN routing | RIPE RIS, RouteViews, HE BGP Toolkit, BGP.tools, Team Cymru, Cloudflare Radar |
| Certificate Transparency | crt.sh (Sectigo), Google CT (Argon/Xenon), Cloudflare Nimbus, Let's Encrypt Oak, DigiCert |
| Dark web intelligence | Intel471, Recorded Future, FalconFeeds, SpyCloud, KELA, Intelligence X |
| Infostealer data | Hudson Rock (30M+ machines), SpyCloud, Group-IB |
| Web technology fingerprinting | BuiltWith, Netcraft, Shodan, Censys |
| Email OSINT | Hunter.io, theHarvester, WhoisXML API |
| Web archive / history | Wayback Machine (1T+ pages), CommonCrawl (250B+ pages), Intelligence X (dark web) |
| IP reputation / blocklists | Spamhaus (DNSBL), GreyNoise, Team Cymru, AlienVault OTX, Pulsedive |
| Attack surface management | FullHunt, Cyble ODIN, Censys ASM, ONYPHE, Netlas, Criminal IP, Maltego, IVRE |
| Chinese internet (geopolitical flag) | ZoomEye (Knownsec), FOFA (Huashun), Quake (Qihoo 360), PassiveDNS.cn, ThreatBook |
| Academic / open datasets | CAIDA, OpenINTEL, CommonCrawl, Rapid7 Open Data, Shadowserver, RIPE RIS |
| Aggregator/framework tools | Maltego, Recon-ng, Amass, Subfinder, theHarvester, SpiderFoot |

---

**Research completed:** June 2026  
**Total entries documented:** 70 (plus ecosystem overviews and sub-entries)  
**Tier 1 complete:** 26 entries (including tooling frameworks)  
**Tier 2 complete:** 44+ entries (including supplementary, Chinese platforms, government intel context)

