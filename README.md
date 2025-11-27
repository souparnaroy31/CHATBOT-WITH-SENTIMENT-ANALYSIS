# CHATBOT-WITH-SENTIMENT-ANALYSIS
#1. Project Overview

This project implements a Python-based chatbot that conducts conversations with users and performs sentiment analysis.
The system supports Tier 1 (mandatory) and Tier 2 (additional credit) requirements as given in the assignment.

The chatbot maintains the full conversation history, generates responses, and evaluates the emotional tone of the conversation using sentiment analysis.

# Features
 # Tier 1 – Mandatory Requirement: Conversation-Level Sentiment Analysis

The system stores every user message throughout the session.

At the end of the conversation, the chatbot evaluates the overall emotional direction of the full conversation.

Final output shows whether the mood of the user was:

Positive

Negative

Neutral

# Tier 2 – Additional Credit: Statement-Level Sentiment Analysis

Each user message is individually analyzed in real-time.

Sentiment for each message is displayed as soon as it is entered.

Sentiments shown:
Positive / Negative / Neutral

Optional enhancement:
The project also calculates a mood trend by adding up polarity scores.

# Technologies Used

Python 3.x

TextBlob (for sentiment polarity scoring)

Basic rule-based chatbot logic

Modular design for production-minded structure

# 4. Sentiment Analysis Logic
TextBlob Polarity Score

Each message receives a polarity score between -1.0 to +1.0:

+1.0 → Very Positive

0 → Neutral

-1.0 → Very Negative

Classification Rules
Score > 0.2     → Positive  
Score < -0.2    → Negative  
Otherwise       → Neutral

Conversation-Level Sentiment

The final sentiment is computed by summing all polarity scores from the entire chat.

Rules:

Total score > 0.5     → Overall Positive  
Total score < -0.5    → Overall Negative  
Otherwise             → Overall Neutral

# 5. Project Structure
chatbot-sentiment/
│
├── src/
│   ├── chatbot.py          # Chatbot reply logic
│   ├── sentiment.py        # Sentiment analysis module
│   └── main.py             # Main program (run this)
│
├── tests/
│   └── test_sentiment.py   # Basic unit tests (optional)
│
├── README.md
└── requirements.txt

# Example Execution
Chatbot: Hello! Start chatting. Type 'end' to finish.

User: Your service disappoints me
→ Sentiment: Negative
Chatbot: I’m sorry to hear that. Please tell me more.

User: Last experience was better
→ Sentiment: Positive
Chatbot: I understand. Could you explain more?


