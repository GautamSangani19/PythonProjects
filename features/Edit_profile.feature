Feature: Company Edit Profile

  Background:
    Given the company is on the edit profile setup page

  Scenario: Mandatory fields must be filled to complete edit profile
    When the company is on the Homepage for edit profile setup
    Then the company is on the edit profile section
    Then the company is on the edit profile icon
    Then Add th website
    Then Unselect the option in type of establishment
    Then select the another option in type of establishment
    Then click on save button for edit profile

