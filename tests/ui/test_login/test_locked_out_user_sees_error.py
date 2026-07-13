import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


@pytest.mark.sanity
@pytest.mark.regression
@pytest.mark.login
def test_locked_out_user_sees_error(page: Page, base_url: str):
    login_page = LoginPage(page, base_url)
    login_page.goto()
    login_page.login("locked_out_user", "secret_sauce")

    expect(login_page.error_message).to_contain_text("locked out")
