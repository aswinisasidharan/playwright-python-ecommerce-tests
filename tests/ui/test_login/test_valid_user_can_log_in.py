import pytest
import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


@pytest.mark.smoke
@pytest.mark.login
def test_valid_user_can_log_in(page: Page, base_url:str):
    login_page = LoginPage(page, base_url)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    # Assert we landed on the inventory page
    expect(page).to_have_url(re.compile("inventory"))
