Feature: Refer and Earn section

  Background:
    Given the company is logged in and on the menu for refer and earn

  Scenario: Verify refer and earn section
    When the company is logged in and on the menu for refer and earn
    Then the company is logged in and select the refer and earn option
    Then Click on the copy icon for copied the refer and earn code
#    Then Click on the share icon for copied the refer and earn code
    Then Close the current section
    Then Logout from the app
