from langchain.tools import tool
from dotenv import load_dotenv

load_dotenv()

from deerflow.community.browser_use.browser_use_client import BrowserUseClient

@tool("web_search", parse_docstring=True)
def web_search_tool(query: str) -> str:
    """Search the web.

    Args:
        query: The query to search for.
    """

    browser_use_client = BrowserUseClient()
    return browser_use_client.search(query)

@tool("web_fetch", parse_docstring=True)
def web_fetch_tool(url: str) -> str:
    """Fetch the contents of a web page at a given URL.
    Only return the markdown of given URL

    Args:
        url: The URL to fetch the contents of.
    """
    browser_use_client = BrowserUseClient()
    html_content = browser_use_client.html2md(url)
    return html_content[:4096]
