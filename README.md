#  Intelligent Pregnancy Chatbot

## Overview

The **Pregnancy Chatbot** or **PREGABOT** is a smart and dynamic tool designed to assist pregnant women by providing tailored, accurate, and user-friendly responses to their queries. The chatbot supports multilingual input and output, ensuring accessibility for users from diverse linguistic backgrounds. By combining a static dataset with dynamic API integration, the system provides precise and meaningful assistance.

**Note**: This project is a work in progress and will be further enhanced with additional features and optimizations.

---

## Features

### Core Functionalities:
1. **Query Validation**:
   - User queries are cross-checked with a curated dataset named **`pregabot.xlsx`** to confirm if they are valid pregnancy-related questions.

2. **Dynamic Response Generation**:
   - For validated queries, dynamic and detailed responses are generated using the **GEMINI API**, enabling precise and informative answers.

3. **Multilingual Input and Output**:
   - Users can interact with the chatbot in their preferred language.
   - The chatbot processes user inputs in different languages and provides responses in the same language.

4. **Recommended Questions**:
   - Suggests follow-up questions to help users explore their pregnancy journey more comprehensively.

5. **Secure Data Handling**:
   - Implements robust APIs and security protocols to protect user interactions and ensure safe handling of personal data.

---

## How It Works

1. **Multilingual Input Processing**:
   - The chatbot accepts inputs in the user’s preferred language using natural language processing (NLP) libraries.
   - It translates and validates the input using the **`pregabot.xlsx`** dataset and other NLP tools.

2. **Query Validation**:
   - Inputs are compared against the `pregabot.xls` dataset to verify relevance and validity.

3. **Dynamic Response Generation**:
   - Valid queries are processed through the **GEMINI API** for dynamic and context-aware responses.
   - Responses are translated back to the user’s preferred language for seamless interaction.

4. **User Guidance**:
   - The chatbot provides detailed answers and offers follow-up questions to enhance understanding.

---

## Tech Stack

- **Backend**: Python
- **Database**: MongoDB
- **Dataset**: `pregabot.xlsx`
- **API**: GEMINI API
- **NLP Libraries**: BERT (BioBERT, Clinical BERT), NLTK, Stanford NLP
- **Translation Libraries**: Integrated tools for multilingual input/output support

---

## Installation and Setup

1. Clone this repository.
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the **GEMINI API KEY** in the environment file (`.env`) as follows:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```
4. Add the `pregabot.xls` dataset to the project directory.
5. Start the chatbot server:
   ```bash
   python chatbot.py
   ```

---

## Future Enhancements

1. **Expanded Dataset**:
   - Enrich the `pregabot.xls` dataset for a broader scope of validation.
2. **Image Analysis**:
   - Allow image uploads for analyzing pregnancy symptoms and tracking growth milestones.
3. **Enhanced Multilingual Features**:
   - Improve input/output language processing for less commonly spoken languages.
4. **Faster Query Processing**:
   - Optimize integration between the dataset and GEMINI API for reduced response times.

---

## License and Team

Developed by **Team GEEK_ELITE** as part of Hackspire2024.  

- **Team Leader**: Madhurima Saha  
- **Team Members**: Ahana Biswas, Anusree Dam, Rajarshi Bhattacharya  

For inquiries, contact the team at **[sahamadhu558@gmail.com]**.
