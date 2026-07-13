import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


@pytest.mark.regression
@pytest.mark.login
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
        ("", "secret_sauce", "Epic sadface: Username is required"),
        ("standard_user", "", "Epic sadface: Password is required"),
    ],
    ids=["locked-out-user", "empty-username", "empty-password"],
)
def test_login_shows_expected_error(
    base_url, page: Page, username: str, password: str, expected_error: str
):
    login_page = LoginPage(page, base_url)
    login_page.goto()
    login_page.login(username, password)
    expect(login_page.error_message).to_have_text(expected_error)
