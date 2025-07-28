# 🧠 Generative AI with Vertex AI: Prompt Design (GSP1151)

This solution is part of the **Google GenAI Exchange Program**.

## 📌 Lab Overview

This lab focuses on prompt engineering using the **Google Gen AI SDK** and **Vertex AI**. You’ll learn how to structure effective prompts, apply system instructions, and use examples to improve LLM performance using Gemini Pro and Gemini Flash.

## ✅ What I Learned

- Writing concise, specific, and task-focused prompts  
- Reducing hallucinations with system instructions  
- Improving response quality with few-shot examples  
- Converting generative tasks into classification tasks  
- Exploring ideation, summarization, extraction, and more

## 📝 Notes

- **Clear prompts reduce ambiguity**: Focus on single, well-defined tasks. Avoid vague or compound instructions.  
- **System instructions improve control**: These help restrict responses to domain-specific or safe content. Especially useful for chatbots or sensitive use cases.  
- **Examples enhance quality**: Few-shot examples help the model understand the expected output style and structure. Aim for 1–5 quality examples.  
- **Classification reduces variability**: For tasks like sentiment or intent detection, framing the task as classification improves consistency and avoids hallucination.  
- **Gemini Models**:  
  - *Gemini Pro*: High performance for complex reasoning, multimodal tasks, and long context understanding.  
  - *Gemini Flash*: Lightweight and fast, suitable for high-throughput, cost-sensitive applications.  
- **Best practice**: Use concise language, give relevant context, avoid overload, and guide output with format hints if needed.

## 📂 Prompt Files

This repo includes example prompt templates designed during the lab:

| File | Description |
|------|-------------|
| `ideation_prompt.txt` | Prompt to generate creative startup ideas in healthtech |
| `summarization_prompt.txt` | Prompt for summarizing long text into bullet points |
| `classification_prompt.txt` | Prompt for classifying text sentiment |
| `extraction_prompt.txt` | Prompt for extracting structured data (name, date, location) |
| `chatbot_guardrail_prompt.txt` | System prompt to constrain chatbot responses to travel-related queries only |

## 🧪 Tools & Technologies

- Google Gen AI SDK  
- Vertex AI Workbench  
- Gemini API (Pro & Flash)  
- Python (Jupyter Notebooks)

## 🔗 Resources

- [Vertex AI Studio](https://cloud.google.com/generative-ai-studio?hl=en)
- [Gemini Overview](https://deepmind.google/technologies/gemini)
- [Prompt Design Guide](https://cloud.google.com/vertex-ai/docs/generative-ai/prompt-design)

---

**#SolveWithAI | 🇮🇳 Part of Google GenAI Exchange Program**
