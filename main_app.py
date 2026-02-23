import re
import streamlit as st
import pandas as pd
import time
from datetime import datetime
from logic import process_reports_and_generate_audio

# --- Detection Heuristic: Financial vs Non-Financial Emails ---
FINANCIAL_SENDERS = {"Bloomberg", "Reuters", "FactSet", "Goldman Sachs"}
FINANCIAL_KEYWORDS = [
    "Fed", "Market", "Earnings", "NVIDIA", "Crude", "Oil", "OPEC", "Inflation",
    "Rate", "ECB", "Rally", "Volatility", "Bond", "Yield", "Stock", "Revenue",
    "Analyst", "Investor", "Treasury", "Central Bank", "Shares", "Trading",
    "Energy", "Refinery", "Growth", "Economy", "Investment", "Equity"
]

def is_financial_email(row):
    """Detect if an email is financial based on sender and keyword heuristics."""
    sender_match = row["Sender"] in FINANCIAL_SENDERS
    combined_text = f"{row['Subject']} {row['Content']}".lower()
    keyword_match = any(kw.lower() in combined_text for kw in FINANCIAL_KEYWORDS)
    return sender_match or keyword_match

def filter_selects_email(row, suggestion, max_date):
    """Return True if this financial email matches the active filter."""
    def matches(text, pattern):
        return bool(re.search(pattern, str(text), re.I))

    if suggestion == "Manual Selection":
        return False
    if suggestion == "Market Volatility (High Impact)":
        return matches(row["Subject"], r"Surge|Rally|Crash|Volatility|Shock")
    if suggestion == "Tech & AI Sector":
        return matches(row["Subject"], r"NVIDIA|AI|Microsoft|Chips|Tech")
    if suggestion == "Bullish Sentiment":
        return matches(row["Content"], r"Growth|Higher|Positive|Upward|Gain")
    if suggestion == "Central Banks & Rates":
        return matches(row["Subject"], r"Fed|Rate|Inflation|ECB|Central Bank")
    if suggestion == "Global Energy":
        return matches(row["Subject"], r"Oil|OPEC|Energy|Crude|Gas")
    if suggestion == "Last 24 Hours":
        return row["Date"] == max_date
    if suggestion == "Bloomberg/Reuters Only":
        return row["Sender"] in ["Bloomberg", "Reuters"]
    return False

# --- 1. PAGE CONFIG AND STYLING ---
st.set_page_config(page_title="Briefly AI", layout="wide", page_icon="")

st.markdown("""
    <style>
        [data-testid="stSidebarNav"] { display: none; }
        .stApp, [data-testid="stSidebar"] { 
            background-color: #f1f3f4; 
            font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', sans-serif;
        }
        .main-card {
            background-color: white;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 1px 3px rgba(60,64,67,0.3);
            margin-bottom: 20px;
            font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', sans-serif;
        }
        .email-row {
            padding: 12px 15px;
            margin: 0 -15px;
            border-bottom: 1px solid #e8eaed;
            font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', sans-serif;
            font-size: 14px;
        }
        .email-row.financial {
            background-color: #e8f0fe;
            border-left: 3px solid #1a73e8;
        }
        .email-row.noise {
            background-color: #ffffff;
        }
        div.stButton > button:first-child {
            border-radius: 24px;
            padding: 12px 40px;
            font-weight: bold;
            background-color: #c5221f;
            color: white;
            border: none;
        }
        div.stButton > button:disabled {
            opacity: 0.5;
        }
        [data-testid="stMetricValue"] { font-size: 24px; color: #c5221f; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Gmail_icon_%282020%29.svg/2560px-Gmail_icon_%282020%29.svg.png", width=100)
    st.write("")

    if "view" not in st.session_state:
        st.session_state.view = "inbox"
    if "archive" not in st.session_state:
        st.session_state.archive = []

    if st.button("Inbox", width="stretch"):
        st.session_state.view = "inbox"
    if st.button("Archive", width="stretch"):
        st.session_state.view = "archive"

    st.write("---")
    st.subheader("Smart Filters")

    suggestion = st.radio(
        "Auto-select reports:",
        [
            "Manual Selection",
            "Market Volatility (High Impact)",
            "Tech & AI Sector",
            "Bullish Sentiment",
            "Central Banks & Rates",
            "Global Energy",
            "Last 24 Hours",
            "Bloomberg/Reuters Only"
        ]
    )

    st.write("---")
    st.subheader("Target Briefing Length")
    duration_minutes = st.radio(
        "Duration",
        options=[1, 3, 5],
        format_func=lambda x: f"{x} minute{'s' if x > 1 else ''}",
        index=1,
        label_visibility="collapsed"
    )

# --- 3. MAIN CONTENT ---

if st.session_state.view == "inbox":
    col_t, col_m1, col_m2, col_m3 = st.columns([2, 1, 1, 1])
    with col_t:
        st.title("Briefly AI")

    col_m1.metric("Unread Reports", "20", "+5")
    col_m2.metric("Saved Time", "45 min", "")
    col_m3.metric("AI Status", "Ready", "")

    try:
        df = pd.read_csv("data.csv")

        # Apply detection heuristic
        df["Is_Financial"] = df.apply(is_financial_email, axis=1)
        max_date = df["Date"].max()

        # Reset checkbox state when filter changes
        if st.session_state.get("_last_suggestion") != suggestion:
            for c in list(st.session_state.keys()):
                if c.startswith("sel_"):
                    del st.session_state[c]
            st.session_state["_last_suggestion"] = suggestion

        # Single Inbox: custom Gmail-like rows
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.subheader("Inbox")

        selected_rows = []

        for _, row in df.iterrows():
            row_id = row["ID"]
            is_fin = row["Is_Financial"]
            row_class = "financial" if is_fin else "noise"

            col_cb, col_content = st.columns([0.03, 0.97])

            with col_cb:
                if is_fin:
                    key = f"sel_{row_id}"
                    if key not in st.session_state:
                        st.session_state[key] = filter_selects_email(row, suggestion, max_date)
                    if st.checkbox(" ", key=key, label_visibility="collapsed"):
                        selected_rows.append(row)
                else:
                    st.write("")

            with col_content:
                st.markdown(
                    f'<div class="email-row {row_class}">'
                    f'<strong>{row["Sender"]}</strong> &nbsp; {row["Subject"]} &nbsp; '
                    f'<span style="color: #5f6368; font-size: 0.9em;">{row["Date"]}</span>'
                    f'</div>',
                    unsafe_allow_html=True
                )

        st.markdown("</div>", unsafe_allow_html=True)

        selected_reports = pd.DataFrame(selected_rows) if selected_rows else pd.DataFrame()

        has_selection = len(selected_reports) > 0
        if st.button("Generate Audio Brief", width="stretch", disabled=not has_selection):
            st.toast("Connecting to AI Engine...")

            progress_text = "AI is clustering news and synthesizing your audio brief..."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1, text=progress_text)

            try:
                script, audio_path = process_reports_and_generate_audio(selected_reports, duration_minutes)
                my_bar.empty()

                # Save to archive (capture audio bytes before next overwrite)
                with open(audio_path, "rb") as f:
                    audio_bytes = f.read()
                st.session_state.archive.insert(0, {
                    "timestamp": datetime.now(),
                    "script": script,
                    "audio_bytes": audio_bytes,
                    "sources_count": len(selected_reports),
                    "filter_used": suggestion,
                    "duration_minutes": duration_minutes
                })

                st.markdown('<div class="main-card">', unsafe_allow_html=True)
                st.subheader("Your AI Morning Briefing")

                st.audio(audio_path)
                st.divider()

                col_text, col_meta = st.columns([3, 1])
                with col_text:
                    st.markdown("### Executive Summary")
                    st.write(script)

                with col_meta:
                    st.markdown("### Metadata")
                    st.caption(f"**Sources:** {len(selected_reports)}")
                    st.caption(f"**Filter:** {suggestion}")
                    st.caption(f"**Duration:** {duration_minutes} min")
                    st.caption(f"**Time:** {datetime.now().strftime('%H:%M:%S')}")

                st.markdown("</div>", unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Error during AI processing: {e}")

        if not has_selection:
            st.caption("Select at least one financial email to enable generation.")

    except Exception as e:
        st.error(f"Error loading data.csv: {e}")

elif st.session_state.view == "archive":
    st.title("Archive")
    st.markdown('<div class="main-card">', unsafe_allow_html=True)

    if not st.session_state.archive:
        st.write("No briefings generated yet. Generate an audio brief from the Inbox to see it here.")
    else:
        for i, entry in enumerate(st.session_state.archive):
            ts = entry["timestamp"]
            script = entry["script"]
            audio_bytes = entry["audio_bytes"]
            sources = entry.get("sources_count", "-")
            filter_used = entry.get("filter_used", "-")
            duration = entry.get("duration_minutes", "-")

            with st.expander(f"Briefing - {ts.strftime('%Y-%m-%d %H:%M:%S')} | {sources} sources | {duration} min", expanded=(i == 0)):
                st.audio(audio_bytes, format="audio/mp3")
                st.markdown("**Script:**")
                st.write(script)
                st.caption(f"Filter: {filter_used} | Sources: {sources} | Duration: {duration} min")

    st.markdown("</div>", unsafe_allow_html=True)
