# 🔍 Multimodal Retrieval Augmented Generation (RAG) with Gemini (GSP1231)

This project is part of the **Google GenAI Exchange Program**.

## 🧪 Lab Summary

In this lab, we explore how to implement **Multimodal Retrieval Augmented Generation (RAG)** using **Gemini 2.0 Flash** in **Vertex AI**. This involves leveraging the Gemini API to perform **Q&A over financial documents** containing both **text and images**.

Traditional RAG techniques rely on textual inputs, but **multimodal RAG** enhances understanding by incorporating **images, graphs, and charts** to support LLMs in producing grounded, accurate responses.

---

## ✅ What I Learned

- How to **extract metadata and generate embeddings** from multimodal documents (text + images)
- Running **text-based semantic search** to retrieve document chunks using text embeddings
- Running **image-based semantic search** using image embeddings and similarity scoring
- Performing **comparative reasoning** over visual data (e.g., comparing stock charts)
- Building a **complete multimodal RAG pipeline**:
  - Retrieve similar **text** and **image** chunks from a document
  - Use both as **context** in Gemini API prompts for **grounded generation**
  - Return **citations** (sources) for all content used in the answer
- Working in **Vertex AI Workbench** to combine Gemini API, embeddings, and search

---

## 📝 Notes

- 📄 **Document Understanding**: Gemini can analyze structured financial documents, including text blocks and visual content like tables and graphs.
- 🔍 **Multimodal Search**: You can query with **text or images**, and retrieve matching content in either modality.
- 🤝 **Fusion for Contextual RAG**: By combining retrieved text & images, Gemini gives context-aware answers—much better than isolated search.
- 🧠 **Comparative Reasoning**: You can ask Gemini to reason over charts or financial graphs—e.g., comparing two stock types visually.
- 🔧 **Helper Utilities**: Reusable Python functions (provided in the lab) help with formatting, image loading, embedding, and Gemini prompting.
- 💡 **Real-World Use Cases**:
  - Financial document analysis
  - Medical or legal image-heavy reports
  - Comparative product reviews or specs
- 💬 **Prompting Best Practices**:
  - Use precise questions, and add system instructions for how Gemini should reason (e.g., “only use provided content”).
  - Use Gemini Flash for faster, lightweight reasoning.

---

## 🔧 Tools & APIs Used

- **Gemini API via Vertex AI SDK (Python)**
- **Vertex AI Workbench (JupyterLab)** with GPU support
- **Text and Image Embedding models**
- **Google Cloud Storage (GCS)** for uploading documents
- **Custom Python Utilities** from `intro_multimodal_rag_utils.py`

---

**#SolveWithAI | Google GenAI Exchange India 🇮🇳**