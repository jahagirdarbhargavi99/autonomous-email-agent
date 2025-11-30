from googleapiclient.discovery import build
from datetime import datetime, timedelta

def create_calendar_reminder(creds, summary, full_email, urgency):

    print("Creating Calendar Reminder...")

    service = build("calendar", "v3", credentials=creds)

    now = datetime.now()

    if urgency == "High":
        minutes = 1
    elif urgency == "Medium":
        minutes = 12 * 60
    else:
        minutes = 48 * 60

    start = now + timedelta(minutes=1)
    end = now + timedelta(minutes=30)

    event = {
        "summary": f"[Task] {summary}",
        "description": full_email,
        "start": {"dateTime": start.isoformat(), "timeZone": "America/New_York"},
        "end": {"dateTime": end.isoformat(), "timeZone": "America/New_York"},
        "reminders": {
            "useDefault": False,
            "overrides": [
                {"method": "popup", "minutes": minutes}
            ]
        }
    }

    created = service.events().insert(calendarId="primary", body=event).execute()

    print("Reminder created:", created.get("htmlLink"))
