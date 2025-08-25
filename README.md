# 📑 Retrieval-Augmented Generation (RAG) Contract QA System

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline to answer natural language questions directly from legal contracts.  

Example:  
> *Question: “When does the data plan expire?”*  
>  
> Answer: The system retrieves the relevant contract clause and generates an accurate, context-aware answer.

---

## Dataset

Kaggle Dataset: https://www.kaggle.com/datasets/konradb/atticus-open-contract-dataset-aok-beta

---


## 🚀 Features
- **Document Ingestion**: Parses `.pdf` and `.txt` contracts using `pypdf` and custom loaders.  
- **Text Preprocessing**: Cleans raw text and applies **word-level chunking with overlaps** to preserve context.  
- **Semantic Embeddings**: Supports both:  
  - Local embeddings with [SentenceTransformers](https://www.sbert.net/) (`all-MiniLM-L6-v2`)  
  - Remote embeddings with [OpenAI API](https://platform.openai.com/) (`text-embedding-3-small`)  
- **Vector Indexing**: Stores embeddings in a **FAISS vector database** for fast similarity search.  
- **Retrieval + Generation**:  
  - Embeds user queries  
  - Finds relevant chunks with FAISS  
  - Sends context to **Llama 3** (or other LLMs) for final answers  
- **Modular Codebase**: Each stage (`load_files.py`, `chunking.py`, `embeddings.py`, `retrieval.py`) is independent for clarity and reuse.

---

## 📂 Project Structure
 - add this -
---


## ⚙️ Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/RAG-Contracts.git
   cd RAG-Contracts
 - add this -


## Tech Stack

 - Python 3.12
 - PyPDF – PDF parsing
 - SentenceTransformers – local embeddings
 - OpenAI API – optional embeddings
 - FAISS – vector similarity search
 - Llama 3 – retrieval-augmented generation


## Project is still in Progress
