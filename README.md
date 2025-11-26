## 📧 Prompt-Driven Email Productivity Agent

AI-Powered Inbox Automation using Gemini API + Streamlit

This project is a prompt-driven Email Productivity Agent that automatically processes emails, categorizes them, extracts action items, drafts replies, and enables chat-style inbox interaction.
All behaviors are controlled through editable “Agent Brain” prompts.

Built with Python, Streamlit, and Gemini 1.5 Flash API.

## 🚀 Features
✅ Email Processing

Load a mock inbox (JSON)

Automatic email categorization

Extract tasks/action items

Save processed outputs


## 🤖 Agent-Driven Inbox Chat

Ask the agent to summarize any email

Ask: “What tasks do I need to do?”

Ask: “Draft a reply in friendly tone”

General inbox queries (“Show all urgent emails”)


## 📝 Draft Generation Agent

Auto-draft replies using your prompt

Edit and save drafts (not sent automatically)

Safe-mode drafts only


## $$ 🧠 Prompt-Driven Architecture

You can edit:

Categorization Prompt

Action-Item Extraction Prompt

Auto-Reply Prompt

All LLM processing uses your saved prompts.

## 📂 Project Structure
```bash
Email_Agent_Project/
│
├── app.py                  # Main Streamlit application
├── utils.py                # LLM + backend functions (Gemini version)
├── .env                    # Stores Gemini API key
│
├── assets/
│   ├── inbox.json          # Mock inbox (10–20 sample emails)
│   └── prompts.json        # Default prompt templates
│
└── README.md               # Documentation file

```


## 🛠️ Installation & Setup
1️⃣ Clone or download the project
```bash
git clone https://github.com/Anshraut9/Ocean_AI_Assignment
cd Email_Agent_Project
```

2️⃣ Create and activate a virtual environment
Windows
```bash
python -m venv venv
.\venv\Scripts\activate
```

Mac/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

3️⃣ Install required dependencies
```bash
pip install streamlit google-generativeai python-dotenv pandas
```

4️⃣ Add your Gemini API key

Create a file named .env in the project root:
```bash
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY_HERE
```

You can get a free key from:
```bash
🔗 https://aistudio.google.com
```


##▶️ Running the Application

Start the Streamlit app:
```bash
streamlit run app.py
```

A browser will open automatically 

📥 Loading the Mock Inbox

Your mock inbox file is located at:

assets/inbox.json



# It contains 10–20 sample emails including:

Meeting requests

Work updates

Spam-like emails

Newsletters

Task requests

The system loads it automatically on startup.


# 🧠 Configuring Prompts (Agent Brain)

On the left sidebar, you can edit 3 prompts:

Categorization Prompt

Action Extraction Prompt

Auto-Reply Draft Prompt

Click Save Prompts to update the internal “agent brain”.

Changing the prompt instantly changes the agent’s behavior.



## 📥 Phase 1 – Inbox Processing

Go to the Inbox & Processing tab → Click:

Process Inbox (Run LLM)

The agent will:

Read each email

Categorize it

Extract action items

Save results to UI state

A progress bar shows processing status.



## 🤖 Phase 2 – Email Agent Chat

Select an email → ask questions like:

“Summarize this email”

“What should I do here?”

“Draft a polite reply”

“Show all urgent emails”

The agent uses:

The selected email

Your stored prompts

Your query

to generate a reply.



## 📝 Phase 3 – Draft Generation

Go to Drafts tab:

Select an email

Click Generate Draft Reply

The draft uses:

Auto-reply prompt



## 🙌 Credits

Built using:

🧠 Google Gemini API

📊 Streamlit UI Framework

🐍 Python

Email content

Gemini API

Draft is displayed safely (not sent automatically).
