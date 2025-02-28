import os
from PyPDF2 import PdfReader
from html import escape

def extract_pdf_to_html(pdf_path, output_html_path):
    """
    Extracts text from a PDF file and converts it to an HTML file.
    
    :param pdf_path: Path to the input PDF file
    :param output_html_path: Path to save the output HTML file
    """
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file '{pdf_path}' not found.")
        return
    
    try:
        # Read the PDF
        reader = PdfReader(pdf_path)
        content = ""
        
        print(f"Extracting text from PDF: {pdf_path}")
        
        for page_number, page in enumerate(reader.pages, start=1):
            text = page.extract_text()  # Extract text from the current page
            content += f"<h2>Page {page_number}</h2>\n<pre>{escape(text)}</pre>\n"
        
        # Generate HTML structure
        html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Extracted PDF Content</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }}
        h2 {{ color: #333; }}
        pre {{ background: #f4f4f4; padding: 10px; border: 1px solid #ddd; overflow-x: auto; }}
    </style>
</head>
<body>
    <h1>PDF Content</h1>
    {content}
</body>
</html>"""
        
        # Write to the HTML file
        with open(output_html_path, "w", encoding="utf-8") as html_file:
            html_file.write(html_template)
        
        print(f"HTML file created: {output_html_path}")
    
    except Exception as e:
        print(f"Error while processing the PDF: {e}")


# Example usage
if __name__ == "__main__":
    input_pdf = "example.pdf"  # Replace with your PDF file path
    output_html = "output.html"  # Replace with your desired output HTML file path
    extract_pdf_to_html(input_pdf, output_html)
