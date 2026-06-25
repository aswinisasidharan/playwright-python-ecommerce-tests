import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_empty_credentials_shows_error(page: Page, base_url: str):
    """Submitting empty credentials shows a validation error."""
    login_page = LoginPage(page, base_url)
    login_page.goto()
    login_page.login("", "")  # empty credentials — triggers validation

    expect(login_page.error_message).to_contain_text("Username is required")
