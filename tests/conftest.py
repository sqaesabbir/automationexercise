import pytest
from playwright.sync_api import Page, Browser, BrowserContext
from typing import Generator
import os
from datetime import datetime

from config.config import Config
from pages.home_page import HomePage

def pytest_addoption(parser):
    """Add custom command line options"""
    parser.addoption(
        "--browser-type",
        action="store",
        default="chromium",
        help="Browser to use for testing (chromium, firefox, webkit)"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode"
    )

@pytest.fixture(scope="session")
def browser_type_launch_args(pytestconfig) -> dict:
    """Get browser launch arguments"""
    return {
        "headless": pytestconfig.getoption("headless"),
        **Config.get_browser_config()
    }

@pytest.fixture(scope="session")
def browser_context_args() -> dict:
    """Get browser context arguments"""
    return {
        "viewport": {
            "width": 1920,
            "height": 1080
        },
        "ignore_https_errors": True
    }

@pytest.fixture(scope="session")
def browser_name(pytestconfig) -> str:
    """Get browser name from command line options"""
    return pytestconfig.getoption("browser-type")

@pytest.fixture
def page(browser: Browser, browser_context_args) -> Generator[Page, None, None]:
    """Create a new page for each test"""
    context = browser.new_context(**browser_context_args)
    page = context.new_page()
    yield page
    try:
        page.close()
    except:
        pass
    try:
        context.close()
    except:
        pass

@pytest.fixture
def home_page(page: Page) -> HomePage:
    """Create HomePage instance"""
    return HomePage(page)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Take screenshot on test failure"""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed and "page" in item.funcargs:
        page: Page = item.funcargs["page"]
        screenshot_dir = Config.SCREENSHOT_PATH
        os.makedirs(screenshot_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(
            screenshot_dir,
            f"failure_{item.name}_{timestamp}.png"
        )
        
        try:
            if not page.is_closed():
                page.screenshot(path=screenshot_path)
                print(f"\nScreenshot saved to: {screenshot_path}")
        except Exception as e:
            print(f"\nFailed to take screenshot: {str(e)}") 