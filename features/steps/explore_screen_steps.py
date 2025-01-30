from appium.webdriver.common.appiumby import AppiumBy
from behave import given, when, then
from hamcrest import assert_that

@then('user should be redirected to the explore cosmos screen')
def user_is_on_explore_screen(context):
  cosmoCatsImage = context.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='cosmoCatsImage')
  assert_that(cosmoCatsImage.is_displayed(), True)


