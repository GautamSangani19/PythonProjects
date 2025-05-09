Feature: Company Delete Account

  Background:
    Given the company is logged in and on the settings page for delete account

  Scenario: Verify Privacy Settings for delete account
    When the company is logged in and on the settings page for delete account
    Then the company clicks on Delete Account
    Then the company clicks on Send OTP
    Then Enter your verification code

