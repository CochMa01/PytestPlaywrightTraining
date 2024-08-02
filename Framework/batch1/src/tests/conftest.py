import logging
import os
import pytest
from playwright.sync_api import Page


@pytest.fixture(scope="session")
def logger():
    log_file = "batch1/src/utils/logs/test_log.log"
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    loggerName = "test_logger"

    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    handler = logging.FileHandler(log_file, mode='a')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name=loggerName)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger

@pytest.fixture()
def setup_teardown(page: Page):
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("https://www.saucedemo.com/")
    yield page


@pytest.fixture()
def setup_teardown_inventory(page: Page):
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("https://www.saucedemo.com/inventory.html")
    yield page
