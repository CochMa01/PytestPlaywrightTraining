import pytest
import pandas as fileReader
from playwright.sync_api import expect
from batch1.src.pages.LoginPage import LoginPage


@pytest.fixture(scope="module")
def test_data(logger):
    sheet_name = "Login"
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


@pytest.mark.parametrize("test_name", ["test_login_with_standard_user"])
def test_login_with_standard_user(test_data, test_name, setup_teardown, logger) -> None:
    page = setup_teardown
    username = get_test_data(test_data, test_name, "Username")
    password = get_test_data(test_data, test_name, "Password")

    logger.info(f"---------- Running test: {test_name} ----------")

    credentials = {"username": username, "password": password}
    login_page = LoginPage(page, logger)
    products_page = login_page.do_login(credentials)
    expect(products_page.products_header).to_be_visible()
    expect(products_page.products_header).to_have_text("Products")

    logger.info(f"---------- Completed test: {test_name} ----------\n")


@pytest.mark.parametrize("test_name", ["test_login_with_invalid_user"])
def test_login_with_invalid_user(test_data, test_name, setup_teardown, logger) -> None:
    page = setup_teardown
    username = get_test_data(test_data, test_name, "Username")
    password = get_test_data(test_data, test_name, "Password")
    error_msg = get_test_data(test_data, test_name, "Error Message")

    logger.info(f"---------- Running test: {test_name} ----------")

    credentials = {"username": username, "password": password}
    login_page = LoginPage(page, logger)
    login_page.do_login(credentials)
    expect(login_page.error_msg_locator).to_contain_text(error_msg)

    logger.info(f"---------- Completed test: {test_name} ----------\n")


@pytest.mark.parametrize("test_name", ["test_login_with_no_credentials"])
def test_login_with_no_credentials(test_data, test_name, setup_teardown, logger) -> None:
    page = setup_teardown
    error_msg = get_test_data(test_data, test_name, "Error Message")

    logger.info(f"---------- Running test: {test_name} ----------")

    login_page = LoginPage(page, logger)
    login_page.click_login()
    expect(login_page.error_msg_locator).to_contain_text(error_msg)

    logger.info(f"---------- Completed test: {test_name} ----------\n")


@pytest.mark.parametrize("test_name", ["test_access_inventory_without_login"])
def test_access_inventory_without_login(test_data, test_name, setup_teardown_inventory, logger) -> None:
    page = setup_teardown_inventory
    error_msg = get_test_data(test_data, test_name, "Error Message")

    logger.info(f"---------- Running test: {test_name} ----------")

    login_page = LoginPage(page, logger)
    expect(login_page.error_msg_locator).to_contain_text(error_msg)

    logger.info(f"---------- Completed test: {test_name} ----------\n")


    # Run the scripts using the following command:
    # pytest --headed --slowmo 1000 --browser chromium -s -v
    # With reports:
    # pytest --headed --slowmo 1000 --browser chromium -s -v --html-report=batch1\src\utils\reports\report.html