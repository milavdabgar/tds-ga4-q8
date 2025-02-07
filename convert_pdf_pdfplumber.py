import pdfplumber

def pdf_to_markdown(pdf_path):
    markdown_content = ""
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
            
            for paragraph in paragraphs:
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
