# SauceDemo UI Automation Framework

## Project Overview

This project is an end-to-end UI automation framework developed for the [SauceDemo](https://www.saucedemo.com/) e-commerce application using **Python, Playwright and Pytest**.

The framework follows the **Page Object Model (POM)** design pattern to maintain reusable, readable and maintainable automation code.

It automates critical e-commerce workflows, including user login, product selection, cart management and checkout.

## Tech Stack

- **Programming Language:** Python
- **Automation Tool:** Playwright
- **Test Framework:** Pytest
- **Design Pattern:** Page Object Model (POM)
- **Version Control:** Git and GitHub
- **CI/CD:** Jenkins

## Framework Features

- Page Object Model (POM) implementation.
- Reusable Pytest fixtures for browser initialization and test setup.
- End-to-end test automation for critical e-commerce workflows.
- Data-driven testing using Pytest parameterization.
- Cross-browser execution using Chromium and Firefox.
- Playwright assertions for UI validation.
- Centralized browser and context management.
- Jenkins integration for automated test execution.
- Scheduled execution of automation tests through Jenkins.

## Test Scenarios Covered

### Login
- Verify successful login with valid credentials.
- Validate login behavior with invalid credentials.
- Verify login behavior with blank credentials.

### Inventory
- Verify product listing and product details.
- Validate product sorting (A-Z, Z-A, Price Low to High, Price High to Low).
- Add and remove products from the cart.
- Navigate to the shopping cart.

### Cart
- Verify selected products in the cart.
- Remove products from the cart.
- Validate cart contents.

### Checkout
- Complete checkout information.
- Verify selected products and their prices in the order summary.
- Validate item subtotal, tax and total amount.
- Complete the order and verify the order confirmation message.

## Project Structure

```text
SauceDemo-Playwright/
│
├── pageObjects/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_overview_page.py
│   └── checkout_complete_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── conftest.py
├── requirements.txt
└── README.md
```

## Prerequisites

Make sure the following are installed:

- Python
- Git
- Visual Studio Code (recommended)
- Jenkins (for CI/CD execution)

## Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/mohitpatnaik1999/SauceDemo-Playwright-Python.git
```

**2. Navigate to the project directory**

```bash
cd SauceDemo-Playwright-Python
```

**3. Create a virtual environment**

```bash
python -m venv venv
```

**4. Activate the virtual environment**

Windows:

```powershell
venv\Scripts\activate
```

**5. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

**6. Install Playwright browsers**

```bash
python -m playwright install
```

## Test Execution

**Run all tests**

```bash
python -m pytest
```

**Run tests with detailed output**

```bash
python -m pytest -v -s
```

**Run tests on Chromium**

```bash
python -m pytest -v -s --browser_name=chrome
```

**Run tests on Firefox**

```bash
python -m pytest -v -s --browser_name=firefox
```

Note: Browser selection is controlled through the custom `--browser_name` Pytest command-line option.

## Jenkins Integration

The framework is integrated with Jenkins using a Freestyle project.

The Jenkins job is configured to:

- Retrieve the automation framework from GitHub.
- Execute Pytest test cases.
- Accept browser selection through a build parameter.
- Support scheduled test execution.

Example Windows batch command:

```bat
python -m pytest -v -s --browser_name "%browser%"
```

The browser parameter supports:

- chrome
- firefox

## Future Enhancements

- Integrate API automation using Python Requests.
- Implement test reporting and enhanced failure diagnostics.

## Author

**Mohit Patnaik**
