Feature: User

  Scenario: When writing a user to the sheet
    Given there are all required fields for a user
      Then it should return the user in a sheet friendly format

  Scenario: When returning a user to an application
    Given there are all required fields for a user
      Then it should return the user in an app friendly format
