Feature: My tests

Scenario: First test
  Given user is on the main screen
  When user authenticates successfully
  Then user should be redirected to the explore cosmos screen
