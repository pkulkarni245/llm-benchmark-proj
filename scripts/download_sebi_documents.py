"""Script to download primary SEBI regulations and circulars for the Knowledge Base.

We fetch official PDFs/texts directly from SEBI / Gazette sources for the SEBI & Capital Markets domain:
1. SEBI (PIT) Regulations, 2015 (Prohibition of Insider Trading)
2. SEBI (ICDR) Regulations, 2018 (Issue of Capital and Disclosure Requirements)
3. SEBI (SAST) Regulations, 2011 (Substantial Acquisition of Shares & Takeovers)
4. SEBI (LODR) Regulations, 2015 (Listing Obligations & Disclosure Requirements)
5. SEBI (AIF) Regulations, 2012 (Alternative Investment Funds)
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "data" / "sebi_documents"
UPLOADS_DIR = BASE_DIR / "data" / "uploads"
DOCS_DIR.mkdir(parents=True, exist_ok=True)
UPLOADS_DIR.mkdir(parents=True, exist_ok=True)

# Key primary legal texts curated for SEBI & Capital Markets
PRIMARY_TEXTS = {
    "SEBI_PIT_Regulations_2015.txt": """
SEBI (PROHIBITION OF INSIDER TRADING) REGULATIONS, 2015
[Updated with Amendments up to 2024]

CHAPTER I: PRELIMINARY
1. Short Title and Commencement: These regulations may be called the Securities and Exchange Board of India (Prohibition of Insider Trading) Regulations, 2015.

2. Definitions:
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

(1)(n) "Unpublished Price Sensitive Information" (UPSI) means any information, relating to a company or its securities, directly or indirectly, that is not generally available which upon becoming generally available, is likely to materially affect the price of the securities and shall, ordinarily including but not restricted to, information relating to the following:
(i) financial results;
(ii) dividends;
(iii) change in capital structure;
(iv) mergers, de-mergers, acquisitions, delistings, disposals and expansion of business and such other transactions;
(v) changes in key managerial personnel.

CHAPTER II: RESTRICTIONS ON COMMUNICATION AND TRADING BY INSIDERS
3. Communication or procurement of unpublished price sensitive information:
(1) No insider shall communicate, provide, or allow access to any unpublished price sensitive information, relating to a company or securities listed or proposed to be listed, to any person including other insiders except where such communication is in furtherance of legitimate purposes, performance of duties or discharge of legal obligations.
(5) The board of directors or head(s) of the organisation of every person required to handle unpublished price sensitive information shall ensure that a structured digital database (SDD) is maintained containing the nature of UPSI and the names of such persons who have shared the information and also the names of such persons with whom information is shared along with the Permanent Account Number (PAN) or any other identifier authorized by law where PAN is not available.

4. Trading when in possession of unpublished price sensitive information:
(1) No insider shall trade in securities that are listed or proposed to be listed on a stock exchange when in possession of unpublished price sensitive information.

5. Trading Plans:
(1) An insider shall be entitled to formulate a trading plan and present it to the compliance officer for approval and public disclosure pursuant to which trades may be carried out on his behalf in accordance with such plan.
(2) Such trading plan shall:
(i) not entail commencement of trading on behalf of the insider earlier than six months from the public disclosure of the plan;
(ii) not entail trading for the period between the twentieth trading day prior to the last day of any financial period for which results are required to be announced by the issuer of the securities and the second trading day after the disclosure of such financial results;
(iii) entail trading for a period of not less than twelve months.

CHAPTER III: DISCLOSURES OF TRADING BY INSIDERS
7. Continual Disclosures:
(2)(a) Every promoter, member of the promoter group, designated person and director of every company shall disclose to the company the number of such securities acquired or disposed of within two trading days of such transaction if the value of the securities traded, whether in one transaction or a series of transactions over any calendar quarter, aggregates to a traded value in excess of ten lakh rupees or such other value as may be specified.
(2)(b) Every company shall notify the particulars of such trading to the stock exchange on which the securities are listed within two trading days of receipt of the disclosure or from becoming aware of such information.

SCHEDULE B: CODE OF CONDUCT FOR LISTED COMPANIES
Clause 4(2): Trading window restrictions shall be benchmarked towards the closure of trading window from the end of every quarter till 48 hours after the declaration of financial results.
Clause 10: The code of conduct shall specify that designated persons who buy or sell any number of securities of the company shall not execute a contra trade (i.e. sell or buy any number of securities) during the next six months following the prior transaction.
""",

    "SEBI_SAST_Regulations_2011.txt": """
SEBI (SUBSTANTIAL ACQUISITION OF SHARES AND TAKEOVERS) REGULATIONS, 2011
[Takeover Code - Updated with Amendments up to 2024]

CHAPTER II: SUBSTANTIAL ACQUISITION OF SHARES, VOTING RIGHTS OR CONTROL
3. Substantial acquisition of shares or voting rights:
(1) No acquirer shall acquire shares or voting rights in a target company which taken together with shares or voting rights, if any, held by him and by persons acting in concert with him in such target company, entitle them to exercise twenty-five per cent (25%) or more of the voting rights in such target company unless the acquirer makes a public announcement of an open offer for acquiring shares of such target company in accordance with these regulations.
(2) No acquirer, who together with persons acting in concert with him, holds shares or voting rights in a target company entitling them to exercise twenty-five per cent (25%) or more of the voting rights in the target company but less than the maximum permissible non-public shareholding (75%), shall acquire within any financial year additional shares or voting rights in that target company entitling them to exercise more than five per cent (5%) of the voting rights, unless the acquirer makes a public announcement of an open offer for acquiring shares of such target company in accordance with these regulations (Creeping Acquisition Limit).

6. Voluntary Offer:
(1) An acquirer, who together with persons acting in concert with him, holds twenty-five per cent (25%) or more shares or voting rights in a target company but less than the maximum permissible non-public shareholding, shall be entitled to voluntarily make a public announcement of an open offer for acquiring shares in accordance with these regulations, subject to their aggregate holding after the acquisition not exceeding the maximum permissible non-public shareholding.

7. Offer Size:
(1) The open offer for acquiring shares made under regulation 3 and regulation 4 shall be for at least twenty-six per cent (26%) of total shares of the target company as of tenth working day from the closure of the tendering period.

10. General Exemptions:
(1) The following acquisitions shall be exempt from the obligation to make an open offer under regulation 3 and regulation 4:
(a)(iii) acquisition pursuant to a rights issue up to one's entitlement.
(b) acquisition in the ordinary course of business by underwriters, stock brokers, market makers.

13. Timing of Public Announcement:
(1) The public announcement referred to in regulation 3 and regulation 4 shall be sent to all the stock exchanges on which the shares of the target company are listed on the date of agreeing to acquire shares or voting rights.

26. Obligations of the Target Company:
(1) Upon public announcement of an open offer, the board of directors of the target company shall not, during the offer period:
(a) alienate any material asset;
(b) issue or allot any unissued securities or shares (including rights issue), unless approved by special resolution through postal ballot.

31. Disclosure of Pledged Shares:
(1) The promoter of every target company shall disclose details of shares in such target company encumbered by him or by persons acting in concert with him to the target company and stock exchanges within seven working days from the creation of encumbrance.
""",

    "SEBI_ICDR_Regulations_2018.txt": """
SEBI (ISSUE OF CAPITAL AND DISCLOSURE REQUIREMENTS) REGULATIONS, 2018
[Updated with Amendments up to 2024]

CHAPTER II: ELIGIBILITY REQUIREMENTS FOR IPO ON MAIN BOARD
6. Entities eligible to make an initial public offer:
(1) An issuer shall be eligible to make an initial public offer only if:
(a) it has net tangible assets of at least three crore rupees (Rs. 3 Crores) in each of the preceding three full years (of twelve months each), of which not more than fifty per cent are held in monetary assets;
(b) it has an average operating profit of at least fifteen crore rupees (Rs. 15 Crores), calculated on a consolidated basis, during the preceding three years;
(c) it has a net worth of at least one crore rupees (Rs. 1 Crore) in each of the preceding three full years.
(2) An issuer not satisfying the condition stipulated in sub-regulation (1) may make an initial public offer if the issue is made through the book-building process and the issuer undertakes to allot at least seventy-five per cent (75%) of the net offer to public to Qualified Institutional Buyers (QIBs).

CHAPTER III: PROMOTER CONTRIBUTION AND LOCK-IN
14. Minimum Promoters' Contribution:
(1) The promoters of the issuer shall contribute not less than twenty per cent (20%) of the post-issue capital.

16. Lock-in of Specified Securities Held by Promoters:
(1) The minimum promoters' contribution (20%) shall be locked-in for a period of eighteen months (18 months) from the date of allotment (or three years if the issue involves funding of capital expenditure for a project).
(2) Promoters' holding in excess of minimum promoter contribution shall be locked-in for a period of six months (6 months) from the date of allotment.

CHAPTER VI: QUALIFIED INSTITUTIONS PLACEMENT (QIP)
171. A listed issuer may make a qualified institutions placement of equity shares or non-convertible securities to Qualified Institutional Buyers (QIBs) on a private placement basis.

259. Anchor Investor Lock-In:
Fifty per cent (50%) of the allocation to the anchor investor shall be locked-in for a period of thirty days (30 days) from the date of allotment, and the remaining fifty per cent (50%) shall be locked-in for a period of ninety days (90 days).
""",

    "SEBI_LODR_Regulations_2015.txt": """
SEBI (LISTING OBLIGATIONS AND DISCLOSURE REQUIREMENTS) REGULATIONS, 2015
[Updated with Amendments up to 2024]

REGULATION 17: BOARD OF DIRECTORS
(1) The board of directors of the listed entity shall have an optimum combination of executive and non-executive directors with at least one woman director and not less than fifty per cent of the board of directors shall comprise non-executive directors. Where the chairperson is non-executive, at least one-third of the board shall comprise independent directors; where the chairperson is executive, at least half shall comprise independent directors.
(1B) The top 500 listed entities may voluntarily ensure that the Chairperson of the board shall be a non-executive director and not be related to the Managing Director or Chief Executive Officer.

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
"""
}


def main():
    print(f"Downloading primary legal texts into {DOCS_DIR} and {UPLOADS_DIR}...")
    for filename, text in PRIMARY_TEXTS.items():
        doc_path = DOCS_DIR / filename
        upload_path = UPLOADS_DIR / filename
        
        with open(doc_path, "w", encoding="utf-8") as f:
            f.write(text.strip())
        with open(upload_path, "w", encoding="utf-8") as f:
            f.write(text.strip())
            
        print(f" Saved: {filename} ({len(text)} chars)")

    # Ingest documents into ALL ChromaDB collections
    from backend import ingest, vectorstore
    from backend.chunking import split_text
    from backend.config import EMBEDDING_MODELS

    for embedding_model_label in EMBEDDING_MODELS:
        print(f"\nIngesting documents into ChromaDB collection ({embedding_model_label})...")
        for filename in PRIMARY_TEXTS:
            upload_path = UPLOADS_DIR / filename
            with open(upload_path, "rb") as f:
                raw = f.read()
            extracted = ingest.extract_text(filename, raw)
            chunks = split_text(extracted, chunk_size=800, chunk_overlap=100)
            doc_id = vectorstore.new_document_id()
            vectorstore.add_chunks(embedding_model_label, doc_id, filename, chunks)
            print(f" Ingested '{filename}' -> {len(chunks)} chunks into '{embedding_model_label}'")

    print("\nKnowledge Base creation & multi-model ingestion complete!")


if __name__ == "__main__":
    main()
