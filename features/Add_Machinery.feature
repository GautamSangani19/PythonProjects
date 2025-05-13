Feature: Add Machinery section

  Background:
    Given the company is logged in and on the menu for add machinery

  Scenario: Verify Privacy Settings for support
    When the company is logged in and on the menu for add machinery
    Then Add the machine image
    Then Add the machinery name
    Then Add the machinery type
    Then Add the brand name
    Then Add the model name
    Then Enter year of manufracture
    Then Select the condition
    Then Add the price
    Then Add the location
    Then Add the description
    Then Add the contact number
    Then save the details
    Then Machine details added successfully
    Then All added machine list
    Then Machine details screen






