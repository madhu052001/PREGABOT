from flask import Flask, request, jsonify, render_template, session
from flask_cors import CORS
from pymongo import MongoClient
import pandas as pd
from googletrans import Translator
from datetime import timedelta
import os
from googleapiclient.discovery import build
import google.generativeai as gemini_genai

app = Flask(__name__)
CORS(app)

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = 'MY_SECRETKEY'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=180)

gemini_api_key = os.getenv('Gemini-key')
gemini_genai.configure(api_key=gemini_api_key)
model = gemini_genai.GenerativeModel('gemini-1.5-flash')

translator = Translator()

knowledge_base_df = pd.read_excel('pregabot.xlsx')

client = MongoClient("mongodb+srv://ahana2003:ahanabiswas03@wombwhisper.0llkl.mongodb.net/")
db = client['Wombwhisper']
users_collection = db['users']

response_cache = {}

# Route for the chatbot frontend
@app.route('/')
def home():
    return render_template('index.html')

# Endpoint for processing chat messages
@app.route('/api/chat', methods=['POST'])
def chat():
    session.permanent = True  # Extend session for 30 more minutes with each request
    data = request.json
    user_message = data['message'].strip().lower()  # Convert to lowercase for uniformity
    user_id = data['user_id']
    target_language = data.get('language', 'en')  # Default to English if no language is provided

    translated_message = translator.translate(user_message, dest='en').text

    user_details = users_collection.find_one({'username': user_id})
    if not user_details:
        return jsonify({'response': 'User not found.'})

    # Handle "yes" or "no" responses based on the last bot question
    last_bot_question = session.get('last_bot_question', '')

    if translated_message in ['yes', 'no']:
        if last_bot_question:
            # Process the "yes" or "no" based on the last bot question
            response = handle_yes_no_response(translated_message, last_bot_question, user_details)
        else:
            response = "I'm sorry, I don't have a context for that. Can you please elaborate?"
    else:
        # Process the normal user message
        response = generate_response(translated_message, user_details)

    if not response:
        response = "I’m here to assist you with anything related to your pregnancy journey. Feel free to ask!"

    # Store the last bot question for future reference (if it's a question or guidance)
    if is_bot_question(response):
        session['last_bot_question'] = response

    translated_response = translator.translate(response, dest=target_language).text

    full_response = f"{translated_response}".strip()

    return jsonify({'response': full_response})

def is_bot_question(response):
    # Simple check if the response is a question or guidance
    return response.endswith('?') or "would you like" in response.lower()

def handle_yes_no_response(user_response, last_question, user_details):
    if user_response == 'yes':
        return f"Great! Based on our previous discussion, here's how we can proceed with {last_question}."
    else:
        return f"Okay, let's skip that for now. Feel free to ask me something else."

def extract_excel_context(message):
    context_responses = []
    for index, row in knowledge_base_df.iterrows():
        if any(keyword in message.lower() for keyword in str(row['Category']).split()) or \
           any(keyword in message.lower() for keyword in str(row['Information']).split()):
            context_responses.append(str(row['Information']))

    combined_context = " ".join(context_responses)
    return combined_context[:500]

def generate_response(message, user_details):
    if message in response_cache:
        print("Serving from cache!")  # Optional: Log cache hit
        return response_cache[message]

    pregnancy_details = user_details.get('pregnancyDetails', {})
    disorders = ', '.join(pregnancy_details.get('disorders', [])) or 'none'
    relevant_context = extract_excel_context(message)

    prompt = f"""You are a helpful assistant specialized in pregnancy-related information.
    The user is {user_details.get('name', 'a person')}, pregnant with the following conditions: {disorders}.
    Here is some relevant medical context: {relevant_context}.
    Please generate a helpful, compassionate, and personalized response to the user's query: '{message}'."""

    try:
        response = model.generate_content(prompt)
        ai_generated_response = response.text.strip()

        response_cache[message] = ai_generated_response
        return ai_generated_response

    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return "There was an error generating the response. Please try again later."

if __name__ == '__main__':
    app.run(debug=True)