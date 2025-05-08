# Homework Project: Build a RAG (Retrieval-Augmented Generation) System

## Objective
Develop a basic Retrieval-Augmented Generation (RAG) system that retrieves information from an external document source and uses it to answer questions. This will demonstrate how language models can be grounded in up-to-date, domain-specific knowledge.

> The chosen model has a knowledge cutoff in **August 2024**, so answers to recent topics must rely on **retrieved documents**, not internal model knowledge.

---

## Core Requirements

### 1. Document Indexing
- Use **Chromadb** with **persistence enabled**.
- Choose a document of an event that happend after **August 2024**
- Include document **splitting** (≥ 50 chunks) using appropriate text splitting strategies.

### 2. System Components
- Use `gemini-2.0-flash`
- Implement with **LangChain** or **LlamaIndex**.  
- Use **LangSmith** or **LangFuse**.  
- Use **Git and GitHub** for version control.
- Don not use pre-built agents.
- **Dialog flow** (multi-turn interaction)  
- **Memory** (context tracking across interactions)  

### 3. Experimentation  
- Compare **system prompts** and their effects on model behavior.  
- Use a variety of **questions** to evaluate system robustness (at leat 5 different questions with correct answers).

### 4. Reproducibility  
- Submit your code via **GitHub**.  
- Use a clean repository:  
  - ❌ **No large files** in git history  
  - ❌ **No secret tokens** in commit history

### 5. Submission  
- **Deadline:** `11.05 at 23:59`  
- **Deliverables:**
  - GitHub repo link
  - Link to your **LangSmith** or **LangFuse** project.
  - Jupyter notebook or script demonstrating:
    - Index creation
    - Retrieval
    - Answer generation
    - Prompt variations

---

## Bonus Features (Optional, for Extra Credit)

Implement one or more of the following to enhance your RAG system:

- ✅ **Metadata filtering** during document retrieval  
- ✅ **Multi-Query retrieval** (ask multiple questions or rephrase to get better context)

---ERGEBNISSE
🔍 Retrieval-Augmented Generation (RAG) System mit LangChain, ChromaDB und Gemini 2
📌 Projektübersicht
Dieses Projekt implementiert ein einfaches, aber leistungsfähiges Retrieval-Augmented Generation (RAG) System, das Informationen aus der Wikipedia-Seite 2025 in Science extrahiert und verwendet, um Fragen kontextbasiert zu beantworten.

Es kombiniert Google Gemini 2.0 Flash mit LangChain, ChromaDB, und nutzt LangSmith für Tracing & Debugging.

🛠️ Funktionen
✅ Dokumentenindexierung (mit ChromaDB und persistenter Speicherung)

✅ Chunking von Dokumenten in über 50 Textabschnitte

✅ Multi-Query-Retrieval zur Verbesserung der Antwortqualität

✅ Kontextbasiertes Antwortsystem mit Dialogverlauf (ConversationBufferMemory)

✅ Speicherung des Chatverlaufs auf Dateibasis

✅ Integration mit LangSmith für Tracing, Logging und Monitoring

✅ Anpassbare Prompts 

📂 Projektstruktur
bash
Kopieren
Bearbeiten
📁 rag_project/
├── notebook.ipynb         # Jupyter-Notebook mit Implementierung
├── chroma_db/             # Persistente Vektordatenbank
├── chat_history.json      # Persistenter Chatverlauf
├── README.md              # Dieses Dokument
⚙️ Setup & Installation
Erstelle ein neues Python-Environment:

bash
Kopieren
Bearbeiten
conda create -n rag_env python=3.10
conda activate rag_env
Installiere benötigte Pakete:

bash
Kopieren
Bearbeiten
pip install -r requirements.txt
Setze deinen Google API Key:

python
Kopieren
Bearbeiten
os.environ["GOOGLE_API_KEY"] = "DEIN_KEY_HIER"
🚀 Verwendung
Starte das Notebook

Lade die Wikipedia-Seite und indexiere sie

Stelle Fragen wie:

"Welche wissenschaftlichen Ereignisse sind für 2025 geplant?"

"Welche NASA-Missionen sind vorgesehen?"

Verfolge den Dialogverlauf und die abgerufenen Quellen

📊 Erweiterte Funktionen

Multi-Query-Retrieval: Mehrere automatisch generierte Anfragen verbessern die Abdeckung

LangSmith Logging: Mit tracer Callback zur besseren Nachverfolgung

📎 Abhängigkeiten
langchain

chromadb

google-generativeai

sentence-transformers

langsmith: https://smith.langchain.com/o/7f7ff825-5fff-45e7-b604-6d22b5223ead/projects/p/70491b11-92eb-417c-8afb-b5c8a72998c0?timeModel=%7B%22duration%22%3A%227d%22%7D&runtab=0&tab=0&pageIndex=0&pageSize=10&Volume=Success&Latency=P50&Tokens=P50&Cost=P50&Streaming=P50


transformers

👨‍💻 Autor
Volodymyr (https://github.com/vladimir707/GenerativeAI-II-Project)