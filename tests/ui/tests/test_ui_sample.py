def test_homepage_title(page):
    page.goto("https://the-internet.herokuapp.com/")
    assert page.title() == "Welcome to the-internet"


def test_navigation_to_about(page):
    page.goto("https://the-internet.herokuapp.com/")
    page.click("text=A/B Testing")
    assert "A/B Test Variation 1" in page.url


def test_visible_elements(page):
    page.goto("https://the-internet.herokuapp.com/")
    assert page.is_visible("h1")
    assert page.is_visible("p")


def test_external_link_opens_new_tab(page, context):
    page.goto("https://the-internet.herokuapp.com/")
    with context.expect_page() as new_page_info:
        page.click("a[target='_blank']")
    new_page = new_page_info.value
    assert new_page.url.startswith("https://")
