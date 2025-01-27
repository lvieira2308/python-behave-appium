from behave import given
import logging

@given('I do A')
def do_a(context):
  logging.info("Step A")
  pass
