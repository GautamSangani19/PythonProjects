Feature: Company support section

  Background:
    Given the company is logged in and on the settings page for support

  Scenario: Verify Privacy Settings for support
    When the company is logged in and on the settings page for support
    Then the company add subject for support form
    Then the company add the description for the support form
    Then the company add the image
    Then submit the support form

