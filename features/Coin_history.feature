Feature: Buy Coins Process

  Scenario: User buys coins using a card
    Given the company is on the coin history page
    When Click on Buy coins button
    Then select the coin amount
    And click on add coin button
    And click on proceed to buy coins
    And select the card option
    And Add the card details
    And click on secure_card_button
    And click on skip button
    And Enter OTP
    And submit OTP
    And the company click on the menu
    And Click on Coin history button for history list