# 🚀 Getting Started with Google Generative AI Using the Gen AI SDK (GSP1209)

This project is part of the **Google GenAI Exchange Program**.

## 🧪 Lab Summary

This lab explores the **Google Gen AI SDK**, a Python-based software development kit that simplifies integration with Google's generative AI models like **Gemini Pro** and **Gemini Flash**. The lab walks through tasks such as prompt submission, system instructions, model tuning, function calling, and batch predictions—all using notebooks in **Vertex AI Workbench**.

---

## ✅ What I Learned

- How to **install and use the Gen AI SDK** to interact with Gemini models.
- Sending **text prompts**, **image inputs**, and **multimodal data**.
- Using **system instructions** to guide the model’s behavior.
- Adjusting model behavior using parameters like:
  - `temperature`
  - `top_k`
  - `top_p`
  - safety filters
- Implementing **multi-turn conversations** and **asynchronous responses**.
- Building **function calling** pipelines to automate structured workflows.
- Using **streaming output** for real-time interactions.
- Estimating token usage with **token counting tools**.
- Running **batch predictions** using JSONL files in Cloud Storage.
- Generating and using **text embeddings** for similarity and retrieval.

---

## 📝 Notes

- ⚡ **SDK Simplicity**: The SDK abstracts API complexity, allowing developers to focus on prompt design and task logic.
- 🧠 **System Instructions**: They act as persistent instructions—useful for setting tone, persona, or constraints across multiple inputs.
- 🧪 **Multimodal Prompts**: You can combine text, images, and PDFs using `Part.from_uri()` with minimal setup.
- 🔄 **Streaming & Async**: Perfect for chat applications or integrations where latency and responsiveness matter.
- 🔧 **Function Calling**: Allows Gemini to output structured JSON, which can be used to call backend functions or APIs.
- 📦 **Batch Inference**: Best suited for scaling, when you want to process many inputs at once without needing real-time results.
- 🧭 **Embeddings**: Enables vector-based similarity matching. A foundational feature for Retrieval Augmented Generation (RAG).

---

## 🔧 Tools & APIs Used

- **Google Gen AI SDK** (Python)
- **Gemini Pro** and **Gemini Flash**
- **Vertex AI Workbench (JupyterLab)**
- **Vertex AI Gemini APIs** (Text, Multimodal)
- **Cloud Storage** (for batch jobs)
- **Text Embeddings API**

---

**#SolveWithAI | Google GenAI Exchange India 🇮🇳**
