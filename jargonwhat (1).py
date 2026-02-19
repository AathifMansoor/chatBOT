import streamlit as st
import ollama

st.set_page_config(page_title="NeuroFlux Clean", page_icon="🧠")

st.title("🧠 NeuroFlux Cognitive Engine")
st.caption("No requests. No time. No regex.")

SYSTEM_PROMPT = """
You are NeuroFlux, a futuristic AI strategist.

Rules:
1. First think step-by-step.
2. Show reasoning inside <thinking> tags.
3. Then give final answer in EXACTLY 4 words.
4. Final answer must use creative tech/business jargon.

Format:

<thinking>
reasoning here
</thinking>

Final: four word answer
"""

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Enter query...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Call Ollama directly
    response = ollama.generate(
        model="gemma3:latest",
        prompt=SYSTEM_PROMPT + "\nUser: " + user_input + "\nAssistant:",
        options={
            "temperature": 1.0
        }
    )

    reply = response["response"]

    with st.chat_message("assistant"):
        st.markdown(reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })