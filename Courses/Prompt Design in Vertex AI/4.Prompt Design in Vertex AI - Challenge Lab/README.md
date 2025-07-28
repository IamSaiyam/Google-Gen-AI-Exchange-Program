# 🌿 Prompt Design in Vertex AI: Challenge Lab (GSP519)

This solution is part of the **Google GenAI Exchange Program**.  
In this challenge lab, I applied prompt engineering skills to build marketing tools for Cymbal Direct's new outdoor product line using **Vertex AI** and **Gemini models**.

## 🧠 Challenge Scenario

> Cymbal Direct, an outdoor gear retailer, wanted to create a marketing campaign that uses Generative AI to:
> - Generate short, vivid product descriptions from images.
> - Create catchy, emotion-driven taglines for young adventurers.

As an AI engineer, I was tasked with building two prompt templates and experimenting with their Python code for customization and creativity.

---

## ✅ What I Built

### 1. 🖼️ Gemini Image Analysis Tool
- **Prompt Name**: `Cymbal Product Analysis`
- **Goal**: Analyze product images and generate creative, multi-style descriptions.
- **Outputs included**:
  - Descriptive captions
  - Catchy ad phrases
  - Poetic mood-based lines
- **Prompts designed with**:
  - Model: Gemini
  - Adjusted parameters: `temperature`, `max_output_tokens`, etc.
  - Focus on: visual elements + emotional evocation

---

### 2. 🧾 Gemini Tagline Generator
- **Prompt Name**: `Cymbal Tagline Generator Template`
- **Goal**: Generate customizable taglines based on product traits, audience, and tone.
- **Prompt setup included**:
  - System Instructions for Gemini
  - 2 few-shot examples for style guidance
  - Parameters for: product type, audience, emotion
- **Modified versions**: Ensured inclusion of specific keywords like _"nature"_.

---

### 3. 🧪 Python Prompt Experiments

| Notebook | Summary |
|----------|---------|
| `image-analysis.ipynb` | Modified the image prompt to be shorter and more abstract. Increased creativity using higher temperature. |
| `tagline-generator.ipynb` | Customized tagline prompt to include specific keywords and tested response variability. |

> All prompts were exported from **Vertex AI Studio**, tested and refined in **Vertex AI Workbench** Jupyter notebooks.

---

## 📓 Notebooks

These Jupyter notebooks demonstrate how I implemented and refined the prompts using Python code exported from Vertex AI Studio.

| Notebook File             | Description |
|---------------------------|-------------|
| `ImageAnalysis.ipynb`     | Uses Gemini to generate short, creative descriptions from product images. Parameters were adjusted for more abstract, poetic outputs. Prompt was modified to encourage vivid and emotionally resonant responses. |
| `TaglineGenerator.ipynb`  | Implements a dynamic tagline generator using structured prompts and system instructions. Prompt was adjusted to include emotional tones and specific keywords like "nature". Few-shot examples helped guide output consistency. |

Each notebook includes:
- SDK installation & setup
- Prompt definition with Gemini model
- Parameter tuning (`temperature`, `top_p`, `max_output_tokens`, etc.)
- Result evaluation and improvement

> All prompts were exported from **Vertex AI Studio** and enhanced via code to explore creative variations and output control.

---

## 📝 Notes & Observations

- **Prompt specificity matters**: Small tweaks in wording drastically changed the tone and length of generated outputs.
- **System instructions add direction**: Gemini’s responses followed task style better with proper system setup.
- **Model parameters = control levers**:
  - `temperature`: Best for creativity, humor, surprise.
  - `top_p`, `top_k`: Helpful in reducing randomness.
- **Few-shot prompting**: Clear examples improved consistency, especially for tagline structure.
- **Python experimentation**: Ideal for testing parameter effects & reproducibility of prompt outputs.

---

## 🔗 Resources

- [Vertex AI Studio](https://cloud.google.com/vertex-ai/docs/generative-ai/studio/introduction)
- [Gemini Models Overview](https://cloud.google.com/vertex-ai/docs/generative-ai/model-reference/gemini)
- [Prompt Management Guide](https://cloud.google.com/vertex-ai/docs/generative-ai/studio/manage-prompts)
- [Build with Code Docs](https://cloud.google.com/vertex-ai/docs/generative-ai/code-export)

---

**#SolveWithAI | #GenAIExchange | 🇮🇳 Building for India with AI**
