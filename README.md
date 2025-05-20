# 💬 NeoChat – AI Chatbot with LangChain & Ollama

NeoChat is a lightweight and intelligent chatbot built using **Flask**, **LangChain**, and **Ollama** with the `gemma:2b` language model. It simulates a helpful AI assistant capable of answering general knowledge and conversational queries.

---

## 🚀 Features

- 🧠 Uses **LangChain** for intelligent prompt handling
- 🤖 Powered by **Ollama's gemma:2b** language model
- 🌐 Built with **Flask** to serve both API and web interface
- 📩 Simple JSON API to communicate with the chatbot
- 🎨 Clean frontend (HTML + Tailwind CSS)

---

## 📅 Knowledge Limitation Notice

NeoChat uses the `gemma:2b` model which has a **knowledge cutoff date of September 2023**.

This means:

- The chatbot does **not know about events, tools, or changes** that happened **after September 2023**
- It may give outdated or incorrect answers to questions about recent events

> 💡 Example:
> - ✅ “What is LangChain?” → Correct response  
> - ❌ “Who is the current president of the US?” → Might be outdated

---

## 📁 Project Structure

Chat-Bot/
├── chatbot/
│ ├── app.py # Flask backend
│ ├── templates/
│ │ └── index.html # Frontend page
│ └── static/ # (Optional) Static files
├── requirements.txt # Python packages





☁️ Deployment
This project runs locally via Flask + Ollama and is not deployable on GitHub Pages.

Here are some free deployment platforms you can explore:

Platform	Flask Support	Notes
🔁 Replit	✅	Quick to set up; needs manual model handling
🚀 Render	✅	Ideal for Python/Flask deployment
⚙️ Railway	✅	Great for backend services
🧪 Fly.io	✅	Docker-based advanced deployment
🛑 GitHub Pages	❌	Static sites only – no backend support
📦 Requirements
Python 3.8+

Flask

LangChain

Ollama

langchain_ollama
