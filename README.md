# SheetSage
# 📊 SheetSage

**SheetSage** is an open-source full-stack web application that lets you interact with any CSV file using a conversational interface powered by **local AI** — no internet or external API needed.

> Ask complex questions about your data and get accurate, contextual answers. All processing happens **locally** via a RAG (Retrieval-Augmented Generation) pipeline using Ollama, LangChain, and vector search.

---

## 🚀 Features

- 🧠 **Local LLM Integration** with [Ollama](https://ollama.com) (supports models like Deepseek R1, LLaMA3, Mistral, Phi3, etc.)
- 📂 **CSV ingestion** and automatic chunking
- 🔎 **Semantic search & embeddings** via FAISS or Chroma
- 💬 **Chat interface** built with React
- ⚡ **FastAPI backend** for RAG and query orchestration
- 🔒 Fully private & offline: no external APIs or data sharing

---

## 💡 Use Cases

- Analyze large CSV datasets with natural language
- Quickly extract insights from messy or dense tables
- Private and secure spreadsheet QA for finance, business, or research

---

## Launch Backend API Service
Don't forget to add a venv (uv is recommended for FastAPI) and install all packages with
```commandline
uv pip install -r requirements.txt
```

Once venv activated and all packages installed, from the `/backend` folder you can run the server with:
```commandline
fastapi dev /app/api/api.py
```