import streamlit as st
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

st.set_page_config(page_title="Character AI", page_icon="🎭")

st.title("🎭 Character AI (Gemma 3)")
st.caption("Powered by Ollama")

# ------------------ CHARACTER OPTIONS ------------------ #
characters = {
    "Royal Knight 👑": """
You are Arion, a noble royal knight.
Speak with honor and medieval tone.
""",
    "Anime Friend 🌸": """
You are a cheerful anime best friend.
Energetic and supportive.
""",
    "CEO Mentor 💼": """
You are a strategic CEO mentor.
Give clear and powerful advice.
"""
}

selected_character = st.sidebar.selectbox("Choose Character", list(characters.keys()))

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []

# Show previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Build prompt
    full_prompt = characters[selected_character] + "\n"

    for msg in st.session_state.messages:
        role = "User" if msg["role"] == "user" else "Assistant"
        full_prompt += f"{role}: {msg['content']}\n"

    full_prompt += "Assistant:"

    # Call Ollama (no streaming)
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "gemma3:latest",
            "prompt": full_prompt,
            "stream": False
        }
    )

    bot_reply = response.json()["response"]

    st.chat_message("assistant").markdown(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})