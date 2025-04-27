import os
from PyPDF2 import PdfReader

# Step 1: Extract Text from PDF
def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    extracted_text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            extracted_text += page_text + "\n"
    return extracted_text.strip()

# Step 2: Clean Text: Insert Spacing + Indentation
def clean_extracted_text(raw_text):
    lines = raw_text.split("\n")
    cleaned_lines = []
    for i, line in enumerate(lines):
        stripped = line.strip()

        # Default no indent
        indent = ""

        # Detect Section Start (§1, §2, etc.)
        if stripped.startswith("§") and stripped[1].isdigit():
            if cleaned_lines and cleaned_lines[-1].strip() != "":
                cleaned_lines.append("")  # Blank line
                cleaned_lines.append("")  # Second blank line

        # Detect Subsections (e.g., (a), (b))
        elif stripped.startswith("(") and len(stripped) >= 3 and stripped[2] == ")":
            if stripped[1].islower():
                indent = "\t"  # One tab for (a), (b), (c)
                if cleaned_lines and cleaned_lines[-1].strip() != "":
                    cleaned_lines.append("")  # Insert blank line before subsection

            elif stripped[1].isdigit():
                indent = "\t\t"  # Two tabs for (1), (2), (3)

            elif stripped[1].isupper():
                indent = "\t\t\t"  # Optional three tabs for (A), (B), (C) — we can turn this off if you want later

        cleaned_lines.append(f"{indent}{line.rstrip()}")

    return "\n".join(cleaned_lines)

# Step 3: Save Clean Text as Markdown with Metadata
def save_as_markdown(section_number, section_title, body_text, output_folder):
    markdown_content = f"""---
section: {section_number}
title: "{section_title}"
source: "Internal Revenue Code"
year: 2025
---

{body_text}
"""
    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, f"Section_{section_number}.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)
    print(f"✅ Markdown saved to: {output_path}")
    return output_path

# Master runner
def process_pdf_to_markdown(pdf_path, section_number, section_title, markdown_folder):
    # Extract text
    raw_text = extract_text_from_pdf(pdf_path)
    # Clean + indent
    cleaned_text = clean_extracted_text(raw_text)
    # Save
    markdown_path = save_as_markdown(section_number, section_title, cleaned_text, markdown_folder)
    return markdown_path

# Example usage
if __name__ == "__main__":
    pdf_path = r"C:\Users\seanm\OneDrive\Documents\Projects\RAG_tax\section 1.pdf"  # Update to your actual PDF path
    section_number = "1"
    section_title = "Tax Imposed"
    markdown_folder = r"C:\Users\seanm\OneDrive\Documents\Projects\RAG_tax\markdown_sections"

    process_pdf_to_markdown(pdf_path, section_number, section_title, markdown_folder)
