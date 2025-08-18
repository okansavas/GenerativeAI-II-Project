# %%
# 📦 Nötige Bibliotheken herunterladen
%pip install pymupdf openai langchain chromadb PyMuPDF pip install langchain-openai sentence-transformers --quiet


# %%
import fitz
doc = fitz.open("hai_ai_index_report_2025.pdf")
raw_text = ''.join([page.get_text() for page in doc])
print(f"Gesamte Länge: {len(raw_text)}")


# %%
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

chunks = text_splitter.split_text(raw_text)

print(f"Chunk Zählen: {len(chunks)}")


# %%
%pip install -U langchain-community
from langchain.docstore.document import Document

documents = []
for i, chunk in enumerate(chunks):
    documents.append(Document(page_content=chunk, metadata={"chunk_id": i}))


# %%
from langchain_community.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings

# 🔤 Embedding Modell: Texte lässt zu numörischen Vektörn werden
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# 💾erstellen Vektor Database mit ChromaDB
db = Chroma.from_documents(
    documents=documents,
    embedding=embedding_function,
    persist_directory="rag_index"  # speichern in Ordner
)

# 📌 macht fest Database
db.persist()


# %%
%pip install openai
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = "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"  # 🔐 echt API key soll da sein

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)


# %%
from langchain.memory import ConversationBufferMemory
from langchain_core.runnables import RunnableConfig

memory = ConversationBufferMemory()
config = RunnableConfig(memory=memory)


# %%
from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings

embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

db = Chroma(
    persist_directory="rag_index",
    embedding_function=embedding_function
)


# %%
from langchain.chains import ConversationalRetrievalChain

conversation_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=db.as_retriever(),
    memory=memory
)

# %%
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

conversation_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=db.as_retriever(),
    memory=memory,
    return_source_documents=False  # ✅ nur 'answer' Umsetzung, kein Fehler
)

# %%
# Ohne Retrieval: Antwort mit Modell 
q = "What are the main AI investment trends in 2024?"
print("[Retrieval geschlossen]")
print(llm.invoke(q))

# %%
# Retrieval geöffnet: dokumentbasierte Antwort
print("\n[Retrieval Geöffnet]")
print(conversation_chain.run(q))

# %%
# Die gleiche Frage kann mit unterschiedlichen System-Prompts getestet werden.
# (Mit ChatOpenAI wird dies nicht direkt unterstützt; falls Custom Chain benötigt wird, kann dies später umgesetzt werden)
# Als Beispiel verwenden wir 3 verschieden formulierte Versionen der Frage:
variations = [
    "What happened in AI investments last year?",
    "Give me key trends in artificial intelligence funding in 2024.",
    "Summarize AI investment highlights for 2024."
]

for i, v in enumerate(variations):
    print(f"\nPrompt #{i+1}: {v}")
    print(conversation_chain.run(v))



