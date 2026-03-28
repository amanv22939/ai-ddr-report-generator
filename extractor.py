import os
import fitz
from docx import Document


def extract_text_from_pdf(pdf_path: str) -> str:
    text = []
    doc = fitz.open(pdf_path)

    for page_num, page in enumerate(doc, start=1):
        page_text = page.get_text("text")
        text.append(f"\n--- Page {page_num} ---\n{page_text}")

    doc.close()
    return "\n".join(text).strip()


def extract_images_from_pdf(pdf_path: str, output_dir: str, prefix: str = "img") -> list:
    os.makedirs(output_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    saved_images = []

    for page_index in range(len(doc)):
        page = doc[page_index]
        image_list = page.get_images(full=True)

        for img_index, img in enumerate(image_list, start=1):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]

            image_name = f"{prefix}_page{page_index + 1}_{img_index}.{image_ext}"
            image_path = os.path.join(output_dir, image_name)

            with open(image_path, "wb") as img_file:
                img_file.write(image_bytes)

            saved_images.append(image_path)

    doc.close()
    return saved_images


def extract_text_from_docx(docx_path: str) -> str:
    doc = Document(docx_path)
    paragraphs = [para.text for para in doc.paragraphs if para.text.strip()]
    return "\n".join(paragraphs).strip()


def extract_text(file_path: str) -> str:
    lower_path = file_path.lower()

    if lower_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif lower_path.endswith(".docx"):
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format. Please upload PDF or DOCX.")


def extract_images(file_path: str, output_dir: str, prefix: str = "img") -> list:
    if file_path.lower().endswith(".pdf"):
        return extract_images_from_pdf(file_path, output_dir, prefix)
    return []