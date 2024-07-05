from typing import Dict

import pytest
from playwright.sync_api import BrowserType


# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args):
#     return {
#         **browser_context_args,
#         "viewport": {
#             "width": 1280,
#             "height": 720
#         }
#     }

# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args, playwright):
#     iphone_11 = playwright.devices['iPhone 11 Pro']
#     return {
#         **browser_context_args,
#         **iphone_11
#     }

@pytest.fixture(scope="session")
def context(
        browser_type: BrowserType,
        browser_type_launch_args: Dict,
        browser_context_args: Dict
        ):
    context = browser_type.launch_persistent_context(
        "./foobar",
        **{
            **browser_type_launch_args,
            **browser_context_args,
            # "locale": "en-US"
            "locale": "de-DE"
        })
    yield context
    context.close()




