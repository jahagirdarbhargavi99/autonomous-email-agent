import os
import json
from dotenv import load_dotenv
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

import google.generativeai as genai  # <-- IMPORTANT

from agents.email_agent import EmailAgent
from agents.classify_agent import ClassifierAgent
from agents.task_agent import TaskAgent

# ============================
# Load environment + configure Gemini ONCE
# ============================
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
print("Loaded Gemini Key:", api_key)  # DEBUG

genai.configure(api_key=api_key)  # <-- CRITICAL


# ============================
# OAuth Authentication
# ============================
SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/calendar"
]

def authenticate():
    token_path = "credentials/token.json"

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
        if creds and creds.valid:
            print("Using existing token...")
            return creds

    print("Starting OAuth flow...")
    flow = InstalledAppFlow.from_client_secrets_file(
        "credentials/credentials.json", SCOPES
    )
    creds = flow.run_local_server(port=0)

    with open(token_path, "w") as f:
        f.write(creds.to_json())

    print("Token saved.")
    return creds


# ============================
# MAIN
# ============================
if __name__ == "__main__":
    creds = authenticate()

    email_agent = EmailAgent(creds)
    classifier_agent = ClassifierAgent()  # NOW Gemini is already configured
    task_agent = TaskAgent(creds)

    unread_emails = email_agent.get_unread_emails()

    if not unread_emails:
        print("\nNo unread emails.")
        exit()

    for email in unread_emails:
        print("\n====================== EMAIL ======================")
        print(email[:300], "...")

        data = classifier_agent.classify(email)

        summary = data["summary"]
        category = data["category"]
        urgency = data["urgency"]

        task_agent.process_task(summary, category, email, urgency)

        print("--------------------------------------------------\n")
