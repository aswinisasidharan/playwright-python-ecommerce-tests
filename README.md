[![Playwright Tests](https://github.com/aswinisasidharan/playwright-python-ecommerce-tests/actions/workflows/playwright.yml/badge.svg)](https://github.com/aswinisasidharan/playwright-python-ecommerce-tests/actions/workflows/playwright.yml)

# Playwright Python E-commerce Tests

End-to-end UI and API test automation framework built with **Playwright** 
and **Python**, following the Page Object Model design pattern with 
GitHub Actions CI.

## Tech Stack
- Python 3.9+
- Playwright (pytest-playwright)
- pytest + pytest-html
- requests (API testing)
- GitHub Actions (CI/CD)

## Test Coverage
| Folder | File | Tests | What it covers |
|--------|------|-------|----------------|
| ui | test_login.py | 3 | Login validation |
| ui | test_cart.py | 4 | Add and remove items |
| ui | test_checkout.py | 2 | Checkout flow |
| api | test_api_bookings.py | 3 | Booking API — GET, POST |

## How to Run

```bash
# Clone the repo
git clone https://github.com/aswinisasidharan/playwright-python-ecommerce-tests.git
cd playwright-python-ecommerce-tests

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows

# Install dependencies
pip install -r requirements.txt
playwright install

# Run all tests
pytest tests/ --browser chromium -v

# Run UI tests only
pytest tests/ui/ --browser chromium -v

# Run API tests only
pytest tests/api/ -v

# Run with HTML report
pytest tests/ --browser chromium --html=report.html -v
```

## Project Structure

- `pages/` — Page Object Model classes (UI)
- `api/clients/` — API client classes
- `tests/ui/` — UI tests (Playwright)
- `tests/api/` — API tests (requests)
- `conftest.py` — shared pytest fixtures
- `pytest.ini` — pytest configuration
- `requirements.txt` — project dependencies
