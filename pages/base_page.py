from playwright.sync_api import Page
import logging
import time
from typing import Optional

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.automationexercise.com"
        self.logger = logging.getLogger(__name__)

    def navigate(self, url: str, max_retries: int = 3, timeout: int = 60000):
        """Navigate to URL with retry logic"""
        self.logger.info(f"Navigating to {url}")
        for attempt in range(max_retries):
            try:
                self.page.goto(url, timeout=timeout)
                self.page.wait_for_load_state("networkidle", timeout=timeout)
                self.page.wait_for_load_state("domcontentloaded", timeout=timeout)
                return
            except Exception as e:
                if attempt == max_retries - 1:
                    raise e
                time.sleep(2)  # Wait before retry

    def click(self, selector: str, timeout: int = 60000):
        """Click element with retry logic"""
        self.logger.info(f"Clicking element: {selector}")
        try:
            self.page.wait_for_selector(selector, timeout=timeout, state="visible")
            element = self.page.locator(selector)
            element.wait_for(state="visible", timeout=timeout)
            element.click()
            self.page.wait_for_load_state("networkidle", timeout=timeout)
        except Exception as e:
            self.logger.error(f"Failed to click element: {selector}")
            raise e

    def fill(self, selector: str, text: str, timeout: int = 60000):
        """Fill text in element with retry logic"""
        self.logger.info(f"Filling {text} in {selector}")
        try:
            self.page.wait_for_selector(selector, timeout=timeout, state="visible")
            element = self.page.locator(selector)
            element.wait_for(state="visible", timeout=timeout)
            element.fill(text)
        except Exception as e:
            self.logger.error(f"Failed to fill text in element: {selector}")
            raise e

    def get_text(self, selector: str, timeout: int = 60000) -> str:
        """Get text from element with retry logic"""
        try:
            self.page.wait_for_selector(selector, timeout=timeout, state="visible")
            element = self.page.locator(selector)
            element.wait_for(state="visible", timeout=timeout)
            return element.text_content() or ""
        except Exception as e:
            self.logger.error(f"Failed to get text from element: {selector}")
            raise e

    def get_element_count(self, selector: str, timeout: int = 60000) -> int:
        """Get count of elements matching selector"""
        self.page.wait_for_selector(selector, timeout=timeout)
        return len(self.page.query_selector_all(selector))

    def is_visible(self, selector: str, timeout: int = 60000) -> bool:
        """Check if element is visible"""
        try:
            element = self.page.wait_for_selector(selector, timeout=timeout, state="visible")
            return element.is_visible()
        except:
            return False

    def wait_for_navigation(self, timeout: int = 60000):
        """Wait for navigation to complete"""
        self.page.wait_for_load_state("networkidle", timeout=timeout)
        self.page.wait_for_load_state("domcontentloaded", timeout=timeout)

    def wait_for_element(self, locator: str, timeout: int = 30000):
        """Wait for element to be visible"""
        self.page.wait_for_selector(locator, timeout=timeout, state="visible")

    def take_screenshot(self, name: str):
        """Take screenshot"""
        self.page.screenshot(path=f"screenshots/{name}.png") 