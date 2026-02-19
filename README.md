🧠 Local AI Chatbot Suite (Ollama + Streamlit)

A collection of locally hosted AI chatbot applications powered by Ollama (Gemma 3) and Streamlit.

This project contains three AI applications:

🎭 Character AI (Role-Based Chatbot)

🧠 Local AI Chatbot (Configurable Assistant)

🚀 NeuroFlux Cognitive Engine (4-Word Jargon AI)

All apps run fully offline using gemma3:latest via Ollama.

📦 Project Structure
.
├── characterBOT.py     # Role-based character chatbot
├── chatbot.py          # Configurable local chatbot
├── jargonwhat.py       # 4-word thinking + jargon AI
└── README.md

⚙️ Requirements
1️⃣ Install Ollama

Download and install Ollama:

👉 https://ollama.com

Pull the required model:

ollama pull gemma3:latest


Start Ollama server:

ollama serve


Default API runs on:

http://localhost:11434

2️⃣ Install Python Dependencies
pip install streamlit ollama requests

🎭 1. Character AI (characterBOT.py)

A role-based conversational AI with selectable personalities.

✨ Features

Multiple character personas:

👑 Royal Knight

🌸 Anime Friend

💼 CEO Mentor

Conversation memory

Sidebar character selector

Chat history persistence (session-based)

Uses Ollama REST API

🧠 Architecture

Frontend: Streamlit

Backend: Ollama REST API (/api/generate)

Model: gemma3:latest

Non-streaming response mode

▶️ Run
streamlit run characterBOT.py

🧠 2. Local AI Chatbot (chatbot.py)

A configurable local LLM chat interface using Ollama Python SDK.

✨ Features

Model selector

Adjustable temperature (0.0 – 1.5)

Chat memory via st.session_state

Clear chat option

Clean centered UI

🧠 Architecture

Uses ollama.chat() (native Python SDK)

Real-time LLM interaction

Session-based memory

Configurable inference parameters

▶️ Run
streamlit run chatbot.py

🚀 3. NeuroFlux Cognitive Engine (jargonwhat.py)

A structured-thinking AI that:

Thinks step-by-step

Shows reasoning inside <thinking> tags

Replies in exactly 4 words

Uses creative business/tech jargon

No requests, time, or re modules

✨ Features

Strict output formatting

High creativity temperature

Clean futuristic UI

Controlled prompt engineering

🧠 Output Format Example
<thinking>
Analyzing strategic opportunity...
Optimizing solution framing...
Compressing to four-word output...
</thinking>

Final: Scalable Quantum Growth Matrix

▶️ Run
streamlit run jargonwhat.py

🔌 Model Configuration

All applications use:

gemma3:latest


You may change the model inside the scripts if needed.

🏗️ System Architecture Overview
User → Streamlit UI → Ollama (Local LLM) → Gemma 3 → Response → UI


No cloud APIs required.
Fully local.
Privacy-safe.

🔒 Offline Capability

This project:

✅ Runs completely offline
✅ Does not require OpenAI API
✅ Keeps all data local
✅ No external cloud dependency

🧪 Customization Guide
Change Model

Replace:

model="gemma3:latest"


With:

model="your-model-name"

Adjust Creativity

Modify:

options={"temperature": 0.7}


Higher → More creative
Lower → More deterministic

🛠️ Troubleshooting
Ollama not responding?

Make sure:

ollama serve


is running.

Model not found?

Run:

ollama pull gemma3:latest

Port Issue?

Default Ollama API:

http://localhost:11434


Ensure nothing else uses that port.

📈 Future Improvements

Streaming responses

Token usage display

Multi-model switching

Persistent database memory

Docker containerization

Authentication layer

📄 License

This project is open-source and intended for educational and local AI experimentation purposes.

👨‍💻 Author

Developed using:

Streamlit

Ollama

Gemma 3 LLM
