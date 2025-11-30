import base64
from utils.parsing_utils import clean_email, extract_email_body
from utils.gmail_utils import gmail_service

class EmailAgent:

    def __init__(self, creds):
        self.service = gmail_service(creds)

    def get_unread_emails(self, max_results=10):
        print("\nEmailAgent: Fetching unread emails...")
        results = self.service.users().messages().list(
            userId="me",
            labelIds=["UNREAD"],
            maxResults=max_results
        ).execute()

        messages = results.get("messages", [])
        emails = []

        for msg in messages:
            full_msg = self.service.users().messages().get(
                userId="me",
                id=msg["id"],
                format="full"
            ).execute()

            payload = full_msg.get("payload", {})
            email_text = extract_email_body(payload)

            if not email_text.strip():
                email_text = "(No readable body text found)"

            emails.append(email_text)

        print(f"EmailAgent: Found {len(emails)} emails.")
        return emails
