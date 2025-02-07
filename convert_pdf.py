import fitz
import json

def pdf_to_markdown(pdf_path):
    doc = fitz.open(pdf_path)
    markdown_content = ""
    
    for page in doc:
        text = page.get_text()
        markdown_content += text + "\n\n"
    
    # Basic formatting improvements
    lines = markdown_content.split("\n")
    formatted_lines = []
    
    for line in lines:
        line = line.strip()
        if line:
            # Convert potential headers
            if "EduDocs Inc." in line:
                formatted_lines.append(f"# {line}")
            elif "Your Task" in line:
                formatted_lines.append(f"## {line}")
            elif "Impact" in line:
                formatted_lines.append(f"## {line}")
            else:
                formatted_lines.append(line)
    
    markdown_content = "\n\n".join(formatted_lines)
    
    with open("output.md", "w") as f:
        f.write(markdown_content)

if __name__ == "__main__":
    pdf_to_markdown("q-pdf-to-markdown.pdf")
