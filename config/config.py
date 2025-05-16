import os
from typing import Dict

class Config:
    """Test configuration"""
    
    # Base URL
    BASE_URL = "https://www.automationexercise.com"
    
    # Browser settings
    BROWSER = os.getenv("BROWSER", "chromium")  # chromium, firefox, or webkit
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    SLOW_MO = int(os.getenv("SLOW_MO", "0"))  # Slow down execution by X milliseconds
    
    # Timeouts (in milliseconds)
    DEFAULT_TIMEOUT = 30000
    NAVIGATION_TIMEOUT = 30000
    
    # Screenshot settings
    SCREENSHOT_ON_FAILURE = True
    SCREENSHOT_PATH = "screenshots"
    
    # Test data
    TEST_USER: Dict[str, str] = {
        "name": "Test User",
        "email": "testuser@example.com",
        "password": "testpass123",
        "first_name": "Test",
        "last_name": "User",
        "address": "123 Test St",
        "country": "United States",
        "state": "Test State",
        "city": "Test City",
        "zipcode": "12345",
        "mobile_number": "1234567890"
    }
    
    @classmethod
    def get_browser_config(cls) -> Dict:
        """Get browser configuration"""
        return {
            "headless": cls.HEADLESS,
            "slow_mo": cls.SLOW_MO
        }
    
    @classmethod
    def ensure_screenshot_dir(cls):
        """Ensure screenshot directory exists"""
        os.makedirs(cls.SCREENSHOT_PATH, exist_ok=True) 