import pytest
import pandas as fileReader
from playwright.sync_api import expect
from batch1.src.pages.LoginPage import LoginPage

@pytest.fixture(scope="module")
def test_data(logger):
    sheet_name = "Products"
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

@pytest.mark.parametrize("test_name", ["test_add_to_cart_product"])
def test_add_to_cart_product(test_data, test_name, setup_teardown, logger) -> None:
    page = setup_teardown
    username = get_test_data(test_data, test_name, "Username")
    password = get_test_data(test_data, test_name, "Password")
    product = get_test_data(test_data, test_name, "Product Name")

    logger.info(f"---------- Running test: {test_name} ----------")

    credentials = {"username": username, "password": password}
    login_page = LoginPage(page, logger)
    products_page = login_page.do_login(credentials)

    products_page.click_add_to_or_remove_from_cart(product)
    expect(products_page.get_add_to_or_remove_from_cart_locator(product)).to_have_text("Remove")

    logger.info(f"---------- Completed test: {test_name} ----------\n")


@pytest.mark.parametrize("test_name", ["test_remove_product_from_cart"])
def test_remove_product_from_cart(test_data, test_name, setup_teardown, logger) -> None:
    page = setup_teardown
    username = get_test_data(test_data, test_name, "Username")
    password = get_test_data(test_data, test_name, "Password")
    product = get_test_data(test_data, test_name, "Product Name")

    logger.info(f"---------- Running test: {test_name} ----------")

    credentials = {"username": username, "password": password}
    login_page = LoginPage(page, logger)
    products_page = login_page.do_login(credentials)

    products_page.click_add_to_or_remove_from_cart(product)
    products_page.click_add_to_or_remove_from_cart(product)
    expect(products_page.get_add_to_or_remove_from_cart_locator(product)).to_have_text("Add to cart")

    logger.info(f"---------- Completed test: {test_name} ----------\n")
