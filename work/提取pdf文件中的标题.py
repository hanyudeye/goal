import fitz  # PyMuPDF

def extract_titles_from_pdf(pdf_path, min_font_size=12):
    """
    Extract potential titles from a PDF based on font size and style.
    
    :param pdf_path: Path to the PDF file.
    :param min_font_size: Minimum font size to consider as a title.
    :return: A list of titles extracted from the PDF.
    """
    titles = []
    
    try:
        # Open the PDF file
        document = fitz.open(pdf_path)
        print(f"Extracting titles from: {pdf_path}")

        for page_number, page in enumerate(document, start=1):
            blocks = page.get_text("dict")["blocks"]
            for block in blocks:
                for line in block.get("lines", []):
                    for span in line.get("spans", []):
                        # Check the font size
                        font_size = span.get("size", 0)
                        text = span.get("text", "").strip()
                        
                        if font_size >= min_font_size and text:
                            titles.append({"page": page_number, "text": text, "font_size": font_size})

        document.close()
    except Exception as e:
        print(f"Error processing the PDF: {e}")
        return []

    return titles


def save_titles_to_html(titles, output_html_path):
    """
    Save extracted titles to an HTML file.

    :param titles: List of titles with their details.
    :param output_html_path: Path to save the HTML file.
    """
    try:
        html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Extracted Titles</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }
        h1 { color: #333; }
        .title { margin-bottom: 10px; }
        .page-info { font-size: 0.9em; color: #555; }
    </style>
</head>
<body>
    <h1>Extracted Titles</h1>
    <ul>
"""
        for title in titles:
            html_content += f"""
        <li class="title">
            <strong>{title['text']}</strong>
            <div class="page-info">Page: {title['page']} | Font Size: {title['font_size']}</div>
        </li>
"""
        html_content += """
    </ul>
</body>
</html>
"""
        with open(output_html_path, "w", encoding="utf-8") as html_file:
            html_file.write(html_content)

        print(f"HTML file created: {output_html_path}")
    except Exception as e:
        print(f"Error saving titles to HTML: {e}")


# Example usage
if __name__ == "__main__":
    input_pdf = "example.pdf"  # Replace with your PDF file path
    output_html = "titles_output.html"  # Replace with your desired HTML file path

    # Extract titles
    extracted_titles = extract_titles_from_pdf(input_pdf, min_font_size=14)
    if extracted_titles:
        print("Extracted Titles:")
        for title in extracted_titles:
            print(f"Page {title['page']} (Font Size: {title['font_size']}): {title['text']}")

        # Save to HTML
        save_titles_to_html(extracted_titles, output_html)
    else:
        print("No titles found.")
