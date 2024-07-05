import pytest


@pytest.mark.skip_browser("firefox")
def test_visit_youtube(page):
    page.goto("https://youtube.com")
