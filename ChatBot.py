import os
from dotenv import load_dotenv
from groq import Groq

# 1. Load the secret API key from .env file
load_dotenv()

# 2. Initialize the Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 3. System prompt setting up empathetic personality
system_prompt = (
    "You are MindfulTalk, a gentle, empathetic, and supportive companion. "
    "Your primary goal is to provide a safe space for the user to vent about stress and anxiety. "
    "Validate their emotions naturally, offer warm conversational comfort, and gently "
    "suggest grounding techniques (like deep breathing) if they feel overwhelmed."
)

# 4. Initialize chat history
messages = [
    {"role": "system", "content": system_prompt}
]

# 5. Display Welcome Banner & Medical Disclaimer
print("==================================================================")
print("              Welcome to MindfulTalk Companion                    ")
print("==================================================================")
print("⚠️  DISCLAIMER & SAFETY WARNING:")
print("MindfulTalk is an AI companion designed for conversational support only.")
print("It is NOT a medical tool, professional therapist, or crisis service.")
print("If you are experiencing severe distress, crisis, or mental health issues,")
print("please consult a doctor, qualified healthcare professional, or reach out")
print("to emergency medical services immediately.")
print("==================================================================\n")

print("MindfulTalk: Hello! I'm here to listen. What's on your mind today? (Type 'quit' to exit)\n")

# 6. Main Conversation Loop
while True:
    user_input = input("You: ")

    # Exit condition
    if user_input.lower().strip() in ["quit", "exit", "bye"]:
        print("\nMindfulTalk: Thank you for sharing with me today. Please take gentle care of yourself!")
        break

    # Skip empty lines
    if not user_input.strip():
        continue

    # Append user input to history
    messages.append({"role": "user", "content": user_input})

    try:
        # Request completion from Groq using Llama 3.3 70B
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama-3.3-70b-versatile",
            temperature=0.7
        )

        ai_reply = chat_completion.choices[0].message.content
        print(f"\nMindfulTalk: {ai_reply}\n")

        # Save AI response to history for context awareness
        messages.append({"role": "assistant", "content": ai_reply})

    except Exception as e:
        print(f"\nAn error occurred while communicating with the server: {e}\n")