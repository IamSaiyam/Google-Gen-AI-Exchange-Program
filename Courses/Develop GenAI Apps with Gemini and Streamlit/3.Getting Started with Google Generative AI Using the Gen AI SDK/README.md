# 🚀 Getting Started with Google Generative AI Using the Gen AI SDK (GSP1209)

This project is part of the **Google GenAI Exchange Program**.

## 🧪 Lab Summary

This lab introduces the **Google Gen AI SDK**, a Python-based SDK that enables developers to interact with Google's generative AI models like **Gemini Pro** and **Gemini Flash**. You’ll learn to send prompts, manage model interactions, configure responses, and leverage advanced capabilities such as function calling, streaming, embeddings, and batch predictions.

## ✅ What I Learned

- Installing and using the **Gen AI SDK** to send text and multimodal prompts.
- Applying **system instructions** to guide the model behavior and output.
- Managing model parameters like `temperature`, `top_k`, and `safety filters`.
- Running **multi-turn chats**, asynchronous calls, and response streaming.
- Using advanced features: token counting, context caching, and function calling.
- Performing **batch predictions** via Cloud Storage and retrieving structured results.
- Generating **text embeddings** for similarity and search-based applications.

## 📝 Notes

- **SDK Simplicity**: The Gen AI SDK abstracts most API complexities and enables quick prototyping.
- **Multimodal Support**: Easily pass images, PDFs, and text into prompts using `Part.from_uri`.
- **System Instructions**: These serve as long-term memory for the model and help align outputs with task goals.
- **Streaming Responses**: Useful for chat or UI integrations, where you need partial responses in real-time.
- **Function Calling**: You can integrate model output directly with functions in your code—powerful for automation tasks.
- **Batch Prediction**: Best for high-volume inference workloads. Ideal when latency is not critical.
- **Embeddings**: Allow you to compare semantic similarity between texts or for retrieval-augmented generation.


## 🔧 Tools & APIs Used

- Google Gen AI SDK (Python)
- Gemini Pro & Gemini Flash
- Vertex AI Workbench (JupyterLab)
- Cloud Storage (for batch prediction)
- Vertex AI Embeddings API

## 🔗 Resources

- [Google Gen AI SDK](https://cloud.google.com/vertex-ai/generative-ai/docs/sdks/overview)
- [Vertex AI Workbench](https://cloud.google.com/vertex-ai/docs/workbench/introduction)
- [Google Models](https://cloud.google.com/vertex-ai/generative-ai/docs/models#gemini-models)
- [Model Garden](https://cloud.google.com/vertex-ai/generative-ai/docs/model-garden/explore-models)
- [System Instructions](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/system-instruction-introduction)
- [Experimenting with Parameter Values](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values)
- [Configure Safety Features](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/configure-safety-filters )
- [Controlled Generation](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/control-generated-output)
- [List and Count Tokens](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/list-token)
- [Function Calling](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling)
- [Context Caching](https://cloud.google.com/vertex-ai/generative-ai/docs/context-cache/context-cache-overview)
- [Batch Prediction with Gemini](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/batch-prediction-gemini)
- [Batch Predictions API](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/batch-prediction-api)
- [Text Embeddings API](https://cloud.google.com/vertex-ai/generative-ai/docs/embeddings/get-text-embeddings)

---

**#SolveWithAI | Google GenAI Exchange India 🇮🇳**
