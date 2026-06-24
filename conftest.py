import pytest
from playwright.sync_api import Page


# You can add shared fixtures here later — e.g. a logged-in page state
# For now this file tells pytest the test root

@pytest.fixture(scope="session")
def base_url():
    return "https://www.saucedemo.com/"
