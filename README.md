# fynd_task2

📘 Fynd AI Intern – Task 2: Two-Dashboard AI Feedback System

A fully deployed AI-powered feedback collection and administration system built using Streamlit, OpenRouter LLMs, and a shared CSV datastore.

🚀 Live Demo Links
🔹 User Dashboard (Public):

👉 [https://your-user-dashboard-url.streamlit.app](https://fyndtask2-user.streamlit.app/)

🔹 Admin Dashboard (Internal):

👉[ https://your-admin-dashboard-url.streamlit.app](https://fyndtask2-adm.streamlit.app/)


📂 Repository Structure
.
├── app_user.py                 # User-facing dashboard
├── app_admin.py                # Admin dashboard
├── llm_utils.py                # Reusable LLM functions (summaries, responses, actions)
├── data/
│   └── submissions.csv         # Shared datastore (created automatically)
├── requirements.txt            # Streamlit + dependencies
└── README.md                   # Project documentation

📝 Project Overview

This system consists of two deployed dashboards that work together to collect customer feedback, generate AI insights, and present summarized analytics to administrators.

⭐ Task Objectives

Allow users to submit feedback (rating + review).

Generate AI-powered:

User-facing response

Review summary

Recommended business actions

Store all data in a shared CSV.

Provide an admin dashboard with:

Live submissions table

Summaries & recommendations

Analytics (charts, metrics)

🎨 Dashboards Overview
🧾 1. User Dashboard

Users can:

Select a rating (1–5)

Enter a written review

Submit feedback

Receive an AI-generated short response

The dashboard:

Sends the review to an LLM via OpenRouter

Generates:
✔ AI Response
✔ AI Summary
✔ Recommended Actions

Writes all fields to data/submissions.csv

📊 2. Admin Dashboard

Admins can view:

All user submissions (live)

AI summaries & recommendations

Average rating metric

Rating distribution chart

Top recommended actions

Downloadable CSV export

The dashboard automatically updates when new submissions are added.

🧠 LLM Usage

All AI outputs are generated using:

Model: deepseek/deepseek-chat
API Provider: OpenRouter
Functions implemented in llm_utils.py:

generate_user_response(review_text)

generate_summary(review_text)

generate_recommended_actions(review_text)

Prompts are optimized for:

Reliability

Short and clear responses

Zero temperature for stability

🔐 Secret Management (Important)

Your API key must NOT be stored in code.

Add it in Streamlit Cloud:

Secrets Panel → Add:
OPENROUTER_API_KEY = sk-or-v1-xxxxxxxxxxxxxxxx
OPENROUTER_MODEL = deepseek/deepseek-chat


Both apps (User + Admin) need the same secrets.

🛠️ Local Development Setup
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Set your API key
export OPENROUTER_API_KEY="sk-or-v1-xxxxxx"

3️⃣ Run User Dashboard
streamlit run app_user.py

4️⃣ Run Admin Dashboard
streamlit run app_admin.py


Local URLs:

User → http://localhost:8501

Admin → http://localhost:8502

🌐 Streamlit Cloud Deployment
1️⃣ Push this repo to GitHub
2️⃣ Create two separate Streamlit apps:

App 1 → app_user.py

App 2 → app_admin.py

3️⃣ Add secrets to each app:
OPENROUTER_API_KEY = sk-or-v1-xxxxxx
OPENROUTER_MODEL = deepseek/deepseek-chat

4️⃣ Deploy — Streamlit builds the app and gives you public access URLs

Include those URLs at the top of this README.

📈 Example Outputs
User Submission Example:
Rating: 4
Review: "The ambience was great but service was slow."
AI Response: "Thank you for your thoughtful feedback! We'll work on speeding up service."
AI Summary: "Good ambience but slow service."
AI Recommended Actions: 
- Improve staff response time  
- Monitor table wait duration

🎯 Key Features

✔ Clean and intuitive UI
✔ Real-time updates
✔ Secure API key handling
✔ Modular and scalable codebase
✔ AI-driven insights for admins
✔ Deployable with one click

🏁 Final Notes

This project successfully meets all requirements of Fynd AI Intern Task 2:

Two deployed dashboards

Shared datastore

LLM-powered summaries & recommendations

Deployment-ready code and documentation

For enhancements (authentication, SQLite storage, advanced analytics), feel free to request improvements.
