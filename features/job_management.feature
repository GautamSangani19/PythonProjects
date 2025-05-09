Feature: Job Creation and Job Management Process

  Background:
    Given the company is logged into the application

  Scenario: Display job summary on the home screen
    When the company navigates to the home screen
    Then the company should see a list of all posted jobs with the following details

  Scenario: View saved draft jobs
    When the company navigates to the "My Draft" section
    Then all saved draft jobs should be visible

  Scenario: View more details of a posted job
    When the company clicks on the "More Details" link of a job
    Then a detailed job description and all additional information should be displayed
