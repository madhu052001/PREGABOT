# README: Intelligent Pregnancy Chatbot

## Overview  

The **Intelligent Pregnancy Chatbot** or **PREGABOT** is a dynamic, user-friendly, and personalized chatbot designed to assist pregnant women by providing accurate and tailored responses to their queries. It combines query validation through a curated dataset with dynamic API integration for reliable answers. The chatbot ensures accessibility by supporting both multilingual input and output, leveraging the Google Translation API for seamless language processing. Robust security protocols are incorporated to safeguard user interactions and sensitive data.  

**Note**: This project is a work in progress, and additional features and optimizations are being developed.  

---

## Features  

### Core Functionalities:  
1. **Personalized Responses**:  
   - The chatbot tailors its responses based on the user’s query context, ensuring relevant and helpful answers.  

2. **Query Validation**:  
   - User queries are validated against a curated dataset named **`pregabot.xlsx`** to determine if they are pregnancy-related.  

3. **Dynamic Response Generation**:  
   - Validated queries are processed using the **GEMINI API**, ensuring accurate, tailored, and dynamic responses.  

4. **Multilingual Input and Output**:  
   - Users can ask queries and receive responses in their preferred language, thanks to the integration of the **Google Translation API**.  

5. **Recommended Questions**:  
   - The chatbot suggests relevant follow-up questions to guide users in exploring their pregnancy journey further.  

6. **Security Protocols**:  
   - **End-to-End Encryption**: Ensures secure communication between the chatbot and the user.  
   - **Token-Based Authentication**: Uses authentication tokens for secure API calls to the GEMINI and Google Translation APIs.  
   - **Data Sanitization**: Prevents injection attacks by sanitizing user inputs.  
   - **Secure Database Management**: Implements encrypted storage for sensitive user data in MongoDB.  

---

## How It Works  

1. **Multilingual Input Processing**:  
   - The chatbot accepts user queries in any supported language and translates them into the system's working language using the **Google Translation API**.  

2. **Query Validation**:  
   - The translated query is checked against the **`pregabot.xlsx`** dataset to ensure it is valid and relevant to pregnancy topics.  

3. **Response Generation**:  
   - For validated queries, the chatbot uses the **GEMINI API** to provide dynamic, personalized, and context-aware responses.  
   - The responses are translated back to the user’s preferred language via the **Google Translation API**.  

4. **Security Measures**:  
   - All API communications are encrypted, and user queries and responses are anonymized before processing.  
   - Sensitive data is not stored persistently unless explicitly required for further processing.  

5. **User Assistance**:  
   - Detailed responses and recommended follow-up questions are provided to enhance the user’s experience.  

---

## Tech Stack  

- **Backend**: Python  
- **Database**: MongoDB  
- **Dataset**: `pregabot.xlsx`  
- **APIs**:  
  - GEMINI API (for dynamic responses)  
  - Google Translation API (for multilingual input and output)  
- **Security Protocols**:  
  - End-to-End Encryption  
  - Token-Based Authentication  
  - Data Sanitization  

---

## Installation and Setup  

1. Clone the repository to your local machine.  
2. Install required Python dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3. Set up the **GEMINI API KEY** and **Google Translation API KEY** in the environment file (`.env`) as follows:  
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here  
   GOOGLE_API_KEY=your_google_translation_api_key_here  
   ```  
4. Add the `pregabot.xlsx` dataset to the project directory.  
5. Run the chatbot server:  
   ```bash
   python chatbot.py  
   ```  

---

## Future Enhancements  

1. **Enhanced Dataset**:  
   - Expand the `pregabot.xlsx` dataset for broader query validation coverage.  

2. **Image Support**:  
   - Enable image-based query handling for analyzing pregnancy symptoms or tracking growth milestones.  

3. **Advanced NLP Integration**:  
   - Replace or supplement the Google Translation API with advanced NLP libraries for better natural language understanding and response generation.  

4. **Mobile Application**:  
   - Develop a mobile-friendly interface for broader accessibility.  

5. **Improved Security**:  
   - Implement two-factor authentication (2FA) for user accounts and enhance encryption algorithms.  

---

## License and Team  

Developed by **Team GEEK_ELITE** as part of Hackspire2024.  

- **Team Leader**: Madhurima Saha  
- **Team Members**: Ahana Biswas, Anusree Dam, Rajarshi Bhattacharya  

For inquiries, contact the team at **[sahamadhu558@gmail.com]**.  
