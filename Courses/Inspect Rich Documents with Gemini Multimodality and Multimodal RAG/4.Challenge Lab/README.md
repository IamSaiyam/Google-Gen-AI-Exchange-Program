
# 📄 Inspect Rich Documents with Gemini Multimodality and Multimodal RAG (GSP520)

This project is part of the **Google GenAI Exchange Program**.

## 🧪 Lab Summary

This challenge lab focused on **leveraging Gemini's multimodal capabilities** to understand and analyze rich documents, including videos, images, and text content. The objective was to simulate a real-world marketing analysis use case—using Gemini's powerful models to extract insights from Google's brand materials.

📁 The solution is implemented in the notebook:  
**`inspect_rich_documents_w_gemini_multimodality_and_multimodal_rag-v1.0.0.ipynb`**

---

## ✅ What I Learned

- How to generate **video summaries**, **tags**, and **ask contextual questions** using a single video input.
- Compared multiple images to extract visual **differences** and **object-level insights**.
- Explored how to **retrieve extra information** by combining video + text queries.
- Built **metadata** from documents containing both text and images.
- Utilized **Multimodal Retrieval Augmented Generation (RAG)** techniques with Gemini to extract highly relevant chunks from documents.
- Queried documents with **helper functions** to get citations, chunk mappings, and semantic matches.
- Applied **multimodal embeddings** to perform knowledge retrieval across diverse input types.

---

## 📝 Notes

- 🧠 Gemini enables rich multimodal understanding: images, videos, and documents can be queried together.
- 🧩 Metadata generation (chunks, embeddings, and citations) is essential for building robust RAG pipelines.
- 🧪 We used helper functions like `get_similar_text_from_query()`, `get_similar_image_from_query()`, and `get_gemini_response()` to integrate Gemini into RAG workflows.
- 🎥 Video analysis included generating descriptions, tagging objects in frames, and follow-up QA on context.
- 📊 Image analysis allowed side-by-side comparisons for detecting subtle differences.
- 📚 Multimodal RAG retrieves meaningful content beyond text—bridging gaps between visual and textual content.
- ⚙️ The notebook interface on Vertex AI Workbench makes experimenting with multimodal AI seamless.

---

## 🔧 Tools & APIs Used

- **Gemini API (via Vertex AI SDK - Python)**  
- **Vertex AI Workbench (JupyterLab)**  
- **Gemini Flash Model (Multimodal)**  
- **Cloud Storage (video/image references)**  
- **RAG Helper Functions** provided in lab environment

---

**#SolveWithAI | Google GenAI Exchange India 🇮🇳**
