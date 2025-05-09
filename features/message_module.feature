Feature: Message Module Functionality

  Scenario: Verify Contact List
    Given the company is logged in
    When the company navigates to the message section
    Then the company should see a list of all message contacts
    And each contact should display the name, profile picture, and latest message snippet

  Scenario: Verify Start Chat
    Given the company is on the message section
    When the company clicks on "Start Chat"
    And the company selects a contact to start chat
    And the company composes and sends the first message
    Then the message should be sent successfully
    And the chat should be initiated with the selected contact

  Scenario: Verify Pending Tab
    Given the company is on the message section
    When the company navigates to the Pending tab
    Then the company should see all pending messages
    And the messages should require a response or action

  Scenario: Verify Received Tab
    Given the company is on the message section
    When the company navigates to the Received tab
    Then the company should see all received messages
    And the messages should display the sender's name, profile picture, and message status

  Scenario: Mark Message as Read/Unread
    Given the company is viewing received messages
    When the company marks a message as read or unread
    Then the message status should be updated accordingly
