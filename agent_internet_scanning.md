# Internet Scanning & Asset Discovery Database Research

**Last Updated:** 2026-06-23
**Session status:** Research complete — 42 entries documented across Tier 1 and Tier 2.

## Master Index

| # | Name | Type | Status | Geopolitical Flag |
|---|------|------|--------|-------------------|
| 1 | Shodan | Commercial public database | Active | US |
| 2 | Censys | Commercial public database | Active | US |
| 3 | FOFA | Commercial public database | Active | ⚠️ CHINA (PRC intelligence access) |
| 4 | ZoomEye | Commercial public database | Active | ⚠️ CHINA (PRC intelligence access) |
| 5 | GreyNoise | Commercial passive sensor | Active | US |
| 6 | LeakIX | Community/commercial | Active | EU (Belgium) |
| 7 | Netlas.io | Commercial public database | Active | Eastern Europe |
| 8 | IVRE | Open source framework | Active (maintained) | France (CEA/academic) |
| 9 | Onyphe | Commercial public database | Active | France (EU sovereignty) |
| 10 | RiskIQ / Microsoft Defender EASM | Enterprise ASM | Active (Microsoft) | US |
| 11 | Shadowserver Foundation | Nonprofit/government-adjacent | Active | US (Five Eyes aligned) |
| 12 | CAIDA | Academic research | Active | US (NSF/academic) |
| 13 | Rapid7 Project Sonar | Commercial dataset | Active (licensed) | US |
| 14 | Criminal IP | Commercial public database | Active | South Korea |
| 15 | BinaryEdge | Commercial public database | ❌ SHUT DOWN Mar 2025 | Portugal → US (Coalition) |
| 16 | Spyse | Commercial database | ❌ DEFUNCT | Ukraine |
| 17 | Intrigue.io / Mandiant ASM | Enterprise ASM | Active (Google Cloud) | US |
| 18 | Cortex Xpanse (Expanse) | Enterprise ASM | Active (Palo Alto) | US |
| 19 | runZero | Internal+external scanner | Active | US |
| 20 | CyCognito | Enterprise EASM | Active | US/Israel |
| 21 | Hunt.io | Threat infrastructure scanning | Active | US |
| 22 | FullHunt | Enterprise EASM | Active | US |
| 23 | SecurityTrails / Recorded Future ASI | Enterprise (passive DNS + ASM) | Active (Mastercard) | US |
| 24 | Tenable ASM | Enterprise EASM | Active | US |
| 25 | PublicWWW | Source code search engine | Active | Independent |
| 26 | Natlas (Netflix) | Open source framework | ❌ DORMANT | US (Netflix, unmaintained) |
| 27 | UK NCSC Scanning Programme | Government program | Active | UK (GCHQ) |
| 28 | CISA Cyber Hygiene Scanning | Government program | Active | US (DHS/CISA) |
| 29 | Positive Technologies | Enterprise scanner | Active (SANCTIONED) | ⚠️ RUSSIA (US-sanctioned) |
| 30 | BI.ZONE | Enterprise/TI | Active | ⚠️ RUSSIA (Sberbank, sanctioned parent) |
| 31 | 360 Quake (Qihoo 360) | Commercial public database | Active | ⚠️ CHINA (state-linked) |
| 32 | Hunter.how | Commercial public database | Active | ⚠️ CHINA |
| 33 | Cyble ODIN | Enterprise EASM | Active | US/India |
| 34 | scans.io (Stanford ESRG) | Academic archive | Active | US (Stanford) |
| 35 | Stretchoid | Unknown/gray zone | Active | Unknown (DigitalOcean) |
| 36 | Alpha Strike Labs | Enterprise scanner | Active | Germany (EU) |
| 37 | Group-IB | Threat intelligence | Active | UAE (formerly Russia) |
| 38 | CrowdStrike Falcon Surface | Enterprise EASM | Active | US/Israel |
| 39 | Bitsight (Groma) | Security ratings + EASM | Active | US (Moody's) |
| 40 | Driftnet / SecurityScorecard | Commercial scanning engine | Active (acquired May 2026) | UK → US |
| 41 | Hadrian | Enterprise EASM | Active | Netherlands (EU) |
| 42 | NETSCOUT / Cyber Threat Horizon | Passive ISP telemetry + active scan | Active | US |

---

## Objective
Research ALL major companies, organizations, and projects that own and operate internet scanning and asset discovery databases — databases built by continuously scanning the entire internet's IP space to index exposed services, devices, banners, certificates, and configurations.

## Status Key
- [ ] = Not started
- [IN PROGRESS] = Currently researching
- [DONE] = Fully researched and documented

---

## Task List

### Tier 1 — Known Major Operators (verify & expand)
- [DONE] Shodan (John Matherly / Shodan LLC)
- [DONE] Censys
- [DONE] FOFA (Chinese — flag)
- [DONE] ZoomEye (Knownsec, Chinese — flag)
- [DONE] GreyNoise
- [DONE] LeakIX
- [DONE] Netlas.io
- [ ] Onyphe (French)
- [ ] IVRE (open source framework)
- [ ] RiskIQ / Microsoft Defender EASM
- [ ] Shadowserver Foundation
- [ ] CAIDA
- [ ] Rapid7 Project Sonar
- [ ] Criminal IP (Korean — AI Spera)
- [ ] BinaryEdge (check current status — was shut down March 2025)
- [ ] Spyse (acquired by Intruder.io — check current status)
- [ ] Intrigue.io (check current status)
- [ ] Palo Alto Cortex Xpanse (formerly Expanse)
- [ ] Runzero (formerly Rumble Network Discovery)
- [ ] CyCognito

### Tier 2 — Additional targets to discover via search
- [DONE] Search: "internet scanning database" lesser-known operators
- [DONE] Search: state-sponsored / government scanners (UK NCSC, CISA)
- [DONE] Search: academic/research scanning projects (scans.io/Stanford, CAIDA)
- [DONE] Search: Chinese internet scanning platforms beyond FOFA/ZoomEye (360 Quake, Hunter.how)
- [DONE] Search: Russian internet scanning platforms (Positive Technologies, BI.ZONE)
- [DONE] Search: recently emerged operators (2023-2026) (Criminal IP, FullHunt, Cyble ODIN, Hunt.io)
- [DONE] Natlas (Netflix open source)
- [DONE] FullHunt
- [DONE] HunterMap → resolved: Hunt.io is the relevant tool; HunterMap is a game map tool
- [DONE] Tenable Attack Surface Management
- [DONE] Recorded Future Attack Surface Intelligence / SecurityTrails
- [DONE] PublicWWW (source code search engine)
- [DONE] IoT-specific scanning databases (Shodan, Censys, Netlas, Criminal IP all cover IoT; LeakIX covers specific IoT devices)
- [DONE] ICS/SCADA-specific databases (Shodan ICS filters, Shadowserver ICS honeypots, Dragos WorldView, LeakIX ICS protocols, 360 Quake ICS coverage)
- [DONE] CrowdStrike Falcon Surface
- [DONE] Bitsight / Groma
- [DONE] Group-IB
- [DONE] Alpha Strike Labs
- [DONE] Stretchoid (gray zone)
- [DONE] Cyble ODIN
- [DONE] 360 Quake (Chinese)

---

## Findings

*(Updated after every search)*

---

### 1. Shodan
- **Organization:** Shodan LLC (founded by John Matherly, 2009)
- **Website:** https://www.shodan.io / https://enterprise.shodan.io
- **What data:** Open ports, service banners, TLS/SSL certificates, HTTP headers, IoT device fingerprints, ICS/SCADA banners, vulnerabilities, geolocation, ASN data. Screenshots via experimental features.
- **Scan frequency/coverage:** Continuous crawling; entire internet scanned at least once per week. ~1,237 ports covered (compared to Censys which scans all 65,535). New service detection averages ~76 hours.
- **Scale:** Billions of devices indexed; established since 2009 with one of the largest historical archives.
- **Access model:** Free tier (limited); paid plans starting at $69/month; Enterprise plan for bulk data, real-time firehose, on-demand scanning API. 10,000 free API credits/month with no credit card required.
- **Users:** Security researchers, red teamers, defenders, threat intelligence teams, journalists, academics, IoT researchers.
- **Notable:** Pioneer of the internet scanning database category. On-demand scanning allows API users to trigger immediate scans of specific IPs/networks. Shodan Monitor product for continuous monitoring.
- **Controversies:** Frequently cited for enabling mass exploitation by threat actors who use its data to find vulnerable targets. John Matherly has defended it as defensive research infrastructure.

---

### 2. Censys
- **Organization:** Censys Inc. (originated from University of Michigan research, now fully commercial; Ann Arbor, MI)
- **Website:** https://censys.io / https://censys.com
- **What data:** Full port scan data across all 65,535 ports, TLS certificates, banners, HTTP headers, DNS records, WHOIS, CVE enrichment, threat actor fingerprints. IPv4 and IPv6.
- **Scan frequency/coverage:** Near-daily refresh (under 16 hours average). Predictive scanning accounts for >40% of services found. Scans from multiple geographically diverse data centers.
- **Scale:** ~4 billion services indexed. 96% coverage of IPv4 services on top 10 ports; 92% on top 100; 82% across all 65K ports. Claims 92% accuracy for verified, real-time services (vs. competitors at 68%).
- **Access model:** Free community tier; paid tiers for enterprises; ASM (Attack Surface Management) products. Research access available for academics.
- **Users:** Enterprise security teams, researchers, vulnerability management teams, red teamers, government agencies.
- **Notable:** Originated from the ZMap academic project at University of Michigan (Zakir Durumeric et al.). Offers Attack Surface Management platform. Stanford Internet Research Data Repository (scans.io) is a related open dataset archive.
- **Controversies:** Being derived from an academic scanning tool has raised questions about responsible disclosure practices for mass-found vulnerabilities.

---

### 3. FOFA
- **Organization:** Baimaohui (白帽汇, "White Hat Meeting") — Beijing, China. Founded 2015. Also known as Huashun Xinan (华顺信安).
- **Website:** https://en.fofa.info / https://fofa.info
- **What data:** Internet-connected assets globally — open ports, banners, TLS certificates, web application fingerprints, network device fingerprints. 350,000+ fingerprint rules. Products include FOFA (asset retrieval), FOEYE (network asset mapping & risk analysis), FOCII (key information infrastructure mapping).
- **Scan frequency/coverage:** Continuous; global IPv4/IPv6 coverage.
- **Scale:** 4+ billion assets identified via active detection.
- **Access model:** Free tier; paid plans. Chinese and English language support.
- **Users:** Chinese government, security researchers, red teamers, threat intelligence. **GEOPOLITICAL FLAG: Used by Chinese state-affiliated threat actors for pre-attack reconnaissance. Beijing-based operator subject to Chinese national security laws requiring cooperation with intelligence services.**
- **Geopolitical context:** BAIMAOHUI is a Beijing-based company operating under PRC law (National Intelligence Law, Data Security Law), meaning the Chinese state can compel access to all data. FOFA is widely documented in threat intelligence reports as a tool used by PRC-nexus APT groups for targeting. The Internet 2.0 report "Unveiling China's Cyber Scanning Capabilities" specifically calls out FOFA. The platform's fingerprint database and scanning infrastructure constitute significant intelligence-gathering capability.
- **Controversies:** Documented use by threat actors; operates under PRC data laws; significant geopolitical concern for Western organizations whose assets appear in FOFA's index.

---

### 4. ZoomEye
- **Organization:** Knownsec (知道创宇) — 404 Laboratory, Beijing, China. Founded ~2008.
- **Website:** https://www.zoomeye.ai / https://www.zoomeye.org
- **What data:** Global cyberspace assets — open ports, services, device fingerprints, vulnerabilities, geolocation (accurate to building level, <50m error), historical data, vulnerability trends over time. AI-powered search via ZoomEyeGPT (integrates DeepSeek).
- **Scan frequency/coverage:** Continuous, 24/7 scanning of global IPv4 and IPv6 space + domain names; multiple service ports and protocols; ~13 years of historical archive since 2008.
- **Scale:** Large; specific numbers not publicly disclosed but described as China's first and most established cyberspace search engine.
- **Access model:** Free tier; paid plans; API access.
- **Users:** Security researchers, Chinese government, red teamers, threat intelligence. **GEOPOLITICAL FLAG: Knownsec is a Chinese company with documented ties to the Chinese government and military-industrial complex. ZoomEye data is available to Chinese state actors.**
- **Geopolitical context:** Knownsec is deeply embedded in China's cyber ecosystem. ORF India analysis ("KnowSec and China's Information State") documents the company's ties to state information operations. ZoomEyeGPT integration with DeepSeek (another Chinese AI) extends the geopolitical concern. Knownsec 404 Team is a well-known Chinese threat research group. PRC national security laws apply.
- **Controversies:** Same structural geopolitical concerns as FOFA. Documented in Western threat intelligence reports as reconnaissance platform used by PRC-affiliated actors.

---

### 5. GreyNoise
- **Organization:** GreyNoise Intelligence, Inc. — Washington, DC, USA.
- **Website:** https://www.greynoise.io
- **What data:** Passive sensor network data — identifies IPs conducting mass internet scanning and crawling; classifies intent (benign vs. malicious); C2 detection; tracks exploited vulnerabilities in real time; internet-wide exploitation activity. NOT a traditional port-scan database — focuses on characterizing scanner/attacker infrastructure.
- **Scan frequency/coverage:** Real-time passive collection; 5,000+ sensors across 80+ countries; analyzes up to 1 billion sessions per day.
- **Scale:** Tracks 50+ million IPs; 2026 State of the Edge Report based on 4 billion malicious sessions / 2.97 billion sessions over 90 days from 3.8 million unique source IPs.
- **Access model:** Free community lookup; paid plans; enterprise API; integrations with CrowdStrike Falcon platform, SIEMs, SOARs.
- **Users:** SOC teams, SIEM/SOAR integrations, threat intelligence, defenders, incident responders.
- **Notable:** Unique positioning — passive sensor network rather than active scanner. Adds noise classification to alerts. GreyNoise Query Language (GNQL). C2 Detection module launched April 2026. Published 2026 State of the Edge Report with empirical scanning data.
- **Controversies:** None significant; generally regarded positively by the security community as a defensive tool.

---

### 6. LeakIX
- **Organization:** LeakIX — European-based (Belgium LinkedIn presence), open/community-oriented.
- **Website:** https://leakix.net / https://scan.leakix.net
- **What data:** Exposed/misconfigured services — databases (MongoDB, Elasticsearch, Redis, CouchDB, Cassandra, MySQL, PostgreSQL), cloud storage (S3, Azure Blob, GCP), ICS/SCADA (native protocol communication — PLCs, DNP3, BACnet), web applications, AI/vector databases (Qdrant, Weaviate, Milvus, Marqo, Meilisearch, Typesense), security appliances.
- **Scan frequency/coverage:** Continuous IPv4 scanning; 211 detection plugins (142 public, 69 pro). Actually connects and queries targets — not just banner grabbing.
- **Scale:** Full IPv4 coverage; specific record count not publicly stated.
- **Access model:** Free public index; paid Pro tier (more plugins, more detail); API access; open-source scanner components on GitHub.
- **Users:** Security researchers, defenders, red teamers, journalists, incident responders investigating exposed data.
- **Notable:** Specializes in finding actual data leaks — databases with no auth, exposed storage buckets, etc. 2026 infrastructure overhaul underway (new backend, frontend, API, on-demand scanning coming). Expanding ICS protocol coverage.
- **Controversies:** Ethical tension around indexing exposed databases that contain real private data. Platform tries to notify owners of serious exposures.

---

### 7. Netlas.io
- **Organization:** Netlas (privately held, founded circa 2021; Eastern European team)
- **Website:** https://netlas.io
- **What data:** Five major collections: (1) Internet scan results — host/service responses across all IPv4 across major protocols (HTTP, FTP, SMTP, POP3, IMAP, SMB/CIFS, SSH, Telnet, SQL, etc.); (2) DNS records — 2.56 billion domain entries; (3) IP WHOIS — 11.38 million records; (4) Domain WHOIS — 248.77 million records; (5) SSL/TLS certificates — 4.28 billion parsed certificates. Technology fingerprinting with 1,000+ tags. Passive vulnerability detection via CVE/NVD correlation. Geolocation data.
- **Scan frequency/coverage:** Continuous rescanning of all IPv4 addresses; CVE data updated with each new scan cycle. Historical data available for trend analysis.
- **Scale:** ~687 million active internet services indexed; 2.56 billion DNS records; 4.28 billion SSL certificates.
- **Access model:** Free community tier (50 requests/day after registration); paid plans starting at $49/month (Freelancer, Business, Corporate, Enterprise tiers); bulk API/dataset purchases $500–$4,500. Python SDK and CLI available. Browser extensions (Chrome/Firefox).
- **Users:** Penetration testers, bug bounty hunters, OSINT professionals, threat hunters, security researchers, attack surface management teams.
- **Notable:** Advanced query language with logical operators, wildcards, regex, fuzzy and proximity search. On-demand private scanner for non-intrusive recon. Attack surface discovery mapping domains-IPs-services-certificates. Competitive positioning vs. Shodan/Censys with emphasis on SSL certificate depth and DNS coverage.
- **Controversies:** None significant documented.

---

### 8. IVRE (Instrument de veille sur les réseaux extérieurs)
- **Organization:** Open-source project. Created by Pierre Lalet (pierre.lalet@cea.fr) — affiliated with CEA (Commissariat à l'Énergie Atomique et aux Énergies Alternatives), France's Atomic Energy and Alternative Energies Commission. Active maintainer is GitHub user p-l-.
- **Website:** https://ivre.rocks / https://github.com/ivre/ivre
- **What data:** Self-hosted framework that aggregates and indexes output from: Nmap, Masscan, ZGrab2, ZDNS, Nuclei, httpx, dnsx, tlsx, Dismap (active recon); Zeek/Bro, Argus, Nfdump, p0f, airodump-ng (passive recon). Captures: open ports, service banners, version fingerprints, OS fingerprints, TLS certificates, DNS records, HTTP headers, network flows, traceroute data, script outputs. Full schema normalization.
- **Scan frequency/coverage:** Self-determined — users run their own scans at chosen frequency. Designed for both internet-wide scanning and internal network recon.
- **Scale:** User-determined; framework supports MongoDB backend for large-scale storage. No centralized hosted database.
- **Access model:** Fully open source (GPL); self-hosted. Web interface + CLI tools + Python API. MCP (Model Context Protocol) server for LLM agent integration (new in 2025). GitHub: 4.1k stars, 694 forks; latest release v0.9.21 (September 2024).
- **Users:** Security teams building private Shodan/Censys alternatives, EASM tool builders, red teamers, network recon researchers, academic researchers. Organizations wanting no third-party data exposure.
- **Notable:** Full name in French: "Instrument de veille sur les réseaux extérieurs." Also backronymed DRUNK ("Dynamic Recon of UNKnown networks"). Key differentiator: entirely self-hosted — no data shared with third parties. Custom metadata annotation for EASM use cases. 2025 addition: MCP server lets LLM agents query the database in natural language.
- **Geopolitical context:** CEA affiliation is notable — CEA is a French state research agency involved in nuclear, defense, and security research. IVRE's origins in a French state research institution and its sophisticated network recon capability suggests potential dual-use awareness.
- **Controversies:** None; open source and well-regarded in the French and global security community.

---

### 9. Onyphe
- **Organization:** ONYPHE SAS — Paris, France. Founded 2017 by Patrice Auffret (aka GomoR), who serves as Founder, CEO, and CTO. Previously worked at La Poste Groupe, Secure-Side, Technicolor; prominent French security researcher and SSTIC presenter.
- **Website:** https://www.onyphe.io / https://blog.onyphe.io
- **What data:** Internet-wide scanning (IPv4 + IPv6), passive DNS, dark web monitoring, threat intelligence feeds, WHOIS. 2,100+ ports scanned. Specific data: open ports/banners, TLS certificates, HTTP headers, protocol identification (RDP/VNC/VPN regardless of port), botnet C2 lists, malware server IPs, brute-force sources, Tor exit nodes. CISA KEV integration for vulnerability correlation.
- **Scan frequency/coverage:** Continuous; 20+ billion banners collected monthly; 5+ billion DNS entries monthly. 7 months of scan history; 48 months of historical DNS data. Domain-centric approach (assets bound to domain names, not just IPs).
- **Scale:** 20+ billion banners/month; 5+ billion DNS entries/month; 2,100+ ports scanned.
- **Access model:** Freemium (1 query/min, limited data); Eagle plan ~$10/month; Whale plan ~$50/month; Enterprise pricing by contact. SIEM-like key/value query interface for building custom asset inventories.
- **Users:** Cyber defenders, security analysts, French critical infrastructure operators. Notable French customers: La Poste Groupe, Crédit Mutuel ARKEA, EDF, Crédit Agricole, CERT Santé, France Cyber Maritime. Government and CERT-adjacent usage.
- **Notable:** Data stored entirely in the EU — a deliberate compliance/sovereignty choice attractive to European organizations. Combines internet scanning + passive DNS + threat feeds + WHOIS in a single query interface. Provides real-time monitoring/alerting for exposed assets. French cybersecurity ecosystem's primary answer to Shodan.
- **Geopolitical context:** French sovereignty positioning; EU data residency; ANSSI/CERT-FR adjacent (major French customers include CERT Santé and France Cyber Maritime). Not directly a state tool but embedded in French critical infrastructure security.
- **Controversies:** None significant documented.

---

### 10. RiskIQ / Microsoft Defender EASM
- **Organization:** Originally RiskIQ Inc. (San Francisco, CA; founded 2009). Acquired by Microsoft for ~$500 million in July 2021. Now operates as Microsoft Defender External Attack Surface Management (EASM), part of Azure/Microsoft Security.
- **Website:** https://www.microsoft.com/en-us/security/business/cloud-security/microsoft-defender-external-attack-surface-management / https://learn.microsoft.com/en-us/azure/external-attack-surface-management/
- **What data:** Internet-wide continuous discovery of internet-facing assets — IPs, domains, web properties, SSL certificates, open ports, service banners, web app components, cloud resources, unmanaged/shadow IT assets. Historical data for trend analysis. PassiveTotal product provided passive DNS, WHOIS, malware infrastructure mapping, and threat actor tracking (crowd-sourced from security research community + ML analysis). Defender EASM: daily scanning builds full catalogue of customer-facing external assets including previously unknown/agentless assets.
- **Scan frequency/coverage:** Daily scanning of the internet; continuous discovery. Global IPv4/IPv6 coverage.
- **Scale:** RiskIQ had 10+ years of internet scanning data pre-acquisition. Scale not publicly disclosed post-Microsoft acquisition.
- **Access model:** Azure subscription-based; priced per billable asset per day. 30-day free trial. Integrated into Microsoft Defender for Cloud. Defender EASM is an Azure resource billed through Azure.
- **Users:** Enterprise security teams, SOCs, vulnerability management programs, large organizations managing complex external attack surfaces. Tight integration with Microsoft 365 Defender and Azure ecosystems.
- **Notable:** RiskIQ PassiveTotal was widely used by threat intelligence analysts for tracking malicious infrastructure (C2 servers, phishing domains, APT infrastructure). Microsoft Defender Threat Intelligence (MDTI) is the successor TI product, providing RiskIQ-sourced data to Defender XDR customers. The acquisition gave Microsoft one of the largest historical internet scan datasets.
- **Controversies:** None significant post-acquisition. Pre-acquisition, RiskIQ data was commercially licensed and used extensively by APT tracking teams globally.

---

### 11. Shadowserver Foundation
- **Organization:** The Shadowserver Foundation — nonprofit organization (US-based). Founded circa 2004 by volunteer security researchers; now operates as a major global cyber defense nonprofit.
- **Website:** https://www.shadowserver.org
- **What data:** Multi-source threat intelligence combining: (1) Active scanning — 90+ distinct data sets produced daily, 3.7 billion IPv4 addresses scanned daily across 140+ ports, 1+ billion IPv6 addresses (hitlist-based). Service banners, software versions, TLS certificate data, protocol details, vulnerability indicators, RDP NLA status, certificate fingerprints. (2) Sinkhole operations — hundreds of malware families simultaneously; captures botnet drone data (IP, ASN, country, C2 domain, bot ID, malware family). (3) Honeypot network — global sensors covering ICS/OT protocols (Modbus, DNP3, BACnet, Siemens S7), IoT device compromise detection, darknet telescope. (4) Malware sample analysis.
- **Scan frequency/coverage:** 100+ scan types per day; full IPv4 daily; IPv6 hitlist-based daily.
- **Scale:** 3.7 billion IPv4 addresses daily; 90+ datasets; 1+ billion IPv6 addresses; hundreds of sinkholes; reports to 9,000+ network operators in 170+ countries.
- **Access model:** Free to vetted recipients — national CSIRTs, network operators, governments. Reports delivered via email or SFTP in CSV/JSON. Not publicly searchable like Shodan. API access for vetted partners.
- **Users:** 9,000+ vetted network operators globally; national CERTs/CSIRTs in 170+ countries; law enforcement; government agencies. Reports tailored to each network owner's own IP space.
- **Notable:** Unique model — gives away data for free to defenders; does not sell access commercially. Named participant in major botnet takedowns: Operation Duck Hunt (QakBot, FBI 2023), Operation Dying Ember (Moobot/APT28), Operation PhishOFF (LabHost), VPNFilter sinkhole (2018), Cyclops Blink (2022). One of the most trusted non-commercial cyber defense infrastructure providers globally.
- **Funding:** UK NCSC, Dutch NCSC, German BSI, Japanese Cybersecurity Strategy Office (government funders); Mastercard, Akamai, Trend Micro, Avast, Craig Newmark Philanthropies (private funders); Internet Society Foundation Common Good Cyber Fund (2025-2026).
- **Controversies:** None. Widely regarded as one of the most important and neutral global cybersecurity nonprofits.

---

### 12. CAIDA (Center for Applied Internet Data Analysis)
- **Organization:** CAIDA — UC San Diego / San Diego Supercomputer Center (SDSC). Academic/research nonprofit. Founded 1997. Primary funder: NSF (National Science Foundation); also DHS, DARPA, private sector.
- **Website:** https://www.caida.org
- **What data:** Multiple distinct datasets: (1) UCSD Network Telescope — "Internet Background Radiation" (IBR) monitor of 1/256th of all IPv4 address space; captures unsolicited traffic from scanning, worm propagation, DDoS backscatter, botnet activity. 3+ TB/day of uncompressed traces; historical data from 2003+. (2) Archipelago (Ark) — globally distributed active measurement platform (Raspberry Pi + 1U servers); continuous traceroute to every routed /24 prefix; IPv4 topology, path data, BGP mapping. (3) RouteViews/BGP data — BGP routing tables, AS-level topology. (4) Aggregated RSDoS (Reflected DDoS) attack metadata. (5) UCSD Network Telescope Aggregated Flow Dataset (ongoing since 2003).
- **Scan frequency/coverage:** Network Telescope: continuous passive; Ark: continuous active traceroutes of entire routed IPv4 space; BGP: live feeds.
- **Scale:** Telescope: monitors 1/256 of IPv4 (~16.7 million IPs), 3+ TB uncompressed data/day; Ark: traces to every routed /24 globally; historical archives from 2003.
- **Access model:** Restricted — requires application/request and agreement to data use policy. Most datasets available to vetted academic researchers. Not public/commercial. Historical telescope data from 2008+ available on request.
- **Users:** Academic researchers, network scientists, government agencies (NSF, DHS, DARPA), internet topology researchers, cybersecurity researchers.
- **Notable:** ROOTBEER project (2025, NSF-funded) — collaboration with Internet2 for routing security research. Ark platform used by 70+ published papers. Data feeds BGP/routing research globally. One of the world's most important passive internet measurement archives.
- **Controversies:** None; purely academic mission. Dataset access controls intended to prevent misuse.

---

### 13. Rapid7 Project Sonar
- **Organization:** Rapid7 Inc. (NASDAQ: RPD) — Boston, MA. Commercial cybersecurity company (vulnerability management, SIEM, MDR).
- **Website:** https://www.rapid7.com/research/project-sonar / https://sonardata.rapid7.com
- **What data:** Internet-wide scan datasets across entire public IPv4 space (4.3 billion addresses). 8 dataset categories (57 TB total, 45,617+ files as of mid-2026): (1) SSL/TLS certificates and X.509 metadata; (2) HTTP/HTTPS responses and content; (3) DNS — ANY, A, AAAA, TXT, MX, CNAME, PTR responses; (4) TCP service scans — SSH, SMB, RDP, MongoDB, Redis, NetBIOS, NTP, SNMP; (5) UDP scan results; (6) SMTP/IMAP/POP3 STARTTLS responses; (7) DNS IPv4 PTR responses. 70+ different services and protocols surveyed.
- **Scan frequency/coverage:** Varies by dataset — HTTP scanned approximately monthly; other services less frequently. No guaranteed SLA. Full IPv4 coverage.
- **Scale:** 57 TB total data; 45,617 files; 8 active dataset types; scanning since ~2013. Historical datasets archived.
- **Access model:** Formerly fully public (open data); now requires commercial licensing agreement. Submit use case, datasets needed, utilization plan. Pricing case-by-case. Individual researcher sponsorship available on request. Contact opendata@rapid7.com. Not publicly queryable via web UI like Shodan — raw data downloads only.
- **Users:** Academic security researchers, threat intelligence teams, vulnerability researchers, government security agencies, enterprise security teams.
- **Notable:** One of the most comprehensive raw internet scan open datasets ever released. Previously hosted at opendata.rapid7.com. Integrated with Rapid7's InsightVM and Nexpose products for customer attack surface context. Sonar data feeds Rapid7's vulnerability intelligence.
- **Controversies:** Shift from fully open to licensed access disappointed the open research community. Data has been used by researchers to track vulnerability exposure at internet scale (e.g., Heartbleed, Log4Shell prevalence studies).

---

### 14. Criminal IP (by AI Spera)
- **Organization:** AI Spera Inc. — Seoul, South Korea. Founded 2017 as a spin-off from Korea University's hacking and countermeasure research center. CEO: Byung-Tak Kang. Series B funded (~$8.5M / 12B KRW in 2024; total cumulative ~$16M / 23B KRW). Investors: KB Investment, JB Investment, Kyobo Life Insurance, Smilegate Investment.
- **Website:** https://www.criminalip.io / https://search.criminalip.io
- **What data:** Full IPv4 scan data with AI-powered threat scoring. Data: open ports, service banners, TLS/SSL certificates, HTTP headers, WHOIS, screenshots, passive DNS history, CVE/vulnerability mapping, malware associations, IP risk scoring (5-level risk scale), scanner/bot identification, geolocation. Exploit Search: maps exploitable vulnerabilities by CVE ID in real-time.
- **Scan frequency/coverage:** Full 4.29 billion global public IPv4 addresses scanned approximately every 3 days; continuous updates to web service. Ports scanned daily.
- **Scale:** 4.29 billion IPs covered; continuous scanning.
- **Access model:** Free tier (limited); paid plans with tiered pricing; full-featured API (copy API key after registration). ASM product (Criminal IP ASM) for enterprise continuous external attack surface monitoring. FDS product (Fraud Detection System) for real-time traffic analysis.
- **Users:** Security analysts, threat intelligence teams, SOCs, enterprise attack surface management, fraud detection teams. 40+ technology partnerships including Cisco, Tenable, VirusTotal, Hybrid Analysis, Sumo Logic, Quad9.
- **Notable:** AI-native design from inception — threat scoring uses ML. STIX 2.1 formatted data available on GitHub for threat information sharing. VirusTotal contributor (IP/URL scanning). IPO planned within 2-3 years per company roadmap. KISA (Korea Internet & Security Agency) R&D partner.
- **Geopolitical context:** South Korean company; Korea University origin; KISA partnership. South Korea is a US-allied nation. No significant geopolitical concerns analogous to Chinese platforms. Aggressive global expansion into North America and Europe.
- **Controversies:** None significant.

---

### 15. BinaryEdge [SHUT DOWN March 31, 2025]
- **Organization:** BinaryEdge (Lisbon, Portugal; founded ~2015). Acquired by Coalition Inc. (cyber insurance, San Francisco) in January 2020. Platform permanently shut down March 31, 2025.
- **Website:** https://www.binaryedge.io (defunct as of April 2025)
- **Status:** ALL accounts (free and paid) terminated March 31, 2025 at 11:59 PM GMT. Standalone platform discontinued.
- **What data was:** Internet-wide scanning database — open ports, service banners, TLS certificates, vulnerability data, CVE mapping, ASN/WHOIS. Focused on attack surface visibility and cyber risk scoring.
- **What happened:** Coalition acquired BinaryEdge in 2020 and integrated the scanning technology into Coalition Control (Coalition's cyber risk management product). The standalone BinaryEdge product became redundant to Coalition's core product. Coalition Control (coalitioninc.com/control) is the recommended alternative for former BinaryEdge customers.
- **Legacy:** BinaryEdge data powered Coalition's cyber insurance underwriting — one of the first major examples of internet scan data being embedded into insurance risk models.
- **Controversies:** None beyond the disappointment of discontinuing a community-used platform.

---

### 16. Spyse [STATUS: Defunct — connection refused as of 2025]
- **Organization:** Spyse (Ukraine-based team; founded ~2019). Crunchbase lists as "permanently closed."
- **Website:** https://spyse.com (domain currently returns ECONNREFUSED — offline)
- **Status:** Appears defunct. Crunchbase marks as permanently closed. Site does not respond. Note: The "acquired by Intruder.io" claim in research instructions could not be independently confirmed — no press releases or news coverage found for this acquisition. The Intruder.io product (intruder.io) is a separate UK-based vulnerability scanner with no evident relationship to Spyse.
- **What data was:** Cybersecurity asset search engine ("Internet Assets Registry"). Data: domains, IPs, SSL/TLS certificates, WHOIS, open ports, service banners, ASN data, DNS records. Marketed to pentesters and bug bounty hunters.
- **Legacy:** Was a popular Shodan/Censys alternative particularly among bug bounty community. Had free and paid API access. Its offline status leaves a gap in the Eastern European cybersecurity tool ecosystem.
- **Controversies:** None documented. Circumstances of shutdown unclear.

---

### 17. Intrigue.io / Mandiant Attack Surface Management / Google Cloud ASM
- **Organization:** Intrigue Corporation (Austin, TX; founded 2019 by Jonathan Cran, formerly of Rapid7, Bugcrowd, Kenna Security). Acquired by Mandiant for undisclosed amount, August 10, 2021. Mandiant then acquired by Google for $5.4 billion, closing September 12, 2022. Now operates as Mandiant Attack Surface Management under Google Cloud Security.
- **Website:** https://cloud.google.com/security/products/attack-surface-management (original https://intrigue.io defunct)
- **Status:** Active — rebranded as Mandiant ASM, sold as Google Cloud Security product.
- **What data:** Internet-wide asset discovery — domains, IPs, web properties, cloud assets, open ports, services, TLS certificates, web application fingerprints. Discovers unknown/unmanaged internet-facing assets. Continual monitoring for exploitable exposures. Graph database relationships between assets.
- **Scan frequency/coverage:** Continuous monitoring of external attack surface.
- **Scale:** Not publicly disclosed. Backed by Google's global infrastructure.
- **Access model:** Enterprise cloud product (Google Cloud subscription). Not publicly searchable.
- **Users:** Large enterprises managing complex external attack surfaces. Google Cloud customers.
- **Notable:** Intrigue Core (open-source version) remains available on GitHub. Full acquisition chain: Intrigue → Mandiant → Google. One of the few internet scanning databases now fully integrated into a hyperscaler cloud platform.
- **Controversies:** None significant.

---

### 18. Palo Alto Networks Cortex Xpanse (formerly Expanse)
- **Organization:** Originally Expanse Inc. (San Francisco; founded 2012 by Tim Junio and Matt Kraning). Acquired by Palo Alto Networks for ~$800M–$1.25B in November 2020 (closed January 2021). Now: Cortex Xpanse, part of Palo Alto Networks' Cortex platform (NASDAQ: PANW).
- **Website:** https://www.paloaltonetworks.com/cortex/cortex-xpanse
- **What data:** Internet-wide continuous scanning — all IPv4 addresses scanned multiple times daily. 500+ billion ports scanned daily. Data: open ports and services, TLS certificates, web application components, cloud asset discovery, shadow IT detection, misconfigurations (exposed RDP, OpenSSH, unpatched services), vulnerability mapping (CVE correlation), geolocation, ASN/WHOIS. Machine-learning powered asset attribution back to specific organizations.
- **Scan frequency/coverage:** Full IPv4 scanned multiple times daily; 500+ billion port scans/day. Continuous.
- **Scale:** Internet-scale; 500B+ port scans/day. One of the largest active scanning operations commercially.
- **Access model:** Enterprise product — requires Palo Alto Networks subscription/licensing. Not publicly searchable. Integrates with Cortex XSOAR for automated remediation playbooks.
- **Users:** Large enterprises, government agencies, MSSPs using Palo Alto Networks' Cortex platform. Competes with Microsoft Defender EASM, CyCognito, Tenable ASM.
- **Notable:** Expanse's founding innovation was attributing internet-wide scan results back to specific organizations — a breakthrough for enterprise attack surface management. Cortex Xpanse Active ASM includes automated response (e.g., automatically disabling exposed RDP without manual intervention). Used by US Department of Defense and major financial institutions pre-acquisition.
- **Controversies:** $800M+ acquisition price raised analyst eyebrows at the time. No significant ongoing controversies.

---

### 19. runZero (formerly Rumble Network Discovery)
- **Organization:** runZero Inc. (Austin, TX; formerly Rumble Network Discovery). Founded by HD Moore (creator of Metasploit Framework) and Chris Kirsch. Rebranded from Rumble to runZero in August 2022. Venture-backed; 30,000+ users.
- **Website:** https://www.runzero.com
- **What data:** Internal and external network asset inventory — IT, OT, IoT, cloud, mobile, and remote assets. Proprietary unauthenticated active scanner with high-fidelity fingerprinting. Data: discovered devices (managed and unmanaged), open ports, service banners, operating system fingerprinting, vulnerability data, cloud asset discovery (API-based), passive traffic analysis. NOT primarily an internet-wide public scan database — focus is on scanning customer-owned networks.
- **Scan frequency/coverage:** On-demand or scheduled scanning of defined network scopes. External attack surface scanning also supported. Not a persistent internet-wide index like Shodan.
- **Scale:** Covers IT, OT, IoT, cloud, mobile, remote assets. Customer-defined scope. 30,000+ users globally.
- **Access model:** Community Edition (free, ≤100 assets); paid Platform plans $10,000–$60,000/year by asset count; 21-day free trial. Enterprise pricing by asset volume.
- **Users:** Enterprise security teams, IT/OT security engineers, attack surface management teams. Particularly strong in OT/ICS visibility where passive-only tools miss devices.
- **Notable:** HD Moore's involvement makes this especially significant — he created the dominant open-source exploit framework and brings deep network scanning expertise. Rated #1 on Gartner Peer Insights for CAASM. NPS score of 82. Key differentiator: finds devices that passive tools miss, including legacy OT/ICS equipment. Integrates with major security platforms.
- **Controversies:** None. HD Moore has previously been controversial in the security community (Metasploit dual-use debate) but runZero itself is uncontroversial.

---

### 20. CyCognito
- **Organization:** CyCognito Inc. (Palo Alto, CA + Tel Aviv, Israel; founded 2017 by Dima Potekhin and Rob Gurzeev). Israeli-American cybersecurity company. Rob Gurzeev is a former Unit 8200 (Israeli military cyber intelligence) veteran who was the youngest CTO of the product department within Unit 8200. Total funding: $153M (Seed → Series A $23M → Series B $30M led by Accel → Series C $100M led by The Westly Group, 2021). Investors: Lightspeed, Accel, UpWest, Sorenson Capital.
- **Website:** https://www.cycognito.com
- **What data:** Internet-wide external attack surface scanning. Discovers and maps assets linked to an organization by scanning the global internet — domains, subdomains, IPs, cloud assets, APIs, subsidiaries, third-party infrastructure, development/test environments, shadow IT. AI-driven asset attribution. Data: open ports, services, TLS certificates, vulnerabilities, misconfigurations, leaked credentials, risky SaaS usage, web application fingerprints. Continuous exposure enrichment.
- **Scan frequency/coverage:** Continuous (daily/weekly/bi-weekly/monthly options). Global internet scanning.
- **Scale:** Positioned as "the only EASM solution capable of scaling to the needs of the world's largest global organizations." Specific scale metrics not publicly disclosed. Leader/Outperformer in 2026 GigaOm Radar for ASM (out of 32 vendors).
- **Access model:** Enterprise SaaS product — not publicly searchable. Pricing by engagement. Competes with Cortex Xpanse, Microsoft Defender EASM, Tenable ASM.
- **Users:** Large global enterprises, multinational corporations with complex subsidiary structures, financial institutions. Targets organizations that struggle with unknown/forgotten assets.
- **Notable:** "Attacker's perspective" framing — maps attack surface the way a threat actor would, without relying on internal asset inventories. AI-driven business entity correlation. Strong for discovering assets across subsidiaries and M&A-acquired companies.
- **Geopolitical context:** Unit 8200 alumni in founding team — this elite Israeli signals intelligence unit has produced numerous cybersecurity companies (Check Point, Palo Alto Networks founders, NSO Group, etc.). Israel-US dual presence. No state-control concerns given Israel's close security partnership with the US.
- **Controversies:** None significant. Unit 8200 background is noteworthy but not controversial in the Western security industry context.

---

## Tier 2 — Additional Operators

### 21. Hunt.io
- **Organization:** Hunt.io (formerly HuntSynergy; US-based). Privately held threat intelligence company focused on malicious infrastructure hunting.
- **Website:** https://hunt.io
- **What data:** Internet-wide scanning focused on threat actor infrastructure — C2 servers, exploit servers, phishing infrastructure, red team tools, team servers. Scale: 15 billion HTTPS scans (encrypted service behavior); 96 billion protocol scans (custom/malicious/non-standard services); 150 billion certificate grabs indexed; 6 billion SSH banner/key grabs; 1.2 trillion rows of open port history (~500 TB compressed, ~3 PB uncompressed). URLx database: 10.6 billion URLs for infrastructure hunting. Machine-readable IOCs auto-extracted from threat research. AttackCapture™ feature.
- **Scan frequency/coverage:** Continuous internet-wide scanning. Real-time C2 and malicious infrastructure tracking.
- **Scale:** 1.2 trillion rows port history; ~500 TB compressed data; 150B certificates indexed.
- **Access model:** Commercial platform; OEM API for embedding intelligence in other security products. C2 Feed, Threat Intelligence Feeds, IOC Hunter Feed.
- **Users:** Threat hunters, SOC teams, red/blue teams, threat intelligence teams, security platform builders (OEM).
- **Notable:** Distinguished from Shodan/Censys by focus on adversary infrastructure rather than general internet mapping. First-party validation of C2 activity. 2025 platform version "Hunt 2.1–2.8" series added major workflow improvements. Strong competitor positioning as "Censys Alternative for OEM Threat Intelligence."
- **Controversies:** None documented.

---

### 22. FullHunt
- **Organization:** FullHunt (San Francisco, CA; founded ~2021). Venture-backed EASM startup.
- **Website:** https://fullhunt.io
- **What data:** External attack surface — domains, subdomains, IPs, cloud assets (AWS, Azure, GCP, Alibaba, Oracle Cloud), APIs, tech stack fingerprinting. Vulnerability detection with zero false positives (runtime validation). Dark web monitoring (via OEM Intelligence API, May 2025). Vulnerability Intelligence module (September 2025): aggregates CVE data, exploit PoCs, research papers.
- **Scan frequency/coverage:** Continuous (24/7 monitoring). Changes, new assets, configuration drift detected in real-time.
- **Scale:** Internet-scale; specific counts not publicly disclosed.
- **Access model:** Enterprise SaaS. OEM Intelligence API (launched May 2025) for embedding attack surface + dark web intelligence into third-party security platforms. Free trial available.
- **Users:** Enterprise security teams, MSSPs, security platform builders via OEM API.
- **Notable:** Multi-cloud visibility without credentials required. Exploit-aware vulnerability prioritization (claims 70%+ reduction in patch queues). OEM API launched May 2025 — positions FullHunt as intelligence infrastructure provider. Listed in Gartner Peer Insights.
- **Controversies:** None documented.

---

### 23. SecurityTrails / Recorded Future Attack Surface Intelligence (now Mastercard)
- **Organization:** SecurityTrails (originally independent; acquired by Recorded Future for $65 million, January 2022). Recorded Future acquired by Mastercard for $2.65 billion (closed December 2024). SecurityTrails technology now part of Mastercard's cybersecurity portfolio via Recorded Future.
- **Website:** https://www.recordedfuture.com/products/attack-surface-intelligence (SecurityTrails standalone site remains but functionality integrated)
- **What data:** 10+ years of current and historical DNS, WHOIS, SSL/TLS certificate data. Passive DNS history for pivoting between domains and IPs. Attack surface intelligence: discovers unknown/forgotten assets including shadow IT, cloud sprawl, acquired infrastructure. Integrated with Recorded Future Intelligence Graph for threat actor context — cross-references CVE exploitation, dark web exposure, active threat actor targeting.
- **Scan frequency/coverage:** Continuous discovery and monitoring. Historical archive extending 10+ years.
- **Scale:** One of the largest passive DNS historical archives. Specific record counts not publicly disclosed.
- **Access model:** Enterprise product. Free tier significantly restricted post-acquisition. ServiceNow ITSM integration (Version 2, 2025). Cortex XSOAR integration.
- **Users:** Enterprise security teams, threat intelligence analysts, SOCs, financial sector (now Mastercard subsidiary — fraud and financial crime intelligence potential).
- **Notable:** Acquisition chain: SecurityTrails → Recorded Future → Mastercard. Mastercard's $2.65B acquisition of Recorded Future was one of the largest cybersecurity acquisitions ever. Open security community expressed concern about free tier restrictions post-acquisition. Historical DNS is SecurityTrails' core differentiator — invaluable for tracking infrastructure changes over years.
- **Controversies:** Free tier restrictions post-acquisition disappointed OSINT community. Mastercard ownership raises questions about use of threat intelligence in financial fraud detection (positive) and potential for combining scan data with financial transaction data (novel concern).

---

### 24. Tenable Attack Surface Management (formerly Bit Discovery)
- **Organization:** Tenable Inc. (NASDAQ: TENB; Columbia, MD). Tenable ASM originated from acquisition of Bit Discovery (founded by Jason Haddix). Now part of Tenable One exposure management platform.
- **Website:** https://www.tenable.com/products/attack-surface-management
- **What data:** 5+ billion internet-facing assets indexed. Discovers unknown/unmanaged assets including shadow IT, cloud assets. 120+ columns of data per asset. Supports IPv4 and IPv6. TCP port scanning (not UDP). Data: open ports, web application components, TLS certificates, technology fingerprints, CVE/vulnerability mapping, cloud resource discovery.
- **Scan frequency/coverage:** Continuous internet-wide scanning. Daily asset discovery.
- **Scale:** 5+ billion assets in database. One of the largest EASM asset indexes.
- **Access model:** Part of Tenable One subscription (enterprise). Also available as standalone Tenable ASM. Not publicly searchable.
- **Users:** Enterprise vulnerability management teams, CISOs, large organizations. Integrates with Tenable Nessus/Tenable.io for combined internal+external visibility.
- **Notable:** Largest disclosed asset database size (5B+) among commercial EASM products. Passive reconnaissance approach — does not require agents or network access. Tight integration with Tenable's vulnerability management ecosystem is a key differentiator.
- **Controversies:** None significant.

---

### 25. PublicWWW
- **Organization:** PublicWWW (independent; founder not publicly disclosed).
- **Website:** https://publicwww.com
- **What data:** Source code search engine — indexes HTML, JavaScript, CSS, and HTTP headers of publicly accessible web pages. 469+ million web pages indexed. Searchable by code snippets, analytics codes, tracking IDs, embedded widgets, themes, API keys, JavaScript libraries. Respects robots.txt. Supports regex searches, domain filters.
- **Scan frequency/coverage:** Periodic re-crawling of indexed pages. Frequency not publicly disclosed.
- **Scale:** 469+ million web pages.
- **Access model:** Free searches (limited); paid plans for bulk/API access; CSV downloads; alert subscriptions for query matches; sorted by site popularity.
- **Users:** Security researchers (finding exposed API keys/secrets in public code), OSINT investigators, SEO professionals, SaaS founders, bug bounty hunters, brand monitoring teams.
- **Notable:** Distinct niche — searches *within* page source code, not traditional port scanning. Valuable for finding exposed secrets, tracking technology spread (e.g., "who uses this analytics tag?"), identifying related infrastructure via shared code. Featured in Bellingcat's investigative toolkit.
- **Controversies:** None significant; use for finding exposed API keys/credentials in public HTML is dual-use.

---

### 26. Natlas (Netflix, now dormant)
- **Organization:** Originally developed at Netflix by internal security team. Open-source project. Now dormant/unmaintained.
- **Website:** https://github.com/natlas/natlas (GitHub)
- **What data:** Self-hosted internet scanning platform. Components: natlas-server (data storage + web search UI) + natlas-agent (distributed scan workers using Nmap). Designed for scaling network scanning across distributed agents. Screenshots of web services, Nmap scan data, service banners.
- **Status:** Dormant. Last significant activity ~2020-2021. Netflix has not actively maintained the project. Most recent GitHub activity sparse.
- **Access model:** Open source; self-hosted only. No central database.
- **Users:** Security teams that want a self-hosted distributed scanning framework.
- **Notable:** Netflix released this as part of its security infrastructure open-source contributions. Designed for massive scale through distributed agent architecture — any number of agents can be added. Web UI for searching and visualizing scan results. Influenced subsequent open-source scanning frameworks.
- **Controversies:** None.

---

### 27. UK NCSC Internet Scanning Programme (Government)
- **Organization:** UK National Cyber Security Centre (NCSC) — part of GCHQ (UK signals intelligence agency). Government program.
- **Website:** https://www.ncsc.gov.uk/collection/vulnerability-management/scanning-services
- **Scanner source:** scanner.scanning.service.ncsc.gov.uk (IPs: 18.171.7.246, 35.177.10.231 — hosted on AWS UK infrastructure)
- **What data:** Scans all internet-accessible devices hosted in the UK. Data collected: full HTTP responses (including headers), service banners, software versions, TLS certificate data, timestamps, source/destination IPs. Designed to identify vulnerable software versions and known exploitable vulnerabilities. Minimally invasive — collects only data returned by the scanned service.
- **Scan frequency/coverage:** Continuous; covers all internet-exposed systems hosted in UK IP space.
- **Scale:** All UK-hosted internet-facing devices.
- **Access model:** Government-operated; data not publicly accessible. Used internally by NCSC to generate risk assessments and notify owners of vulnerable systems.
- **Users:** NCSC internal use; findings shared with system owners. Not a searchable commercial database.
- **Notable:** Launched 2022. Part of NCSC's "Active Cyber Defence" programme. Opt-out available — organizations can email scanning@ncsc.gov.uk to exclude their IPs. Privacy-by-design — personal data inadvertently captured is deleted. GCHQ connection means this is effectively a state intelligence agency conducting national internet mapping (for defense, not offense).
- **Geopolitical context:** The UK government (GCHQ/NCSC) now formally scans its own national internet space. This is a significant policy development — a Five Eyes nation openly conducting state-level internet scanning of its own territory for cyber defense purposes. Sets precedent for similar programs in allied nations.
- **Controversies:** Initial announcement caused concern about government surveillance of internet devices. NCSC emphasized defensive intent and opt-out mechanism. No known abuse documented.

---

### 28. CISA Cyber Hygiene Vulnerability Scanning (US Government)
- **Organization:** CISA (Cybersecurity and Infrastructure Security Agency) — US Department of Homeland Security. Federal government program.
- **Website:** https://www.cisa.gov/cyber-hygiene-services
- **What data:** Scans internet-accessible public static IPv4 addresses of enrolled organizations. Web Application Scanning for publicly accessible web apps. Checks for: known exploited vulnerabilities, software versions, risky/exposed services, OWASP Top 10 web vulnerabilities, misconfigurations.
- **Scan frequency/coverage:** Weekly vulnerability scanning; monthly web application scanning reports; ad-hoc alerts for urgent findings.
- **Scale:** 7,600+ enrolled organizations; 3M+ known vulnerabilities identified since 2022 program expansion.
- **Access model:** Free to eligible US entities — federal, state, local, tribal, territorial governments; private sector critical infrastructure. Opt-in (organizations must enroll).
- **Users:** US government agencies, state/local governments, critical infrastructure operators (energy, water, healthcare, finance, etc.).
- **Notable:** Different from NCSC UK program — entirely voluntary/opt-in rather than scanning all UK space. Reports sent to enrolled organizations weekly. Not a searchable public database. CISA uses findings for national risk posture assessment.
- **Controversies:** None significant. Complementary to Shadowserver data CISA uses.

---

### 29. Positive Technologies (Russian — GEOPOLITICAL FLAG)
- **Organization:** Positive Technologies (Москва/Moscow, Russia; founded 2002). Listed on Moscow Stock Exchange (MOEX: POSI). Sanctioned by US Treasury (April 2021) for supporting FSB (Federal Security Service) operations.
- **Website:** https://www.ptsecurity.com / https://global.ptsecurity.com
- **What data:** Primarily vulnerability management and enterprise scanning — MaxPatrol VM (vulnerability management), MaxPatrol SIEM (security information/event management), PT NAD (network traffic analysis). MaxPatrol actively scans and inventories IT infrastructure. Internet-wide scanning capability not publicly documented in the same manner as Shodan/Censys, but Positive Technologies conducts extensive internet-wide research and has knowledge of global infrastructure.
- **Scan frequency/coverage:** Enterprise product — scans customer-defined networks. Their research team conducts internet-wide studies for publications.
- **Scale:** Products deployed across Russian critical infrastructure, government, and major enterprises. 300+ system types supported in MaxPatrol.
- **Access model:** Commercial enterprise product. MaxPatrol licensing. Not a public internet database.
- **Users:** Russian government agencies, Russian critical infrastructure, Eastern European enterprises. NOT recommended for use in Western organizations due to sanctions.
- **Geopolitical context:** SANCTIONED by US Treasury (April 2021) under Executive Order 13694 for "supporting Russian government cyberoperations against the United States and its allies." Positive Technologies holds regular security conferences (PHDays) that are attended by Russian intelligence and military personnel. After Russia's February 2022 invasion of Ukraine, the company publicly sided with Russian government narratives. All data controlled by a sanctioned Russian entity. Western use of their products constitutes potential sanctions violations.
- **Controversies:** US sanctions are the primary controversy. Documented cooperation with Russian intelligence services. Despite producing legitimate security research, the company is considered part of Russia's cyber-industrial complex.

---

### 30. BI.ZONE (Russian — GEOPOLITICAL FLAG)
- **Organization:** BI.ZONE (Безопасные Информационные Зоны, "Safe Information Zones") — Moscow, Russia. Subsidiary of Sberbank (Russia's largest state-owned bank). Founded 2016.
- **Website:** https://bi.zone
- **What data:** Cyber threat intelligence, attack surface management, digital risk monitoring. Products include BI.ZONE Threat Intelligence, BI.ZONE Brand Protection, BI.ZONE Attack Surface Management. Conducts internet scanning for attack surface and threat intelligence purposes. Monitors dark web, social media, and internet infrastructure.
- **Scan frequency/coverage:** Continuous threat monitoring and scanning.
- **Scale:** Not publicly disclosed; serves major Russian enterprises and government entities.
- **Access model:** Commercial enterprise product; Russian market focus.
- **Users:** Russian corporations, Russian government entities, Sberbank ecosystem clients.
- **Geopolitical context:** Sberbank subsidiary — Sberbank is under US/EU sanctions since 2022 (Russia-Ukraine war). BI.ZONE itself has not been directly sanctioned but is an extension of a sanctioned financial institution's cybersecurity arm. Operates under Russian law with all associated intelligence service access obligations. NOT suitable for Western organizations.
- **Controversies:** Sberbank parent under Western sanctions. Operates in the same regulatory environment as other Russian entities subject to FSB intelligence-sharing laws.

---

### 31. 360 Quake (Qihoo 360 — GEOPOLITICAL FLAG)
- **Organization:** Qihoo 360 Technology Co., Ltd. (奇虎360, Beijing, China; NASDAQ-delisted 2016, re-listed on Shanghai Stock Exchange 2018). Qihoo 360 is China's largest cybersecurity company by user base. The Quake product is operated by their security intelligence division.
- **Website:** https://quake.360.net / https://360.net/en/product-center/security-intelligence/quake-cs-mapping-system
- **What data:** "Cyberspace Surveying and Mapping System" — accumulates billions of asset data points. Covers 1,000+ common network protocols and industrial control protocols, across 20+ categories and 120+ subcategories including: communications, industrial control (ICS/SCADA), blockchain, IoT, video. Uses Vscan self-developed detection engine + 360 big data for AI-enhanced recognition. Dynamic asset mapping using multiple task strategies.
- **Scan frequency/coverage:** Continuous active detection; "dynamic asset mapping across the network."
- **Scale:** Billions of assets; 1,000+ protocols (including ICS/SCADA). Qihoo 360's massive infrastructure and user data (500M+ users of its security products) provides additional telemetry beyond raw port scanning.
- **Access model:** Commercial; Chinese and English interfaces. API access available.
- **Users:** Chinese government, Chinese enterprise security teams, Chinese security researchers. **GEOPOLITICAL FLAG: Qihoo 360 is a Chinese state-linked company with deep ties to Chinese government and military. Qihoo 360 has been involved in intelligence operations, and its products are distributed across Chinese government systems. The company publishes threat intelligence reports that align with Chinese government interests.**
- **Geopolitical context:** Qihoo 360 is considered part of China's cyber-industrial complex. The company has been awarded Chinese government contracts and participates in state cybersecurity initiatives. Qihoo 360's CEO Zhou Hongyi has close ties to the Chinese government. Quake's ICS/SCADA coverage and industrial protocol depth is particularly significant from a critical infrastructure intelligence perspective.
- **Controversies:** Western cybersecurity researchers have flagged Qihoo 360 for publishing vulnerability research timed to political events and for its deep integration with Chinese government surveillance. Not directly sanctioned by the US (unlike Positive Technologies) but considered a geopolitical concern.

---

### 32. Hunter.how (Chinese — GEOPOLITICAL FLAG)
- **Organization:** Hunter (hunter.how) — Chinese-operated cyberspace asset search engine. Operator identity not fully transparent publicly.
- **Website:** https://hunter.how
- **What data:** Cyberspace asset search — open ports, services, TLS certificates, banners. Search by IP, domain, protocol. Listed alongside Shodan, FOFA, ZoomEye in security research contexts. Referenced in OpenFilters/internet-scanners as an active global scanner.
- **Scan frequency/coverage:** Continuous internet-wide scanning.
- **Scale:** Not publicly disclosed.
- **Access model:** Free tier with limited queries; paid plans.
- **Users:** Security researchers, Chinese-market users, red teamers.
- **Geopolitical context:** Chinese-operated scanning platform; similar regulatory concerns as FOFA/ZoomEye — subject to PRC national security laws. Less extensively documented than FOFA or ZoomEye but actively scanning the global internet.
- **Controversies:** Limited public documentation. Operator transparency concerns.

---

### 33. Cyble ODIN
- **Organization:** Cyble Inc. (Atlanta, GA + India; founded 2019 by Beenu Arora and Manish Chachada). Global threat intelligence company with significant India operations.
- **Website:** https://odin.io / https://cyble.com
- **What data:** Internet-wide attack surface scanning — entire IPv4 and IPv6 space. Cloud bucket exposure scanning across 7 major cloud providers (detected 200+ billion exposed files). Domains, subdomains, IPs, open ports, exposed cloud storage, dark web monitoring, threat intelligence. AI/ML-based content classification for exposed data. Integration with Cyble Vision (broader threat intelligence platform) and Cyble Saratoga (Cyber Risk Quantification).
- **Scan frequency/coverage:** Continuous; real-time asset monitoring.
- **Scale:** 200+ billion exposed cloud files detected. Full IPv4/IPv6 coverage. Named in Gartner EASM reports.
- **Access model:** Enterprise SaaS (Cyble ODIN + Cyble Vision); commercial pricing. Available on Microsoft Azure Marketplace.
- **Users:** Enterprise security teams, MSSPs, government agencies, threat intelligence teams. India-US dual market focus.
- **Notable:** Unique focus on cloud bucket/storage exposure at massive scale. AI-native from inception. Cyble is one of the fastest-growing threat intelligence companies with significant India market presence. Gartner-recognized EASM vendor.
- **Controversies:** None significant.

---

### 34. scans.io — Stanford/Censys Internet Research Data Repository (Academic)
- **Organization:** Stanford Empirical Security Research Group (ESRG) and originally University of Michigan (Censys team). Primarily maintained by Stanford ESRG. Non-commercial academic archive.
- **Website:** https://scans.io / https://data.esrg.stanford.edu
- **What data:** Public archive of internet-wide scan research datasets. Hosts: ZMap/ZGrab scan results, Censys snapshots (daily IPv4/IPv6 snapshots ~2TB each), X.509 certificate datasets (8 billion certificates, 15-20 TB), DNS datasets, HTTP/HTTPS response datasets. Daily snapshots of 3.3B+ services. Data uploaded by Censys, academic researchers, and other organizations.
- **Scan frequency/coverage:** Passive archive — data deposited by scanning projects at various frequencies. Censys deposits daily snapshots.
- **Scale:** Terabytes of scan data; 8B certificates; multiple years of historical data.
- **Access model:** Non-commercial use only; JSON interface; contact support@esrg.stanford.edu. Free to vetted academic researchers. No login required for browsing dataset catalog.
- **Users:** Academic security researchers, data scientists, Internet measurement community. Data has been used in hundreds of published academic papers.
- **Notable:** Created alongside and closely tied to Censys. The original Censys paper (IEEE S&P 2015, Durumeric et al.) established scans.io as the open data complement to the Censys search engine. Critical infrastructure for internet measurement research community.
- **Controversies:** None; deliberately academic and non-commercial.

---

### 35. Stretchoid (Gray Zone / Unknown Operator)
- **Organization:** Stretchoid.com — operator identity not publicly disclosed. Website claims it "helps identify an organization's online services" and states "our activity is completely harmless." All scanning IPs originate from DigitalOcean.
- **Website:** https://stretchoid.com (opt-out form available; opt-out form has raised concerns among security community)
- **What data:** Mass internet scanning — appears focused on finding vulnerable admin interfaces and exposed services. Likely open ports, service banners, potentially admin login pages, exposed management interfaces.
- **Scan frequency/coverage:** Continuous; one of the top internet scanning organizations by activity (15-25% of observed security research scanning activity in SANS ISC studies).
- **Scale:** High activity volume — among top scanners globally by packet count in honeypot studies.
- **Access model:** Unknown — no public database or search interface documented. Unclear if data is sold, used internally, or for what purpose.
- **Users:** Unknown.
- **Notable:** Significant opaque scanning activity with no identified owner raises concern in the security community. SANS Internet Storm Center has flagged Stretchoid multiple times. Opt-out mechanism's trustworthiness questioned (community discussions advise against submitting data via their opt-out form due to unknown operator identity). Pure gray-zone operator.
- **Controversies:** Complete lack of transparency about operator, purpose, or data use. Listed by SANS ISC as a recurring topic of concern. The security community treats it with significant skepticism.

---

### 36. Alpha Strike Labs (European)
- **Organization:** Alpha Strike Labs GmbH — Hamburg, Germany. Founded ~2014. European-focused cybersecurity company.
- **Website:** https://www.alphastrike.io
- **What data:** Internet-wide scanning — open ports, service banners, TLS certificates, vulnerability data. Focused on German/European market. EASM capabilities.
- **Scan frequency/coverage:** Continuous internet-wide scanning.
- **Scale:** Not publicly disclosed; European-focused but scans globally.
- **Access model:** Commercial enterprise product.
- **Users:** European enterprises, German market security teams.
- **Notable:** Listed in OpenFilters/internet-scanners as an active global scanning organization. Germany-based, which means EU GDPR compliance and no Chinese/Russian data concern. One of the few European-native internet scanning operators besides Onyphe.
- **Controversies:** None documented.

---

### 37. Group-IB (Russian-origin, now UAE-headquartered — GEOPOLITICAL NOTE)
- **Organization:** Group-IB (founded 2003 in Moscow; headquarters relocated to Dubai, UAE in 2022 following founder Ilya Sachkov's arrest in Russia in 2021 on treason charges). Now operates as a non-Russian company.
- **Website:** https://www.group-ib.com
- **What data:** Threat intelligence platform with internet scanning and infrastructure tracking. Tracks cybercriminal infrastructure, C2 servers, phishing sites, botnet infrastructure, dark web. Attack surface discovery capabilities. Digital forensics and incident response.
- **Scan frequency/coverage:** Continuous threat intelligence collection.
- **Scale:** One of the world's largest threat intelligence databases for criminal infrastructure. Specific internet scan database size not publicly disclosed.
- **Access model:** Commercial enterprise platform (Threat Intelligence & Attribution, Managed XDR, Digital Risk Protection).
- **Users:** Law enforcement agencies (partnered with Europol, Interpol, FBI), banks, enterprises, governments.
- **Geopolitical context:** COMPLEX: Founder Ilya Sachkov arrested by Russian FSB in September 2021 and convicted of treason in 2023 (allegedly for sharing intelligence with Western partners). Company subsequently relocated from Russia to Dubai/Singapore. Now operates independently of Russian influence — possibly the opposite: founder's arrest suggests he was NOT cooperating with Russian intelligence. UAE headquarters means no Russian law obligations. However, historical Russian origin and some employee retention in Russia creates residual concern.
- **Controversies:** Sachkov conviction is the major controversy — Russian government accused him of treason for cooperating with Western intelligence agencies. The company itself maintains it operates independently and lawfully.

---

### 38. CrowdStrike Falcon Surface
- **Organization:** CrowdStrike Inc. (NASDAQ: CRWD; Austin, TX). Falcon Surface is built on technology acquired from Reposify (Israeli startup, acquired 2021 for ~$190M). Now part of CrowdStrike Falcon Exposure Management platform.
- **Website:** https://www.crowdstrike.com/en-us/platform/exposure-management/easm/
- **What data:** Proprietary 24/7 real-time internet scanning engine — continuously indexes the entire global internet. Discovers unknown/unmanaged internet-facing assets without requiring prior inventory. Data: IPs, domains, open ports, services, TLS certificates, CVE vulnerability mapping, cloud assets, adversary intelligence correlation (cross-referenced with CrowdStrike's adversary threat intelligence). Industry-specific risk context.
- **Scan frequency/coverage:** Continuous 24/7; full global internet coverage.
- **Scale:** "Entire internet" continuously indexed. Specific numbers not disclosed. Reposify's technology was described as scanning 4B+ IPs daily pre-acquisition.
- **Access model:** Falcon Platform subscription (enterprise). Not publicly searchable. Integrates with CrowdStrike Falcon XDR ecosystem.
- **Users:** CrowdStrike enterprise customers. 2025 Gartner Customers' Choice for EASM (sole vendor).
- **Notable:** Differentiated by adversary intelligence integration — maps attack surface from the attacker's perspective using CrowdStrike's threat intelligence on 200+ named adversaries. Does not require initial asset inventory. Israeli Unit 8200 lineage through Reposify acquisition.
- **Controversies:** None significant. CrowdStrike's July 2024 Falcon sensor update caused global IT outages (unrelated to Falcon Surface specifically, but reputational context).

---

### 39. Bitsight (Groma Internet Scanning Engine)
- **Organization:** Bitsight Technologies Inc. (Boston, MA; founded 2011). Acquired by Moody's Corporation for $2.2 billion in 2023. Pioneer of cyber risk ratings.
- **Website:** https://www.bitsight.com / https://www.bitsight.com/groma-explorer
- **What data:** Groma is Bitsight's proprietary internet scanning engine. Continuously scans entire internet for: open ports, SSL/TLS certificates, web application headers, security misconfigurations, CVE-vulnerable software, cloud storage buckets (AWS, Azure, GCP), SaaS services, exposed databases, shadow IT, ICS/OT devices. New assets discoverable within 2 hours of appearing on internet (per GreyNoise validation study).
- **Scan frequency/coverage:** Continuous; Groma Explorer provides public visibility into scan methodology.
- **Scale:** Full internet-scale. Bitsight rates 850,000+ companies globally using scan data. Tracks security posture of entire industries and supply chains.
- **Access model:** Commercial enterprise product (Security Ratings, EASM, Attack Surface Intelligence). Not publicly searchable database. Moody's integration enables financial risk + cyber risk synthesis.
- **Users:** CISOs, cyber insurance underwriters, investors, supply chain risk teams, financial institutions. Moody's ownership enables integration into financial/credit risk assessments.
- **Notable:** Groma's 2-hour asset detection speed is a notable technical achievement. Moody's acquisition uniquely positions Bitsight as the bridge between cybersecurity risk and financial risk — cyber risk data feeding into investment and credit decisions. ICS/OT coverage extended in recent years.
- **Controversies:** The concept of "security ratings" for companies (that companies cannot opt out of) has been controversial — organizations object to being rated on data they didn't consent to sharing.

---

### 40. Driftnet / SecurityScorecard (acquired May 2026)
- **Organization:** Driftnet Ltd (UK; founded ~2020 by British researchers; AS211298). Acquired by SecurityScorecard (New York, NY; TPRM/security ratings company founded 2013) on May 14, 2026. Terms not disclosed.
- **Website:** https://driftnet.io (pre-acquisition) / https://securityscorecard.com (post-acquisition)
- **What data:** High-fidelity internet-wide scanning with specific strengths: non-standard port enumeration, advanced TLS fingerprinting (JARM, JA4X, JA4TScan), TCP stack fingerprinting, forward DNS/MX/TXT records, device identification (nmap/recog/webappanalyzer/nuclei integration), CVE/CPE enrichment from NIST NVD with CVSS and EPSS scoring, ASN/geolocation tagging. Full IPv4 coverage. IPv6 emphasis. Discovers "chained misconfigurations" in infrastructure relationships.
- **Scan frequency/coverage:** Continuous; full IPv4 space; IPv6 hitlist-based.
- **Scale:** Claims to index 40% more internet-exposed hosts than rival platforms. Discovered 816,000+ internet-exposed AI OpenClaw agent deployments in one study.
- **Access model:** Pre-acquisition: API-based commercial access. Post-acquisition (May 2026): integrated into SecurityScorecard's TITAN AI platform for TPRM and threat intelligence. API likely continued for enterprise customers.
- **Users:** TPRM (Third-Party Risk Management) teams, SOCs, threat hunters, supply chain security. SecurityScorecard's 12,000+ enterprise customers now gain access to Driftnet engine.
- **Notable:** Acquired just weeks before this research session (May 14, 2026) — one of the most recent internet scanning acquisitions. SecurityScorecard's position: using Driftnet's scanning to power AI-driven third-party risk management — a major evolution in how internet scan data feeds enterprise risk decisions. NCSC UK listed Driftnet as a collaborator in their Active Cyber Defence ASM experiment.
- **Controversies:** None significant. SecurityScorecard itself faces the same "opt-out" controversy as Bitsight regarding unsolicited security ratings.

---

### 41. Hadrian
- **Organization:** Hadrian Security (Amsterdam, Netherlands; founded ~2021). European EASM/offensive security company.
- **Website:** https://hadrian.io
- **What data:** Continuous internet-wide scanning of external attack surface — domains, IPs, web applications, cloud assets, misconfigurations, vulnerabilities, outdated software. Offensive security perspective ("hacking team" approach). Competes with CyCognito and CrowdStrike Falcon Surface.
- **Scan frequency/coverage:** Continuous.
- **Access model:** Commercial enterprise SaaS.
- **Notable:** European-based EASM competitor. Listed in OpenFilters/internet-scanners as an active global scanning organization. Published 2026 threat trend predictions based on their scanning data. EU-native, GDPR-compliant alternative to US-centric EASM platforms.
- **Controversies:** None documented.

---

### 42. NETSCOUT / Cyber Threat Horizon
- **Organization:** NETSCOUT Systems Inc. (NASDAQ: NTCT; Westford, MA). Network management and security company.
- **Website:** https://horizon.netscout.com (Cyber Threat Horizon — live DDoS and cyber attack map) / https://www.netscout.com
- **What data:** Real-time DDoS attack intelligence from NETSCOUT's Arbor Networks infrastructure. Passive observation from 550+ ISP and carrier customers globally (network-level visibility). Tracks DDoS attacks, botnets, internet background radiation. Internet Albedo Network (internet-albedo.net) — their internet scanning infrastructure. Biannual DDoS Threat Intelligence Reports.
- **Scan frequency/coverage:** Passive real-time telemetry from ISP partners; also active scanning.
- **Scale:** Network-level telemetry from hundreds of ISP customers globally; one of the largest passive network intelligence datasets in the world.
- **Access model:** Commercial enterprise product (Arbor DDoS protection, Omnis Security). Cyber Threat Horizon DDoS map is publicly accessible (free visualization). Research reports publicly published.
- **Users:** ISPs, large enterprises, government agencies, SOCs for DDoS protection.
- **Notable:** NETSCOUT's Arbor Networks division has operated the world's largest passive internet telemetry network for 20+ years. The internet-albedo.net domain is NETSCOUT's active scanning infrastructure. Distinct from Shodan/Censys in that its primary data comes from passive ISP telemetry rather than active scanning, but combined active+passive gives unique visibility.
- **Controversies:** None significant.

---
