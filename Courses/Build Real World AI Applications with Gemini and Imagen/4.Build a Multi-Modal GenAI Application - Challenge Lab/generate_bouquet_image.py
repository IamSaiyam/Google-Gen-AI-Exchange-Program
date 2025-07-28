import vertexai
from vertexai.preview.vision_models import ImageGenerationModel

def generate_image(project_id, location, output_file, prompt):
    vertexai.init(project=project_id, location=location)
    model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-002")
    images = model.generate_images(
        prompt=prompt,
        number_of_images=1,
        seed=1,
        add_watermark=False,
    )
    images[0].save(location=output_file)
    print(f"Image saved to: {output_file}")
    return images

generate_image(
    project_id="your-project-id",
    location="your-region",
    output_file="bouquet.png",
    prompt="Create an image containing a bouquet of 2 sunflowers and 3 roses"
)