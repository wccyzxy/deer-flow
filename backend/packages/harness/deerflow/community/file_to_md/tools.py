import json
from langchain.tools import tool
from dotenv import load_dotenv

load_dotenv()

from markitdown import MarkItDown


@tool("file_to_markdown", parse_docstring=True)
def file_to_markdown_tool(file_path: str, output_path: str = "", metadata: json = {}) -> str:
    """Convert a file to Markdown format.

    This tool supports converting various file formats to Markdown:
    - Excel files (.xlsx, .xls)
    - CSV files (.csv)
    - Word documents (.docx)
    - PDF files (.pdf)
    - Text files (.txt, .md)
    - Code files (.py, .js, .java, etc.)

    The tool will extract the content and structure from the file and convert it to well-formatted Markdown.

    Args:
        file_path: The path to the file to convert (required)
        output_path: The path where the Markdown file should be saved (optional, will generate automatically if not provided)
        metadata: JSON string of metadata to include in the output (optional, format: '{"author": "name", "version": "1.0"}')

    Returns:
        str: Success message with output path or error message
    """
    try:
        md = MarkItDown()
        result = md.convert(file_path)
        metadata_txt = "---\n"
        for k,v in metadata:
            metadata += k + ":" + v + "\n"
        metadata_txt += "---\n\n"

        with open(output_path, "w", encoding="utf-8") as f:
            if metadata != {}:
                f.write(metadata_txt)
            f.write(result.text_content)

    except Exception as e:
        return f"❌ 工具执行错误: {str(e)}"
