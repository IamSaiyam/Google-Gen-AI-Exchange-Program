
# 🚀 Streamlit + Cloud Run + Gemini API in Vertex AI (GSP1229)

This solution is part of the **Google GenAI Exchange Program**.

## 📌 Lab Overview

This lab walks through building a **generative AI application** using **Streamlit** and **Gemini API on Vertex AI**, then deploying it with **Cloud Run**. You'll create an interactive web app that generates stories based on prompts using Gemini models.

The lab involves running the app locally in **Cloud Shell**, testing it, and then deploying it using a containerized setup to **Google Cloud Run**.

## ✅ What I Learned

- How to build interactive AI-powered apps using **Streamlit**.
- Integrating **Gemini models** with UI to generate story content.
- Containerizing Python applications and deploying them to **Cloud Run**.
- Using **Vertex AI SDK** for prompt generation and model inference.
- Creating scalable endpoints with auto-managed infrastructure.

## 📝 Notes

- **Streamlit + Gemini = Fast Prototyping**: Easily build web apps with LLM capabilities.
  
- **Vertex AI Initialization**: Required project ID and region for the SDK.
  
- **Cloud Run Deployment Steps**:
  - Clone repo → Install dependencies → Set env variables.
  - Create Docker image → Push to Artifact Registry.
  - Deploy with `gcloud run deploy` using correct region, image, and service name.

- **Model Options**:
  - `Gemini Pro` for reasoning and summarization.
  - `Gemini Flash` for low-latency, cost-efficient usage.

- Remember to enable **required Google Cloud APIs** (Vertex AI, Cloud Run, Artifact Registry) before running.

## 🧪 Tools & Technologies

- **Google Cloud Run**
- **Vertex AI Gemini API**
- **Streamlit**
- **Google Cloud Shell**
- **Docker + Artifact Registry**
- **Python (venv + pip)**

## 🔗 Useful Links

- [Vertex AI Gemini Overview](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini)
- [Streamlit](https://streamlit.io)
- [Cloud Run Documentation](https://cloud.google.com/run)
- [Google GenAI SDK for Python](https://cloud.google.com/vertex-ai/docs/generative-ai/sdk/setup)
- [Artifact Registry](https://cloud.google.com/artifact-registry)

---

**#SolveWithAI | 🇮🇳 Part of Google GenAI Exchange Program**
