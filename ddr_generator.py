import os
from dotenv import load_dotenv
from google import genai
from prompts import DDR_PROMPT_TEMPLATE

load_dotenv()


def build_image_references(image_paths: list) -> str:
    if not image_paths:
        return "No extracted images found. Mention 'Image Not Available' where needed."

    refs = []
    for idx, path in enumerate(image_paths, start=1):
        refs.append(f"Image {idx}: {os.path.basename(path)}")
    return "\n".join(refs)


def generate_ddr_report(inspection_text: str, thermal_text: str, image_paths: list) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in .env file")

    client = genai.Client(api_key=api_key)

    image_references = build_image_references(image_paths)

    prompt = DDR_PROMPT_TEMPLATE.format(
        inspection_text=inspection_text[:30000],
        thermal_text=thermal_text[:30000],
        image_references=image_references
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text