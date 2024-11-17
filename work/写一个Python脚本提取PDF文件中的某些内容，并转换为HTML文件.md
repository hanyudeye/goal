 
以下是一个Python脚本，使用 `PyPDF2` 和 `html` 模块提取 PDF 文件中的文本内容，并将其转换为 HTML 文件：

### 脚本代码

```python
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
```

---

### 脚本功能说明
1. **PDF 文本提取**：
   - 使用 `PyPDF2.PdfReader` 提取每一页的文本内容。
   - 对提取的文本使用 `escape`，将 HTML 保留字符（如 `<`, `>`, `&`）转换为安全字符。

2. **HTML 文件生成**：
   - 将提取的内容逐页嵌入 HTML `<pre>` 标签，保持原始格式。
   - 使用一个简单的 HTML 模板包装内容。

3. **输出文件**：
   - 提取的内容保存到指定的 `output.html` 文件。

---

### 使用步骤
1. 安装依赖：
   ```bash
   pip install PyPDF2
   ```

2. 准备 PDF 文件：
   - 将待提取的 PDF 文件（如 `example.pdf`）放在与脚本相同的目录下，或提供其完整路径。

3. 运行脚本：
   ```bash
   python script_name.py
   ```

4. 查看结果：
   - 脚本运行后，生成的 HTML 文件会保存到指定的 `output.html` 路径。

---

### 结果示例
生成的 HTML 文件结构如下：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Extracted PDF Content</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }
        h2 { color: #333; }
        pre { background: #f4f4f4; padding: 10px; border: 1px solid #ddd; overflow-x: auto; }
    </style>
</head>
<body>
    <h1>PDF Content</h1>
    <h2>Page 1</h2>
    <pre>Text extracted from page 1...</pre>
    <h2>Page 2</h2>
    <pre>Text extracted from page 2...</pre>
</body>
</html>
```

### 注意事项
- **PDF 文档的复杂性**：某些 PDF 文档使用图像而非文本格式，可能无法提取文本。为此，你可以尝试 OCR 工具（如 Tesseract）。
- **内容优化**：如果需要保留更复杂的格式，可以使用其他 PDF 解析库（如 `pdfplumber` 或 `PyMuPDF`）。