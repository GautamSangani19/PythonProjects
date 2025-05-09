Feature: Resume Viewing and Coin Management

  Background:
    Given the company is logged into the platform

  # Resume Viewing Process
  Scenario: Viewing a resume and coin deduction
    When the company clicks on a user profile and selects the resume option
    Then a pop-up should display the resume and deduct Ponis from the coin balance

  Scenario: Display available coins before viewing resume
    When the company clicks to view a resume
    Then a pop-up should display current coins with proceed and cancel options

  Scenario: Click Yes and deduct coins
    When the company clicks "Yes" on the coin confirmation pop-up
    Then the resume should be displayed and Ponis deducted

  Scenario: Click Cancel without deducting coins
    When the company clicks "Cancel" on the coin confirmation pop-up
    Then the pop-up should close without any coin deduction

  Scenario: Insufficient coins to view resume
    When the company clicks "Yes" but has insufficient coins
    Then an "Out of coins" message should appear
    And the company should be redirected to the coin purchase page upon confirmation

  # Buy Coin Process
  Scenario: Purchasing coins with available plans
    When the company selects a coin plan
    Then the company should be able to proceed and purchase coins

  Scenario: Purchase coins with custom amount
    When the company selects a custom coin amount
    Then the custom coin purchase should be processed successfully

  Scenario: Verify current coin balance after purchase
    Then the updated coin balance should be displayed on the dashboard

  # Offers and Coupons
  Scenario: Viewing available offers and coupons
    When the company views available offers
    Then offer details should be displayed

  Scenario: Applying expired coupon code
    When the company tries to apply an expired coupon
    Then an error message should be shown for expired coupon code

  Scenario: Applying manual coupon code
    When the company enters a manual coupon code
    Then the discount should be applied if valid

  Scenario: Admin setting coin deduction for coupon
    Given the admin sets coin or point values for a coupon
    Then the updated values should apply during transactions

  Scenario: Navigate back from offer page
    When the company clicks the back button on the offer page
    Then the company should return to the previous page without changes

  Scenario: Display purchase summary
    Then the system should show the total amount, coins purchased, and discounts

  Scenario: Adding optional GST number
    When the company adds a GST number
    Then it should be saved optionally

  Scenario: Proceed to pay
    When the company confirms purchase details
    Then the company should proceed to the payment gateway

  Scenario: Complete payment via Razorpay
    When the company pays via Razorpay
    Then the coin purchase should be confirmed

  # Coupon Code Validation
  Scenario: Validating coupon codes
    When the company enters a coupon code
    Then the system should validate and apply the discount

  Scenario: Prevent duplicate coupon usage
    Then the same coupon code should not be used more than once

  Scenario: Handling invalid coupon code
    When an invalid coupon code is entered
    Then an error message should be displayed

  Scenario: Handling expired coupon code
    When an expired coupon code is entered
    Then an error message should be shown

  Scenario: Using multiple coupons
    Then the platform should apply multiple coupons appropriately

  # Notifications
  Scenario: Notification after successful purchase
    Then the company should receive a confirmation message and updated coin balance
