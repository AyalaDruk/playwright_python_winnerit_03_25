from playwright.sync_api import Page, expect

BASE_URL = "https://www.qa-practice.com/elements/select/mult_select"

def test_select_option(page: Page):
  page.goto(BASE_URL)
  #select
  page.get_by_label("Choose the place you want to go").select_option("Ocean")
  #select2
  page.get_by_label("Choose how you want to get there").select_option("Car")
  #select3
  page.get_by_label("Choose when you want to go").select_option("Next week")
  #submit button
  page.get_by_role("button",name="Submit").click()
  result_test=page.locator("#result")
  expect(result_test).to_have_text("You selected to go by car to the ocean next week")