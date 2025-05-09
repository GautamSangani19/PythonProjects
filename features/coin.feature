Feature: Company coin history

  Background:
    Given the company is on the Home page

  Scenario: Mandatory fields must be filled to complete edit profile
    When the company is on the Homepage for coin history
    Then Click on Coin history button
    Then download history
    Then Select the calendar
    Then click on save button on calendar
    Then click on filter icon
    Then select the start date
    Then select the end date
    Then click on type selection
    Then select the amount
    Then click on apply button



