![Playwright Tests](https://github.com/aswinisasidharan/playwright-python-ecommerce-tests/actions/workflows/playwright.yml/badge.svg)

# Playwright Python E-commerce Tests

Automation test framework built with Playwright and Python using pytest.

## Tech Stack
- Python 3.9+
- Playwright
- pytest
- pytest-html

## Test Coverage
- Login validation (3 tests)
- Cart — add and remove items (4 tests)
- Checkout flow (2 tests)

## How to Run

```bash
# Install dependencies
pip install -r requirements.txt
playwright install

# Run all tests
pytest tests/ --browser chromium -v

# Run with HTML report
pytest tests/ --browser chromium --html=report.html -v
```

## Project Structure
```
tests/
├── test_login.py
├── test_cart.py
└── test_checkout.py
```