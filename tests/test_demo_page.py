from playwright.sync_api import Page,expect



BASE_URL="https://devexpress.github.io/testcafe/example/"

def test_demo_page_loaded(page:Page):
 page.goto(BASE_URL)
 # assert page.url == BASE_URL+"/home-page"
 expect(page).to_have_url(BASE_URL, timeout=7500)


def test_demo_page_title(page: Page):
    page.goto(BASE_URL)
    expect(page).to_have_title("TestCafe Example Page")


def test_user_name_presented(page: Page):
    pass