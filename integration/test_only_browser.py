import pytest


@pytest.mark.only_browser("firefox")
def test_visit_youtube(page):
    page.goto("https://youtube.com")
