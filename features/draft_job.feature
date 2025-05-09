Feature: Company Edit Profile

  Background:
    Given the company is on the draft page


  Scenario: Mandatory fields must be filled to complete draft job
    When the user is in the home screen for draft a job
    Then the user is on the Post a Job page for draft
    Then the user add the job title
    Then the company selects the type of job
    Then click on back button
    Then click on save as draft button
    Then the company is on the Homepage for draft job
    Then the company is on the draft job section
    Then the company clicks on the edit draft job
