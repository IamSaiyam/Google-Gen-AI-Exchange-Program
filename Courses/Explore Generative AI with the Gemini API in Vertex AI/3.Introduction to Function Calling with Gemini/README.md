# 🔧 Introduction to Function Calling with Gemini (GSP1227)

This solution is part of the **Google GenAI Exchange Program**.

## 📌 Lab Overview

This lab introduces the concept of **Function Calling** using the **Gemini API** on **Vertex AI**, where LLMs generate structured function call arguments (in JSON) from natural language inputs. Unlike Vertex AI Extensions which execute functions directly, function calling gives developers fine-grained control by letting them interpret and invoke functions manually.

You interact with the **Gemini Flash** model via Python in **Vertex AI Workbench** to handle tasks like structured product queries, geolocation with external APIs, and log-based entity extraction.

## ✅ What I Learned

- How to use **function calling** to extract structured data (JSON) from natural prompts  
- Leveraging Gemini Flash to generate function names and arguments dynamically  
- Creating interactive applications that use LLM-generated function arguments  
- Building apps that connect Gemini outputs to external APIs (e.g., geocoding)  
- Using function calling for **entity extraction** from raw log messages

## 📝 Notes

- **Function Calling ≠ Extensions**: Function calling returns the *what to call* and *with what*, while Extensions *run* the functions directly.
  
- **Structured response generation**: You define the schema, Gemini fills in the arguments from unstructured input.

- **Use cases covered**:
  - Google Store queries → Convert natural questions into structured product info lookups
  - Geocoding → Extract addresses, then call a maps API using the generated lat/lon
  - Log Analysis → Extract fields like error type, timestamp, and user from plain log lines

- **Gemini Flash model** is ideal for this due to its speed and efficient parameter extraction.

- Best practice: **Validate output** from function calling before executing external functions, especially for user-driven inputs.

## 🧪 Tools & Technologies

- **Vertex AI Workbench**
- **Gemini API (gemini-2.0-flash)**
- **Google Gen AI SDK for Python**
- **OpenStreetMap Nominatim API (for geocoding)**
- **Python (Jupyter Notebook)**

## 🔗 Useful Links

- [Gemini](https://deepmind.google/models/gemini/)
- [Gemini Documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models#gemini-models)
- [Vertex AI Workbench](https://cloud.google.com/vertex-ai/docs/workbench/introduction)
- [OpenStreetMap Nomitanim API](https://nominatim.openstreetmap.org/ui/search.html)

---

**#SolveWithAI | 🇮🇳 Part of Google GenAI Exchange Program**
