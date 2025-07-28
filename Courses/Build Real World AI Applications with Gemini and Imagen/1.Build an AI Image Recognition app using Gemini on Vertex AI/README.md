
# 🧠 AI Image Recognition with Gemini on Vertex AI

This project demonstrates how to use the **Gemini 2.0 model** on **Vertex AI** to analyze images and return natural language descriptions using Google Cloud’s GenAI SDK.

---

## 📚 What You'll Learn

By completing this lab, you'll understand how to:

- Connect to Vertex AI using the GenAI Python SDK
- Use **Gemini's multimodal capabilities** (image + text)
- Provide image URIs as part of your input prompts
- Interpret and handle **AI-generated responses**
- Write and run a complete Python script that uses generative AI

---

## 🛠️ Tools & Technologies Used

- Google Cloud Vertex AI
- Gemini 2.0 Flash Model
- Vertex AI Python SDK
- Python 3.x
- Google Cloud Storage

---

## ⚙️ Environment Setup

Make sure the `google-generativeai` SDK is installed:

```bash
pip install google-generativeai
```

Then set your environment variables before running the script:

```bash
export GOOGLE_CLOUD_PROJECT="your-project-id"
export GOOGLE_CLOUD_LOCATION="your-region"
export GOOGLE_GENAI_USE_VERTEXAI=True
```

> Replace `your-project-id` and `your-region` with actual values from your Google Cloud lab or project.

---

## ▶️ How to Run

Once the environment is set:

```bash
/usr/bin/python3 /genai.py
```

This script uses a sample image of scones (`gs://cloud-samples-data/generative-ai/image/scones.jpg`) and asks:

> “What is shown in this image?”

---

## 🧪 Expected Output

You'll receive a short, natural language description of the image from Gemini, such as:

```
AI Response: A plate of scones, possibly with some icing or powdered sugar.
```

Try changing the prompt or image URI to explore more capabilities.

---

## 📝 Notes

- If you see a 400 error, re-run the script.
- You can replace the sample image with your own uploaded image in GCS.
- This script demonstrates **multimodal input** (image + text) with Vertex AI.

---

## 🏁 Status

✅ Lab Complete  
⏱️ Time Taken: ~15 minutes  
💰 Cost: None (Qwiklabs sandbox)

---

Happy experimenting with AI! 🤖✨
