Feature: Company Settings Management

  Background:
    Given the company is logged in and on the settings page

  Scenario: Verify Privacy Settings for Phone Number Visibility
    When the company is logged in and on the settings page
    And  the company clicks on Privacy
    And the company selects Phone Number Visibility
    And the company toggles phone number visibility off
    Then phone number should be hidden from others

  Scenario: Verify Privacy Settings for Email Address Visibility
    When the company clicks on Privacy
    And the company selects Email Address Visibility
    And the company toggles email address visibility off
    Then close the current pop-up

#  Scenario: Verify Settings - Delete Account (Send OTP)
#    When the company clicks on Delete Account
#    And the company clicks on Send OTP
#    Then Enter your verification code

#  Scenario: Verify Settings - Delete Account (Select Own Number)
#    When the company clicks on Delete Account
#    And the company selects their own number
#    And clicks on Send OTP
#    Then OTP should be sent to the selected number
#
#  Scenario: Verify Settings - Change Mobile Number
#    When the company clicks on Change Mobile Number
#    And clicks on Send OTP
#    Then the company should receive an OTP for number change
#
#  Scenario: Verify Settings - Change Mobile Number (Add Another Mobile Number)
#    When the company enters a new mobile number
#    And clicks on Send OTP
#    Then OTP should be sent to the new mobile number
