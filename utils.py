import json
import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Load the Environment Variables
load_dotenv()

# 2. Configure the Google Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def load_data(filepath):
    """Loads JSON data from assets"""
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return []

def save_prompts(filepath, data):
    """Saves modified prompts back to JSON"""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def analyze_email(email_body, prompt_template):
    """
    Sends email content + instructions to Google Gemini 2.5 Pro
    """
    try:
        # Initialize the Model
        model = genai.GenerativeModel('gemini-2.5-pro')
        
        # Construct the full prompt
        full_prompt = f"{prompt_template}\n\nEMAIL CONTENT:\n{email_body}"
        
        # Generate the content
        response = model.generate_content(full_prompt)
        
        # Return the text result
        return response.text
        
    except Exception as e:
        return f"Error: {str(e)}"