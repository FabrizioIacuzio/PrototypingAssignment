import pandas as pd

# The 15 financial reports provided for Phase 1
reports = [
    # --- AI & TECH STOCKS (4) ---
    {
        "ID": 1,
        "Sender": "Bloomberg",
        "Subject": "NVIDIA Extends Rally as AI Chip Demand Surges",
        "Date": "2026-02-10",
        "Content": (
            "NVIDIA shares continued their upward momentum this week as investors responded to "
            "stronger-than-expected demand for advanced AI accelerators across cloud and enterprise "
            "markets. Industry analysts noted that hyperscalers are accelerating procurement cycles "
            "to support next‑generation large‑language‑model deployments, contributing to a tightening "
            "supply environment. Several investment banks raised their price targets, citing improved "
            "visibility into NVIDIA’s data‑center revenue pipeline. Executives from major cloud "
            "providers have emphasized that AI infrastructure remains their highest‑priority capital "
            "expenditure category for 2026. Despite concerns about potential regulatory scrutiny of "
            "AI‑related energy consumption, market sentiment remains broadly positive. Traders also "
            "highlighted NVIDIA’s expanding software ecosystem as a key differentiator, enabling "
            "customers to optimize training workloads more efficiently. With demand outpacing supply "
            "in several regions, analysts expect continued volatility but maintain a constructive "
            "outlook for the company’s long‑term growth trajectory."
        )
    },
    {
        "ID": 2,
        "Sender": "Reuters",
        "Subject": "Microsoft Advances AI Integration Across Enterprise Cloud",
        "Date": "2026-02-11",
        "Content": (
            "Microsoft shares traded higher after the company announced expanded AI capabilities "
            "across its enterprise cloud portfolio. The update includes new model‑hosting options, "
            "enhanced security layers, and improved cost‑optimization tools designed to help "
            "businesses scale generative‑AI workloads. Analysts noted that Microsoft’s strategy "
            "continues to emphasize vertical‑specific solutions, particularly in healthcare, "
            "financial services, and manufacturing. Early customer feedback suggests that the new "
            "features significantly reduce deployment friction, enabling faster time‑to‑value for "
            "AI‑driven applications. Investors also reacted positively to comments from executives "
            "indicating that AI‑related revenue growth remains ahead of internal forecasts. While "
            "competition from other cloud providers remains intense, Microsoft’s broad distribution "
            "and enterprise relationships provide a structural advantage. Market observers expect the "
            "company to maintain strong momentum as organizations accelerate digital‑transformation "
            "initiatives throughout 2026."
        )
    },
    {
        "ID": 3,
        "Sender": "FactSet",
        "Subject": "Global Regulators Signal New AI Oversight Framework",
        "Date": "2026-02-12",
        "Content": (
            "Tech stocks were mixed after global regulators outlined a coordinated framework aimed at "
            "strengthening oversight of advanced AI systems. The proposal includes new transparency "
            "requirements, risk‑classification tiers, and mandatory reporting for high‑impact models. "
            "While the guidelines remain in draft form, industry groups expect implementation to begin "
            "later this year. Investors expressed cautious optimism, noting that clearer regulatory "
            "boundaries could reduce long‑term uncertainty for AI developers and cloud providers. "
            "However, some analysts warned that compliance costs may rise, particularly for smaller "
            "firms lacking the resources to meet new documentation standards. Large‑cap companies such "
            "as Microsoft and NVIDIA are expected to adapt more easily due to existing governance "
            "infrastructure. Market reaction suggests that investors are still assessing the potential "
            "impact on innovation cycles, though most agree that regulatory clarity could ultimately "
            "support more sustainable industry growth."
        )
    },
    {
        "ID": 4,
        "Sender": "Bloomberg",
        "Subject": "AI Hardware Supply Chain Shows Signs of Stabilization",
        "Date": "2026-02-13",
        "Content": (
            "After months of tight supply conditions, the AI hardware supply chain is showing early "
            "signs of stabilization, according to new industry data. Component manufacturers reported "
            "improved yields for advanced packaging technologies, easing pressure on GPU and accelerator "
            "availability. Investors welcomed the update, noting that supply constraints had previously "
            "limited revenue upside for several major chipmakers. Analysts cautioned that demand remains "
            "exceptionally strong, meaning that inventory normalization will likely be gradual. "
            "Nevertheless, improved visibility into production timelines has boosted confidence among "
            "cloud providers planning large‑scale AI infrastructure expansions. Market participants also "
            "highlighted increased collaboration between semiconductor firms and equipment suppliers as a "
            "positive structural trend. While geopolitical risks and export‑control policies continue to "
            "pose challenges, the overall outlook for the AI hardware ecosystem appears more balanced "
            "than in previous quarters."
        )
    },
    # --- OIL & ENERGY (4) ---
    {
        "ID": 5,
        "Sender": "Reuters",
        "Subject": "OPEC+ Signals Cautious Approach to Production Adjustments",
        "Date": "2026-02-10",
        "Content": (
            "Oil markets traded in a narrow range after OPEC+ officials signaled a cautious approach to "
            "future production adjustments. Delegates indicated that the group remains focused on "
            "maintaining market stability amid uneven global demand recovery. Analysts noted that recent "
            "inventory data from major consuming nations shows mixed trends, with some regions reporting "
            "stronger‑than‑expected refinery activity while others continue to face sluggish consumption. "
            "Traders are closely watching upcoming economic indicators that could influence demand "
            "forecasts for the second quarter. While some members have advocated for modest output "
            "increases, others prefer to extend existing cuts to prevent downward price pressure. Market "
            "participants expect the group to revisit its strategy at the next ministerial meeting, with "
            "decisions likely to hinge on updated demand projections and geopolitical developments."
        )
    },
    {
        "ID": 6,
        "Sender": "Bloomberg",
        "Subject": "Brent Crude Edges Higher on Supply Tightness",
        "Date": "2026-02-11",
        "Content": (
            "Brent crude prices moved higher as traders assessed tightening supply conditions across key "
            "exporting regions. Several unplanned outages at offshore facilities contributed to reduced "
            "shipments, prompting refiners to seek alternative sources. Analysts noted that the supply "
            "disruptions come at a time when seasonal demand is beginning to strengthen, amplifying "
            "upward price pressure. Market participants also pointed to declining inventories in Europe "
            "and Asia as evidence of a more constrained environment. Despite the price gains, some "
            "economists warned that persistent macroeconomic uncertainty could limit the sustainability "
            "of the rally. Investors will be watching upcoming OPEC+ communications for signals on "
            "whether the group intends to offset the recent disruptions with additional production."
        )
    },
    {
        "ID": 7,
        "Sender": "FactSet",
        "Subject": "Energy Sector Sees Renewed Investment Amid Price Volatility",
        "Date": "2026-02-12",
        "Content": (
            "The energy sector is experiencing renewed investment activity as firms position themselves "
            "for continued price volatility in global oil markets. Private‑equity groups and strategic "
            "investors have increased their exposure to upstream assets, citing attractive valuations and "
            "improving cash‑flow profiles. Analysts observed that companies with strong balance sheets are "
            "accelerating capital‑expenditure plans, particularly in regions with favorable regulatory "
            "frameworks. Meanwhile, integrated energy majors are expanding their hedging programs to "
            "manage short‑term price swings. Market observers noted that the sector’s fundamentals remain "
            "supported by disciplined supply management from OPEC+ and steady demand from emerging "
            "economies. However, geopolitical risks and currency fluctuations continue to influence "
            "trading patterns. Overall, investors appear increasingly confident that the sector can "
            "navigate near‑term uncertainty while maintaining long‑term growth prospects."
        )
    },
    {
        "ID": 8,
        "Sender": "Reuters",
        "Subject": "Refiners Adjust Output as Crude Prices Remain Elevated",
        "Date": "2026-02-13",
        "Content": (
            "Refining companies are adjusting output levels as elevated crude prices continue to pressure "
            "margins. Several operators have shifted production toward higher‑value distillates to improve "
            "profitability, while others are conducting maintenance earlier than planned to optimize "
            "utilization rates. Analysts noted that the current pricing environment has created challenges "
            "for refiners in regions with limited access to discounted feedstock. Despite these pressures, "
            "demand for transportation fuels remains resilient, supported by steady economic activity in "
            "major markets. Traders are monitoring crack spreads closely for signs of margin recovery, "
            "particularly as seasonal demand patterns evolve. Market participants expect refiners to "
            "maintain a flexible approach in the coming weeks as they navigate shifting supply dynamics "
            "and ongoing price volatility."
        )
    },
    # --- INTEREST RATES & CENTRAL BANKS (4) ---
    {
        "ID": 9,
        "Sender": "Bloomberg",
        "Subject": "Fed Officials Signal Patience Ahead of Next Rate Decision",
        "Date": "2026-02-10",
        "Content": (
            "Federal Reserve officials signaled a patient approach to upcoming policy decisions, citing "
            "the need for additional data to assess the trajectory of inflation and labor‑market "
            "conditions. Recent economic indicators show moderating price pressures, though several "
            "categories remain above the central bank’s long‑term target. Analysts noted that policymakers "
            "are increasingly focused on balancing the risks of easing too early against the potential "
            "costs of maintaining restrictive conditions for too long. Treasury yields moved slightly "
            "lower following the comments, reflecting expectations that the Fed may delay any policy "
            "adjustments until later in the year. Market participants are closely watching upcoming "
            "inflation releases and employment reports for signals that could influence the central "
            "bank’s next steps."
        )
    },
    {
        "ID": 10,
        "Sender": "FactSet",
        "Subject": "Inflation Data Shows Gradual Cooling Across Key Sectors",
        "Date": "2026-02-11",
        "Content": (
            "New inflation data released this week indicates gradual cooling across several key sectors, "
            "providing cautious optimism for policymakers. Core goods prices continued their downward "
            "trend, supported by improved supply‑chain efficiency and stable shipping costs. Services "
            "inflation, while still elevated, showed signs of easing as wage growth moderated. Analysts "
            "highlighted that housing‑related components remain a significant contributor to overall "
            "inflation, though forward‑looking indicators suggest potential relief in the coming months. "
            "Bond markets reacted positively to the report, with yields declining across the curve. "
            "Economists noted that while the data supports the case for eventual policy easing, the "
            "Federal Reserve is likely to maintain a cautious stance until it sees sustained progress "
            "toward its inflation target."
        )
    },
    {
        "ID": 11,
        "Sender": "Reuters",
        "Subject": "Central Banks in Europe Maintain Restrictive Policy Tone",
        "Date": "2026-02-12",
        "Content": (
            "European central banks maintained a restrictive policy tone this week, emphasizing the need "
            "to ensure inflation continues its downward trajectory. Officials from several institutions "
            "stressed that premature easing could risk undoing recent progress, particularly in sectors "
            "where price pressures remain persistent. Market analysts noted that while headline inflation "
            "has moderated, underlying components such as services and food continue to show resilience. "
            "Bond markets across the region saw modest volatility as investors recalibrated expectations "
            "for potential rate cuts later in the year. Despite the cautious messaging, some economists "
            "believe that slowing economic activity may eventually prompt a shift in policy stance. For "
            "now, central bankers appear committed to maintaining a data‑dependent approach."
        )
    },
    {
        "ID": 12,
        "Sender": "Bloomberg",
        "Subject": "Global Bond Markets Steady Ahead of Key Fed Testimony",
        "Date": "2026-02-13",
        "Content": (
            "Global bond markets traded steadily as investors awaited key testimony from Federal Reserve "
            "leadership. Market participants expect policymakers to reiterate their commitment to a "
            "data‑driven approach, with particular emphasis on inflation dynamics and labor‑market "
            "conditions. Analysts noted that recent economic data has provided mixed signals, contributing "
            "to uncertainty around the timing of potential policy adjustments. Treasury yields remained "
            "range‑bound, while European and Asian bond markets showed similar stability. Investors are "
            "closely monitoring forward‑guidance language for clues about the central bank’s medium‑term "
            "outlook. Many expect policymakers to maintain a cautious tone, emphasizing the importance of "
            "sustained progress toward inflation targets before considering any changes to interest‑rate "
            "policy."
        )
    },
    # --- RETAIL / CONSUMER TRENDS (3) ---
    {
        "ID": 13,
        "Sender": "Reuters",
        "Subject": "Retailers Report Steady Foot Traffic Despite Economic Uncertainty",
        "Date": "2026-02-10",
        "Content": (
            "Major retailers reported steady foot traffic in early February, suggesting that consumer "
            "spending remains resilient despite broader economic uncertainty. Analysts noted that "
            "promotional activity has moderated compared to the holiday season, yet shoppers continue to "
            "prioritize essential goods and value‑oriented purchases. Several chains highlighted improved "
            "inventory management as a key factor supporting margins, particularly in apparel and home "
            "goods. While discretionary categories remain uneven, early indicators point to stable demand "
            "heading into the spring season. Economists cautioned that consumer sentiment could shift if "
            "labor‑market conditions weaken or inflation reaccelerates. For now, retailers appear focused "
            "on maintaining operational efficiency and optimizing product assortments to align with "
            "evolving customer preferences."
        )
    },
    {
        "ID": 14,
        "Sender": "Bloomberg",
        "Subject": "E‑Commerce Growth Accelerates as Consumers Shift to Online Deals",
        "Date": "2026-02-11",
        "Content": (
            "E‑commerce platforms reported accelerating growth as consumers increasingly sought online "
            "discounts and flexible delivery options. Analysts observed that digital‑sales momentum has "
            "remained strong even after the holiday season, driven by competitive pricing and expanded "
            "loyalty programs. Retailers have invested heavily in fulfillment‑center automation to reduce "
            "shipping times and improve order accuracy. Market observers noted that mobile‑commerce "
            "engagement continues to rise, particularly among younger demographics. Despite the positive "
            "trends, some companies face margin pressure due to elevated logistics costs. Nevertheless, "
            "the sector’s long‑term outlook remains favorable as consumers continue to prioritize "
            "convenience and personalized shopping experiences. Investors are watching upcoming earnings "
            "reports for insights into how retailers are balancing growth initiatives with profitability "
            "goals."
        )
    },
    {
        "ID": 15,
        "Sender": "FactSet",
        "Subject": "Consumer Confidence Holds Steady as Spending Patterns Shift",
        "Date": "2026-02-12",
        "Content": (
            "Consumer‑confidence readings held steady this week, reflecting a balanced outlook among "
            "households navigating evolving economic conditions. Survey data indicates that while "
            "consumers remain cautious about long‑term financial prospects, near‑term spending intentions "
            "have stabilized. Analysts noted a shift toward practical and experience‑based purchases, with "
            "travel, dining, and home‑improvement categories showing relative strength. Retailers are "
            "responding by adjusting product assortments and expanding services that cater to value‑driven "
            "shoppers. Economists highlighted that wage growth and employment stability continue to "
            "support consumer activity, though rising housing and insurance costs remain headwinds. "
            "Overall, the data suggests that consumers are adapting their spending habits rather than "
            "pulling back significantly, providing a measure of stability for the retail sector."
        )
    }
]

# Non-financial "noise" emails for filtering demo
noise_emails = [
    {
        "ID": 16,
        "Sender": "HR Department",
        "Subject": "Reminder: Q1 Performance Review Deadlines",
        "Date": "2026-02-10",
        "Content": (
            "Dear colleagues, this is a friendly reminder that the Q1 performance review self-assessment "
            "forms are due by Friday, February 14. Please ensure you have completed your objectives "
            "section and submitted to your line manager. The 360 feedback window will open next week. "
            "Contact hr@company.com if you have any questions."
        )
    },
    {
        "ID": 17,
        "Sender": "Accounts Payable",
        "Subject": "Invoice #INV-2026-0892 – Payment Due",
        "Date": "2026-02-11",
        "Content": (
            "Please find attached invoice #INV-2026-0892 for office supplies and equipment maintenance "
            "dated January 15, 2026. Total amount: EUR 2,450.00. Payment is due within 30 days. "
            "Our bank details are available in the attached PDF. For queries, reply to ap@company.com."
        )
    },
    {
        "ID": 18,
        "Sender": "IT Support",
        "Subject": "Scheduled Maintenance – VPN Services Feb 13 02:00–04:00 UTC",
        "Date": "2026-02-12",
        "Content": (
            "IT will perform scheduled maintenance on VPN services on Thursday, February 13, between "
            "02:00 and 04:00 UTC. During this window, remote access may be interrupted. Please save "
            "your work and disconnect before the maintenance window. Contact itsupport@company.com "
            "if you experience issues afterward."
        )
    },
    {
        "ID": 19,
        "Sender": "Facilities",
        "Subject": "Building HVAC Maintenance – Floor 3",
        "Date": "2026-02-12",
        "Content": (
            "Facilities will conduct HVAC maintenance on Floor 3 on Friday, February 14. Access to "
            "some meeting rooms may be limited between 09:00 and 12:00. If you have bookings, please "
            "consider relocating. We apologize for any inconvenience."
        )
    },
    {
        "ID": 20,
        "Sender": "Corporate Events",
        "Subject": "Team Offsite – Save the Date March 20",
        "Date": "2026-02-13",
        "Content": (
            "Save the date for our Q1 team offsite on Friday, March 20. Location and agenda will follow. "
            "Please block your calendar. Lunch will be provided. RSVP by March 6."
        )
    },
]

# Combine financial reports and noise emails, interleave by date for realism
all_emails = reports + noise_emails
df = pd.DataFrame(all_emails)

# Sort by Date then ID to interleave
df = df.sort_values(by=["Date", "ID"]).reset_index(drop=True)

# Save to data.csv
df.to_csv("data.csv", index=False)

print("Successfully created 'data.csv' with 15 financial reports and 5 noise emails.")