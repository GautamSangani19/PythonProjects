Feature: Post a Job

  Scenario: The company posts a new job
    Given the company is on the login page for add job
    When the user is on the Post a Job page
    Then the user fills out the job form with valid data
    Then the company selects the Looking For option
    And the company selects the job duration option
    And the company adds the minimum salary
    And the company adds the maximum salary
    And the company selects the skills
    And the company selects the experience
    And the company adds the location
    And the company adds the Supplemental Pay
    And the company adds the Benefits
    And the company adds the Job Description
    And the company selects the Job Availability Duration
    And the company selects the open position
#    And the company adds the email
    And the company selects send an individual email when someone applies
    Then select Send WhatsApp updates
    And clicks on Save
    Then the job preview screen should appear with all filled details
    And the Job post successfully
