
# Explore Generative AI with the Gemini API in Vertex AI: Challenge Lab

**Lab ID:** GSP515  
**Duration:** 1 hour 30 minutes  
**Difficulty:** Intermediate  

This challenge lab tests your skills in using Google's Gemini API for text generation, function calling, and video content analysis. It is part of the **"Explore Generative AI with the Gemini API in Vertex AI"** course.

---

## 🚀 Challenge Scenario

As a developer at an AI-powered video analysis startup, your goal is to implement three Gemini-powered features:
1. Generate text
2. Execute function calls
3. Describe video content using AI

You’ll demonstrate your ability to apply these features in production-like workflows through Vertex AI and Jupyter notebooks.

---

## ✅ Task 1: Generate Text using Gemini (via Cloud Shell)

You must make an API call to Gemini using `curl` and authenticate using your Cloud Shell credentials.

### 🔧 Step 1: Set Environment Variables

```bash
PROJECT_ID=your-project-id
LOCATION=your-location
API_ENDPOINT="${LOCATION}-aiplatform.googleapis.com"
MODEL_ID="gemini-2.0-flash-001"
```

### 🧩 Step 2: Enable Required APIs

Use the Cloud Console or CLI to enable:
- Vertex AI API
- IAM Service Account Credentials API

```bash
gcloud services enable aiplatform.googleapis.com iamcredentials.googleapis.com
```

### 🔑 Step 3: Authenticate with Access Token

```bash
ACCESS_TOKEN=$(gcloud auth print-access-token)
```

### 📦 Step 4: Prepare Request Payload

Create a prompt to ask Gemini a question:

```bash
cat > request.json <<EOF
{
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "Why is the sky blue?"
        }
      ]
    }
  ]
}
EOF
```

### 🌐 Step 5: Make the API Request

```bash
curl -X POST \
  -H "Authorization: Bearer ${ACCESS_TOKEN}" \
  -H "Content-Type: application/json" \
  https://${API_ENDPOINT}/v1beta1/projects/${PROJECT_ID}/locations/${LOCATION}/publishers/google/models/${MODEL_ID}:generateContent \
  -d @request.json
```

### 📝 Notes:
- You should receive a JSON response with Gemini’s answer.
- Make sure your `PROJECT_ID` and `LOCATION` match your lab setup.
- If you hit a rate limit (HTTP 429), wait 60 seconds before retrying.

---

## ✅ Task 2–4: Vertex AI Workbench Tasks

All code for the following tasks is provided in the [**`gemini-explorer-challenge.ipynb`**](./gemini-explorer-challenge.ipynb) Jupyter notebook.

> 💡 Make sure to open the Workbench instance `generative-ai-jupyterlab` and select Python 3 kernel.

---

### 📘 Task 2: Open the Notebook

- Navigate to Vertex AI → Workbench
- Open the `generative-ai-jupyterlab` instance
- Launch JupyterLab

🔁 **Note**: If Jupyter fails to load, reset the instance and try again.

---

### 🧠 Task 3: Create a Function Call Using Gemini

- Open `gemini-explorer-challenge.ipynb`
- Complete code under **Task 3**
- Provide correct `project_id` and `location` as needed
- Make sure the output includes **weather-related data**

---

### 🎥 Task 4: Describe Video Contents Using Gemini

- In the same notebook, navigate to **Task 4**
- Complete all required cells that describe video contents using Gemini Flash 001
- Ensure outputs are being generated for video analysis

---

## 🏁 Conclusion

By completing this lab, you have:

- Made secure API calls to Gemini from Cloud Shell
- Used Gemini to generate structured text and trigger function calls
- Leveraged Gemini’s video analysis capabilities in real-world scenarios

This demonstrates your practical skills in deploying multimodal GenAI models using Google Cloud Vertex AI.

---

## 📁 Files

- [`gemini-explorer-challenge.ipynb`](./gemini-explorer-challenge.ipynb) – contains Tasks 2–4
- `request.json` – payload for Task 1
- `README.md` – this file

---

## 🔐 Notes

- This lab uses **temporary credentials**; do not use your personal GCP account.
- Run labs in **Incognito Mode** to avoid credential conflicts.
- If the notebook fails to open, reset the Vertex AI Workbench instance.

---
