Feature: Company edit job

  Background:
    Given the company is logged in for edit job detail

  Scenario: Verify Privacy Settings for support
    When click on the more details button
    Then click on edit icon
    Then the company edit the Job Description
    Then the company edit the Job Availability Duration
    Then the company edit the details successfully
    Then the Job successfully edited


