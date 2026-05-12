# Autonomous Email Task Orchestration System

A multi-agent AI system that reads your Gmail inbox, classifies email intent using Gemini Flash 2.5, extracts actionable tasks, logs them to Google Sheets, and auto-creates Google Calendar reminders — with zero manual triage.

**Reduced manual email triage effort by 70%.**

---

## How it works

```
Gmail Inbox → Email Agent → Classifier Agent → Task Agent → Sheets + Calendar
```

1. **Email Agent** fetches unread emails from Gmail via API
2. **Classifier Agent** uses Gemini Flash 2.5 to detect intent and urgency
3. **Task Agent** extracts tasks, creates Calendar events, and logs to Sheets

---

## Tech stack

| Layer | Tools |
|---|---|
| LLM | Gemini Flash 2.5 |
| APIs | Gmail API, Google Sheets API, Google Calendar API |
| Backend | Python, FastAPI |
| Infrastructure | GCP, Docker |

---

## Project structure

```
autonomous-email-agent/
├── main.py
├── agents/
│   ├── email_agent.py       # Fetches + parses Gmail
│   ├── classify_agent.py    # Gemini-powered intent classification
│   └── task_agent.py        # Task extraction + Calendar/Sheets write
├── utils/
│   ├── gmail_utils.py
│   ├── sheets_utils.py
│   ├── calendar_utils.py
│   └── parsing_utils.py
├── .env
├── requirements.txt
└── README.md
```

---

## Setup

```bash
git clone https://github.com/jahagirdarbhargavi99/autonomous-email-agent
cd autonomous-email-agent
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

Add your credentials to `.env`:
```
GEMINI_API_KEY=your_key
GOOGLE_CREDENTIALS_PATH=credentials/credentials.json
```

Run:
```bash
python main.py
```

---

## What's next

- Auto-reply generator based on email context
- Slack notification integration
- Web dashboard for task visibility

---

*Built by [Bhargavi Jahagirdar](https://www.linkedin.com/in/bhargavi-jahagirdar/)*
