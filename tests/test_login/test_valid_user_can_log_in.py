import pytest
import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_valid_user_can_log_in(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    # Assert we landed on the inventory page
    expect(page).to_have_url(re.compile("inventory"))
