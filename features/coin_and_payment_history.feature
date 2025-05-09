Feature: Coin History and Payment History Management

  Background:
    Given the company is logged into the platform for coin

  # ----------------- Coin History -----------------

  Scenario: Verify Coin History Detail Page
    When the company navigates to the Coin History page
    Then the Coin History page should display fields for Spending, Earning, Purchase, Bonus, and Coupon Code

  Scenario: Verify Coin History Filters
    When the company applies a date range filter on the Coin History page
    Then the filtered coin transactions should be displayed

    When the company filters by transaction type "Purchase"
    Then only purchase transactions should be displayed

    When the company searches for a transaction by keyword
    Then the matching transaction should be displayed

  # ----------------- Payment History -----------------

  Scenario: Verify Payment History Details
    When the company navigates to the Payment History page
    Then the Payment History page should display Transaction ID, Amount, Date, Payment Method, Status, and Invoice Number

  Scenario: Verify Download of Payment History
    When the company clicks the "Download" button on Payment History page
    Then the payment history file should be downloaded with all transaction details
