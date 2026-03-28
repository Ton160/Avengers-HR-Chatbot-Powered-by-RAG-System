# 🦸‍♂️ Avengers HR Chatbot – Powered by RAG System

## Project Overview
**Avengers HR Chatbot** is an interactive HR assistant built with **LangChain** and **Streamlit**, designed to answer human resources questions for the Avengers Global Alliance Inc.  
This project leverages **RAG (Retrieval-Augmented Generation)** to read and understand HR PDF documents, delivering accurate, context-aware responses along with source references.

---

## 🚀 Key Features
- **Interactive Chat Interface** using Streamlit.
- **PDF Document Loader** to read HR policies and handbooks.
- **RAG System Integration**: Retrieves relevant information from documents before generating answers.
- **Vectorstore + Embeddings** for smart document search.
- **Context-aware Responses** that reference the original documents.
- **LangChain Groq API** integration for human-like natural language answers.
- **LangSmith Tracking** for monitoring RAG query history and performance.

---

## 🛠️ Tech Stack
- Python 3.10+
- [Streamlit](https://streamlit.io/)
- [LangChain Community](https://github.com/langchain-ai/langchain-community)
- [LangChain Groq](https://www.groq.com/)
- Chroma Vectorstore
- HuggingFace Embeddings
- PyPDFLoader
- dotenv

---

## 📂 Project Structure


avengers-hr-chatbot/
├── RAG_System.py # Main chatbot code
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── screenshots/
│ └── chatbot.png # Chatbot screenshot

