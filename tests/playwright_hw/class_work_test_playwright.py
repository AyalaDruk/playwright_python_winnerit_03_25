from playwright.sync_api import Page, expect

BASE_URL = "https://devexpress.github.io/testcafe/example/"

def test_user_name(page: Page):
  page.goto(BASE_URL)
  page.locator("#developer-name").press_sequentially("Ayala",delay=200)
  page.get_by_test_id("linux-radio").check()
  #check all feature
  page.get_by_label("Support for testing on remote devices").check()
  page.get_by_test_id("reusing-js-code-checkbox").check()
  page.get_by_test_id("parallel-testing-checkbox").check()
  page.get_by_label("Easy embedding into a Continuous integration system").check()
  page.get_by_test_id("analysis-checkbox").check()
  #check all feature 2
  test_ids = [
   "remote-testing-checkbox",
    "reusing-js-code-checkbox",
    "parallel-testing-checkbox",
    "ci-checkbox",
    "analysis-checkbox"
  ]
  for test_id in test_ids:
    checkbox = page.get_by_test_id(test_id)
    checkbox.check()
    if checkbox.is_checked():
        print(f"️ {test_id} is checked ")
    else:
        print(f"️ {test_id} is NOT checked ")

# select
  page.get_by_test_id("preferred-interface-select").select_option("Both")

  #check
  page.get_by_label("I have tried TestCafe").check()
  #text
  page.locator("textarea[name=comments]").fill("the page very nice")
  #submit button
  page.get_by_role("button",name="submit").click()
  page.wait_for_timeout(300)

  #validtion tests
  #check actual url
  expect(page).to_have_url("https://devexpress.github.io/testcafe/example/thank-you.html")
  #check actual name
  user_name = "Ayala"
  expect(page.locator("#article-header")).to_have_text(f"Thank you, {user_name}!")
  #visible text
  expect(page.get_by_text("To learn more about TestCafe, please visit:")).to_be_visible()
  #check link
  link=page.get_by_role("link",name="devexpress.github.io/testcafe")
  expect(link).to_be_visible()
  #title
  expect(page).to_have_title("Thank you!")
