from behave import then

@then('I see C')
def see_C(context):
  print("I see C!")
  pass
