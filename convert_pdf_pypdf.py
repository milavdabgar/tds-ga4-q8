import PyPDF2

def pdf_to_markdown(pdf_path):
    reader = PyPDF2.PdfReader(pdf_path)
    markdown_content = ""
    
    for page in reader.pages:
        text = page.extract_text()
        paragraphs = text.split('\n\n')
        
        for paragraph in paragraphs:
            paragraph = paragraph.strip()
            if paragraph:
                # Convert potential headers
                if "EduDocs Inc." in paragraph:
                    markdown_content += f"# {paragraph}\n\n"
                elif any(header in paragraph for header in ["Your Task", "Impact"]):
                    markdown_content += f"## {paragraph}\n\n"
                else:
                    markdown_content += f"{paragraph}\n\n"
    
    with open("output.md", "w", encoding="utf-8") as f:
        f.write(markdown_content)

if __name__ == "__main__":
    pdf_to_markdown("q-pdf-to-markdown.pdf")
