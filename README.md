Autonomous Email Task Manager (Multi-Agent AI Workflow)  
<br/>A fully autonomous multi-agent AI system that reads your Gmail inbox, extracts tasks, classifies their urgency, logs them into Google Sheets, and auto-creates Google Calendar reminders.  
<br/>Features:  
\- Multi-Agent Architecture (3 Agents)  
\- AI-Powered Task Extraction  
\- Automatic Google Sheets Logging  
\- Google Calendar Reminders  
\- Clean Modular Codebase  
<br/>Project Structure:  
autonomous-email-agent/  
├── main.py  
├── agents/  
│ ├── email_agent.py  
│ ├── classify_agent.py  
│ └── task_agent.py  
├── utils/  
│ ├── gmail_utils.py  
│ ├── sheets_utils.py  
│ ├── calendar_utils.py  
│ └── parsing_utils.py  
├── credentials/  
│ ├── credentials.json  
│ └── token.json  
├── .env  
├── requirements.txt  
└── README.md  
<br/>Architecture Overview:  
Gmail Inbox → Email Agent → Classifier Agent → Task Agent → Sheets + Calendar  
<br/>Installation:  
1\. Clone repo  
2\. Create venv  
3\. Install requirements  
4\. Set environment variables  
5\. Run python main.py  
<br/>Future Improvements:  
\- Auto reply generator  
\- Slack notifications  
\- Dashboard UI