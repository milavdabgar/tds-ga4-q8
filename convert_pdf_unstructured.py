from unstructured.partition.pdf import partition_pdf
from pathlib import Path

def convert_to_markdown():
    elements = partition_pdf("q-pdf-to-markdown.pdf")
    markdown_content = ""
    
    for element in elements:
        text = str(element).strip()
        if text:
            # Convert potential headers
            if "EduDocs Inc." in text:
                markdown_content += f"# {text}\n\n"
            elif any(header in text for header in ["Your Task", "Impact"]):
                markdown_content += f"## {text}\n\n"
            else:
                markdown_content += f"{text}\n\n"
    
    with open("output.md", "w") as f:
        f.write(markdown_content)

if __name__ == "__main__":
    convert_to_markdown()
