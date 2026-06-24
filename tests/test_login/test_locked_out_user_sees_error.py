import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_locked_out_user_sees_error(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("locked_out_user", "secret_sauce")

    expect(login_page.error_message).to_contain_text("locked out")
