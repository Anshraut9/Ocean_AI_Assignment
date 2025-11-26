import streamlit as st
import pandas as pd
import json
from utils import load_data, save_prompts, analyze_email

# --- Page Config ---
st.set_page_config(page_title="Email Agent", layout="wide")
st.title("📧 Prompt-Driven Email Productivity Agent")

# --- Load Assets ---
INBOX_PATH = 'assets/inbox.json'
PROMPTS_PATH = 'assets/prompts.json'

if 'emails' not in st.session_state:
    st.session_state.emails = load_data(INBOX_PATH)
if 'prompts' not in st.session_state:
    st.session_state.prompts = load_data(PROMPTS_PATH)

# --- Sidebar: Prompt Brain (Configuration) ---
with st.sidebar:
    st.header("🧠 Agent Brain (Prompts)")
    st.info("Edit these prompts to change how the agent behaves.")
    
    # Allow user to edit prompts
    cat_prompt = st.text_area("Categorization Prompt", st.session_state.prompts['categorization'])
    act_prompt = st.text_area("Action Extraction Prompt", st.session_state.prompts['action_item'])
    reply_prompt = st.text_area("Auto-Reply Prompt", st.session_state.prompts['auto_reply'])
    
    if st.button("Save Prompts"):
        st.session_state.prompts = {
            "categorization": cat_prompt,
            "action_item": act_prompt,
            "auto_reply": reply_prompt
        }
        save_prompts(PROMPTS_PATH, st.session_state.prompts)
        st.success("Prompts updated!")

# --- Main Tabs ---
tab1, tab2, tab3 = st.tabs(["📥 Inbox & Processing", "🤖 Email Agent Chat", "📝 Drafts"])

# --- TAB 1: Inbox ---
with tab1:
    st.subheader("Inbox Processing")
    
    if st.button("Process Inbox (Run LLM)"):
        progress_bar = st.progress(0)
        for idx, email in enumerate(st.session_state.emails):
            # Run Categorization
            email['category'] = analyze_email(email['body'], st.session_state.prompts['categorization'])
            # Run Action Extraction
            email['actions'] = analyze_email(email['body'], st.session_state.prompts['action_item'])
            progress_bar.progress((idx + 1) / len(st.session_state.emails))
        st.success("Inbox Processed!")

    # Display Inbox as a Table
    if st.session_state.emails:
        df = pd.DataFrame(st.session_state.emails)
        
        # Check if we have processed the emails yet
        if 'category' in df.columns and 'actions' in df.columns:
            # If processed, show full details
            st.dataframe(df[['sender', 'subject', 'category', 'actions']])
        else:
            # If NOT processed yet, show only available columns
            st.info("Click 'Process Inbox' to see categories and actions.")
            st.dataframe(df[['sender', 'subject']])
    else:
        st.warning("Inbox is empty or failed to load.")

# --- TAB 2: Email Agent Chat ---
with tab2:
    st.subheader("Chat with your Inbox")
    
    # Select an email to talk about
    email_options = {f"{e['sender']}: {e['subject']}": e for e in st.session_state.emails}
    selected_option = st.selectbox("Select an email context:", list(email_options.keys()))
    selected_email = email_options[selected_option]
    
    st.write(f"**Viewing:** {selected_email['subject']}")
    st.text_area("Content", selected_email['body'], disabled=True, height=100)
    
    user_query = st.text_input("Ask the Agent (e.g., 'Summarize this', 'Draft a rude reply')")
    
    if user_query and st.button("Ask Agent"):
        # Combine user query with the specific email content
        agent_prompt = f"User Query: {user_query}\n\nContext Email: {selected_email['body']}"
        response = analyze_email(agent_prompt, "You are a helpful assistant analyzing a specific email.")
        st.chat_message("assistant").write(response)

# --- TAB 3: Draft Generation ---
with tab3:
    st.subheader("Auto-Drafting")
    
    target_email = st.selectbox("Select email to reply to:", list(email_options.keys()), key="draft_select")
    target_data = email_options[target_email]
    
    if st.button("Generate Draft Reply"):
        with st.spinner("Drafting..."):
            # Use the stored Prompt Logic
            draft = analyze_email(target_data['body'], st.session_state.prompts['auto_reply'])
            st.text_area("Generated Draft (Safe Mode - Not Sent)", draft, height=300)
            st.success("Draft saved to local state.")