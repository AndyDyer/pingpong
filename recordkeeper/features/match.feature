Feature: Matches

  Scenario: When getting a Match
    Given there are no winners determined
      Then it should determine a winner
  
   Scenario: When getting a Match
    Given there is a winner on file
      Then it should not determine anything

  Scenario: When writing a match to the sheet
    Given there are all required fields for a match
      Then it should return the match in a sheet friendly format

  Scenario: When returning a match to an application
    Given there are all required fields for a match
      Then it should return the match in an app friendly format
