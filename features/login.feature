Feature: Company Login Options - Mobile Number and Google Authentication

  Background:
    Given the company is on the login page

  # -------- Login Option 1: Mobile Number Login --------

  Scenario: Successful login with valid mobile number and OTP
    When the company enters a valid 10-digit mobile number
    And the company clicks on the 'Send OTP' button
    Then a 6-digit OTP should be sent to the registered mobile number
    When the company enters the correct OTP within 30 seconds
    And the company clicks on the 'Verify OTP' button
    Then the company should be redirected to the 'Add Profile Details' screen
#
#  Scenario: Resend OTP if not received or expired (Mobile Login)
#    When the company enters a valid 10-digit mobile number
#    And the company clicks on the 'Send OTP' button
#    And the OTP is not received within 30 seconds
#    When the company clicks on the 'Resend OTP' button
#    Then a new OTP should be sent to the registered mobile number
#
#  Scenario: Login fails with incorrect OTP (Mobile Login)
#    When the company enters a valid 10-digit mobile number
#    And the company clicks on the 'Send OTP' button
#    And the company enters an incorrect OTP
#    And the company clicks on the 'Verify OTP' button
#    Then an error message 'Invalid OTP. Please try again.' should be displayed
#
#  # -------- Login Option 2: Google Signup/Login --------
#
#  Scenario: Successful login via Google and verified mobile number
#    When the company selects the 'Continue with Google' option
#    And the company completes Google authentication successfully
#    Then the company should be prompted to enter a mobile number
#
#    When the company enters a valid 10-digit mobile number
#    And the company clicks on the 'Send OTP' button
#    Then a 6-digit OTP should be sent to the registered mobile number
#
#    When the company enters the correct OTP within 30 seconds
#    And the company clicks on the 'Verify OTP' button
#    Then the company should be redirected to the 'Add Profile Details' screen
#
#  Scenario: Login fails due to incorrect OTP after Google authentication
#    When the company selects the 'Continue with Google' option
#    And the company completes Google authentication successfully
#    Then the company should be prompted to enter a mobile number
#
#    When the company enters a valid 10-digit mobile number
#    And the company clicks on the 'Send OTP' button
#    And the company enters an incorrect OTP
#    And the company clicks on the 'Verify OTP' button
#    Then an error message 'Invalid OTP. Please try again.' should be displayed
#
#  Scenario: Resend OTP after Google login if OTP is not received
#    When the company selects the 'Continue with Google' option
#    And the company completes Google authentication successfully
#    Then the company should be prompted to enter a mobile number
#
#    When the company enters a valid 10-digit mobile number
#    And the company clicks on the 'Send OTP' button
#    And the OTP is not received within 30 seconds
#    When the company clicks on the 'Resend OTP' button
#    Then a new OTP should be sent to the registered mobile number
