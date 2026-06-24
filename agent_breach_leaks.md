# Breach/Credential Leak Database Research

## Objective
Research and document ALL significant breach/credential leak database operators — commercial, free/open, government, academic, nonprofit, and gray/dark market. Global scope. Flag geopolitical context where relevant.

## Task List
- [x] HaveIBeenPwned (Troy Hunt)
- [x] DeHashed
- [x] LeakCheck
- [x] Snusbase
- [x] IntelligenceX
- [x] BreachDirectory
- [x] SpyCloud
- [x] Constella Intelligence (formerly 4iQ)
- [x] Recorded Future (credential monitoring)
- [x] Hudson Rock [DONE]
- [x] RaidForums / BreachForums [DONE]
- [x] WeLeakInfo (seized) [DONE]
- [x] Ghost Project [DONE]
- [x] Scattered Secrets [DONE]
- [x] Genesis Market (seized) [DONE]
- [x] Russian Market [DONE]
- [x] 2easy.shop [DONE]
- [x] Flashpoint [DONE]
- [x] Flare Systems [DONE]
- [x] Breachsense [DONE]
- [x] XposedOrNot [DONE]
- [x] Privacy Rights Clearinghouse [DONE]
- [x] LeakRadar [DONE]
- [x] psbdmp (paste monitoring) [DONE]
- [x] SOCRadar [DONE]
- [x] CybelAngel [DONE]
- [x] KELA Cyber [DONE]
- [x] Leak-Lookup (MOAB) [DONE]
- [x] OSINTLeak [DONE]
- [x] National Public Data (notable breach/data broker) [DONE]
- [x] Cyble [DONE]
- [x] ZeroFox [DONE]
- [x] Group-IB [DONE]
- [x] Cybersixgill / Bitsight [DONE]
- [x] ImmuniWeb [DONE]
- [x] ProxyNova COMB [DONE]
- [x] Telegram combolist channels (distribution channel) [DONE]
- [x] Webz.io / Lunar [DONE]

## Status
- Session started: 2026-06-17
- Last updated: 2026-06-23

---

# FINDINGS

---

## 1. HaveIBeenPwned (HIBP) [DONE]

- **Organization:** Troy Hunt (individual founder/operator); Cloudflare partnership (infrastructure/funding)
- **Website:** https://haveibeenpwned.com
- **Database:** Breach notification and credential monitoring; indexes email addresses and passwords from public breach incidents and infostealer logs
- **Scale:** 12+ billion breach records total; ~2 billion unique email addresses indexed; 1.3 billion unique passwords in Pwned Passwords; 625 million passwords added Nov 2025 (previously unseen)
- **Access model:** Free consumer lookup; Pwned Passwords API is free; paid API tiers for bulk/enterprise use; FBI and other LEA partnerships for adding data
- **Who uses it:** Individual consumers, IT teams, developers integrating into apps, law enforcement (FBI feeds data), enterprise security teams
- **Notable:** Non-commercial origin; Troy Hunt sole operator. Recently added large stealer-log datasets: Synthient (183M unique emails), Data Troll (109M unique emails). BreachForums 2025 breach of 672k emails added after law enforcement takedown. CISA acquisition discussions happened then dropped.
- **Controversies:** Debate over whether including stealer logs (not traditional database breaches) changes the nature of the service; some argue it normalizes mass surveillance

---

## 2. DeHashed [DONE]

- **Organization:** DeHashed (private company, USA)
- **Website:** https://dehashed.com
- **Database:** Breach intelligence platform — searchable leaked database contents including usernames, passwords (plaintext and hashed), IP addresses, names, phone numbers, addresses, VINs, web domains; historical WHOIS records
- **Scale:** Billions of records; self-described "largest firm in the industry"
- **Access model:** Paid subscription; API available; free teaser results with registration; bulk/enterprise pricing available
- **Who uses it:** OSINT investigators (featured in Bellingcat toolkit), security researchers, red teamers, fraud prevention teams, journalists
- **Notable:** Exposes actual credential pairs (not just notification like HIBP). Four service lines: Search, Monitor, API, WHOIS (WHOIS added April 2025).
- **Controversies:** Gray-area service — exposes plaintext credentials; critics argue it enables credential stuffing and abuse; defenders argue it is a valid security research tool

---

## 3. SpyCloud [DONE]

- **Organization:** SpyCloud (private company, Austin TX, USA; founded ~2016)
- **Website:** https://spycloud.com
- **Database:** Largest private recaptured darknet credential repository; includes breach data, malware/infostealer logs, phishing kit results; 90%+ of credentials cracked to plaintext
- **Scale:** 36 billion+ credentials indexed
- **Access model:** Enterprise paid; government/LEA clients; no public free search; API for enterprise customers; consumer monitoring via ISP/telecom data partnerships
- **Who uses it:** Fortune 10 companies, global enterprises, mid-sized companies, government agencies, fraud prevention teams
- **Notable:** Recaptures data BEFORE it hits public dark web markets by infiltrating criminal communities. Includes malware infostealer logs and phishing results — broader scope than traditional breach databases. 2026 report flagged surge in exposed API keys, session tokens, machine identities.
- **Controversies:** Legally gray area holding cracked credentials; positioned purely as defense; holds data that criminals actively seek

---

## 4. LeakCheck.io [DONE]

- **Organization:** LeakCheck (private; Eastern European origin suspected but not publicly confirmed)
- **Website:** https://leakcheck.io
- **Database:** Credential breach search engine; data collected exclusively from public sources; searches by email, username, keyword, corporate domain, or password
- **Scale:** 7–10 billion+ leaked records (claims vary; 10B claimed on site)
- **Access model:** Free limited lookup (email only, no password shown); paid plans for full access and API; bulk search up to 100,000 lines per batch; no search history stored
- **Who uses it:** Security researchers, OSINT practitioners, corporate IT teams monitoring domain exposure
- **Notable:** Privacy-focused design — supports SHA256 hash of email address to avoid sending plaintext queries. Operational ~6 years. Offers enterprise API for bulk searches.
- **Controversies:** Dual-use concerns; used by both defenders and attackers; geopolitical origin unclear

---

## 5. Snusbase [DONE]

- **Organization:** Snusbase (private; exact jurisdiction unclear; operating since 2016)
- **Website:** https://snusbase.com
- **Database:** Database breach search engine; indexes email, username, IP, phone, password hash; shows uncensored full PII results to paying members
- **Scale:** Not publicly stated; indexes numerous breach datasets
- **Access model:** Paid subscription ($5–$16/month tiers); API free to paying members up to 2,048 requests/day
- **Who uses it:** Security researchers, OSINT investigators, fraud investigators, law enforcement (per self-claim), corporate security teams
- **Notable:** Founded 2016; displays clear uncensored breach results including full names, addresses; one of cheapest credential lookup services
- **Controversies:** Dual-use concerns; unclear jurisdiction and legal accountability; actively used by threat actors; no clear vetting of user intent

---

## 6. IntelligenceX [DONE]

- **Organization:** IntelligenceX (independent; founded 2018 by Peter Kleissner; Prague, Czech Republic)
- **Website:** https://intelx.io
- **Database:** Search engine and data archive; indexes dark web, deep web, paste sites, data leaks, Tor/I2P content, deleted web content, historic domains, WikiLeaks; preserves PII and malware source code for forensic analysis
- **Scale:** 200+ billion records indexed
- **Access model:** Freemium — limited free searches; paid plans for full access; API available; researcher/journalist discounts
- **Who uses it:** Cybersecurity professionals, OSINT researchers, threat intelligence analysts, journalists, digital forensics teams
- **Geopolitical:** Prague-based; Czech Republic (EU); has indexed leaked data from Russian and Chinese state-linked sources
- **Notable:** Deliberately preserves content others delete or refuse to host — WikiLeaks, dark web market archives, historical breach dumps. Founded in EU but not subject to heavy GDPR enforcement on archived breach data.
- **Controversies:** 2021 — attacker scraped IntelligenceX Pastes section, harvesting ~92.6M email addresses. Ongoing debate about whether archiving stolen PII at scale is itself a privacy violation.

---

## 7. BreachDirectory [DONE]

- **Organization:** BreachDirectory (private; operator identity not publicly disclosed)
- **Website:** https://breachdirectory.org / https://breachdirectory.com
- **Database:** Public breach data search engine; indexes email addresses, usernames, passwords (shown as truncated hashes), domains, IPs, phone numbers, full names, blockchain addresses
- **Scale:** Not publicly stated; covers "all public data breaches"
- **Access model:** Freemium — 10 free searches/month; paid API via RapidAPI marketplace; bulk unlimited API plan available
- **Who uses it:** Security researchers, OSINT practitioners, developers building breach-check tools; integrated into various OSINT CLI tools (e.g. eBreached)
- **Notable:** Password results shown as hashed (partial protection vs. DeHashed/Snusbase); integrated into RapidAPI marketplace making it easy to embed in third-party apps; also links to CVE/KEV vulnerability data
- **Controversies:** Minimal known controversies; dual-use; anonymous operator raises accountability questions

---

## 8. Constella Intelligence (formerly 4iQ) [DONE]

- **Organization:** Constella Intelligence (formed Dec 2020 from merger of 4iQ + Alto Analytics; 4iQ founded 2016 by Julio Casal; CEO Kailash Ambwani; HQ Santa Clara, CA, USA)
- **Website:** https://constella.ai
- **Database:** Claims "largest breach data collection on the planet"; spans 125 countries and 53 languages
- **Scale:** 100+ billion attributes; 45 billion curated identity records
- **Access model:** B2B enterprise only; no public search; API integrations for identity theft monitoring and fraud detection; named products: "Dome" (risk monitoring), "Hunter" (deep OSINT investigations)
- **Who uses it:** Large enterprises, government agencies, intelligence professionals, identity theft monitoring services, financial fraud detection platforms
- **Geopolitical:** US-based; backed by C5 Capital (defense/intelligence-focused VC); US government/intelligence community clients
- **Notable:** Lineage: Survela (2013) → 4iQ → Constella. Focuses on Digital Risk Protection (DRP). Operates one of the largest private identity intelligence repositories globally.
- **Controversies:** Operating at massive scale aggregating personal breach data; debate over legal basis under GDPR for EU-sourced data

---

## 9. Recorded Future [DONE]

- **Organization:** Recorded Future (founded 2009; acquired by Mastercard in 2024 for $2.65 billion; HQ Somerville MA, USA)
- **Website:** https://recordedfuture.com
- **Database:** Enterprise threat intelligence platform; identity/credential intelligence module indexes dark web, paste sites, criminal forums, malware logs; NOT a standalone searchable breach lookup — alert/API driven
- **Scale:** 1M+ sources indexed; 2025: indexed hundreds of millions of credentials including 276M with active session cookies
- **Access model:** Enterprise paid; government/intelligence community clients; API-driven integrations; no public search interface
- **Who uses it:** Large enterprises, financial institutions, government agencies, intelligence community, MSSPs
- **Notable:** 2025 report: 36.4% of indexed credentials detected within 24 hours of exfiltration; 52.9% within one week; 276M credentials with active session cookies enabling MFA bypass. Credential monitoring is one module within a broader geopolitical/nation-state threat intel platform.
- **Controversies:** Acquisition by Mastercard (2024) raised concerns about payment network owning major threat intel platform with law enforcement/intelligence access

---

## 10. Hudson Rock [DONE]

- **Organization:** Hudson Rock Limited (Israeli cybersecurity company; co-founded 2020 by Alon Gal and Roi Carthy; HQ Tel Aviv, Israel)
- **Website:** https://www.hudsonrock.com / https://cavalier.hudsonrock.com
- **Database:** Cavalier — infostealer-derived credential and corporate intelligence platform; data sourced directly from threat actors and augmented monthly; focuses on compromised machines (bots) from global malware campaigns rather than static breach dumps
- **Scale:** 30M+ analyzed compromised computers as of early 2025; ~11.6M compromised domains identified; hundreds of thousands of new compromised machines added monthly
- **Access model:** B2B enterprise paid (SaaS); free limited public lookup at https://www.hudsonrock.com/free-tools; CavalierGPT AI query interface (launched Dec 2024)
- **Who uses it:** Enterprise security teams, fraud prevention, incident response teams, financial institutions; 100+ customers worldwide as of April 2025; achieved 4,600% ARR growth in ~4 years
- **Geopolitical:** Israeli company; founders have IDF Unit 8200 background (elite signals intelligence/cyber unit). Alon Gal previously ran "Under the Breach" threat intelligence research. Israeli cyber industry has deep ties to IDF intelligence pipelines.
- **Notable:** Focus is infostealer malware logs, not traditional database breaches. Data comes from RedLine, Raccoon, Vidar, LummaC2 and similar malware families. Identified breaches at Facebook, Airbus, Telefónica, Samsung, Jaguar Land Rover. December 2024: launched CavalierGPT, first AI bot dedicated to infostealer intelligence. Platform redesigned 2024 as dual-purpose investigation + monitoring tool.
- **Controversies:** Gray-area holding of stolen credential data; Alon Gal (as "Under the Breach") was a prominent public commentator on major breaches — some debate over line between researcher and intel trader

---

## 11. RaidForums / BreachForums [DONE]

- **Organization:** Criminal forums (not companies); primary operators: Diogo Santos Coelho ("omnipotent") — RaidForums; Conor Brian Fitzpatrick ("Pompompurin") — BreachForums v1; "ShinyHunters" group — BreachForums v2; "IntelBroker" — BreachForums v3; "Anastasia" — BreachForums v4
- **Website:** raidforums.com (seized); breachforums.to / .cx / .st (cycling domains, seized multiple times)
- **Database:** Primary dark web marketplaces/forums for stolen data, hacked databases, and credential dumps; not a searchable service but the primary distribution channel for leaked data that feeds other services
- **Scale:** RaidForums: ~500,000 registered users; hosted thousands of breach datasets. BreachForums: similar scale; hosted AT&T, Ticketmaster, National Public Data, and hundreds of other major breach postings
- **Access model:** Dark web forum; free registration with credits/currency for premium data; data sold or traded between members; some data freely posted
- **Who uses it:** Cybercriminals, credential stuffers, ransomware groups, OSINT researchers (monitoring), threat intelligence firms
- **Geopolitical:** RaidForums operator was Portuguese (Diogo Santos Coelho, arrested Faro, Portugal). BreachForums v1 operator was American (Fitzpatrick, NY). ShinyHunters is a loosely international group — four members arrested by French authorities June 2025.

### Timeline:
- **RaidForums:** 2015–April 2022. Seized by DOJ/international LE coalition April 2022. Founder arrested January 2022. Database of 478,000 users leaked May 2023.
- **BreachForums v1:** March 2022–March 2023. Fitzpatrick arrested March 15, 2023; sentenced January 2024 to 20 years supervised release.
- **BreachForums v2:** June 2023–May 2024 (ShinyHunters/Baphomet). FBI seized May 15, 2024 (Operation: coordinated with Europol). ShinyHunters reclaimed domain via EPP code within hours.
- **BreachForums v3:** 2024 — IntelBroker takes ownership; steps down; transfers to "Anastasia."
- **BreachForums v4:** August 2025 — forum goes offline; ShinyHunters claims law enforcement compromise. October 2025 — FBI seizes again. ShinyHunters officially exits, leaks 300,000 user records, warns all remaining BreachForums domains are impostors or honeypots.
- **Current (2026):** No legitimate BreachForums. ShinyHunters states in April 2026 that any active site using the name is either a criminal impostor or a law enforcement honeypot. BreachForums database of 324,000 criminal users itself leaked in a "doomsday" leak.
- **Notable:** The forum chain was the primary vector through which nearly every major public data breach of 2022–2025 was disclosed or monetized (AT&T, Ticketmaster/Live Nation, National Public Data, etc.)
- **Controversies:** FBI ran v3-era forum as a potential honeypot; ShinyHunters' claim that LE has controlled the domain at various points is credible given multiple seizures and recaptures

---

## 12. WeLeakInfo [DONE]

- **Organization:** Three co-operators (identities: Dutch national, Northern Irish national, third person at large); private criminal enterprise, no formal company structure
- **Website:** weleakinfo.com (original, seized January 2020); weleakinfo.to (seized by DOJ, date varies); and related domains ipstress.in, ovh-booter.com
- **Database:** Searchable breach data marketplace; aggregated data from 10,000+ breached databases; indexed 7 billion+ records (later claimed 12+ billion); searchable by name, email, username, phone, password
- **Scale:** 10,368 hacked databases; 12.4 billion indexed records (per DOJ indictment)
- **Access model:** Paid subscription ($2/day, $7/week, $25/month, $70/3 months, $399/lifetime); unlimited searches during subscription; no per-query limits
- **Who uses it:** Cybercriminals (credential stuffing, fraud, identity theft), some security researchers; 24,000+ registered users at time of seizure
- **Geopolitical:** Dutch and Northern Irish operators; seized through US/Netherlands/Belgium/UK joint action

### Legal History:
- **January 15–16, 2020:** FBI and DOJ seized weleakinfo.com; Dutch police arrested Dutch operator; PSNI (Police Service of Northern Ireland) arrested 22-year-old in Fintona, Northern Ireland
- **December 2020:** UK National Crime Agency arrested 21 WeLeakInfo customers in separate crackdown
- **December 2022:** Dutch operator sentenced in Netherlands to 2 years imprisonment (1 year suspended)
- **January 2023:** DOJ seized weleakinfo.to and related domains in second action; two UK nationals (22 and 23 years old) arrested by NCA on suspicion of computer misuse and fraud; one suspect had operated service after original seizure
- **Third operator:** Remains at large as of last known reporting

- **Notable:** First major US enforcement action specifically targeting a breach-data subscription service (as opposed to seizing data or arresting hackers). Set precedent for treating credential marketplace operators as criminal enterprises rather than passive hosts.
- **Controversies:** Service was legally registered and appeared legitimate to some users; debate over whether data aggregation services that charge for access constitute criminal enterprises vs. information services

---

## 13. Ghost Project [DONE]

- **Organization:** Anonymous/unknown operator
- **Website:** https://ghostproject.fr (primary); ghostproject.me (earlier domain)
- **Database:** Breach data search engine focused on plaintext credential pairs (email:password combinations); data sourced from public breach dumps and combo lists
- **Scale:** Claims 15+ billion records from 7,200+ data breaches; earlier versions indexed ~1.4 billion credential pairs
- **Access model:** Free search (email or username lookup); shows whether credentials appear in database; historically showed partial password previews; full results may require account or payment depending on version
- **Who uses it:** OSINT researchers, security teams, individuals checking personal exposure; also abused by attackers for credential stuffing
- **Geopolitical:** Unknown operator; .fr domain (France) but operator identity undisclosed
- **Notable:** One of the older alternative breach search engines; status fluctuates — periodically marked as discontinued then reappears. API access documented in open-source OSINT tools (GitHub gists). Listed in OSINT tool catalogs alongside HIBP, Snusbase, etc.
- **Controversies:** Plaintext password exposure (more aggressive than HIBP); anonymous operator = no accountability; unclear legal basis for operating

---

## 14. Scattered Secrets [DONE]

- **Organization:** Scattered Secrets BV (private company; Amsterdam, Netherlands; Chamber of Commerce ID 68867530)
- **Founders:** Jeroen van Beek and Rickey Gevers (both Dutch cybersecurity professionals with backgrounds in incident response and forensics)
- **Website:** https://scatteredsecrets.com
- **Database:** Breach notification service with plaintext password recovery; continuously collects publicly available hacked databases and actively cracks password hashes to provide plaintext passwords to verified account owners; also processes infostealer logs
- **Scale:** ~4 billion plaintext passwords in database at last public report
- **Access model:** Free personal lookup (email-based; user must verify ownership of the account); B2B "BreachCheck" API for organizations to monitor employee/customer exposure; enterprise paid tiers
- **Who uses it:** Individuals checking personal exposure; IT/security teams; businesses monitoring for account takeover risk; fraud prevention teams
- **Geopolitical:** Netherlands-based; EU jurisdiction; GDPR-compliant design (only verified account owners see their own passwords)
- **Notable:** Distinguishes itself from HIBP by showing actual plaintext passwords (not just breach notification) to verified owners. Actively cracks hashed passwords rather than just indexing plaintext dumps. Published research on password cracking methodology (cracked 57% of Hookers.nl breach in 3 days). Rickey Gevers is a known figure in Dutch/European cybersecurity community.
- **Controversies:** Holding cracked plaintext passwords at scale creates liability questions; privacy advocates debate whether even verified-owner access to cracked passwords is appropriate; potential for operator abuse of stored plaintext credential database

---

## 15. Genesis Market [DONE — SEIZED]

- **Organization:** Criminal enterprise (operator identities not fully disclosed; believed to be Eastern European/Russian-speaking operators)
- **Website:** genesis.market (Tor and clearnet; seized April 2023)
- **Database:** Bot/credential marketplace; sold "digital fingerprints" — complete packages of stolen credentials, cookies, session tokens, browser fingerprints, and device profiles from malware-infected computers; each "bot" package represented a single compromised victim device
- **Scale:** ~460,000 bot packages listed for sale as of February 2023; 80 million credentials and digital fingerprints from 2+ million victims over lifetime; $8.7M+ in confirmed proceeds
- **Access model:** Dark web marketplace (Tor); also had clearnet mirror; individual bot packages sold (pricing varied by victim profile value); invitation-only or open registration depended on period
- **Who uses it:** Cybercriminals conducting account takeover, fraud, identity theft, corporate espionage; attackers used session cookies to bypass MFA
- **Geopolitical:** Believed to be operated by Russian-speaking cybercriminals; sanctions imposed by US Treasury OFAC alongside seizure; geopolitical dimension because platform enabled nation-state-adjacent criminal activity
- **Legal/Law enforcement:**
  - **April 4, 2023:** Operation Cookie Monster — FBI, Dutch National Police, Europol, 17-country coalition; domain seized; 119 arrests; 208 property searches across 13 nations
  - US Treasury OFAC sanctioned the platform simultaneously
  - Site data used to notify victims via law enforcement "Have I Been Pwned"-style notifications
- **Notable:** Most sophisticated credential marketplace seized to date — not just selling static passwords but complete device impersonation packages enabling MFA bypass and fraud detection evasion. First major marketplace to sell full "browser fingerprint" packages as a product category.
- **Controversies:** Scale of law enforcement notification campaign unprecedented; debate over whether seized domain could/should have been operated as a notification service (as FBI did briefly)

---

## 16. Russian Market (russianmarket.gs) [DONE]

- **Organization:** Anonymous criminal operator(s); believed to be Russian-speaking
- **Website:** russianmarket.gs (and rotating domains; accessible via Tor and clearnet mirrors)
- **Database:** Dark web marketplace specializing in infostealer logs (stealer logs), RDP access credentials, CVV credit card data, and corporate network access; primary product is stealer logs from RedLine, Raccoon, Vidar, LummaC2, and similar malware families
- **Scale:** ~30,000 "bots" (compromised device logs) listed per month in H1 2025; one of the largest active credential marketplaces globally as of 2026
- **Access model:** Dark web marketplace; requires account; cryptocurrency payments (typically Bitcoin/Monero); logs priced individually based on victim profile; no subscription model
- **Who uses it:** Cybercriminals for account takeover, corporate intrusion, fraud; ransomware affiliates purchasing network access
- **Geopolitical:** Russian-language operators; hosted on infrastructure resistant to Western takedowns; operates in gray zone of Russian cybercrime tolerance by authorities
- **Notable:** Dominant marketplace for stealer logs as of 2025-2026 following Genesis Market's seizure. Infostealer deliveries via phishing rose 84% YoY 2023-2024; 180% surge vs 2023 in early 2025 data. Sells credentials with session cookies enabling MFA bypass within 24-72 hour freshness window. Logs are sorted/filtered by victim country, software installed, banking sites accessed.
- **Controversies:** Persistent despite Western law enforcement pressure; demonstrates limits of single-jurisdiction takedowns against Russian-hosted criminal infrastructure

---

## 17. 2easy.shop [DONE]

- **Organization:** Anonymous criminal operator(s)
- **Website:** 2easy.shop (rotating domains)
- **Database:** Dark web marketplace for infostealer logs; positioned as "budget" alternative to Russian Market; high-volume, low-price model for credential dumps from RedLine, Raccoon, Vidar malware families
- **Scale:** Significant volume; individual log packages priced $5–$25; launched 2018, significant volume from 2020
- **Access model:** Dark web marketplace; account-based; cryptocurrency payments; per-log pricing
- **Who uses it:** Entry-level cybercriminals, credential stuffers, fraud actors; lower barrier to entry than Russian Market
- **Geopolitical:** Eastern European/Russian-speaking operator ecosystem
- **Notable:** Entered brief hiatus mid-January 2025 (went inactive); posted return announcement March 22, 2025; demonstrates resilience of criminal marketplace model. Prior to hiatus was second-largest infostealer log market globally. Tidal Cyber noted 2easy as "significant dark web marketplace" in 2022-2023 period.
- **Controversies:** Availability of low-cost logs at scale democratizes credential-stuffing attacks; $5 entry point means even low-resource attackers can purchase fresh credentials

---

## 18. Flashpoint [DONE]

- **Organization:** Flashpoint (private company; founded ~2010; largest privately held threat intelligence provider; HQ New York, USA)
- **Website:** https://flashpoint.io
- **Database:** Ignite platform — comprehensive threat intelligence including credential data from open-source leaks, infostealer malware logs, illicit marketplaces, criminal forums, closed underground communities; monitors 500+ sources across surface/deep/dark web; includes forums, data leak sites, encrypted chat (Telegram, Discord, etc.)
- **Scale:** 3.2 billion credentials compromised in 2024 tracked across monitored sources (per Flashpoint annual report); monitors 500+ sources continuously
- **Access model:** Enterprise paid SaaS; API integrations; available on AWS Marketplace; no public search interface; MSSP/partner distribution
- **Who uses it:** Financial institutions, enterprises, government agencies, MSSPs; partner ecosystem via Analyst1 and AWS Marketplace
- **Notable:** 2024 Annual Report: 3.2B credentials compromised (33% increase over 2023); 75% of 2024 stolen credentials from infostealers. Provides "credential buyback" capability — proactively acquiring stolen credentials from criminal markets before victims are targeted. Deep coverage of closed criminal communities that other services lack (maintains long-term infiltration of private forums). Distinct from "breach notification" services — provides raw intelligence feed, not user-facing lookup.
- **Controversies:** Deep infiltration of criminal communities raises questions about legal and ethical boundaries of "passive" monitoring vs. active participation

---

## 19. Flare Systems [DONE]

- **Organization:** Flare (private company; founded ~2017; Montreal, Quebec, Canada)
- **Website:** https://flare.io
- **Database:** Threat exposure management platform; credential and identity intelligence from dark web forums, Telegram channels, paste sites, ransomware leak sites, infostealer log markets, and clearnet breach sources; nearly a decade of archived historical data
- **Scale:** 20B+ leaked credentials in database; 2M+ threat actor profiles; monitors 58,000+ Telegram channels; has indexed credentials, secrets, and brand threats from hundreds of dark web forums
- **Access model:** Enterprise paid SaaS; API; MSSP tiers; demo available; no public search
- **Who uses it:** Enterprise security teams, MSSPs, SOC teams, fraud prevention; integrates with Microsoft Entra ID for automated remediation
- **Funding:** $30M Series B (December 2024, Base10 Partners); $30M growth round (November 2025); ~$60M total recent fundraising
- **Geopolitical:** Canadian company; EU GDPR considerations for European clients; data collection covers global sources including Russian/Eastern European criminal infrastructure
- **Notable:** October 2025 launch of "Identity Exposure Management" feature — maps exposed credentials to specific users, shows "Blast Radius" of each exposure, integrates with IdP for automated remediation. Positioned as "identity-first threat intelligence." Competes with SpyCloud and Recorded Future at enterprise level.
- **Controversies:** Monitoring of 58,000+ Telegram channels at scale raises questions about scope of surveillance; Canadian company holding data on criminal actors and victims subject to complex jurisdictional questions

---

## 20. Breachsense [DONE]

- **Organization:** Breachsense (private company; exact HQ not prominently disclosed; operates as US-market SaaS)
- **Website:** https://www.breachsense.com
- **Database:** Dark web credential monitoring platform; continuously scans hacker forums, ransomware leak sites, and infostealer logs for stolen credentials, session tokens, and company data; cracks hashed passwords to plaintext where possible; tracks active session tokens from infostealers
- **Scale:** 343B+ compromised credentials indexed (per company's own facts page); founded 2018; Cleveland, Ohio
- **Access model:** Four-tier paid subscription (scales by watchlist size, API quota, alert latency, dark web market coverage); annual billing discount; API-first design; MSP-specific plan for multi-client monitoring; integrates with SIEM/SOAR; available on ConnectWise Marketplace
- **Who uses it:** Enterprise security teams, MSPs, SOC analysts, fraud prevention teams
- **Notable:** Explicitly tracks active session tokens from infostealers (enabling MFA bypass detection); API-first design distinguishes it from notification-only services. Available through ConnectWise Marketplace indicating MSP distribution channel. Positions against Flare.io as focused/specialized alternative. Competes in same tier as Snusbase/LeakCheck but with stronger enterprise positioning.
- **Controversies:** Holding active session tokens at scale creates liability questions; MFA bypass detection requires possessing the very artifacts attackers use

---

## 21. XposedOrNot [DONE]

- **Organization:** XposedOrNot (open-source project with commercial tier; individual/small team operator; exact identity/HQ not prominently disclosed)
- **Website:** https://xposedornot.com / https://plus.xposedornot.com (commercial xonPlus tier)
- **Database:** Breach lookup service; directory of 740+ known data breaches with record counts, risk levels, and details; searchable by email; open-source API (GitHub)
- **Scale:** Not specified; covers 740+ known breaches; smaller than HIBP, DeHashed, or Snusbase
- **Access model:** Free public lookup (email); open-source API (GitHub: XposedOrNot/XposedOrNot-API); commercial "xonPlus" tier for partners, MSSPs, and product teams with API and bulk access; hosted XposedOrNot Hackathon 2024 for community engagement
- **Who uses it:** Developers integrating breach checks, OSINT researchers, MSSPs, individuals
- **Notable:** One of the few breach lookup services with a fully open-source API component, making it auditable. Commercial tier (xonPlus) launched to monetize without compromising free tier. Smaller footprint than major players but notable for transparency.
- **Controversies:** Minimal; open-source nature provides more accountability than anonymous operators

---

## 22. Privacy Rights Clearinghouse — Data Breach Chronology [DONE]

- **Organization:** Privacy Rights Clearinghouse (nonprofit; founded 1992; San Diego, CA, USA)
- **Website:** https://privacyrights.org/data-breaches
- **Database:** Structured compilation of US data breach notifications aggregated from 21 state and federal government sources; NOT a credential lookup service — tracks breach incidents/notifications, not actual stolen data
- **Scale:** 96,000+ records spanning 2005–present; updated weekly; 65 structured fields per record across 12 categories; 7 breach classification categories and 36 specific breach method types
- **Access model:** Free public browsing and search at privacyrights.org/data-breaches; full database available for purchase (store.databreachchronology.org); complimentary access for qualifying academic researchers, nonprofits, and media via request
- **Who uses it:** Academic researchers (250+ institutions across 26 countries); policy researchers; journalists; compliance teams; government agencies; insurance actuaries
- **Geopolitical:** US-focused database (US state/federal notification laws); does not cover international breaches
- **Notable:** Unique role as nonprofit aggregator of *official government breach notification filings* — complements services like HIBP (which tracks actual leaked data) by providing the regulatory/compliance dimension. January 2025: launched Data Breach Chronology 2.0 with major database improvements. Not a threat intelligence tool — a public accountability and research resource.
- **Controversies:** US-centric scope; does not cover GDPR notifications or non-US incidents; passive (notification-based) vs. active (leaked-data) tracking means it captures only officially disclosed breaches

---

## 23. LeakRadar [DONE]

- **Organization:** LeakRadar (private company; operator/HQ not prominently disclosed)
- **Website:** https://leakradar.io
- **Database:** Plain-text credential search platform; aggregates malware logs, combolists, database breaches, and dark web dumps; indexes credentials with associated metadata (URLs, infected host info, timestamps)
- **Scale:** 497B+ plain text credentials indexed (as of 2025; self-reported)
- **Access model:** Unlock-based pricing (pay per credential revealed rather than flat subscription); continuous domain/email monitoring with webhook/Slack/Discord/Telegram/email alerts; REST API with Python wrapper; Chrome browser extension (color-coded breach status per site); team workflow features
- **Who uses it:** Enterprise security teams, SOC analysts, OSINT investigators, fraud prevention teams; Chrome extension for individual users
- **Notable:** "Unlock-based" pricing model is novel — no flat subscription, pay only for credentials you actually reveal. Chrome extension provides passive real-time breach monitoring while browsing. Provides infected host metadata (malware family, timestamp) alongside credentials, enabling infection timeline reconstruction. Positions as combined investigative + monitoring platform.
- **Controversies:** 497B credential claim is exceptionally large if accurate; unlock-based model creates incentive to expose real credentials; anonymous operator

---

## 24. psbdmp / Paste Site Monitoring Services [DONE]

- **Organization:** psbdmp.ws (operator anonymous); ecosystem of paste monitoring tools
- **Website:** https://psbdmp.ws; also psbdmp.com
- **Database:** Archive and search engine for public Pastebin posts and other paste site content; indexes paste content including credential dumps, combolists, source code leaks; provides API for programmatic access
- **Scale:** Millions of archived pastes; real-time indexing of new Pastebin posts
- **Access model:** Free web search; free API (limited); paid API tiers for higher rate limits
- **Who uses it:** Threat intelligence analysts, OSINT researchers, security teams monitoring for credential dumps, incident responders
- **Notable:** Pastebin is a primary first-posting location for credential dumps before migration to dark web forums. psbdmp fills gap left when Pastebin removed its search functionality. Other notable paste monitoring tools in this category: PasteMon (open-source Python), Hunchly, IntelTechniques paste search. Complementary to breach databases — captures dumps *before* they are indexed by services like DeHashed or IntelligenceX.
- **Controversies:** Archives content that Pastebin itself may have removed for ToS violations; re-hosting removed credential dumps creates persistent availability of data the original platform deleted

---

## 25. SOCRadar [DONE]

- **Organization:** SOCRadar (private company; founded 2019; HQ Ankara/Istanbul, Turkey with US offices)
- **Website:** https://socradar.io
- **Database:** Extended Threat Intelligence (XTI) platform; dark web and deep web monitoring for credentials, PII, credit cards, stealer logs, underground forum discussions; free "Dark Web Report" tool for organizations (scans 15B+ breach records); also provides EASM (External Attack Surface Management), CTI, and Supply Chain Intelligence
- **Scale:** Free tool scans 15B+ breach records; Annual Dark Web Report 2025 tracked 1.6M+ email-password credentials and 75,000 credit card details exposed globally (sampled)
- **Access model:** Freemium — free Dark Web Report for orgs; paid enterprise platform; API; MSSP tiers; Maltego integration for OSINT workflows
- **Who uses it:** Enterprise security teams, SOC analysts, MSSPs, government agencies; Maltego users for OSINT pivot
- **Geopolitical:** Turkish company with US operations; Turkish cybersecurity industry is growing in NATO/allied context; publishes annual dark web reports covering global criminal underground including Russian-language forums
- **Notable:** Publishes one of the more comprehensive annual dark web monitoring reports (2024 and 2025 editions). Free tier makes it more accessible than most enterprise competitors. Provides country-specific and sector-specific threat intelligence on credential exposures.
- **Controversies:** Turkish origin raises some scrutiny from certain government clients; data residency questions for EU clients

---

## 26. CybelAngel [DONE]

- **Organization:** CybelAngel (private company; founded 2013; HQ Paris, France; offices in New York, London)
- **Website:** https://cybelangel.com
- **Database:** Digital risk protection and credential intelligence platform; continuously scans dark/deep web forums, marketplaces, Telegram/Discord channels, unprotected cloud databases (ElasticSearch, MongoDB, MySQL, PostgreSQL), paste sites; 11M+ posts/discussions monitored in 200+ languages
- **Scale:** 6 billion+ data points scanned daily; near real-time detection (within 24 hours of credential exposure)
- **Access model:** Enterprise paid SaaS; no public search; API integrations; French-market and international enterprise clients
- **Who uses it:** Large enterprises, financial institutions, luxury brands (French companies), government adjacent organizations; European enterprise market focus
- **Geopolitical:** French company; EU jurisdiction/GDPR compliance; EU AI Act considerations; provides intelligence on Russian-language dark web communities from a Western European vantage point; French government-friendly security posture (ANSSI ecosystem)
- **Notable:** Unique capability: scans unprotected cloud databases (open S3 buckets, exposed Elasticsearch, MongoDB) in addition to dark web sources — catches breaches at point of exposure before criminal indexing. Monitors 200+ languages including Arabic, Russian, Chinese — broader linguistic scope than most competitors. Publishes annual "Infostealer Logs" research.
- **Controversies:** Scale of passive monitoring of 11M+ forum posts raises ethical questions; French intelligence community adjacency

---

## 27. KELA Cyber Threat Intelligence [DONE]

- **Organization:** KELA (private company; founded 2015; HQ Tel Aviv, Israel)
- **Website:** https://www.kelacyber.com
- **Database:** Cybercrime underground intelligence platform; automated monitoring of dark web forums, marketplaces, encrypted communications channels; tracks credential theft, compromised accounts (including SaaS), ransomware activity, initial access broker listings, and infostealer data
- **Scale:** 2024: tracked 4.3M+ infected machines resulting in 330M+ compromised credentials; tracked 5,230+ ransomware victims
- **Access model:** Enterprise paid; API; Gartner-reviewed platform; no public search interface
- **Who uses it:** Enterprise security teams, government agencies, financial institutions, MSSPs; international clientele with strong European and US presence
- **Geopolitical:** Israeli company; similar IDF/Unit 8200 talent pipeline to Hudson Rock and other Israeli cyber firms; deep coverage of Russian-language cybercriminal underground; publishes State of Cybercrime annual reports
- **Notable:** "State of Cybercrime 2024" report (February 2025): 4.3M infected machines, 330M credentials, 5,230 ransomware victims; attackers forming alliances, leveraging AI, shifting monetization models. Strong focus on tracking Initial Access Broker (IAB) ecosystem — the criminal layer that sells network access to ransomware groups. Distinct positioning as "preventing cybercrime" rather than just monitoring.
- **Controversies:** Israeli company monitoring global criminal underground; geopolitical questions about data access and intelligence sharing with Israeli government entities

---

## 28. Leak-Lookup [DONE]

- **Organization:** Leak-Lookup (private; operator "GhostR" or team identity not fully disclosed; exact jurisdiction unclear)
- **Website:** https://leak-lookup.com
- **Database:** Breach data search engine; aggregates thousands of breach datasets; searchable by username, email, IP address
- **Scale:** Multi-billion record database; became notable for "Mother of All Breaches" (MOAB) incident January 2024; also involved in June 2026 exposure of 24B-record Elasticsearch database
- **Access model:** Subscription-based; API access; paid tiers for full results
- **Who uses it:** Security researchers, OSINT investigators, individuals checking exposure
- **Notable incidents:**
  - **January 2024 — "Mother of All Breaches" (MOAB):** 26 billion records exposed from Leak-Lookup's infrastructure; discovered by security researcher Bob Dyachenko and Cybernews; exposed records aggregated from 4,144 prior breaches including LinkedIn, Twitter, Weibo, Tencent; 12 terabytes of data; operator attributed to misconfigured server; largest individual data exposure ever identified at time
  - **June 2026:** Researchers uncovered a second publicly accessible Elasticsearch database containing 24 billion records (8.3TB) aggregated from 36 sources including Telegram channels, prior breach compilations, and infostealer logs
- **Controversies:** Two massive infrastructure misconfigurations exposed the operator's own aggregated database to the public; each event made the stolen data accessible to anyone rather than just paying customers; highlighted the security irony of breach aggregators suffering their own breaches

---

## 29. OSINTLeak [DONE]

- **Organization:** OSINTLeak (private; operator identity not prominently disclosed; Trace Labs supporter/partner)
- **Website:** https://osintleak.com
- **Database:** Breach intelligence and stealer log search platform; real-time search across breach databases, stealer logs, and leaked credentials; 15+ search selectors (email, username, IP, domain, phone, etc.); built-in results analyzer; AI reverse image search; IP intelligence; WHOIS; UserHunter (username tracking across 500+ platforms)
- **Scale:** Billions of records (specific count not prominently stated); growing continuously with new stealer log ingestion
- **Access model:** Subscription/account-based; API for programmatic access; used by security researchers and enterprise teams; Trace Labs partnership (OSINT for missing persons)
- **Who uses it:** Security researchers, bug bounty hunters, enterprise security teams, incident responders, OSINT investigators; Trace Labs community for legitimate missing persons investigations
- **Notable:** Broader than pure breach lookup — combines breach data with OSINT pivoting tools (image search, WHOIS, username tracking) in a single platform. Association with Trace Labs (legitimate missing persons OSINT) provides community legitimacy. 2024 context: 330M credentials stolen from 4.3M devices; 13.2B credentials from stealer logs alone.
- **Controversies:** Combination of stealer logs + OSINT tools in one platform creates high-capability dual-use risk; anonymous operator

---

## 30. National Public Data (Notable Breach/Data Broker) [DONE]

*Note: This is a data broker that suffered a catastrophic breach, not a breach database operator. Included because the breach affected all downstream breach databases and is geopolitically significant.*

- **Organization:** National Public Data (Jerico Pictures Inc., Coral Springs, Florida, USA; operated by Salvatore "Sal" Verini)
- **Website:** nationalpublicdata.com (defunct; company filed bankruptcy December 2024)
- **Database:** Background check data broker; aggregated public records including SSNs, full names, current/past addresses, dates of birth, phone numbers for US, UK, and Canadian individuals
- **Scale:** 2.9 billion records exposed in breach; 272 million unique SSNs (approximately 60% of all historical US SSNs ever issued); 2.69 billion lines / 277GB of data released by hacker "Fenice" on August 6, 2024
- **Breach timeline:**
  - December 2023: Initial unauthorized access gained
  - April 2024: Active exfiltration begins
  - April 2024: Hacker group "USDoD" offered 2.9B record database for $3.5M on BreachForums
  - August 6, 2024: Complete dataset released for free by "Fenice"
  - August 16, 2024: Company confirmed breach
  - December 2024: National Public Data filed for bankruptcy
- **Who is affected:** Nearly all US adults; individuals in UK and Canada also included
- **Downstream impact:** Data indexed by HIBP, Constella Intelligence, SpyCloud, and other breach databases; Constella published analysis verifying the breach; remains in breach lookup databases as of 2026
- **Notable:** Most significant SSN exposure in US history. 60% of all SSNs ever issued compromised. Unlike typical breach (one company's customers), this affected the general population. Post-breach, class action lawsuits filed before company dissolved.
- **Controversies:** Data brokers aggregating SSN databases represent systemic risk; company had no customer relationship with most people in its database; bankruptcy meant no remediation for victims; exposed the unregulated nature of US background-check data broker industry

---

## 31. Cyble [DONE]

- **Organization:** Cyble Inc. (private company; founded 2019; HQ Alpharetta, Georgia, USA; R&D center in India; offices in Singapore, UK, UAE, Australia)
- **Website:** https://cyble.com
- **Database:** AI-native threat intelligence platform ("Cyble Vision"); dark web and deep web monitoring for credentials, PII, stealer logs, ransomware leaks, brand abuse; strong coverage of Indian subcontinent threat landscape alongside global monitoring
- **Scale:** 2025: tracked 6,046 global data breach and leak incidents; extensive stealer log coverage; Indian enterprise credential exposure a specialty research area
- **Access model:** Enterprise paid SaaS; API; free community tools available; MSSP distribution; Gartner-reviewed (Gartner Peer Insights listed)
- **Who uses it:** Enterprises (particularly Indian and Asia-Pacific organizations), financial institutions, government agencies, MSSPs; international clientele
- **Geopolitical:** US-incorporated with strong India operations; covers dark web credential threats to Indian enterprises (35% YoY increase in cyberattacks per Cyble 2024 report); positioned as bridge between Western threat intelligence industry and Indian/APAC cybersecurity market; tracks Chinese and Russian-language criminal infrastructure
- **Notable:** One of the most active publishers of dark web threat research for Indian enterprise context. 2024 research: cyberattacks on Indian enterprises up 35% YoY; ransomware +45%; phishing +30%; dark web leaks involving Indian entities +50%. Also covers general global threat intelligence with strong infostealer and ransomware tracking.
- **Controversies:** Rapid growth with India R&D center raises questions about data handling under Indian data protection law (DPDP Act 2023); US incorporation with India operations creates complex jurisdictional profile

---

## 32. ZeroFox [DONE]

- **Organization:** ZeroFox (public company, NASDAQ: ZFOX; founded 2013; HQ Baltimore, Maryland, USA)
- **Website:** https://www.zerofox.com
- **Database:** External cybersecurity platform with dark web intelligence module; monitors TOR, I2P, ZeroNet, Telegram, Discord, paste sites, criminal forums for leaked credentials, PII, sensitive data; 12B+ total data points in Intelligence Evidence Graph; uses human operatives ("Dark Ops") alongside AI for collection
- **Scale:** 12B+ total data points in Intelligence Evidence Graph; monitoring across TOR, I2P, ZeroNet, Telegram, Discord, paste sites and criminal forums
- **Access model:** Enterprise paid; public company; API integrations; includes compromised credential monitoring, dark web risk management, digital risk protection as product lines
- **Who uses it:** Enterprise security teams, financial institutions, government agencies; US-market focused
- **Geopolitical:** US public company; public market accountability; US government/defense sector clients; uses human "Dark Ops" operatives in addition to automated collection — raises questions about covert activities in criminal forums
- **Notable:** One of the few publicly traded companies (NASDAQ) in the breach intelligence/digital risk protection space, providing more financial transparency than private competitors. "Dark Ops" human operatives distinguish it from purely automated competitors. Maintains "persistent access" to criminal forums through covert means.
- **Controversies:** Human operatives maintaining persistent access in criminal forums raises legal and ethical questions about entrapment boundaries; public company status means investor pressure may influence threat intelligence business decisions

---

## 33. Group-IB [DONE]

- **Organization:** Group-IB (private company; founded 2003 in Moscow, Russia; redomiciled to Singapore 2019; HQ currently Singapore; Global Digital Crime Resistance Centers in Singapore, Amsterdam, Dubai, Tashkent, Phuket, Hanoi, Santiago)
- **Website:** https://www.group-ib.com
- **Database:** Unified Risk Platform — threat intelligence including dark web and deep web monitoring, credential theft tracking, compromised account detection, combolist analysis, initial access broker tracking, ransomware ecosystem intelligence; industry's claimed "largest library of dark web data sources"
- **Scale:** Unspecified but described as industry-leading; monitors dark web forums, marketplaces, Telegram channels, paste sites; historical archive
- **Access model:** Enterprise paid; API; government/LEA partnerships; global MSSP distribution; no public search interface
- **Who uses it:** Enterprises, financial institutions, law enforcement agencies (Interpol, Europol, national agencies), government cybersecurity bodies; strong LEA relationships through cybercrime investigation history
- **Geopolitical:** Highly significant geopolitical profile. Founded in Moscow; co-founder Ilya Sachkov arrested by Russian FSB in September 2021 on treason charges (accused of sharing intelligence with foreign services); sentenced to 18 years in Russian prison. Company subsequently divested all Russian operations in 2023, with Sachkov relinquishing 37.5% stake and Volkov selling 10%. Now operates fully from Singapore. Russian government relations: antagonistic. Western government relationships: cooperative. Cyber Security Agency of Singapore supported relocation.
- **Notable:** One of the most historically significant cybercrime investigation firms globally — responsible for numerous major criminal takedowns in cooperation with Interpol and Europol. Sachkov arrest widely interpreted as politically motivated (he exposed FSB officers' involvement in cybercrime). Transition from Russian to Singaporean base represents major geopolitical inflection point. Continues to publish widely-cited threat intelligence research.
- **Controversies:** Sachkov case is the defining controversy — FSB treason charges against company's own founder; whether company's data was shared with Western intelligence (as Russia alleged) vs. whether prosecution was political retaliation for exposing corrupt FSB officers (Western interpretation); Russian divestment did not immediately resolve trust questions with some Western clients

---

## 34. Cybersixgill (now part of Bitsight) [DONE]

- **Organization:** Cybersixgill (founded 2014, Tel Aviv, Israel; acquired by Bitsight, November 2024; Bitsight HQ Boston, Massachusetts, USA)
- **Website:** https://www.bitsight.com/cybersixgill (formerly cybersixgill.com)
- **Database:** Underground intelligence platform; automated collection from dark web forums, invite-only messaging groups, code repositories, paste sites, underground markets, and clear web; historical archive from as early as the 1990s; 10 million intelligence items collected and analyzed daily; creates behavioral profiles and patterns of dark web users/threat actors
- **Scale:** 10M intelligence items collected daily; multi-decade historical archive; tracks credit card markets, stealers, access brokers, ransomware groups
- **Access model:** Enterprise paid; API integrations; ThreatConnect marketplace integration; Bitsight platform integration post-acquisition
- **Who uses it:** Enterprise security teams, financial institutions, government agencies, MSSPs; global clientele; post-acquisition, accessible through Bitsight's security ratings customer base
- **Geopolitical:** Israeli origin (IDF talent pipeline); acquired by US company (Bitsight); creates US-Israeli combined entity with deep underground intelligence capabilities; 2024 acquisition by Bitsight marks consolidation of underground intelligence market
- **Notable:** Distinguished by behavioral profiling of dark web users (not just content collection) — tracks threat actor identity and patterns across forums. March 2024 Bitsight announced acquisition for undisclosed sum. Post-acquisition, Bitsight launched "Identity Intelligence Solution" (April 2025) to detect credential-based threats using Cybersixgill's data. Research finding: underground credit card markets rebounded 25% in 2023 to 12M cards; four new stealer malware families emerged at scale in 2023 (Stealc, Risepro, Lumma, Silencer).
- **Controversies:** Behavioral profiling of dark web users by a private company raises questions about scope (defenders vs. law enforcement role); Israeli intelligence community adjacency; post-acquisition integration means Cybersixgill data now flows through US corporate structure

---

## 35. ImmuniWeb [DONE]

- **Organization:** ImmuniWeb SA (private company; founded 2019 from High-Tech Bridge; HQ Geneva, Switzerland)
- **Website:** https://www.immuniweb.com
- **Database:** Dark Web Monitoring module within broader Application Security and CTEM (Continuous Threat Exposure Management) platform; monitors 20B+ stolen credentials, 10M+ malicious domains, 250+ threat intelligence feeds, 50+ law enforcement feeds; crawls millions of new dark web files/entries daily; monitors phishing campaigns, domain squatting, fake social media, malicious mobile apps alongside credential exposure
- **Scale:** 20B+ stolen credentials monitored; 250+ threat intelligence feeds; 50+ law enforcement feeds
- **Access model:** Enterprise paid SaaS; free "Dark Web Exposure Test" (enter company domain for basic exposure report); API; Cybersecurity Excellence Awards 2024 finalist for ImmuniWeb Discovery dark web monitoring
- **Who uses it:** Enterprise security teams, compliance teams, organizations needing GDPR/regulatory compliance awareness of credential exposures; European market focus
- **Geopolitical:** Swiss company; EU/Swiss privacy law jurisdiction; operates in compliance-friendly legal environment; GDPR-aware design; serves European enterprise market with sensitivity to data protection regulation
- **Notable:** Swiss jurisdiction provides strong legal protections for legitimate threat intelligence operations. Combination of app security (web/mobile testing) with dark web monitoring in single platform is unusual. 50+ law enforcement feeds integration means access to LEA-shared breach data alongside criminal underground data. Free exposure test tool lowers barrier for SMB awareness.
- **Controversies:** 20B+ credential claim requires verification; Swiss jurisdiction not immune from US/EU data requests; dual-use of held credential data

---

## 36. ProxyNova COMB Search [DONE]

- **Organization:** ProxyNova (private; operator identity not prominently disclosed)
- **Website:** https://www.proxynova.com/tools/comb/
- **Database:** Free public search tool for the "Compilation of Many Breaches" (COMB) dataset; COMB was a 2021 compilation of 3.2B+ credentials aggregated from multiple prior breaches (Netflix, LinkedIn, and hundreds of others); ProxyNova makes this searchable by email/username/password; also offers password uniqueness check tool
- **Scale:** 3.2B+ credentials from the COMB dataset (2021 compilation)
- **Access model:** Free, no registration required; web-based search; provides uncensored results including plaintext passwords
- **Who uses it:** Individuals checking personal exposure; attackers validating credential lists; OSINT researchers; security teams; anyone — no access controls
- **Geopolitical:** Unknown operator/jurisdiction; no apparent legal controls on access
- **Notable:** One of the most permissive breach search tools available — free, no registration, shows plaintext passwords immediately. COMB dataset originated from a February 2021 leak on RaidForums. ProxyNova was not the source of the breach but makes the data permanently accessible. Widely referenced in OSINT tool lists (OH SHINT, s0cm0nkey reference guide, etc.).
- **Controversies:** Maximum permissiveness — free, anonymous, no controls, plaintext passwords visible — makes it the most attacker-friendly service in this document; no operator accountability; permanently preserves 2021 COMB data

---

## 37. Telegram Combolist Channels (Distribution Channel) [DONE]

*Note: Telegram itself is a messaging platform, not a breach database operator. However, Telegram channels have become one of the primary distribution channels for stolen credentials, functioning as a de facto dark web alternative accessible via clearnet.*

- **Organization:** Anonymous cybercriminals operating individual Telegram channels; thousands of channels globally
- **Platform:** Telegram (Telegram FZ-LLC, Dubai, UAE)
- **Database:** Distributed; no central database — individual channels post stealer logs, combolists (email:password pairs), breach dumps, infostealer output; channels rotate names frequently to evade moderation
- **Scale:** June 2024: researcher shared 122GB scraped from thousands of Telegram cybercrime channels with Troy Hunt — contained 361M unique email addresses; Q1-Q3 2025: 13.6B email:password pairs identified from stealer logs distributed via Telegram; 29.7B passwords total associated with those emails
- **Access model:** Free (for recipients); channels accessible via Telegram app (clearnet, no Tor required); operators may charge for premium/fresh logs in private channels
- **Who uses it:** Cybercriminals, credential stuffers, fraud actors; also monitored by threat intelligence firms (Flare monitors 58,000+ Telegram channels; SOCRadar tracks stealer log channels; Searchlight Cyber monitors)
- **Geopolitical:** Telegram's Dubai-based registration and Pavel Durov's legal status (arrested in France August 2024, released on bail; investigations by French authorities into Telegram's moderation failures) make it a major geopolitical flashpoint for credential distribution; Russian-language channels dominant; French legal pressure on Durov has affected Telegram's moderation stance
- **Notable:** Telegram has supplanted traditional dark web forums for many credential distribution use cases because it's accessible via clearnet, has mobile apps, requires no technical setup, and posts are searchable. Password-to-email ratio in leaked Telegram data jumped from 1.39 (2024) to 2.18 (2025) — reflecting growing stealer log volume (multiple passwords per device). HIBP added "Combolists Posted to Telegram" as a named breach dataset. Despite increased moderation post-Durov arrest, channels persist by rotating names and using backup/mirror groups.
- **Controversies:** Telegram's reluctance to moderate criminal channels until French legal pressure; Durov arrest (August 2024) as geopolitical event; debate over whether clearnet access to stealer logs represents a qualitative shift in criminal accessibility of stolen credentials

---

## APPENDIX: Summary Statistics and Scale Reference

| Service | Scale | Type | Access | Origin |
|---|---|---|---|---|
| HIBP | 12B+ records, 2B unique emails | Breach notification | Free/API | Australia (Troy Hunt) |
| DeHashed | Billions | Search engine | Paid | USA |
| SpyCloud | 36B+ credentials | Enterprise TI | Paid/Enterprise | USA |
| LeakCheck | 10B+ records | Search engine | Free/Paid | Eastern European |
| Snusbase | Unlisted | Search engine | Paid | Unknown |
| IntelligenceX | 200B+ records | Archive/search | Freemium | Czech Republic |
| BreachDirectory | Unlisted | Search engine | Freemium/API | Anonymous |
| Constella | 45B curated records, 100B+ attributes | Enterprise TI | B2B only | USA |
| Recorded Future | 1M+ sources | Enterprise TI | B2B only | USA (Mastercard) |
| Hudson Rock / Cavalier | 30M+ compromised computers | Infostealer TI | Paid/Enterprise | Israel |
| RaidForums/BreachForums | ~500K users (forums); thousands of breach datasets | Criminal forum (seized) | Dark web | Portugal/USA/Intl |
| WeLeakInfo | 12.4B records, 10,368 databases | Criminal marketplace (seized) | Paid (seized) | Netherlands/N.Ireland |
| Ghost Project | 15B+ records, 7,200 breaches | Search engine | Free (status unclear) | Anonymous (.fr) |
| Scattered Secrets | ~4B plaintext passwords | Breach notification + cracking | Free personal/Paid B2B | Netherlands |
| Genesis Market | 80M credentials, 460K bot packages | Criminal marketplace (seized) | Dark web (seized) | Unknown (Russian-speaking) |
| Russian Market | ~30K bots/month | Criminal marketplace | Dark web | Russian-speaking |
| 2easy.shop | High volume | Criminal marketplace | Dark web | Eastern European |
| Flashpoint | 3.2B+ 2024 events tracked | Enterprise TI | Paid/Enterprise | USA |
| Flare Systems | 20B+ credentials | Enterprise TI | Paid/Enterprise | Canada |
| Breachsense | Unlisted | Enterprise TI | Paid/SaaS | USA |
| XposedOrNot | 740+ breaches | Search engine | Free/Open-source | Unknown |
| Privacy Rights Clearinghouse | 96K+ notifications (2005–present) | Academic/nonprofit | Free/Academic | USA (nonprofit) |
| LeakRadar | 497B+ plain text credentials | Search engine | Unlock-based | Unknown |
| psbdmp | Millions of pastes | Paste archive | Free/API | Anonymous |
| SOCRadar | 15B+ records (free tool) | Enterprise TI | Freemium | Turkey |
| CybelAngel | 6B+ data points/day | Enterprise TI | Paid/Enterprise | France |
| KELA | 4.3M machines, 330M creds (2024) | Enterprise TI | Paid/Enterprise | Israel |
| Leak-Lookup | 26B records (MOAB, Jan 2024) | Search engine | Paid | Unknown |
| OSINTLeak | Billions (unspecified) | OSINT/search engine | Paid/API | Unknown |
| National Public Data | 2.9B records, 272M SSNs (breached) | Data broker (bankrupt) | N/A — victim organization | USA |
| Cyble | 6,046 incidents tracked (2025) | Enterprise TI | Paid/Enterprise | USA/India |
| ZeroFox | 12B+ data points | Enterprise TI (public co.) | Paid/Enterprise | USA (NASDAQ) |
| Group-IB | Largest dark web library (claimed) | Enterprise TI | Paid/Enterprise | Singapore (ex-Russia) |
| Cybersixgill/Bitsight | 10M items/day | Enterprise TI | Paid/Enterprise | Israel/USA |
| ImmuniWeb | 20B+ stolen creds monitored | Enterprise TI | Freemium | Switzerland |
| ProxyNova COMB | 3.2B credentials | Free public search | Free/No controls | Unknown |
| Telegram channels | 13.6B+ email:pass pairs (2025) | Criminal distribution | Free/Dark | Global (Dubai HQ) |
| Webz.io / Lunar | Massive open/deep/dark web archive | Enterprise TI/API | Paid/API | Israel |

---

## 38. Webz.io / Lunar [DONE]

- **Organization:** Webz.io (private company; founded 2011; HQ Tel Aviv, Israel; offices in New York)
- **Website:** https://webz.io / https://webz.io/products/lunar/
- **Database:** Two relevant products: (1) **Data Breach Detection API** — real-time access to structured infostealer logs, public/private breaches, combo lists (URL:username:password), and cookie data; updated continuously from underground forums, Telegram channels, stealer sources; (2) **Lunar** — SaaS dark web intelligence engine converting Webz.io's open/deep/dark web archive into operational stolen-credential prevention (monitors privileged credentials, PII, threats in real time)
- **Scale:** Webz.io maintains one of the largest commercial open/deep/dark web data collections; specific credential count not prominently disclosed; continuously updated
- **Access model:** B2B API-first; Data Breach Detection API for enterprise integration; Lunar as SaaS for operational prevention; no public consumer lookup; pricing not publicly listed
- **Who uses it:** Enterprises integrating breach intelligence into authentication flows (login fraud prevention); cybersecurity platforms embedding breach data via API; threat intelligence teams; one of the services highlighted alongside ImmuniWeb and Mandiant in dark web monitoring comparisons
- **Geopolitical:** Israeli company; US office; data collection spans global underground forums including Russian-language criminal communities; Israeli intelligence/cyber industry proximity
- **Notable:** Distinct positioning: rather than just alerting on breaches, Lunar is designed to *prevent stolen credentials from logging in* — real-time integration with authentication systems. API provides structured data fields: URL, username, password, cookie name/value/expiration — enabling precise login fraud prevention integration. Publishes "Dark Web Pulse" research archive with reports on top malware types and leak sites.
- **Controversies:** Holding real-time cookie/session token data creates same liability questions as SpyCloud and Breachsense; Israeli company with US operations subject to complex data governance questions

---
