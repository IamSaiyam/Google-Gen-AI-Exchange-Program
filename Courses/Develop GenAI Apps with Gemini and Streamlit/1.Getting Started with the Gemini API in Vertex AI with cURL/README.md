# 🚀 Getting Started with the Gemini API in Vertex AI with cURL (GSP1228)

This solution is part of the **Google GenAI Exchange Program**.

## 📌 Lab Overview

This lab introduces the usage of the **Gemini API** on **Vertex AI** using `cURL` commands to perform generative AI tasks. You interact directly with the `gemini-2.0-flash` model via REST API to generate text, perform chat completions, and generate responses from **images and video inputs** — all without using the Python SDK.

## ✅ What I Learned

- How to use `cURL` to interact with Vertex AI's Gemini models  
- Generate text from prompts using Gemini 2.0 Flash  
- Create multi-turn conversations through chat prompts  
- Use multimodal capabilities: generate text from images and video  
- Add system instructions and model parameters to improve results  
- Troubleshoot errors like rate limiting (HTTP 429)

## 📝 Notes

- **cURL gives SDK-free control**: Helpful for automation, testing, and integration into non-Python apps or backend pipelines.
  
- **Gemini 2.0 Flash is fast and efficient**: Ideal for responsive GenAI tasks that require low latency.

- **Multimodal input is powerful**: You can pass image and video files directly to the API to get descriptive and contextual text output.

- **You can stream or batch responses**: Though this lab focused on non-streaming, the API supports both.

- **Rate limits are common**: Especially during multi-modal generation. Use backoff and retry for stability.

## 🧪 Tools & Technologies

- **Vertex AI**
- **Gemini API (gemini-2.0-flash)**
- **cURL**
- **Google Cloud Storage (GCS)**
- **Vertex AI Workbench (JupyterLab)**

## 🔗 Useful Links

- [Gemini](https://deepmind.google/models/gemini/)
- [Gemini Documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models#gemini-models)
- [Vertex AI Workbench](https://cloud.google.com/vertex-ai/docs/workbench/introduction)
- [Develop GenAI Apps with Gemini and Streamlit](https://www.cloudskillsboost.google/)

---

**#SolveWithAI | 🇮🇳 Part of Google GenAI Exchange Program**
