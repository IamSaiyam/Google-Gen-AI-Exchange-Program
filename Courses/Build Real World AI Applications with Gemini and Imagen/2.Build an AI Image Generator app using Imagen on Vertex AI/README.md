
# 🖼️ AI Image Generator using Imagen on Vertex AI

This project demonstrates how to generate images using **Imagen 3.0** on **Vertex AI** by providing text prompts. You will learn how to build a basic AI-powered image generation application using Google Cloud’s Vertex AI SDK.

---

## 📚 What You'll Learn

- Connect to Vertex AI using the Vertex AI Python SDK
- Load and use the pre-trained **Imagen 3.0 image generation model**
- Pass text prompts and generate image outputs
- Save and preview AI-generated images
- Understand how to use optional parameters like watermark and seed

---

## 🛠️ Tools & Technologies Used

- Google Cloud Vertex AI
- Imagen 3.0 Model (`imagen-3.0-generate-002`)
- Vertex AI Python SDK (`vertexai`)
- Python 3.x

---

## ⚙️ Environment Setup

Install the required SDK:

```bash
pip install google-cloud-aiplatform
```

Set the following environment variables before running the script:

```bash
export GOOGLE_CLOUD_PROJECT="your-project-id"
export GOOGLE_CLOUD_LOCATION="your-region"
```

> Replace `your-project-id` and `your-region` with your actual Google Cloud project info.

---

## ▶️ How to Run

Run the Python script using:

```bash
python3 GenerateImage.py
```

This will generate a file named `image.jpeg` based on the given prompt:

> “Create an image of a cricket ground in the heart of Los Angeles”

Open `image.jpeg` to preview the result.

---

## 🧪 Expected Output

An image file (`image.jpeg`) will be generated and saved in your working directory. The image reflects the content of your prompt using the Imagen model’s capabilities.

---

## 📝 Notes

- By default, SynthID watermarks are added. Use `add_watermark=False` to disable it.
- You cannot use a `seed` and watermark together.
- This model is **prompt-driven only** (no input images required).
- You can change the prompt to generate different creative outputs.

---

## 🏁 Status

✅ Lab Complete  
⏱️ Time Taken: ~15 minutes  
💰 Cost: None (Qwiklabs sandbox)

---

Happy Generating! 🎨🤖
