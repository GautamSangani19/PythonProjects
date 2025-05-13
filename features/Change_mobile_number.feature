Feature: Company Settings Management

  Background:
    Given the company is logged in and on the settings page for change mobile number

  Scenario: Verify Privacy Settings for Phone Number Visibility
    When the company is logged in and on the settings page for change mobile number
    Then Click on change details button
    Then Click on send OTP button
    Then add otp
    Then Click on send OTP button
    Then click on the next button
    Then Enter Your New Mobile Number
    Then Click on submit button


