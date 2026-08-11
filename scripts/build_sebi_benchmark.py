import csv
import json
from pathlib import Path

BENCHMARK_DIR = Path(__file__).resolve().parent.parent / "data" / "benchmark"
BENCHMARK_DIR.mkdir(parents=True, exist_ok=True)

QUESTIONS = [
    # ==================== TIER 1: FACTUAL RECALL (10 QUESTIONS) ====================
    {
        "question_id": "SEBI-T1-01",
        "tier": 1,
        "question_text": "Under the SEBI (Prohibition of Insider Trading) Regulations, 2015, what is the statutory monetary threshold and timeline for mandatory disclosure of trades by promoters, directors, or designated persons?",
        "expected_answer": "Under Regulation 7(2)(a) of SEBI (PIT) Regulations, disclosure is mandatory when the value of securities traded (whether in one transaction or a series of transactions over any calendar quarter) aggregates to a traded value in excess of Rs. 10 Lakhs. The disclosure must be made within 2 trading days of such transaction.",
        "source_citation": "SEBI (PIT) Regulations, 2015, Regulation 7(2)(a) & 7(2)(b)",
        "source_url": "https://www.sebi.gov.in/legal/regulations/jan-2015/sebi-prohibition-of-insider-trading-regulations-2015-last-amended-on-nov-24-2022-_38830.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T1-02",
        "tier": 1,
        "question_text": "What is the minimum initial promoter contribution requirement for a Main Board IPO under the SEBI (ICDR) Regulations, 2018, and what is its lock-in period?",
        "expected_answer": "Under Regulation 14 & Regulation 16 of SEBI (ICDR) Regulations, 2018, promoters must contribute not less than 20% of the post-issue capital. The minimum promoter contribution of 20% is locked in for a period of 18 months from the date of allotment (or 3 years if the project involves capital expenditure for which funding is raised). Excess promoter holding beyond 20% is locked in for 6 months.",
        "source_citation": "SEBI (ICDR) Regulations, 2018, Regulations 14, 16(1), and 16(2)",
        "source_url": "https://www.sebi.gov.in/legal/regulations/sep-2018/sebi-issue-of-capital-and-disclosure-requirements-regulations-2018_40328.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T1-03",
        "tier": 1,
        "question_text": "What is the mandatory trigger percentage for an open offer under Regulation 3(1) of the SEBI (Substantial Acquisition of Shares and Takeovers) Regulations, 2011?",
        "expected_answer": "Under Regulation 3(1) of SEBI (SAST) Regulations, 2011, an acquirer who acquires shares or voting rights that entitle them to exercise 25% or more of the voting rights in a target company must make a public announcement of an open offer to acquire at least an additional 26% of the voting rights.",
        "source_citation": "SEBI (SAST) Regulations, 2011, Regulation 3(1) & Regulation 7(1)",
        "source_url": "https://www.sebi.gov.in/legal/regulations/sep-2011/sebi-substantial-acquisition-of-shares-and-takeovers-regulations-2011_21136.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T1-04",
        "tier": 1,
        "question_text": "Under SEBI (LODR) Regulations, 2015, within how many hours must a listed entity disclose outcome of a Board Meeting regarding financial results?",
        "expected_answer": "Under Regulation 30(6) read with Schedule III Part A of SEBI (LODR) Regulations, 2015, the outcome of the Board Meeting considering financial results must be disclosed to stock exchanges within 30 minutes of the closure of the board meeting.",
        "source_citation": "SEBI (LODR) Regulations, 2015, Regulation 30(6), Schedule III Part A Para A.4",
        "source_url": "https://www.sebi.gov.in/legal/regulations/jan-2024/sebi-listing-obligations-and-disclosure-requirements-regulations-2015-last-amended-on-january-10-2024-_80644.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T1-05",
        "tier": 1,
        "question_text": "What is the maximum investment limit allowed by a single investor in an Angel Fund under SEBI (AIF) Regulations, 2012?",
        "expected_answer": "Under Regulation 19F of SEBI (AIF) Regulations, 2012, no angel investor can invest more than Rs. 10 Crores in a single angel fund. Additionally, the minimum investment per angel investor in an angel fund is Rs. 25 Lakhs.",
        "source_citation": "SEBI (Alternative Investment Funds) Regulations, 2012, Regulation 19F",
        "source_url": "https://www.sebi.gov.in/legal/regulations/may-2012/sebi-alternative-investment-funds-regulations-2012_22864.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T1-06",
        "tier": 1,
        "question_text": "Under SEBI (Mutual Funds) Regulations, 1996, what is the maximum total expense ratio (TER) allowed for an equity-oriented mutual fund scheme with AUM up to Rs. 500 Crores?",
        "expected_answer": "Under Regulation 52(6)(c) of SEBI (Mutual Funds) Regulations, 1996, the maximum total expense ratio (TER) allowed for an equity scheme on the first Rs. 500 Crores of daily net assets is 2.25%.",
        "source_citation": "SEBI (Mutual Funds) Regulations, 1996, Regulation 52(6)(c)",
        "source_url": "https://www.sebi.gov.in/legal/regulations/dec-1996/sebi-mutual-funds-regulations-1996-last-amended-on-jan-2024_80800.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T1-07",
        "tier": 1,
        "question_text": "What is the timeline for submitting quarterly financial results by a listed entity under Regulation 33 of SEBI (LODR) Regulations, 2015?",
        "expected_answer": "Under Regulation 33(3)(a) of SEBI (LODR) Regulations, 2015, un-audited/audited quarterly financial results must be submitted to stock exchanges within 45 days from the end of each quarter (except for the last quarter, where audited annual results must be submitted within 60 days of the end of the financial year).",
        "source_citation": "SEBI (LODR) Regulations, 2015, Regulation 33(3)(a) & 33(3)(d)",
        "source_url": "https://www.sebi.gov.in/legal/regulations/jan-2024/sebi-listing-obligations-and-disclosure-requirements-regulations-2015-last-amended-on-january-10-2024-_80644.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T1-08",
        "tier": 1,
        "question_text": "What is the mandatory minimum public shareholding (MPS) requirement for listed companies in India under SCRR Rule 19A & SEBI regulations?",
        "expected_answer": "Under Rule 19A of Securities Contracts (Regulation) Rules, 1957 (SCRR) and SEBI guidelines, every listed company must maintain a minimum public shareholding (MPS) of at least 25%. Newly listed companies achieving less than 25% at IPO have a specified timeframe to comply.",
        "source_citation": "SCRR, 1957 Rule 19A & SEBI (LODR) Regulations Regulation 38",
        "source_url": "https://www.sebi.gov.in/legal/rules/jul-1957/securities-contracts-regulation-rules-1957_18968.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T1-09",
        "tier": 1,
        "question_text": "Under SEBI (SAST) Regulations, 2011, what is the creeping acquisition limit allowed per financial year without triggering an open offer for acquirers holding between 25% and 75%?",
        "expected_answer": "Under Regulation 3(2) of SEBI (SAST) Regulations, 2011, an acquirer holding 25% or more but less than 75% can acquire up to an additional 5% of voting rights in a financial year without triggering an open offer requirement.",
        "source_citation": "SEBI (SAST) Regulations, 2011, Regulation 3(2)",
        "source_url": "https://www.sebi.gov.in/legal/regulations/sep-2011/sebi-substantial-acquisition-of-shares-and-takeovers-regulations-2011_21136.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T1-10",
        "tier": 1,
        "question_text": "What is the statutory lock-in period for anchor investors in a main board public issue under SEBI (ICDR) Regulations, 2018?",
        "expected_answer": "Under Regulation 259 of SEBI (ICDR) Regulations, 2018 (as amended), 50% of the anchor investor allocation is locked in for 30 days, while the remaining 50% is locked in for 90 days from the date of allotment.",
        "source_citation": "SEBI (ICDR) Regulations, 2018, Schedule XIII / Regulation 259",
        "source_url": "https://www.sebi.gov.in/legal/regulations/sep-2018/sebi-issue-of-capital-and-disclosure-requirements-regulations-2018_40328.html",
        "known_trap": "N/A"
    },

    # ==================== TIER 2: CONCEPTUAL DISTINCTIONS (10 QUESTIONS) ====================
    {
        "question_id": "SEBI-T2-01",
        "tier": 2,
        "question_text": "What distinguishes a 'Connected Person' from a 'Designated Person' under the SEBI (Prohibition of Insider Trading) Regulations, 2015, and why does this distinction matter for compliance?",
        "expected_answer": "A 'Connected Person' (Regulation 2(1)(d)) is defined objectively by association with the company (e.g. director, officer, employee, or frequent contact) that allows access to UPSI, carrying a rebuttable legal presumption of possessing UPSI. A 'Designated Person' is an internal classification designated by the company board (e.g. key executives, finance team, promoters) subject to strict internal code of conduct, trading window restrictions, and pre-clearance requirements.",
        "source_citation": "SEBI (PIT) Regulations, 2015, Regulation 2(1)(d) & Schedule B",
        "source_url": "https://www.sebi.gov.in/legal/regulations/jan-2015/sebi-prohibition-of-insider-trading-regulations-2015-last-amended-on-nov-24-2022-_38830.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T2-02",
        "tier": 2,
        "question_text": "How do Category I, Category II, and Category III Alternative Investment Funds (AIFs) differ in terms of leverage allowed and fund objective under SEBI (AIF) Regulations, 2012?",
        "expected_answer": "Category I & II AIFs are restricted from taking leverage except for meeting temporary day-to-day operational requirements (up to 30 days and 10% of investible funds). Category III AIFs employ complex/diverse trading strategies (including hedge funds) and are explicitly permitted to engage in leverage/derivatives up to 2 times the NAV.",
        "source_citation": "SEBI (AIF) Regulations, 2012, Regulation 3(2) & Regulation 18",
        "source_url": "https://www.sebi.gov.in/legal/regulations/may-2012/sebi-alternative-investment-funds-regulations-2012_22864.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T2-03",
        "tier": 2,
        "question_text": "What is the key regulatory distinction between an SME IPO platform and a Main Board IPO under SEBI (ICDR) Regulations regarding track record and minimum net tangible assets?",
        "expected_answer": "Main Board IPO requires net tangible assets of at least Rs. 3 Crores in each of the preceding 3 full years and operating profit in 3 of the last 5 years (or QIB route). SME IPO (Chapter IX) requires a minimum post-issue face value capital of up to Rs. 25 Crores, track record of 2 years, and 100% underwriting requirement.",
        "source_citation": "SEBI (ICDR) Regulations, 2018, Regulation 6 (Main Board) vs Regulation 229 (SME)",
        "source_url": "https://www.sebi.gov.in/legal/regulations/sep-2018/sebi-issue-of-capital-and-disclosure-requirements-regulations-2018_40328.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T2-04",
        "tier": 2,
        "question_text": "What is the distinction between 'Material Events' disclosed under Regulation 30(2) Part A (deemed material) vs Regulation 30(3) Part B (subject to materiality guidelines) of SEBI (LODR)?",
        "expected_answer": "Part A events of Schedule III (e.g. acquisition, financial results, auditor appointment, fraud, board decisions) are deemed material and must be disclosed mandatorily without applying any threshold test. Part B events (e.g. commencement of commercial operations, dispute/litigation, licensing) are disclosed based on materiality guidelines framed by the board under quantitative thresholds.",
        "source_citation": "SEBI (LODR) Regulations, 2015, Regulation 30(2), 30(3), and Schedule III Part A/B",
        "source_url": "https://www.sebi.gov.in/legal/regulations/jan-2024/sebi-listing-obligations-and-disclosure-requirements-regulations-2015-last-amended-on-january-10-2024-_80644.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T2-05",
        "tier": 2,
        "question_text": "How does a Voluntary Open Offer under Regulation 6 of SEBI (SAST) differ from a Mandatory Open Offer under Regulation 3(1) regarding prior shareholding requirements?",
        "expected_answer": "A Mandatory Open Offer (Reg 3(1)) is triggered when an acquirer reaches 25% voting rights. A Voluntary Open Offer (Reg 6) can only be made by an acquirer who prior to the offer holds at least 25% or more voting rights, but less than the maximum permissible non-public shareholding (75%). An acquirer holding under 25% cannot make a voluntary open offer.",
        "source_citation": "SEBI (SAST) Regulations, 2011, Regulation 3(1) vs Regulation 6",
        "source_url": "https://www.sebi.gov.in/legal/regulations/sep-2011/sebi-substantial-acquisition-of-shares-and-takeovers-regulations-2011_21136.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T2-06",
        "tier": 2,
        "question_text": "What is the difference between Unpublished Price Sensitive Information (UPSI) and general non-public information under SEBI (PIT) Regulations, 2015?",
        "expected_answer": "UPSI under Regulation 2(1)(n) is non-public information specifically relating to a company or its securities that, if disclosed, is likely to materially affect the market price of the securities (e.g., financial results, dividends, M&A, capital structure changes). General non-public operational info that lacks price sensitivity does not constitute UPSI.",
        "source_citation": "SEBI (PIT) Regulations, 2015, Regulation 2(1)(n)",
        "source_url": "https://www.sebi.gov.in/legal/regulations/jan-2015/sebi-prohibition-of-insider-trading-regulations-2015-last-amended-on-nov-24-2022-_38830.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T2-07",
        "tier": 2,
        "question_text": "What distinguishes a Qualified Institutions Placement (QIP) from a Rights Issue under SEBI (ICDR) Regulations, 2018?",
        "expected_answer": "A QIP (Chapter VI) is issued exclusively to Qualified Institutional Buyers (QIBs) on a private placement basis without a public prospectus. A Rights Issue (Chapter III) is offered to existing shareholders in proportion to their existing shareholding as of a record date.",
        "source_citation": "SEBI (ICDR) Regulations, 2018, Chapter III (Rights Issue) vs Chapter VI (QIP)",
        "source_url": "https://www.sebi.gov.in/legal/regulations/sep-2018/sebi-issue-of-capital-and-disclosure-requirements-regulations-2018_40328.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T2-08",
        "tier": 2,
        "question_text": "Under SEBI (LODR) Regulations, what is the conceptual difference between a Related Party Transaction (RPT) requiring Audit Committee approval versus one requiring Shareholder Approval?",
        "expected_answer": "All RPTs and subsequent modifications require prior approval of the Audit Committee (Reg 23(2)). However, Material RPTs exceeding Rs. 1000 Crore or 10% of annual consolidated turnover of the listed entity (whichever is lower) additionally require prior shareholder resolution by ordinary resolution (Reg 23(4)).",
        "source_citation": "SEBI (LODR) Regulations, 2015, Regulation 23(2) & Regulation 23(4)",
        "source_url": "https://www.sebi.gov.in/legal/regulations/jan-2024/sebi-listing-obligations-and-disclosure-requirements-regulations-2015-last-amended-on-january-10-2024-_80644.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T2-09",
        "tier": 2,
        "question_text": "What is the difference between an Angel Investor and a Venture Capital Fund under Category I AIF rules?",
        "expected_answer": "An Angel Investor (Reg 19A) is an individual or corporate body meeting net worth/experience criteria investing via Angel Funds with min investment of Rs. 25 Lakhs per investee company. A VCF (Reg 3(2)(a)) is an institutional pool of capital investing primarily in unlisted venture undertakings with higher fund size requirements (min corpus Rs. 20 Crores).",
        "source_citation": "SEBI (AIF) Regulations, 2012, Regulation 3(2)(a) & Regulation 19A-19F",
        "source_url": "https://www.sebi.gov.in/legal/regulations/may-2012/sebi-alternative-investment-funds-regulations-2012_22864.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T2-10",
        "tier": 2,
        "question_text": "What distinguishes a General Information Document (GID) from a Key Information Document (KID) in debt private placement under SEBI (NCS) Regulations?",
        "expected_answer": "A GID contains full static disclosures about the issuer valid for 1 year for multiple debt issuances. A KID contains specific dynamic transaction details (tenure, coupon, size) for a specific tranche issued under that GID.",
        "source_citation": "SEBI (Issue and Listing of Non-Convertible Securities) Regulations, 2021",
        "source_url": "https://www.sebi.gov.in/legal/regulations/aug-2021/sebi-issue-and-listing-of-non-convertible-securities-regulations-2021_51775.html",
        "known_trap": "N/A"
    },

    # ==================== TIER 3: SCENARIO APPLICATION (10 QUESTIONS) ====================
    {
        "question_id": "SEBI-T3-01",
        "tier": 3,
        "question_text": "A Chief Financial Officer (CFO) of a listed Indian company acquires Rs. 15 Lakhs worth of equity shares of her company on Monday in the open market during an open trading window. What compliance steps and disclosure timelines are mandated under SEBI PIT Regulations?",
        "expected_answer": "1. The CFO is a Designated Person and key managerial personnel. She must ensure prior clearance from Compliance Officer if required by internal code.\n2. Since traded value exceeds Rs. 10 Lakhs in a quarter, under Reg 7(2)(a), CFO must disclose the transaction to the company within 2 trading days of the trade (by Wednesday).\n3. Under Reg 7(2)(b), the company must notify the stock exchanges within 2 trading days of receiving CFO's disclosure.\n4. CFO must not execute a contra-trade (selling shares) for 6 months under Schedule B.",
        "source_citation": "SEBI (PIT) Regulations, 2015, Regulation 7(2)(a), 7(2)(b), and Schedule B Clause 10",
        "source_url": "https://www.sebi.gov.in/legal/regulations/jan-2015/sebi-prohibition-of-insider-trading-regulations-2015-last-amended-on-nov-24-2022-_38830.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T3-02",
        "tier": 3,
        "question_text": "Acquirer A holds 22% voting rights in Target Company T (a listed entity). On April 10, Acquirer A buys an additional 4% equity stake via block deal. What are the immediate regulatory consequences under SEBI SAST Regulations, 2011?",
        "expected_answer": "1. 22% + 4% = 26% voting rights.\n2. Crossing the 25% threshold triggers Regulation 3(1) mandatory open offer requirement.\n3. Acquirer A must issue a Public Announcement (PA) on the same day (April 10) to stock exchanges and target company to acquire at least an additional 26% public shares.\n4. Acquirer must also disclose the acquisition under Regulation 29(1) within 2 working days.",
        "source_citation": "SEBI (SAST) Regulations, 2011, Regulation 3(1), 13(1), and 29(1)",
        "source_url": "https://www.sebi.gov.in/legal/regulations/sep-2011/sebi-substantial-acquisition-of-shares-and-takeovers-regulations-2011_21136.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T3-03",
        "tier": 3,
        "question_text": "A listed company's Board of Directors meets to finalize financial results for Q3 ending December 31. When must the trading window close for designated persons, and when can it reopen?",
        "expected_answer": "Under Clause 4(2) of Schedule B of SEBI PIT Regulations, the trading window closure is mandatory from the end of every quarter (i.e. December 31 midnight) until 48 hours after the declaration of financial results to stock exchanges.",
        "source_citation": "SEBI (PIT) Regulations, 2015, Schedule B Clause 4(2)",
        "source_url": "https://www.sebi.gov.in/legal/regulations/jan-2015/sebi-prohibition-of-insider-trading-regulations-2015-last-amended-on-nov-24-2022-_38830.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T3-04",
        "tier": 3,
        "question_text": "A promoter group entity pledges 5% of its shareholding in a listed company with a commercial bank to secure a corporate loan. What disclosures are required under SEBI SAST Regulations?",
        "expected_answer": "Under Regulation 31(1) of SEBI SAST Regulations, 2011, the promoter must disclose details of the encumbrance/pledge within 7 working days from the creation of pledge to the listed company and all stock exchanges where shares are listed.",
        "source_citation": "SEBI (SAST) Regulations, 2011, Regulation 31(1) & 31(3)",
        "source_url": "https://www.sebi.gov.in/legal/regulations/sep-2011/sebi-substantial-acquisition-of-shares-and-takeovers-regulations-2011_21136.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T3-05",
        "tier": 3,
        "question_text": "A listed telecom company suffers an unexpected tax demand order of Rs. 450 Crores, which exceeds 10% of its annual consolidated turnover. Under SEBI LODR 2023 amendments, what is the mandatory disclosure timeline?",
        "expected_answer": "Under the 2023 amendment to Regulation 30 of SEBI LODR, quantitative materiality threshold is 2% of turnover or net worth, or 10% of profit. Since Rs 450 Cr exceeds 10% turnover, it is material. Disclosure must be made within 24 hours of receipt of the order (or 12 hours if decision comes from an internal meeting).",
        "source_citation": "SEBI (LODR) Regulations, 2015, Regulation 30(6) & Schedule III Part B",
        "source_url": "https://www.sebi.gov.in/legal/regulations/jan-2024/sebi-listing-obligations-and-disclosure-requirements-regulations-2015-last-amended-on-january-10-2024-_80644.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T3-06",
        "tier": 3,
        "question_text": "An Indian Category II AIF wants to co-invest along with a foreign institutional investor in an unlisted tech startup. Is the AIF allowed to take borrowing to fund this investment?",
        "expected_answer": "No. Under Regulation 17(c) of SEBI AIF Regulations, Category II AIFs shall not borrow funds directly or indirectly or engage in leverage except for meeting temporary funding requirements for not more than 30 days and not more than 10% of investible funds.",
        "source_citation": "SEBI (AIF) Regulations, 2012, Regulation 17(c)",
        "source_url": "https://www.sebi.gov.in/legal/regulations/may-2012/sebi-alternative-investment-funds-regulations-2012_22864.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T3-07",
        "tier": 3,
        "question_text": "A listed company wants to reclassify a promoter holding 2% equity into a 'public shareholder'. What key conditions must be fulfilled under Regulation 31A of SEBI LODR?",
        "expected_answer": "Under Regulation 31A(3), promoter seeking reclassification must not hold >10% voting rights, must not exercise control, must not act as KMP/Director, must not be a wilful defaulter. Reclassification requires Board approval, Shareholder approval (by ordinary resolution), and Stock Exchange approval.",
        "source_citation": "SEBI (LODR) Regulations, 2015, Regulation 31A(3)",
        "source_url": "https://www.sebi.gov.in/legal/regulations/jan-2024/sebi-listing-obligations-and-disclosure-requirements-regulations-2015-last-amended-on-january-10-2024-_80644.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T3-08",
        "tier": 3,
        "question_text": "A mutual fund scheme experiences redemptions exceeding 5% of scheme AUM in a single day due to market rumor. Can the AMC suspend redemptions immediately?",
        "expected_answer": "No. Under SEBI Circular SEBI/HO/IMD/DF2/CIR/P/2016/57, suspension of redemption can only be allowed during extraordinary circumstances (liquidity issues, market closure, breakdown). Suspension requires prior approval of the Board of AMC and Board of Trustees, and SEBI must be informed immediately.",
        "source_citation": "SEBI Master Circular for Mutual Funds, 2024 / Circular 2016",
        "source_url": "https://www.sebi.gov.in/legal/master-circulars/may-2023/master-circular-for-mutual-funds_71329.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T3-09",
        "tier": 3,
        "question_text": "An Independent Director of a listed firm completes two consecutive terms of 5 years each. Can she be re-appointed immediately for a 3rd term under SEBI LODR?",
        "expected_answer": "No. Under Regulation 25(2) of SEBI LODR read with Companies Act Sec 149(11), an Independent Director who completes two consecutive 5-year terms is eligible for re-appointment only after a cooling-off period of 3 years during which she must not be associated with the company in any capacity.",
        "source_citation": "SEBI (LODR) Regulations, 2015, Regulation 25(2)",
        "source_url": "https://www.sebi.gov.in/legal/regulations/jan-2024/sebi-listing-obligations-and-disclosure-requirements-regulations-2015-last-amended-on-january-10-2024-_80644.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T3-10",
        "tier": 3,
        "question_text": "A non-promoter investor holds 49% of a listed company. She acquires another 6% through market purchases in May 2024. Does this trigger an open offer, and what is the maximum holding allowed?",
        "expected_answer": "Yes. Holding is between 25% and 75%. Under Regulation 3(2), acquiring >5% in a financial year triggers mandatory open offer. Furthermore, under MPS rules, promoter + non-public holding cannot exceed 75%.",
        "source_citation": "SEBI (SAST) Regulations, 2011, Regulation 3(2)",
        "source_url": "https://www.sebi.gov.in/legal/regulations/sep-2011/sebi-substantial-acquisition-of-shares-and-takeovers-regulations-2011_21136.html",
        "known_trap": "N/A"
    },

    # ==================== TIER 4: MULTI-STEP REASONING (10 QUESTIONS) ====================
    {
        "question_id": "SEBI-T4-01",
        "tier": 4,
        "question_text": "A listed pharmaceutical company P plans a Rights Issue to raise Rs. 500 Crores while simultaneously an external acquirer A makes a Hostile Open Offer under SAST. During this period, Company P receives CDSCO approval for a blockbuster drug (UPSI). Walk through the regulatory compliance obligations under ICDR, SAST, LODR, and PIT regulations.",
        "expected_answer": "1. **PIT (UPSI Handling):** CDSCO approval is UPSI (Reg 2(1)(n)). Company must immediately make public disclosure under LODR Reg 30 before any rights issue allotment or board action.\n2. **SAST (Target Restrictions):** Under SAST Reg 26, during the open offer period, the target board shall not issue any authorized shares (including Rights Issue) without passing a special resolution by postal ballot.\n3. **ICDR (Rights Issue):** Company P must ensure Draft Letter of Offer (DLOF) incorporates the CDSCO approval and open offer details as material developments.\n4. **Trading Window:** Insiders are barred from trading until 48 hours post CDSCO disclosure.",
        "source_citation": "SEBI (SAST) Reg 26, SEBI (PIT) Reg 2(1)(n), SEBI (ICDR) Chapter III, SEBI (LODR) Reg 30",
        "source_url": "https://www.sebi.gov.in/legal/regulations/sep-2011/sebi-substantial-acquisition-of-shares-and-takeovers-regulations-2011_21136.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T4-02",
        "tier": 4,
        "question_text": "Company X is an unlisted entity wishing to list on Main Board via IPO. It has net tangible assets of Rs. 4 Crores in Year 1, Rs. 2.5 Crores in Year 2, and Rs. 5 Crores in Year 3. Can it list via the normal profitability route under Regulation 6(1) of ICDR, or must it use Regulation 6(2)? Explain the steps.",
        "expected_answer": "1. Regulation 6(1)(a) requires net tangible assets of at least Rs. 3 Crores in **each** of the preceding 3 full years. Since Year 2 is Rs 2.5 Cr (< Rs 3 Cr), Company X **fails** Regulation 6(1).\n2. Company X must list under **Regulation 6(2)** (QIB Route).\n3. Under Reg 6(2), the issue must be made through Book Building process with at least 75% of the net offer allotted to Qualified Institutional Buyers (QIBs).",
        "source_citation": "SEBI (ICDR) Regulations, 2018, Regulation 6(1) & Regulation 6(2)",
        "source_url": "https://www.sebi.gov.in/legal/regulations/sep-2018/sebi-issue-of-capital-and-disclosure-requirements-regulations-2018_40328.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T4-03",
        "tier": 4,
        "question_text": "An acquirer acquires 28% of listed Target T. Simultaneously, a promoter group entity pledges 15% shares to a lender. Evaluate the open offer obligations, disclosure timelines for both parties, and lock-in implications under SAST and ICDR.",
        "expected_answer": "1. **Acquirer:** Crossing 25% triggers Regulation 3(1) open offer. Must issue Public Announcement within 2 working days and detailed public statement (DPS) within 5 working days.\n2. **Promoter Pledge:** Under Reg 31(1) of SAST, promoter must disclose 15% pledge within 7 working days to target and stock exchanges.\n3. **Encumbered Shares:** Encumbered promoter shares cannot be pledged if locked-in under ICDR minimum promoter contribution rules.",
        "source_citation": "SEBI (SAST) Reg 3(1), Reg 13, Reg 31 & SEBI (ICDR) Reg 17",
        "source_url": "https://www.sebi.gov.in/legal/regulations/sep-2011/sebi-substantial-acquisition-of-shares-and-takeovers-regulations-2011_21136.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T4-04",
        "tier": 4,
        "question_text": "A listed entity enters into a Related Party Transaction (RPT) with a promoter subsidiary valued at Rs. 1,200 Crores. Consolidated turnover is Rs. 10,000 Crores. Trace the full approval hierarchy under SEBI LODR.",
        "expected_answer": "1. 10% of consolidated turnover = Rs. 1,000 Crores.\n2. Rs. 1,200 Crores exceeds the threshold of Rs 1,000 Crores (lower of 10% or Rs 1,000 Cr).\n3. **Step 1:** Prior approval of Audit Committee (only independent members vote).\n4. **Step 2:** Board recommendation.\n5. **Step 3:** Prior shareholder approval by Ordinary Resolution where related parties cannot vote.",
        "source_citation": "SEBI (LODR) Regulations, 2015, Regulation 23(2), 23(4) & 23(7)",
        "source_url": "https://www.sebi.gov.in/legal/regulations/jan-2024/sebi-listing-obligations-and-disclosure-requirements-regulations-2015-last-amended-on-january-10-2024-_80644.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T4-05",
        "tier": 4,
        "question_text": "An AMC launches an ESG thematic Mutual Fund. Trace the compliance steps under SEBI Master Circular 2024 regarding minimum investment in ESG assets, fund name rules, and voting disclosure.",
        "expected_answer": "1. **Portfolio:** At least 80% of total assets of scheme must be invested in equities following the specified ESG strategy.\n2. **Strategy:** Must clearly adopt one of the 6 recognized ESG strategies (e.g. Exclusion, Integration, Impact).\n3. **BRSR:** Investee companies must have Business Responsibility and Sustainability Reporting (BRSR) Core disclosures.\n4. **Voting:** AMC must disclose votes cast on ESG resolutions along with rationale.",
        "source_citation": "SEBI Master Circular for Mutual Funds, 2024 (ESG Framework Chapter)",
        "source_url": "https://www.sebi.gov.in/legal/master-circulars/may-2023/master-circular-for-mutual-funds_71329.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T4-06",
        "tier": 4,
        "question_text": "A Category III AIF plans to use algorithmic trading and derivatives leverage equal to 1.8x NAV. What risk management, leverage monitoring, and SEBI reporting workflows are mandated?",
        "expected_answer": "1. **Leverage Limit:** 1.8x NAV is within the statutory 2-times NAV cap under Reg 18(2).\n2. **Calculation:** Calculated using Gross Absolute Exposure.\n3. **Reporting:** Must report leverage daily/monthly to custodian and submit quarterly report to SEBI.\n4. **Algo Trading:** Must obtain exchange approval for algo software.",
        "source_citation": "SEBI (AIF) Regulations, 2012, Regulation 18 & SEBI Circular on AIF Leverage",
        "source_url": "https://www.sebi.gov.in/legal/regulations/may-2012/sebi-alternative-investment-funds-regulations-2012_22864.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T4-07",
        "tier": 4,
        "question_text": "A listed promoter holds 72% equity and wants to acquire 4% more via creeping acquisition, but the company is also planning a QIP. How do creeping acquisition rules interact with QIP dilution?",
        "expected_answer": "1. Creeping acquisition under Reg 3(2) permits up to 5% per FY provided post-acquisition holding does not exceed 75%.\n2. QIP increases total paid-up equity, diluting promoter % holding.\n3. If promoter acquires 4% before QIP, post-QIP percentage will drop.\n4. Promoter cannot acquire if QIP shares are issued with promoter participation unless QIP pricing/rules complied with.",
        "source_citation": "SEBI (SAST) Reg 3(2) & SEBI (ICDR) Chapter VI",
        "source_url": "https://www.sebi.gov.in/legal/regulations/sep-2011/sebi-substantial-acquisition-of-shares-and-takeovers-regulations-2011_21136.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T4-08",
        "tier": 4,
        "question_text": "An insider communicates UPSI regarding a divestment to an external consultant under a Non-Disclosure Agreement (NDA). The consultant trades shares. Who is liable under PIT Regulations?",
        "expected_answer": "1. **Consultant Liability:** The consultant is a 'Connected Person' (Reg 2(1)(d)) and insider. Trading while in possession of UPSI violates Reg 3(1) and Reg 4(1).\n2. **Insider Communication Liability:** Under Reg 3(1), communicating UPSI is prohibited unless for legitimate purpose. Merely signing an NDA does not grant immunity if communication lacked legitimate business purpose.\n3. **Structured Digital Database (SDD):** Company must verify if consultant entry was logged in SDD under Reg 3(5).",
        "source_citation": "SEBI (PIT) Regulations, 2015, Regulation 3(1), 3(5), 4(1)",
        "source_url": "https://www.sebi.gov.in/legal/regulations/jan-2015/sebi-prohibition-of-insider-trading-regulations-2015-last-amended-on-nov-24-2022-_38830.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T4-09",
        "tier": 4,
        "question_text": "A listed company fails to appoint a mandatory Woman Independent Director for 2 consecutive quarters. What penalties, stock exchange actions, and board compliance steps follow under LODR?",
        "expected_answer": "1. **LODR Reg 17(1):** Board must have at least one independent woman director.\n2. **SOP Fines:** Stock exchanges impose fine of Rs. 5,000 per day under SEBI SOP Circular until compliance.\n3. **Freezing:** If non-compliance continues beyond 60 days, exchange freezes promoter shareholding.",
        "source_citation": "SEBI (LODR) Regulations, 2015, Regulation 17(1) & SEBI SOP Circular 2020",
        "source_url": "https://www.sebi.gov.in/legal/regulations/jan-2024/sebi-listing-obligations-and-disclosure-requirements-regulations-2015-last-amended-on-january-10-2024-_80644.html",
        "known_trap": "N/A"
    },
    {
        "question_id": "SEBI-T4-10",
        "tier": 4,
        "question_text": "An FPI Category I registered entity wants to acquire 12% equity in an Indian listed defence company. Trace the single FPI limit, aggregate FPI limit, and FDI approval requirements.",
        "expected_answer": "1. Under SEBI FPI Regs & FEMA, single FPI/group limit is **less than 10%** of total paid-up equity.\n2. Acquiring 12% automatically reclassifies the entire holding as Foreign Direct Investment (FDI).\n3. Defence sector FDI >49% requires government approval route, while up to 74% is automatic for certain FDI. Reclassification requires reporting to RBI/SEBI within 5 trading days.",
        "source_citation": "SEBI (FPI) Regulations, 2019 & Operational Guidelines / FEMA NDI Rules",
        "source_url": "https://www.sebi.gov.in/legal/regulations/sep-2019/sebi-foreign-portfolio-investors-regulations-2019_44437.html",
        "known_trap": "N/A"
    },

    # ==================== TIER 5: ADVERSARIAL / TRAPS (10 QUESTIONS) ====================
    {
        "question_id": "SEBI-T5-01",
        "tier": 5,
        "question_text": "Is it true that SEBI SAST Regulations allow an acquirer to trigger a mandatory open offer at 15% voting rights if the target company is an SME listed entity?",
        "expected_answer": "FALSE. The mandatory open offer trigger threshold under SEBI (SAST) Regulations, 2011 is strictly 25% for ALL listed companies (including SME platform listed entities). The 15% threshold was under the old repealed 1997 Takeover Code.",
        "source_citation": "SEBI (SAST) Regulations, 2011, Regulation 3(1)",
        "source_url": "https://www.sebi.gov.in/legal/regulations/sep-2011/sebi-substantial-acquisition-of-shares-and-takeovers-regulations-2011_21136.html",
        "known_trap": "LLMs frequently confuse the repealed 1997 SAST Code (which had a 15% open offer trigger) with the active 2011 SAST Code (which mandates a 25% trigger)."
    },
    {
        "question_id": "SEBI-T5-02",
        "tier": 5,
        "question_text": "Does SEBI require a listed company to close its insider trading window for 30 calendar days prior to every quarterly financial result announcement?",
        "expected_answer": "FALSE. SEBI PIT Regulations do NOT prescribe a fixed '30 calendar days' rule. Clause 4(2) of Schedule B specifies that the trading window closure is mandatory from the end of every financial quarter (e.g. March 31, June 30) until 48 hours after the declaration of financial results.",
        "source_citation": "SEBI (PIT) Regulations, 2015, Schedule B Clause 4(2)",
        "source_url": "https://www.sebi.gov.in/legal/regulations/jan-2015/sebi-prohibition-of-insider-trading-regulations-2015-last-amended-on-nov-24-2022-_38830.html",
        "known_trap": "LLMs often hallucinate a rigid '30-day prior' rule derived from obsolete corporate policies or foreign SEC guidelines."
    },
    {
        "question_id": "SEBI-T5-03",
        "tier": 5,
        "question_text": "Under SEBI ICDR 2018, is the minimum promoter contribution locked in for 3 years in all IPO cases without exception?",
        "expected_answer": "FALSE. Under SEBI (ICDR) Regulations, 2018 (as amended in 2021), the minimum promoter contribution of 20% is locked in for **18 months** (not 3 years), unless the issue involves capital expenditure for a project, in which case it remains 3 years.",
        "source_citation": "SEBI (ICDR) Regulations, 2018, Regulation 16(1)",
        "source_url": "https://www.sebi.gov.in/legal/regulations/sep-2018/sebi-issue-of-capital-and-disclosure-requirements-regulations-2018_40328.html",
        "known_trap": "LLMs hallucinate that all minimum promoter contributions are locked in for 3 years, failing to catch the 2021 amendment reducing it to 18 months."
    },
    {
        "question_id": "SEBI-T5-04",
        "tier": 5,
        "question_text": "Can a designated person trade in company shares during trading window closure if they possess an approved Trading Plan under Regulation 5 of PIT Regulations?",
        "expected_answer": "TRUE. A Trading Plan approved by the Compliance Officer under Regulation 5 of SEBI PIT Regulations grants an explicit statutory exception permitting trades during trading window closure, provided the plan was submitted 6 months in advance and trades are non-discretionary.",
        "source_citation": "SEBI (PIT) Regulations, 2015, Regulation 5(3)",
        "source_url": "https://www.sebi.gov.in/legal/regulations/jan-2015/sebi-prohibition-of-insider-trading-regulations-2015-last-amended-on-nov-24-2022-_38830.html",
        "known_trap": "LLMs often over-generalize that 'trading window closure prohibits ALL trading without exception'."
    },
    {
        "question_id": "SEBI-T5-05",
        "tier": 5,
        "question_text": "Is a Category I AIF permitted to invest 50% of its investible funds into a single unlisted startup company?",
        "expected_answer": "FALSE. Under Regulation 15(1)(d) of SEBI (AIF) Regulations, 2012, Category I and Category II AIFs cannot invest more than **25%** of their investible funds in a single investee company.",
        "source_citation": "SEBI (AIF) Regulations, 2012, Regulation 15(1)(d)",
        "source_url": "https://www.sebi.gov.in/legal/regulations/may-2012/sebi-alternative-investment-funds-regulations-2012_22864.html",
        "known_trap": "LLMs frequently confuse diversification limits across Category I/II (25% cap) vs Category III (10% cap for listed equities) or hallucinate higher single-company allowances."
    },
    {
        "question_id": "SEBI-T5-06",
        "tier": 5,
        "question_text": "Is it mandatory under SEBI LODR for every listed company to have the positions of Chairperson and Managing Director (MD/CEO) held by separate individuals?",
        "expected_answer": "FALSE. While SEBI initially mandated separation of Chairperson and MD/CEO under Regulation 17(1B), SEBI amended the regulation to make this requirement **voluntary** rather than mandatory for top 500 listed entities.",
        "source_citation": "SEBI (LODR) Regulations, 2015, Regulation 17(1B) Amendment",
        "source_url": "https://www.sebi.gov.in/legal/regulations/jan-2024/sebi-listing-obligations-and-disclosure-requirements-regulations-2015-last-amended-on-january-10-2024-_80644.html",
        "known_trap": "LLMs frequently cite old 2018 SEBI circulars declaring mandatory separation, missing SEBI's Feb 2022 decision making it voluntary."
    },
    {
        "question_id": "SEBI-T5-07",
        "tier": 5,
        "question_text": "Can a Foreign Portfolio Investor (FPI) hold up to 15% of the total issued equity share capital of a single Indian listed company under FPI regulations?",
        "expected_answer": "FALSE. Under SEBI (FPI) Regulations, 2019, the investment limit for a single FPI or investor group is strictly **less than 10%** (i.e. up to 9.99%) of the total issued equity capital. Holding 10% or more is reclassified as FDI.",
        "source_citation": "SEBI (FPI) Regulations, 2019, Regulation 20(7)",
        "source_url": "https://www.sebi.gov.in/legal/regulations/sep-2019/sebi-foreign-portfolio-investors-regulations-2019_44437.html",
        "known_trap": "LLMs confuse the 10% single-FPI threshold with aggregate sectoral FDI/FPI limits (such as 24% or 49%)."
    },
    {
        "question_id": "SEBI-T5-08",
        "tier": 5,
        "question_text": "Does an acquirer who acquires 26% voting rights in a listed target company through a rights issue need to make an open offer under SAST Regulations?",
        "expected_answer": "FALSE (exempt under conditions). Under Regulation 10(1)(a)(iii) read with Regulation 10(4) of SEBI SAST Regulations, acquisition of shares pursuant to a Rights Issue up to one's entitlement is **exempt** from open offer obligations.",
        "source_citation": "SEBI (SAST) Regulations, 2011, Regulation 10(4)(a)",
        "source_url": "https://www.sebi.gov.in/legal/regulations/sep-2011/sebi-substantial-acquisition-of-shares-and-takeovers-regulations-2011_21136.html",
        "known_trap": "LLMs assume that ANY acquisition reaching 25%+ triggers an open offer, missing statutory exemptions under Regulation 10."
    },
    {
        "question_id": "SEBI-T5-09",
        "tier": 5,
        "question_text": "Under SEBI PIT Regulations, does a spouse of a promoter need to execute trades over Rs. 10 Lakhs to be subject to insider trading laws?",
        "expected_answer": "FALSE. A spouse of a promoter is automatically deemed a 'Connected Person' under Regulation 2(1)(d)(i). Trading while in possession of UPSI is strictly illegal regardless of trade value (even if under Rs 10 Lakhs). Rs 10 Lakhs is merely a reporting threshold under Reg 7(2).",
        "source_citation": "SEBI (PIT) Regulations, 2015, Regulation 2(1)(d)(i) & Regulation 4(1)",
        "source_url": "https://www.sebi.gov.in/legal/regulations/jan-2015/sebi-prohibition-of-insider-trading-regulations-2015-last-amended-on-nov-24-2022-_38830.html",
        "known_trap": "LLMs conflate the Prohibition of Insider Trading (Reg 4) with the Disclosure Threshold (Reg 7)."
    },
    {
        "question_id": "SEBI-T5-10",
        "tier": 5,
        "question_text": "Can a listed company pass a related party transaction resolution where related parties vote in favor, provided they are not interested in that specific transaction?",
        "expected_answer": "FALSE. Under Regulation 23(4) of SEBI LODR (as amended), NO entity that falls under the definition of a 'Related Party' shall vote to approve the resolution, **whether the entity is a party to the particular transaction or not**.",
        "source_citation": "SEBI (LODR) Regulations, 2015, Regulation 23(4)",
        "source_url": "https://www.sebi.gov.in/legal/regulations/jan-2024/sebi-listing-obligations-and-disclosure-requirements-regulations-2015-last-amended-on-january-10-2024-_80644.html",
        "known_trap": "LLMs confuse the Companies Act Sec 188 rule (where only interested related parties are barred) with SEBI LODR Reg 23(4) (where ALL related parties are barred)."
    }
]


def main():
    json_path = BENCHMARK_DIR / "sebi_benchmark_50.json"
    jsonl_path = BENCHMARK_DIR / "sebi_benchmark_50.jsonl"
    csv_path = BENCHMARK_DIR / "sebi_benchmark_50.csv"

    # Save JSON
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(QUESTIONS, f, indent=2)

    # Save JSONL
    with open(jsonl_path, "w", encoding="utf-8") as f:
        for q in QUESTIONS:
            record = {
                "question_id": q["question_id"],
                "tier": q["tier"],
                "prompt": q["question_text"],
                "question": q["question_text"],
                "expected_answer": q["expected_answer"],
                "source_citation": q["source_citation"],
                "source_url": q["source_url"],
                "known_trap": q["known_trap"],
            }
            f.write(json.dumps(record) + "\n")

    # Save CSV (Section 4.2 Excel template format)
    fieldnames = [
        "question_id",
        "tier",
        "question_text",
        "expected_answer",
        "source_citation",
        "source_url",
        "known_trap",
    ]
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for q in QUESTIONS:
            writer.writerow(q)

    print(f"Successfully generated {len(QUESTIONS)} SEBI benchmark questions!")
    print(f"Files saved to:\n  - {json_path}\n  - {jsonl_path}\n  - {csv_path}")


if __name__ == "__main__":
    main()
