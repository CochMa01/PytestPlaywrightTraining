import pytest
import pandas as fileReader
from playwright.sync_api import expect
from batch1.src.pages.LoginPage import LoginPage

@pytest.fixture(scope="module")
def test_data(logger):
    sheet_name = "Logout"
    test_data_file = "batch1/src/tests/data/test_data.xlsx"
    try:
        dataFile = fileReader.read_excel(test_data_file, sheet_name = sheet_name)
        logger.info(f"Successfully read test data from file: {test_data_file} with sheet: {sheet_name}.\n")
    except Exception as e:
        logger.error(f"Failed to read test data: {e}")
        pytest.fail(f"Failed to read test data: {e}")
    return dataFile

def get_test_data(test_data, test_name, column_name):
    return test_data.loc[test_data["Test Name"] == test_name, column_name].values[0]

@pytest.mark.parametrize("test_name", ["test_logout"])
def test_logout(test_data, test_name, setup_teardown, logger) -> None:
    page = setup_teardown
    username = get_test_data(test_data, test_name, "Username")
    password = get_test_data(test_data, test_name, "Password")

    logger.info(f"---------- Running test: {test_name} ----------")

    credentials = {"username": username, "password": password}
    login_page = LoginPage(page, logger)
    products_page = login_page.do_login(credentials)
    expect(products_page.products_header).to_be_visible()
    expect(products_page.products_header).to_have_text("Products")

    products_page.do_logout()
    expect(login_page.login_button_locator).to_be_visible()

    logger.info(f"---------- Completed test: {test_name} ----------\n")
