# app_user.py
import streamlit as st
import pandas as pd
from datetime import datetime
import os
from llm_utils import generate_user_response, generate_summary, generate_recommended_actions

DATA_PATH = "data/submissions.csv"
os.makedirs("data", exist_ok=True)

st.set_page_config(page_title="Feedback — User", page_icon="📝", layout="centered")
st.title("User Feedback Portal")

st.write("Please leave your rating and a short review. The AI will generate a friendly response.")

col1, col2 = st.columns([1,4])
with col1:
    rating = st.slider("Rating", min_value=1, max_value=5, value=5)

with col2:
    review = st.text_area("Write your review here", height=150)

if st.button("Submit"):
    if not review.strip():
        st.error("Please write a review before submitting.")
    else:
        with st.spinner("Generating AI response..."):
            ai_response = generate_user_response(review)
            ai_summary = generate_summary(review)
            ai_actions = generate_recommended_actions(review)

        # Prepare a row
        row = {
            "timestamp": datetime.utcnow().isoformat(),
            "rating": rating,
            "review": review.replace("\n", " "),
            "ai_response": ai_response.replace("\n", " "),
            "ai_summary": ai_summary.replace("\n", " "),
            "ai_actions": ai_actions.replace("\n", " ")
        }

        # Write to CSV (append)
        df_row = pd.DataFrame([row])
        header = not os.path.exists(DATA_PATH)
        df_row.to_csv(DATA_PATH, mode="a", header=header, index=False)

        st.success("Thanks! Your feedback was submitted.")
        st.write("**AI Response:**")
        st.info(ai_response)

st.markdown("---")
st.write("Examples: Try writing a short review like 'Food was cold and service slow' or 'Loved the ambience and desserts!'.")
