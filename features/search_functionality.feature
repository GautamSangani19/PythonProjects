Feature: Search Functionality

  Background:
    Given the company is logged in and on the homepage

  Scenario: Verify Search with Empty Input
    When the company clicks on the search bar
    And the company leaves the input empty and triggers the search
    Then the platform should prompt to enter a valid search term

  Scenario: Verify Search Suggestions/Autocomplete
    When the company clicks on the search bar
    And the company starts typing a search term
    Then relevant autocomplete suggestions should appear

  Scenario: Verify Clear Search Functionality
    When the company enters a search term in the search bar
    And the company clicks on the Clear icon
    Then the search bar should be cleared
