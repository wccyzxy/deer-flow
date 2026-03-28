import logging
import os

import requests

logger = logging.getLogger(__name__)


class BrowserUseClient:
    def __init__(self):
        self.base_url = os.getenv("BROWSER_USE_BASE_URL", "")
        if (self.base_url == ""):
            raise "BROWSER_USE_BASE_URL not set!"
    
    def search(self, query: str) -> str:
        search_url = f"{self.base_url}/search"
        headers = {
            "Content-Type": "application/json",
        }
        data = {
            "task_id": "deerflow_search_task_1",
            "query": query,
            "preview_mode": False
        }
        try:
            response = requests.post(search_url, headers=headers, json=data)

            if response.status_code != 200:
                error_message = f"Browser Use API returned status {response.status_code}: {response.text}"
                logger.error(error_message)
                return f"Error: {error_message}"

            data = response.json()
            if (not data.get("success", False)):
                error_message = f"Browser Use API returned error: {data.get('error', 'Unknown error')}"
                logger.error(error_message)
                return f"Error: {error_message}"
            result = ""
            for item in data.get("items",[]):
                result += f"Title: {item.get("title", "No title")}\nUrl: {item.get("url", "No URL")}\nDescription: {item.get("description", "No description")}\n\n"
            return result
        except Exception as e:
            error_message = f"Request to Browser Use API failed: {str(e)}"
            logger.error(error_message)
            return f"Error: {error_message}"

    def html2md(self, url: str) -> str:
        search_url = f"{self.base_url}/html-to-md"
        headers = {
            "Content-Type": "application/json",
        }
        data = {
            "task_id": "deerflow_search_task_2",
            "url": url,
            "preview_mode": False
        }
        try:
            response = requests.post(search_url, headers=headers, json=data)

            if response.status_code != 200:
                error_message = f"Browser Use API returned status {response.status_code}: {response.text}"
                logger.error(error_message)
                return f"Error: {error_message}"

            data = response.json()
            if (not data.get("success", False)):
                error_message = f"Browser Use API returned error: {data.get('error', 'Unknown error')}"
                logger.error(error_message)
                return f"Error: {error_message}"
            
            return data.get("markdown","")
        except Exception as e:
            error_message = f"Request to Browser Use API failed: {str(e)}"
            logger.error(error_message)
            return f"Error: {error_message}"
