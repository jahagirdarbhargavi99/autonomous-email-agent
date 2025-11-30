import time
from googleapiclient.discovery import build
from datetime import datetime

SHEET_ID = "1xQSYv0i-HyXwjelK0LSsIHr0yYVzWYusj6dVfrCqVNs"   # <-- UPDATE THIS

def write_row_to_sheet(creds, summary, category, full_email, urgency):
    print("\nWriting to Google Sheets...")

    service = build("sheets", "v4", credentials=creds, cache_discovery=False)

    row = [
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        summary,
        category,
        full_email[:2000],
        "Pending",
        urgency
    ]

    body = {"values": [row]}

    service.spreadsheets().values().append(
        spreadsheetId=SHEET_ID,
        range="Sheet1!A:F",
        valueInputOption="RAW",
        body=body
    ).execute()

    print("✔ Sheet updated.")
