Feature: Logout functionality

  As a company user
  I want to be able to log out of the platform
  So that I can securely exit my account

  Scenario: Successfully logging out of the platform
    Given the company is logged into the platform for test
    When the company clicks on the Logout button
    Then the company should be logged out of the platform
    And the login screen should be displayed
