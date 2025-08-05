
# 🛋️ Using Gemini for Multimodal Retail Recommendations (GSP1230)

This project is part of the **Google GenAI Exchange Program**.

## 🧪 Lab Summary

This lab focuses on how **Gemini Flash (gemini-2.0-flash)**—a multimodal model from Google DeepMind—can be used to build a **retail recommendation system** using a combination of **text and visual inputs**.

You will use the **Gemini API** via **Vertex AI Workbench** to process scene images (e.g., a living room) and receive intelligent product suggestions (e.g., furniture), either from Gemini’s built-in knowledge or from a constrained list of options provided by the user.

---

## ✅ What I Learned

- Setting up the **Vertex AI Workbench** and using JupyterLab for prototyping with Gemini.
- Using **Gemini Flash** to interpret an image of a room and provide a **textual description** of the layout and items.
- Crafting **multimodal prompts** combining text + image to retrieve meaningful responses.
- Asking Gemini to **recommend furniture** items that match a scene based on its built-in knowledge.
- Narrowing the scope of recommendations by providing a **custom list of product images** for Gemini to choose from.
- Designing **retail workflows** using Gemini for intelligent suggestions that enhance customer shopping experiences.

---

## 📝 Notes

- 🧠 **Visual Scene Understanding**: Gemini can interpret home/room layouts from images and describe them in natural language—very useful for smart interior design systems.
- 🪑 **Open-Ended Recommendations**: When no product list is provided, Gemini recommends items from its own training data, simulating a personalized shopping assistant.
- 🖼️ **Constrained Recommendations**: You can guide Gemini to select an item only from a set of uploaded product images, enabling **catalog-aware recommendations**.
- 🧵 **Retail Versatility**: The same pattern can be applied to clothing, electronics, or decor. Instead of a living room, the input could be an outfit or a shelf.
- ⚡ **Gemini Flash for Speed**: The lab uses Gemini Flash, which offers fast and cost-effective responses for interactive AI systems.
- 🔄 **Multimodal Prompts**: Blending text and image inputs is intuitive using the Gen AI SDK and `Part.from_uri()` functionality.
- 🛠️ **Prototyping Efficiency**: Vertex AI Workbench integrates well with Cloud Storage, making it easy to upload and access images during development.

---

## 🔧 Tools & APIs Used

- **Gemini API via Vertex AI SDK (Python)**
- **Vertex AI Workbench (JupyterLab)**
- **Gemini Flash Model (gemini-2.0-flash)**
- **Google Cloud Storage (for uploading chair/room images)**

---

**#SolveWithAI | Google GenAI Exchange India 🇮🇳**
