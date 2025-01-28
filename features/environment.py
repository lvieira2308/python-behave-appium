from appium import webdriver
from behave import fixture, use_fixture
from log import *
import yaml

@fixture
def start_driver(context):
  ## APPIUM IMPLEMENTATION HERE
  platform = context.config.userdata.get("PLATFORM", "unknown").lower()

  with open(f"features/setup/devices/{platform}/common_capabilities.yml", "r") as file:
    capabilities = yaml.safe_load(file)

  if platform == 'android':
    context.is_android = True
    log_info('Running on ANDROID')

    ## context.driver = ...

  else:
    context.is_ios = True
    log_info('Running on IOS')

    ## context.driver = ...

  # yield context.driver
  # context.driver.quit()

def before_all(context):
  use_fixture(start_driver, context)
