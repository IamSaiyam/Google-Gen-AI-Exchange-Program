# 🧠 Generative AI with Vertex AI: Prompt Design (GSP1151)

This solution is part of the **Google GenAI Exchange Program**.

## 📌 Lab Overview

This lab explores prompt engineering using the **Google Gen AI SDK** with **Vertex AI Workbench**. It focuses on designing high-quality prompts to improve the relevance, accuracy, and safety of responses from large language models like **Gemini Pro** and **Gemini Flash**.

## ✅ What I Learned

- How to structure effective prompts that reduce ambiguity  
- Techniques for improving model reliability using system instructions  
- Converting open-ended tasks into classification-style prompts  
- Enhancing output quality by including few-shot examples  
- Identifying and reducing hallucinations in LLM responses

## 📝 Notes

- **Prompt clarity is crucial**: Models respond best when instructions are direct and unambiguous. Use short, task-specific wording.
  
- **System instructions help guide behavior**: They act as guardrails for the model. For example, in a travel chatbot, you can instruct the model to only answer travel-related queries.
  
- **Break down tasks**: Avoid multi-step or compound prompts. Asking for one task at a time leads to more accurate and focused responses.
  
- **Use examples for in-context learning**: Providing relevant few-shot examples improves response quality significantly. Aim for 1–5 well-balanced samples.
  
- **Prefer classification for sensitive tasks**: Instead of asking the model to "generate," you can give it options to choose from. This reduces variability and improves safety.
  
- **Model choice matters**:  
  - *Gemini Pro* is better for deep reasoning, summarization, and multimodal understanding.  
  - *Gemini Flash* is faster, optimized for low-latency responses, and more cost-efficient.

- **Error handling**: In some cases, the API may return rate limits (e.g., HTTP 429). Waiting and retrying usually resolves this.

## 🧪 Tools & Technologies

- **Vertex AI Workbench**
- **Gemini API (Pro & Flash)**
- **Google Gen AI SDK**
- **Python (Jupyter Notebook)**

## 🔗 Useful Links

- [Prompt Design](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design)
- [Gemini](https://deepmind.google/models/gemini/)
- [Gemini Documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/models#gemini-models)
- [Vertex AI Workbench](https://cloud.google.com/vertex-ai/docs/workbench/introduction)
- [System Instructions](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/system-instruction-introduction)

---

**#SolveWithAI | 🇮🇳 Part of Google GenAI Exchange Program**
