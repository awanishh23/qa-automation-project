# QA Automation Framework – Selenium + Python + Pytest

## Overview
This project is a QA Automation framework developed using Selenium WebDriver, Python, and Pytest. It automates UI testing of a real web application and includes API testing, logging, screenshots, and HTML reports.

The framework follows industry best practices like Page Object Model (POM), modular structure, and automated reporting.

---

## Features
- Automated UI testing using Selenium WebDriver
- API testing using Python requests library
- Page Object Model (POM) design pattern
- Test execution using Pytest
- Automatic screenshot capture on failure
- HTML test report generation
- Logging system for debugging and tracking
- Organized and scalable framework structure

---

## Tech Stack
- Python 3
- Selenium WebDriver
- Pytest
- Requests (API testing)
- WebDriver Manager
- Pytest HTML Reports

---

## Project Structure

```
qa-automation-selenium
│
├── tests
│   ├── test_valid_login.py
│   ├── test_invalid_login.py
│   ├── test_api_users.py
│
├── pages
│   ├── login_page.py
│
├── utils
│   ├── driver_setup.py
│   ├── logger.py
│
├── testdata
│   ├── test_data.py
│
├── screenshots
├── reports
├── logs
├── requirements.txt
├── README.md
```


---

## Test Scenarios Automated

### UI Tests
- Valid login test
- Invalid login test
- Login functionality validation

Tested website:  
https://the-internet.herokuapp.com/login

---

### API Tests
- GET request validation
- Response status verification
- JSON response validation

Tested API:  
https://httpbin.org/get

---

## Installation

Clone repository:

```bash
git clone https://github.com/awanishh23/qa-automation-project
```
Go to folder:
```
cd qa-automation-selenium
```
Install dependencies:
```
pip install -r requirements.txt
```
---

### How to Run Tests

Run all tests:
```
pytest -v
```
Run tests with HTML report:
```
pytest -v --html=reports/report.html
```
---
### Test Reports

After execution, open:
```
reports/report.html
```
to view detailed test results.

---

### Screenshots

Screenshots are automatically captured in:
```
screenshots/
```
if any test fails.

<img width="1914" height="1123" alt="Screenshot 2026-02-27 132343" src="https://github.com/user-attachments/assets/8b7a39e9-6910-4062-9761-4511d0ee2cbb" />

<img width="1323" height="278" alt="Screenshot 2026-02-27 144815" src="https://github.com/user-attachments/assets/97d92c73-62a4-4438-b2b1-c1e48a6bebc1" />

---
### Logging

Logs are stored in:
```
logs/test.log
```
to help debug failures.

---

## Skills Demonstrated
- Selenium WebDriver Automation
- Python Automation Scripting
- Pytest Framework
- API Testing
- Test Case Design
- Page Object Model
- Test Reporting
- Debugging and Logging

---

## Author
Awanish Ojha
( B.Tech Computer Science Engineering )

