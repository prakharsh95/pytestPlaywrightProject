# Test Automation Project

This project is an automated testing framework that tests a web application. Think of it as a robot that can automatically check if a website works correctly by clicking buttons, filling forms, and verifying that everything appears as expected.

## What Does This Project Do?

This project tests an e-commerce website (an online shopping site). It performs the following checks:

1. **Creates Orders**: Uses the website's API (a way for programs to talk to the website) to create a test order
2. **Logs In**: Automatically logs into the website using test credentials
3. **Views Orders**: Navigates to the orders page and checks if the order that was created appears correctly
4. **Verifies Details**: Makes sure all the order details match what was expected
5. **Cleans Up**: Deletes the test order and logs out

The tests ensure that when you create an order through the API, you can see it correctly in the website's user interface.

## Technologies Used

- **Python**: The programming language used to write the tests
- **pytest**: A testing framework that helps organize and run tests
- **Playwright**: A tool that controls a web browser (like Chrome or Firefox) automatically
- **pytest-bdd**: Allows writing tests in plain English using a format called "Behavior-Driven Development"

## Project Structure

Here's what each folder and file does:

```
pytestPlaywrightProject/
├── pageObject/          # Contains code for interacting with different pages of the website
│   ├── loginPage.py     # Handles login functionality
│   ├── dashboard.py     # Handles the main dashboard page
│   ├── ordersPage.py    # Handles the orders listing page
│   └── orderDetails.py  # Handles viewing individual order details
│
├── utils/               # Helper functions and utilities
│   └── API_utils.py     # Functions for making API calls (creating/deleting orders)
│
├── feature/             # Test scenarios written in plain English
│   └── orderTransaction.feature  # Describes what the test should do
│
├── test_order_transaction_bdd.py  # The main test file that runs the scenarios
├── test_api_1.py        # Additional API tests
├── test_api_ui_e2e.py   # End-to-end tests combining API and UI
├── conftest.py          # Configuration file that sets up the browser for testing
├── requirements.txt     # List of all Python packages needed for this project
└── report.html          # Test results report (generated after running tests)
```

## Prerequisites

Before you can run this project, you need to have:

1. **Python** installed on your computer (version 3.7 or higher)
2. **pip** (Python's package installer) - usually comes with Python

## Setup Instructions

Follow these steps to get the project ready to run:

### Step 1: Install Python Packages

Open your terminal (command prompt) and navigate to this project folder. Then run:

```bash
pip install -r requirements.txt
```

This will install all the necessary tools and libraries needed for the project.

### Step 2: Install Playwright Browsers

After installing the packages, you need to install the browser engines that Playwright will use:

```bash
playwright install
```

This downloads Chrome and Firefox browsers that Playwright will control.

## How to Run the Tests

Once everything is set up, you can run the tests in different ways:

### Run All Tests

To run all the tests in the project:

```bash
pytest
```

### Run Tests with HTML Report

To generate a nice HTML report showing test results:

```bash
pytest --html=report.html
```

After running, open `report.html` in your web browser to see the results.

### Run Tests in a Specific Browser

By default, tests run in Chrome. To run in Firefox instead:

```bash
pytest --browserName=firefox
```

### Run Tests in Parallel (Faster)

If you have multiple tests, you can run them at the same time to save time:

```bash
pytest -n auto
```

### Run a Specific Test File

To run only one test file:

```bash
pytest test_order_transaction_bdd.py
```

## Understanding the Test Flow

Here's what happens when you run the main test:

1. **Create Order via API**: The test creates an order using the website's API (like placing an order programmatically)
2. **Login**: Opens a browser, goes to the website, and logs in with test credentials
3. **Navigate to Orders**: Clicks through the website to find the orders page
4. **View Order**: Finds and clicks on the order that was just created
5. **Verify Details**: Checks that all the order information is correct
6. **Clean Up**: Deletes the test order via API and logs out

## Test Results

After running tests, you'll find:

- **report.html**: A visual report showing which tests passed or failed
- **test-results/**: A folder containing trace files that can help debug if something goes wrong

## Troubleshooting

**Problem**: Tests fail with "browser not found" error
- **Solution**: Make sure you ran `playwright install` after installing requirements

**Problem**: Import errors when running tests
- **Solution**: Make sure you're in the project directory and all packages are installed with `pip install -r requirements.txt`

**Problem**: Tests can't find the website
- **Solution**: Check your internet connection - the tests need to access the website online

## Notes

- Tests run in "headless" mode by default, meaning the browser runs in the background without showing a window. This makes tests run faster.
- The test uses real credentials (stored in the test files) to log into the test website.
- All test orders created during testing are automatically deleted at the end to keep things clean.

## Support

If you encounter any issues or have questions, check:
- The test output in the terminal for error messages
- The HTML report for detailed test results
- The trace files in the `test-results/` folder for debugging information
