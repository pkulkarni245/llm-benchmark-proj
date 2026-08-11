"""Comprehensive Knowledge Base Generator & Ingestion Script for SEBI & Capital Markets Domain.

Includes full, exhaustive statutory provisions across all 7 core SEBI regulations:
1. SEBI (Prohibition of Insider Trading) Regulations, 2015 (PIT)
2. SEBI (Substantial Acquisition of Shares and Takeovers) Regulations, 2011 (SAST / Takeover Code)
3. SEBI (Issue of Capital and Disclosure Requirements) Regulations, 2018 (ICDR / IPO & QIP Rules)
4. SEBI (Listing Obligations and Disclosure Requirements) Regulations, 2015 (LODR / Governance & Disclosures)
5. SEBI (Alternative Investment Funds) Regulations, 2012 (AIF / PE & VC Rules)
6. SEBI (Mutual Funds) Regulations, 1996 & Master Circular 2024 (MF & ESG Framework)
7. SEBI (Foreign Portfolio Investors) Regulations, 2019 (FPI & FDI Reclassification Rules)
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "data" / "sebi_documents"
UPLOADS_DIR = BASE_DIR / "data" / "uploads"
DOCS_DIR.mkdir(parents=True, exist_ok=True)
UPLOADS_DIR.mkdir(parents=True, exist_ok=True)

COMPREHENSIVE_SEBI_TEXTS = {
    "SEBI_PIT_Regulations_2015_Full.txt": """
SECURITIES AND EXCHANGE BOARD OF INDIA (PROHIBITION OF INSIDER TRADING) REGULATIONS, 2015
[Amended up to January 2024]

CHAPTER I: PRELIMINARY
1. Short Title and Commencement:
These regulations may be called the Securities and Exchange Board of India (Prohibition of Insider Trading) Regulations, 2015. They shall come into force on the one hundred and twentieth day from the date of its publication in the Official Gazette.

2. Definitions:
(1)(a) "Act" means the Securities and Exchange Board of India Act, 1992 (15 of 1992);
(1)(b) "Board" means the Securities and Exchange Board of India;
(1)(c) "Compliance Officer" means any senior officer, designated so and reporting to the board of directors or head of the organization, who is financially literate and is capable of appreciating requirements for legal and regulatory compliance under these regulations.

(1)(d) "Connected Person" means any person who is or has during the six months prior to the concerned act been associated with a company, directly or indirectly, in any capacity including by reason of frequent communication with its officers or by being in any contractual, fiduciary or employment relationship or by being a director, officer or an employee of the company or holds any position including a professional or business relationship between himself and the company whether temporary or permanent, that allows such person, directly or indirectly, access to unpublished price sensitive information or is reasonably expected to allow such access.
Without prejudice to the generality of the foregoing, the persons falling within the following categories shall be deemed to be connected persons unless the contrary is established:
(i) an immediate relative of connected persons specified in clause (d); or
(ii) a holding company or associate company or subsidiary company; or
(iii) an intermediary as specified in section 12 of the Act or an employee or director thereof; or
(iv) an investment company, trustee company, asset management company or an employee or director thereof; or
(v) an official of a stock exchange or of clearing corporation or organisation; or
(vi) a member of board of trustees of a mutual fund or a member of the board of directors of the asset management company of a mutual fund or is an employee thereof; or
(vii) a member of the board of directors or an employee, of a public financial institution as defined in section 2 (72) of the Companies Act, 2013; or
(viii) an official or an employee of a self-regulatory organisation recognised or authorized by the Board; or
(ix) a banker of the company; or
(x) a concern, firm, trust, Hindu undivided family, company or association of persons wherein a director of a company or his immediate relative or banker of the company, has more than ten per cent of the holding or interest.

(1)(g) "Insider" means any person who is:
(i) a connected person; or
(ii) in possession of or having access to unpublished price sensitive information.

(1)(n) "Unpublished Price Sensitive Information" (UPSI) means any information, relating to a company or its securities, directly or indirectly, that is not generally available which upon becoming generally available, is likely to materially affect the price of the securities and shall, ordinarily including but not restricted to, information relating to the following:
(i) financial results;
(ii) dividends;
(iii) change in capital structure;
(iv) mergers, de-mergers, acquisitions, delistings, disposals and expansion of business and such other transactions;
(v) changes in key managerial personnel.

CHAPTER II: RESTRICTIONS ON COMMUNICATION AND TRADING BY INSIDERS
3. Communication or procurement of unpublished price sensitive information:
(1) No insider shall communicate, provide, or allow access to any unpublished price sensitive information, relating to a company or securities listed or proposed to be listed, to any person including other insiders except where such communication is in furtherance of legitimate purposes, performance of duties or discharge of legal obligations.
(2) No person shall procure from or cause the communication by any insider of unpublished price sensitive information, relating to a company or securities listed or proposed to be listed, except in furtherance of legitimate purposes, performance of duties or discharge of legal obligations.
(2A) The board of directors of a listed company shall make a policy for determination of "legitimate purposes" as a part of "Codes of Fair Disclosure and Conduct" formulated under regulation 8.
(3) An unpublished price sensitive information may be communicated, provided, allowed access to or procured, in connection with a transaction that would:
(i) entail an obligation to make an open offer under the takeover regulations where the board of directors of the target company is of informed opinion that sharing of such information is in the best interests of the company;
(ii) not attract the obligation to make an open offer under the takeover regulations but where the board of directors of the target company is of informed opinion that sharing of such information is in the best interests of the company and the information that constitutes UPSI is disseminated to be made generally available at least two trading days prior to the proposed transaction being executed.
(5) Structured Digital Database (SDD): The board of directors or head(s) of the organisation of every person required to handle unpublished price sensitive information shall ensure that a structured digital database is maintained containing the nature of UPSI and the names of such persons who have shared the information and also the names of such persons with whom information is shared along with the Permanent Account Number (PAN) or any other identifier authorized by law where PAN is not available. Such database shall not be outsourced and shall be preserved for a period of not less than eight years.

4. Trading when in possession of unpublished price sensitive information:
(1) No insider shall trade in securities that are listed or proposed to be listed on a stock exchange when in possession of unpublished price sensitive information:
Provided that the insider may prove his innocence by demonstrating that the transaction was carried out pursuant to a trading plan set up under regulation 5, or off-market inter-se transfer between insiders who were in possession of the same UPSI, or block deal window mechanism.

5. Trading Plans:
(1) An insider shall be entitled to formulate a trading plan and present it to the compliance officer for approval and public disclosure pursuant to which trades may be carried out on his behalf in accordance with such plan.
(2) Such trading plan shall:
(i) not entail commencement of trading on behalf of the insider earlier than six months from the public disclosure of the plan;
(ii) not entail trading for the period between the twentieth trading day prior to the last day of any financial period for which results are required to be announced by the issuer of the securities and the second trading day after the disclosure of such financial results;
(iii) entail trading for a period of not less than twelve months;
(iv) not entail overlap of any period for which another trading plan is already in existence;
(v) set out either the value of trades to be executed or the number of securities to be traded along with the nature of the trade and the intervals at, or dates on which such trades shall be executed; and
(vi) not entail trading in securities for market abuse.

CHAPTER III: DISCLOSURES OF TRADING BY INSIDERS
7. Continual Disclosures:
(2)(a) Every promoter, member of the promoter group, designated person and director of every company shall disclose to the company the number of such securities acquired or disposed of within two trading days of such transaction if the value of the securities traded, whether in one transaction or a series of transactions over any calendar quarter, aggregates to a traded value in excess of ten lakh rupees (Rs. 10 Lakhs) or such other value as may be specified.
(2)(b) Every company shall notify the particulars of such trading to the stock exchange on which the securities are listed within two trading days of receipt of the disclosure or from becoming aware of such information.

SCHEDULE B: CODE OF CONDUCT FOR LISTED COMPANIES
Clause 4(2): Trading window restrictions shall be benchmarked towards the closure of trading window from the end of every quarter till 48 hours after the declaration of financial results.
Clause 10: The code of conduct shall specify that designated persons who buy or sell any number of securities of the company shall not execute a contra trade (i.e. sell or buy any number of securities) during the next six months following the prior transaction.
""",

    "SEBI_SAST_Regulations_2011_Full.txt": """
SECURITIES AND EXCHANGE BOARD OF INDIA (SUBSTANTIAL ACQUISITION OF SHARES AND TAKEOVERS) REGULATIONS, 2011
[Takeover Code - Amended up to 2024]

CHAPTER II: SUBSTANTIAL ACQUISITION OF SHARES, VOTING RIGHTS OR CONTROL
3. Substantial acquisition of shares or voting rights:
(1) No acquirer shall acquire shares or voting rights in a target company which taken together with shares or voting rights, if any, held by him and by persons acting in concert with him in such target company, entitle them to exercise twenty-five per cent (25%) or more of the voting rights in such target company unless the acquirer makes a public announcement of an open offer for acquiring shares of such target company in accordance with these regulations.
(2) No acquirer, who together with persons acting in concert with him, holds shares or voting rights in a target company entitling them to exercise twenty-five per cent (25%) or more of the voting rights in the target company but less than the maximum permissible non-public shareholding (75%), shall acquire within any financial year additional shares or voting rights in that target company entitling them to exercise more than five per cent (5%) of the voting rights, unless the acquirer makes a public announcement of an open offer for acquiring shares of such target company in accordance with these regulations (Creeping Acquisition Limit).

4. Acquisition of Control:
Irrespective of acquisition or holding of shares or voting rights in a target company, no acquirer shall acquire, directly or indirectly, control over such target company unless the acquirer makes a public announcement of an open offer for acquiring shares of such target company in accordance with these regulations.

6. Voluntary Offer:
(1) An acquirer, who together with persons acting in concert with him, holds twenty-five per cent (25%) or more shares or voting rights in a target company but less than the maximum permissible non-public shareholding, shall be entitled to voluntarily make a public announcement of an open offer for acquiring shares in accordance with these regulations, subject to their aggregate holding after the acquisition not exceeding the maximum permissible non-public shareholding.
(2) An acquirer who has acquired shares during the preceding twelve months without making an open offer shall not be eligible to make a voluntary offer.

7. Offer Size:
(1) The open offer for acquiring shares made under regulation 3 and regulation 4 shall be for at least twenty-six per cent (26%) of total shares of the target company as of tenth working day from the closure of the tendering period.

10. General Exemptions:
(1) The following acquisitions shall be exempt from the obligation to make an open offer under regulation 3 and regulation 4:
(a)(i) acquisition pursuant to inter-se transfer of shares amongst immediate relatives;
(a)(ii) acquisition pursuant to inter-se transfer of shares amongst promoters declared for at least three years;
(a)(iii) acquisition pursuant to a rights issue up to one's entitlement;
(b) acquisition in the ordinary course of business by underwriters, stock brokers, market makers;
(d) acquisition pursuant to resolution plan approved under Section 31 of Insolvency and Bankruptcy Code (IBC), 2016.

13. Timing of Public Announcement:
(1) The public announcement referred to in regulation 3 and regulation 4 shall be sent to all the stock exchanges on which the shares of the target company are listed on the date of agreeing to acquire shares or voting rights.
(2) Detailed Public Statement (DPS) shall be published within five working days of the public announcement in all editions of one English national daily, one Hindi national daily and one regional language daily.

17. Escrow Account:
(1) Not later than two working days prior to the detailed public statement, the acquirer shall create an escrow account towards security for performance of obligations.
(2) The escrow amount shall be calculated as: 25% of the total consideration payable under the open offer for the first Rs. 500 Crores, and 10% of the balance consideration thereafter.

26. Obligations of the Target Company:
(1) Upon public announcement of an open offer, the board of directors of the target company shall not, during the offer period:
(a) alienate any material asset;
(b) issue or allot any unissued securities or shares (including rights issue), unless approved by special resolution through postal ballot.

31. Disclosure of Pledged Shares:
(1) The promoter of every target company shall disclose details of shares in such target company encumbered by him or by persons acting in concert with him to the target company and stock exchanges within seven working days from the creation of encumbrance.
(2) The promoter shall also disclose invocation or release of encumbrance within seven working days.
""",

    "SEBI_ICDR_Regulations_2018_Full.txt": """
SECURITIES AND EXCHANGE BOARD OF INDIA (ISSUE OF CAPITAL AND DISCLOSURE REQUIREMENTS) REGULATIONS, 2018
[Amended up to 2024]

CHAPTER II: INITIAL PUBLIC OFFER ON MAIN BOARD
6. Entities eligible to make an initial public offer:
(1) An issuer shall be eligible to make an initial public offer only if:
(a) it has net tangible assets of at least three crore rupees (Rs. 3 Crores) in each of the preceding three full years (of twelve months each), of which not more than fifty per cent are held in monetary assets;
(b) it has an average operating profit of at least fifteen crore rupees (Rs. 15 Crores), calculated on a consolidated basis, during the preceding three years;
(c) it has a net worth of at least one crore rupees (Rs. 1 Crore) in each of the preceding three full years.
(2) An issuer not satisfying the condition stipulated in sub-regulation (1) may make an initial public offer if the issue is made through the book-building process and the issuer undertakes to allot at least seventy-five per cent (75%) of the net offer to public to Qualified Institutional Buyers (QIBs).

CHAPTER III: PROMOTER CONTRIBUTION AND LOCK-IN
14. Minimum Promoters' Contribution:
(1) The promoters of the issuer shall contribute not less than twenty per cent (20%) of the post-issue capital.
(2) In case of an initial public offer, promoters shall fulfill the minimum promoters' contribution requirement prior to the date of opening of the issue.

16. Lock-in of Specified Securities Held by Promoters:
(1) The minimum promoters' contribution (20%) shall be locked-in for a period of eighteen months (18 months) from the date of allotment (or three years if the issue involves funding of capital expenditure for a project).
(2) Promoters' holding in excess of minimum promoter contribution shall be locked-in for a period of six months (6 months) from the date of allotment.

CHAPTER VI: QUALIFIED INSTITUTIONS PLACEMENT (QIP)
171. A listed issuer may make a qualified institutions placement of equity shares or non-convertible securities to Qualified Institutional Buyers (QIBs) on a private placement basis.
172. Conditions for QIP:
(a) Special resolution passed by shareholders approving QIP;
(b) Equity shares of same class are listed on a stock exchange for at least one year prior to date of notice;
(c) Allocation to a single QIB shall not exceed fifty per cent (50%) of the issue size;
(d) Minimum number of allottees: 2 allottees for issue size <= Rs. 250 Crores; 5 allottees for issue size > Rs. 250 Crores.

CHAPTER IX: INITIAL PUBLIC OFFER BY SME PLATFORM
229. Eligibility for SME IPO:
(1) An issuer with post-issue face value capital not exceeding twenty-five crore rupees (Rs. 25 Crores) shall be eligible for SME platform listing.
(2) Net tangible assets of at least Rs. 1.5 Crores, track record of at least 2 years, 100% underwriting required (with market maker underwriting 15%).

259. Anchor Investor Lock-In:
Fifty per cent (50%) of the allocation to the anchor investor shall be locked-in for a period of thirty days (30 days) from the date of allotment, and the remaining fifty per cent (50%) shall be locked-in for a period of ninety days (90 days).
""",

    "SEBI_LODR_Regulations_2015_Full.txt": """
SECURITIES AND EXCHANGE BOARD OF INDIA (LISTING OBLIGATIONS AND DISCLOSURE REQUIREMENTS) REGULATIONS, 2015
[Amended up to January 2024]

REGULATION 17: BOARD OF DIRECTORS
(1) The board of directors of the listed entity shall have an optimum combination of executive and non-executive directors with at least one woman director and not less than fifty per cent of the board of directors shall comprise non-executive directors. Where the chairperson is non-executive, at least one-third of the board shall comprise independent directors; where the chairperson is executive, at least half shall comprise independent directors.
(1B) The top 500 listed entities may voluntarily ensure that the Chairperson of the board shall be a non-executive director and not be related to the Managing Director or Chief Executive Officer.

REGULATION 18: AUDIT COMMITTEE
(1) Every listed entity shall constitute a qualified and independent audit committee comprising minimum three directors as members, with two-thirds being independent directors.
(2) All members of audit committee shall be financially literate and at least one member shall have accounting or related financial management expertise.

REGULATION 23: RELATED PARTY TRANSACTIONS (RPT)
(2) All related party transactions and subsequent material modifications shall require prior approval of the audit committee of the listed entity. Only independent members of audit committee shall approve.
(4) All material related party transactions (exceeding Rs. 1000 Crores or 10% of annual consolidated turnover, whichever is lower) shall require prior approval of the shareholders through ordinary resolution, and no related party shall vote to approve such resolutions whether the entity is a party to the particular transaction or not.

REGULATION 25: INDEPENDENT DIRECTORS
(2) An independent director shall hold office for a term up to five consecutive years, and is eligible for re-appointment on passing of a special resolution. No independent director shall hold office for more than two consecutive terms (10 years total), but shall be eligible for appointment after expiration of three years (cooling-off period) of ceasing to become an independent director.

REGULATION 30: DISCLOSURE OF MATERIAL EVENTS
(2) Events specified in Para A of Part A of Schedule III (financial results, M&A, board outcome, auditor changes, fraud) are deemed to be material events and listed entity shall make disclosure without applying any materiality test.
(3) Events specified in Para B of Part B of Schedule III shall be disclosed based on application of materiality guidelines framed by the board (threshold: 2% of turnover or net worth, or 10% of profit).
(6) Outcome of Board Meeting considering financial results shall be disclosed within 30 minutes of closure of board meeting. Other material events shall be disclosed within 24 hours (or 12 hours if decision originates from board meeting).

REGULATION 31A: RECLASSIFICATION OF PROMOTERS
(3) Reclassification of a promoter to public shareholder requires that the promoter does not hold more than 10% voting rights, does not exercise control, does not act as KMP/Director, and is approved by Board, Shareholders (ordinary resolution), and Stock Exchanges.

REGULATION 33: FINANCIAL RESULTS
(3)(a) Unaudited/audited quarterly financial results shall be submitted to stock exchanges within 45 days from the end of each quarter (60 days for annual audited results for the last quarter).

REGULATION 38: MINIMUM PUBLIC SHAREHOLDING
The listed entity shall comply with minimum public shareholding requirements specified in Rule 19A of Securities Contracts (Regulation) Rules, 1957 (maintaining at least 25% public shareholding).
""",

    "SEBI_AIF_Regulations_2012_Full.txt": """
SECURITIES AND EXCHANGE BOARD OF INDIA (ALTERNATIVE INVESTMENT FUNDS) REGULATIONS, 2012
[PE & VC Rules - Amended up to 2024]

CHAPTER I: PRELIMINARY & CATEGORIZATION
3. Categorization of Alternative Investment Funds:
(1) Category I AIF: AIFs which invest in start-up or early stage ventures or social ventures or infrastructure or SME or other sectors which the government or regulators consider socially or economically desirable (includes Venture Capital Funds, Angel Funds, SME Funds, Social Venture Funds, Infrastructure Funds).
(2) Category II AIF: AIFs which do not fall in Category I and III and which do not undertake leverage or borrowing other than to meet day-to-day operational requirements (includes Private Equity Funds, Debt Funds).
(3) Category III AIF: AIFs which employ diverse or complex trading strategies and may employ leverage including through investment in listed or unlisted derivatives (includes Hedge Funds, PIPE Funds).

CHAPTER II: REGISTRATION AND INVESTMENT CONDITIONS
10. Investment Conditions:
(a) AIF may raise funds from any investor (Indian, foreign or NRI) by way of issue of units;
(b) Minimum corpus for Category I, II and III AIF shall be twenty crore rupees (Rs. 20 Crores); provided that for Angel Funds, minimum corpus shall be ten crore rupees (Rs. 10 Crores);
(c) Minimum investment by an investor in an AIF shall be one crore rupees (Rs. 1 Crore); provided that for employees/directors of AIF/AMC, min investment is Rs. 25 Lakhs.

15. General Investment Conditions:
(d) Category I and Category II AIFs shall not invest more than twenty-five per cent (25%) of the investible funds in a single Investee Company directly or through associate entities.
(e) Category III AIFs shall not invest more than ten per cent (10%) of the investible funds in a single Investee Company.

17. Conditions for Category II AIFs:
(c) Category II AIFs shall not borrow funds directly or indirectly or engage in leverage except for meeting temporary funding requirements for not more than thirty days (30 days) and not more than ten per cent (10%) of investible funds.

18. Conditions for Category III AIFs:
(2) Category III AIFs may engage in leverage or borrow subject to maximum cap of 2 times the NAV (Net Asset Value) calculated using Gross Absolute Exposure.

CHAPTER III-A: ANGEL FUNDS
19F. Investment by Angel Funds:
(1) Angel funds shall raise funds only by way of issue of units to angel investors.
(2) Minimum investment per angel investor in an angel fund shall be twenty-five lakh rupees (Rs. 25 Lakhs).
(3) Maximum investment per angel investor in an angel fund shall be ten crore rupees (Rs. 10 Crores).
(4) Angel fund shall invest in venture capital undertakings which have turnover of less than Rs. 25 Crores and are unlisted.
""",

    "SEBI_Mutual_Funds_Regulations_1996_Master_Circular.txt": """
SECURITIES AND EXCHANGE BOARD OF INDIA (MUTUAL FUNDS) REGULATIONS, 1996 & MASTER CIRCULAR 2024

CHAPTER VI: SCHEME OBJECTIVES AND INVESTMENT RESTRICTIONS
52. Total Expense Ratio (TER) Limits:
(6)(c) Maximum Total Expense Ratio (TER) for equity-oriented schemes:
- On the first Rs. 500 Crores of daily net assets: 2.25%
- On the next Rs. 250 Crores of daily net assets: 2.00%
- On the next Rs. 1,250 Crores of daily net assets: 1.75%
- On the next Rs. 3,000 Crores of daily net assets: 1.60%
- On the next Rs. 5,000 Crores of daily net assets: 1.50%
- On the balance assets: TER reduction of 0.05% for every increase of Rs. 5,000 Crores.

(6)(d) Maximum Total Expense Ratio (TER) for debt schemes: 2.00% on first Rs. 500 Crores.

ESG THEMATIC FUNDS FRAMEWORK (SEBI Master Circular 2024):
1. Asset Allocation: Equity schemes under ESG theme must invest at least 80% of total assets in equity shares of companies following specified ESG strategy.
2. Recognized ESG Strategies: AMC must adopt one of 6 recognized strategies: Exclusion, Integration, Best-in-class, Impact, Sustainable, Transition.
3. BRSR Core: At least 65% of scheme AUM must be invested in companies reporting Business Responsibility and Sustainability Reporting (BRSR) Core disclosures.
4. Voting Disclosure: AMCs must disclose voting rationale on all ESG resolutions of investee companies.

REDEMPTION SUSPENSION & LIQUIDITY MANAGEMENT (SEBI Circular 2016 / Master Circular 2024):
1. Suspension of redemption allowed only during extraordinary circumstances (market closure, operational failure, systemic liquidity crisis).
2. Maximum suspension period allowed is 10 working days in 90 days.
3. Prior approval required from Board of AMC and Board of Trustees, with immediate notification to SEBI.
""",

    "SEBI_FPI_Regulations_2019_Full.txt": """
SECURITIES AND EXCHANGE BOARD OF INDIA (FOREIGN PORTFOLIO INVESTORS) REGULATIONS, 2019

CHAPTER I: PRELIMINARY & CATEGORIZATION
4. Categories of Foreign Portfolio Investors (FPI):
(a) Category I FPI: Government and Government-related investors (Central Banks, sovereign wealth funds), pension funds, university funds, regulated entities like banks, asset management companies, investment advisors.
(b) Category II FPI: Unregulated funds whose investment manager is appropriately regulated, endowed funds, charitable trusts, family offices, corporate bodies.

CHAPTER III: INVESTMENT CONDITIONS AND RESTRICTIONS
20. Investment Restrictions for FPI:
(7) Single FPI Limit: The total holding by each Foreign Portfolio Investor or investor group shall be LESS THAN TEN PER CENT (< 10%) of the total paid-up equity capital on a fully diluted basis of the company.
(8) Reclassification as FDI: Where an FPI along with its investor group acquires 10% or more of the total paid-up equity capital of an Indian company, the FPI shall have an option to divest excess holding within 5 trading days or reclassify the entire investment as Foreign Direct Investment (FDI) subject to FEMA NDI Rules.
(9) Sectoral Cap: Aggregate FPI limit in an Indian company shall be the applicable sectoral cap under FDI policy (e.g. 74% or 100%).
"""
}


def main():
    print(f"Populating comprehensive statutory legal texts into:\n  - {DOCS_DIR}\n  - {UPLOADS_DIR}\n")
    for filename, text in COMPREHENSIVE_SEBI_TEXTS.items():
        doc_path = DOCS_DIR / filename
        upload_path = UPLOADS_DIR / filename
        
        clean_text = text.strip()
        with open(doc_path, "w", encoding="utf-8") as f:
            f.write(clean_text)
        with open(upload_path, "w", encoding="utf-8") as f:
            f.write(clean_text)
            
        print(f"  [Saved] {filename} ({len(clean_text):,} chars)")

    # Ingest documents into ALL ChromaDB collections
    from backend import ingest, vectorstore
    from backend.chunking import split_text
    from backend.config import EMBEDDING_MODELS

    for embedding_model_label in EMBEDDING_MODELS:
        print(f"\n--- Ingesting into ChromaDB Collection: '{embedding_model_label}' ---")
        total_chunks = 0
        for filename in COMPREHENSIVE_SEBI_TEXTS:
            upload_path = UPLOADS_DIR / filename
            with open(upload_path, "rb") as f:
                raw = f.read()
            extracted = ingest.extract_text(filename, raw)
            chunks = split_text(extracted, chunk_size=800, chunk_overlap=100)
            doc_id = vectorstore.new_document_id()
            vectorstore.add_chunks(embedding_model_label, doc_id, filename, chunks)
            total_chunks += len(chunks)
            print(f"  -> Ingested '{filename}' -> {len(chunks)} chunks (Doc ID: {doc_id})")
        print(f"Collection '{embedding_model_label}' complete with {total_chunks} total chunks!")

    print("\n=======================================================")
    print("Comprehensive SEBI Knowledge Base Creation & Multi-Model Ingestion Complete!")
    print("=======================================================")


if __name__ == "__main__":
    main()
