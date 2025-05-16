# Automation Exercise Website Testing Framework

## Overview
This project is an automated testing framework for [automationexercise.com](https://www.automationexercise.com) using Python, Playwright, and PyTest. The framework implements the Page Object Model (POM) design pattern and includes comprehensive test cases covering various functionalities of the e-commerce website.

## Features
- Page Object Model (POM) implementation
- Data-driven testing
- Allure reporting
- Screenshot capture on test failure
- Retry mechanism for flaky tests
- Comprehensive logging

## Tech Stack
- Python 3.12+
- Playwright
- PyTest
- Allure Report
- pytest-html

## Project Structure
```
ecommerce website/
├── config/
│   └── config.py           # Configuration settings
├── pages/
│   ├── __init__.py
│   ├── base_page.py       # Base page with common methods
│   ├── home_page.py       # Home page object
│   ├── login_page.py      # Login page object
│   └── signup_page.py     # Signup page object
├── tests/
│   ├── test_cases/
│   │   └── test_auth.py   # Authentication test cases
│   └── conftest.py        # PyTest configurations
├── reports/
│   ├── allure-results/    # Allure test results
│   └── allure-report/     # Generated Allure reports
├── screenshots/           # Failed test screenshots
├── requirements.txt      # Project dependencies
├── pytest.ini           # PyTest configuration
└── README.md           # Project documentation
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ecommerce-website
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install Playwright browsers:
```bash
playwright install
```

## Running Tests

### Run all tests:
```bash
pytest tests/test_cases/test_auth.py -v
```

### Run with Allure reporting:
```bash
pytest tests/test_cases/test_auth.py -v --alluredir=reports/allure-results
```

### Generate and view Allure report:
```bash
allure generate reports/allure-results --clean -o reports/allure-report
allure serve reports/allure-results
```

## Test Cases Covered

1. **User Authentication**
   - Register new user
   - Login with correct credentials
   - Login with incorrect credentials
   - Logout user
   - Register with existing email

2. **Contact and Test Cases**
   - Contact us form
   - Test cases page verification

3. **Products and Cart**
   - View all products
   - Product details
   - Search products
   - Add to cart
   - Remove from cart
   - Cart quantity

4. **Checkout Process**
   - Register while checkout
   - Register before checkout
   - Login before checkout
   - Download invoice

5. **Website Features**
   - Subscription in home page
   - Subscription in cart page
   - View category products
   - View & cart brand products
   - Add product reviews
   - Recommended items
   - Scroll functionality

## Configuration

The `config/config.py` file contains various configuration settings:
- Base URL
- Browser settings
- Timeouts
- Test user data
- Screenshot settings

## Page Objects

### BasePage
- Common methods for all pages
- Retry mechanisms
- Wait strategies
- Error handling

### LoginPage
- Login form handling
- Signup form handling
- Error message verification

### SignupPage
- Account creation form
- User details input
- Account verification

## Reporting

### Allure Reports
The framework generates detailed Allure reports including:
- Test execution results
- Test steps
- Screenshots for failed tests
- Test duration
- Error logs

### HTML Reports
Additional HTML reports are generated with:
- Test summary
- Test details
- Failure screenshots

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
[Your Name]

## Acknowledgments
- [Automation Exercise](https://www.automationexercise.com) for providing the test website
- Playwright team for the excellent browser automation framework
- PyTest community for the testing framework 