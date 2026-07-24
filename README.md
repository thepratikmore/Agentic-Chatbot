### End to End Project Agentic AI Chatbots

# 🤖 Agentic AI Chatbot using LangGraph
An AI-powered multi-use-case chatbot built with **LangGraph, LangChain, Streamlit, Groq, and Tavily Search**. The project demonstrates graph-based AI workflows, tool calling, and AI News summarization through an interactive web interface.

## 📖 Project Overview

This project demonstrates how to build a modular Agentic AI application using LangGraph. It supports multiple AI workflows, including a basic chatbot, web search, and AI News summarization.
The application leverages Groq LLM for fast inference, Tavily Search for retrieving up-to-date information, and Streamlit for a clean, interactive user interface.


## ✨ Features

- 🤖 AI-powered conversational chatbot
- 🧠 Stateful conversation management with LangGraph
- 🔍 Web Search using Tavily Search API
- 📰 AI News Summarizer
- 📅 Supports Today, Last 7 Days and Last 30 Days AI news
- ⚡ Groq LLM integration for high-speed responses
- 🌐 Interactive Streamlit interface
- 🗂️ Modular project architecture
- 🔄 Graph-based workflow orchestration


## 🧠 Supported Use Cases

- 💬 Basic Chatbot
- 🔎 Chatbot with Web Search
- 📰 AI News Summarizer


## 📰 AI News Summarizer

The AI News feature retrieves the latest Artificial Intelligence news using Tavily Search and generates a concise summary using Groq LLM.
Supported frequencies:
- Today
- Last 7 Days
- Last 30 Days
The generated summary is saved as a Markdown file and displayed directly in the Streamlit application.


## 🛠️ Technologies

- Python
- LangChain
- LangGraph
- Streamlit
- Groq API
- Tavily Search API


## 📁 Project Structure

```text
Agentic-Chatbot
│
├── src/
│   └── langgraphagenticai/
│       ├── graph/
│       │   └── graph_builder.py
│       ├── nodes/
│       │   ├── basic_chatbot_node.py
│       │   ├── chatbot_with_tool_node.py
│       │   └── ai_news_node.py
│       ├── tools/
│       │   └── search_tool.py
│       ├── ui/
│       │   └── streamlitui/
│       ├── state/
│       │   └── state.py
│       ├── LLMS/
│       └── main.py
│
├── .env
├── app.py
├── requirements.txt
└── README.md
```


## ⚙️ Installation
git clone https://github.com/thepratikmore/Agentic-Chatbot.git

cd Agentic-Chatbot

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt


## 🔐Environment Variables
GROQ_API_KEY=your_api_key
TAVILY_API_KEY=your_tavily_api_key


## ▶️ Run the Project

```bash
streamlit run app.py
```
Open your browser and visit:

```
http://localhost:8501
```


## 🏗️ Architecture

```text
                    User
                      │
                      ▼
              Streamlit Interface
                      │
                      ▼
                LangGraph Workflow
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
 Basic Chatbot   Web Search     AI News
      Node          Node          Node
        │             │             │
        └─────────────┼─────────────┘
                      ▼
             Tavily Search Tool
                      │
                      ▼
                 Groq LLM
                      │
                      ▼
                 Final Response
```


## 🎥 Demo

# Basic Chatbot
<img width="949" height="468" alt="Chatbot" src="https://github.com/user-attachments/assets/f449bd6f-719d-481a-bd38-4e862ddfba96" />

# Chatbot With Web
<img width="960" height="470" alt="Chatbot with web" src="https://github.com/user-attachments/assets/9389d317-c67c-4a3c-a4ea-896150edab9a" />

<img width="960" height="459" alt="Chatbot with web2" src="https://github.com/user-attachments/assets/ef791a25-47a0-4d17-90ad-1d363329618e" />

# AI News Summarizer
<img width="960" height="471" alt="AI News summ" src="https://github.com/user-attachments/assets/93a5de4d-36be-40c0-838f-bc417119d384" />


## 📚 What I Learned

- 🤖 Building Agentic AI applications with LangGraph
- 🧠 Creating graph-based AI workflows
- 🔍 Integrating external tools using Tavily Search
- 📰 Building an AI-powered News Summarizer
- 💬 Developing conversational AI assistants
- ⚡ Integrating Groq LLM for fast inference
- 🎨 Developing interactive Streamlit applications
- 📦 Designing modular and scalable project architectures
- 🔄 Managing application state with LangGraph
- 🚀 End-to-end deployment and GitHub project management


## 📬 Connect With Me
LinkedIn:https://www.linkedin.com/in/pratik-b-more/
Email:pratikmoree21@gmail.com

