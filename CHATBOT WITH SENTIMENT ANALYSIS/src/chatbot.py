def generate_bot_response(user_message):
    user_message = user_message.lower()
    if "hello" in user_message or "hi" in user_message:
        return "Hello! How can I assist you today?"
    if "problem" in user_message or "issue" in user_message:
        return "I’m sorry to hear that. Please tell me more."
    if "thank" in user_message:
        return "You’re welcome! Let me know if you need anything else."
    return "I understand. Could you explain more?"
