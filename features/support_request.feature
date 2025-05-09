Feature: Support Request Submission

  Background:
    Given the company is logged in and on the dashboard

  Scenario: Verify Support Request Submission
    When the company clicks on the Support section
    And the company adds a subject and description
    And the company uploads a screenshot
    And the company clicks the Submit button
    Then the support request should be submitted successfully
