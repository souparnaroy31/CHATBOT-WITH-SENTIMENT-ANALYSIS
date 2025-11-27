from sentiment import analyze_sentiment
from chatbot import generate_bot_response

def main():
    conversation_history = []
    print("Chatbot: Hello! Start chatting. Type 'end' to finish.\n")

    while True:
        user_msg = input("User: ")
        if user_msg.lower() == "end":
            break

        sentiment, score = analyze_sentiment(user_msg)
        print(f"→ Sentiment: {sentiment}")
        conversation_history.append((user_msg, sentiment, score))

        bot_reply = generate_bot_response(user_msg)
        print(f"Chatbot: {bot_reply}\n")

    final_sentiment = summarize_conversation(conversation_history)
    print("\n===== FINAL SENTIMENT SUMMARY =====")
    print(f"Overall conversation sentiment: {final_sentiment}")
    print("===================================")

def summarize_conversation(history):
    total_score = sum(score for _, _, score in history)
    if total_score > 0.5:
        return "Positive – user is mostly satisfied."
    elif total_score < -0.5:
        return "Negative – user expressed dissatisfaction."
    else:
        return "Neutral – balanced mood."

if __name__ == "__main__":
    main()
