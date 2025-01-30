from appium.webdriver.common.appiumby import AppiumBy
from behave import given, when, then
from hamcrest import assert_that

import logging

@given('user is on the main screen')
def user_is_on_main_screen(context):
  helloTextElement = context.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='spaceCatHelloText')
  assert_that(helloTextElement.is_displayed(), True)


@when('user authenticates successfully')
def user_authentication(context):
  context.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='usernameField').send_keys('admin')
  context.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='passwordField').send_keys('Admin123')
  context.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='goToExploreViewButton').click()


