from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

from behave import fixture, use_fixture
from log import *
import yaml

APPIUM_PORT = 4724
APPIUM_HOST = '127.0.0.1'

@fixture
def start_driver(context):
  appium_service(context)

  platform = context.config.userdata.get("PLATFORM", "unknown").lower()

  with open(f"features/setup/devices/{platform}/capabilities.yml", "r") as file:
    capabilities = yaml.safe_load(file)

  if platform == 'android':
    log_info('Running on ANDROID')
    context.is_android = True

    options = UiAutomator2Options()
    for key, value in capabilities.items():
      options.set_capability(key, value)

  else:
    log_info('Running on IOS')
    context.is_ios = True

    options = XCUITestOptions()
    for key, value in capabilities.items():
      options.set_capability(key, value)

  log_info(f"Initializing driver with options: {options.to_capabilities()}")

  context.driver = webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}', options=options)
  yield context.driver
  context.driver.quit()

def appium_service(context):
  context.appium_server = AppiumService()
  context.appium_server.start(
    args=[
        '--address', APPIUM_HOST,
        '-p', str(APPIUM_PORT),
        '--use-plugins', 'images,appium-reporter-plugin',
        '--log-timestamp'
    ],
    timeout_ms=20000,
    stdout=open('appium.log', 'w'),
    stderr=open('appium.log', 'a')
  )

def before_all(context):
  use_fixture(start_driver, context)
