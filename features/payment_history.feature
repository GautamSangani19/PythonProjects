Feature: Company payment history

  Background:
    Given the company is on the Home page for Payment History

  Scenario: Mandatory fields must be filled to complete edit profile
    When the company is on the Homepage for Payment history
    Then Click on Payment history button
    Then Download the payment history
    Then Select the calendar for the payment history
    Then click on save button on calendar for the payment history
