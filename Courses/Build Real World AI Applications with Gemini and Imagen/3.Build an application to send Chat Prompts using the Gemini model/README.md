
# Build an Application to Send Chat Prompts using the Gemini Model

This repository contains learning resources and implementation from the Google Cloud lab: **Build an Application to Send Chat Prompts using the Gemini Model**.

## 🌐 Lab Overview

In this lab, you will learn how to build a chat application that sends prompts to Google's powerful generative AI model – Gemini – using Vertex AI.

You will:

- Connect to Vertex AI with the Python SDK.
- Load a pre-trained generative AI model (Gemini 2.0 Flash).
- Send chat messages (both with and without streaming).
- Extract and display responses from the Gemini model.
- Understand key techniques in building conversational AI applications.

---

## 📁 Files

- `SendChatwithoutStream.py` — Sends chat prompts and displays full response after completion.
- `SendChatwithStream.py` — Streams AI responses as they're generated.

---

## 📚 Learnings

- How to use the `google.genai` SDK with Vertex AI.
- Difference between non-streaming vs. streaming responses.
- Sending and receiving multi-turn conversations with context/history.
- Basic conversational flow design for AI chatbots.

---

## ⚙️ Environment Setup

Make sure to set the required environment variables before running any Python files:

```bash
export GOOGLE_CLOUD_PROJECT="your-project-id"
export GOOGLE_CLOUD_LOCATION="your-region"
export GOOGLE_GENAI_USE_VERTEXAI=True
```

Also install the required libraries (if not already installed):

```bash
pip install google-cloud-aiplatform google-generativeai
```

---

## ▶️ How to Run

For non-streaming chat:

```bash
/usr/bin/python3 SendChatwithoutStream.py
```

For streaming chat:

```bash
/usr/bin/python3 SendChatwithStream.py
```

---

## 🧠 Try It Yourself

Change the prompts in the scripts to test Gemini's chat capabilities in different contexts like:
- Science questions
- Casual conversation
- Creative writing
- Technical help

---

## 🏁 Conclusion

This lab gives hands-on experience in using Google’s Gemini models with Vertex AI to build real-time, intelligent, and responsive chatbot-like applications.

