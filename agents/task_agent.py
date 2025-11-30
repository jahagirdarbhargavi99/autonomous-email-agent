from utils.sheets_utils import write_row_to_sheet
from utils.calendar_utils import create_calendar_reminder

class TaskAgent:

    def __init__(self, creds):
        self.creds = creds

    def process_task(self, summary, category, full_email, urgency):
        print("\nTaskAgent: Processing task...")

        # 1) WRITE TO SHEETS
        write_row_to_sheet(
            creds=self.creds,
            summary=summary,
            category=category,
            full_email=full_email,
            urgency=urgency
        )

        # 2) CREATE REMINDER
        create_calendar_reminder(
            creds=self.creds,
            summary=summary,
            full_email=full_email,
            urgency=urgency
        )

        print("TaskAgent: Task saved + reminder created.")
