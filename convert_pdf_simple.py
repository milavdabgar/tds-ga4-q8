import fitz

def pdf_to_markdown(pdf_path):
    doc = fitz.open(pdf_path)
    markdown_content = ""
    
    for page in doc:
        blocks = page.get_text("blocks")
        for block in blocks:
            text = block[4].strip()
            if text:
                # Convert potential headers
                if "EduDocs Inc." in text:
                    markdown_content += f"# {text}\n\n"
                elif any(header in text for header in ["Your Task", "Impact"]):
                    markdown_content += f"## {text}\n\n"
                else:
                    markdown_content += f"{text}\n\n"
    
    with open("output.md", "w", encoding="utf-8") as f:
        f.write(markdown_content)

if __name__ == "__main__":
    pdf_to_markdown("q-pdf-to-markdown.pdf")
