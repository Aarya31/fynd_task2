# app_admin.py
import streamlit as st
import pandas as pd
import os
from datetime import datetime

DATA_PATH = "data/submissions.csv"

st.set_page_config(page_title="Feedback — Admin", page_icon="📊", layout="wide")
st.title("Admin Dashboard — Feedback Submissions")

st.sidebar.write("Admin Controls")
refresh = st.sidebar.button("Refresh Data")
download = st.sidebar.button("Download CSV")

# Load data
if os.path.exists(DATA_PATH):
    df = pd.read_csv(DATA_PATH)
else:
    df = pd.DataFrame(columns=["timestamp","rating","review","ai_response","ai_summary","ai_actions"])

# Show key metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total submissions", len(df))
with col2:
    st.metric("Average rating", round(df['rating'].mean() if len(df) else 0, 2))
with col3:
    st.metric("Latest submission", df['timestamp'].iloc[-1] if len(df) else "—")

st.markdown("### Submission Table (live)")
st.dataframe(df.sort_values(by="timestamp", ascending=False).reset_index(drop=True), height=400)

st.markdown("### Insights")
if len(df):
    st.subheader("Rating distribution")
    st.bar_chart(df['rating'].value_counts().sort_index())

    st.subheader("Top AI Suggested Actions (sample)")
    # simple split by semicolons/newlines and count tokens
    actions = df['ai_actions'].dropna().astype(str)
    # naive split into lines/semicolons
    exploded = actions.str.split(r'[\n;]').explode().str.strip().value_counts().head(10)
    st.table(exploded.rename_axis("Action").reset_index(name="Count"))
else:
    st.info("No submissions yet.")

st.markdown("---")
st.write("You can click rows above to read details. Use the download button to export data.")
if download and len(df):
    st.download_button("Download CSV", data=df.to_csv(index=False), file_name="submissions.csv")
