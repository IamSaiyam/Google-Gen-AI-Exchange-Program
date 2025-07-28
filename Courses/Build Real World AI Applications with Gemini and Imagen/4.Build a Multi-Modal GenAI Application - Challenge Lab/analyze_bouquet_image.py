import vertexai
from vertexai.generative_models import GenerativeModel, Part, Image

def analyze_bouquet_image(image_path: str):
    vertexai.init(
        project='your-project-id',
        location='your-region',
    )
    multimodal_model = GenerativeModel("gemini-2.0-flash-001")
    messages = [
        "Generate a birthday wish based on the following image",
        Part.from_image(Image.load_from_file(location=image_path))
    ]
    chat = multimodal_model.start_chat()
    
    for chunk in chat.send_message(content=messages, stream=True):
        print(chunk.text, end="", flush=True)

analyze_bouquet_image("bouquet.png")
