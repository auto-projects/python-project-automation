def test_homepage_title(page):
    page.goto("https://example.com")
    assert page.title() == "Example Domain"


def test_navigation_to_about(page):
    page.goto("https://example.com")
    page.click("text=More information")
    assert "iana.org" in page.url


def test_visible_elements(page):
    page.goto("https://example.com")
    assert page.is_visible("h1")
    assert page.is_visible("p")


def test_form_submission(page):
    page.goto("https://example.com/contact")
    page.fill("input[name='name']", "Test User")
    page.fill("input[name='email']", "test@example.com")
    page.click("button[type='submit']")
    assert page.locator(".success-message").is_visible()


def test_external_link_opens_new_tab(page, context):
    page.goto("https://example.com")
    with context.expect_page() as new_page_info:
        page.click("a[target='_blank']")
    new_page = new_page_info.value
    assert new_page.url.startswith("https://")
