Feature:  Machinery Filter option

  Background:
    Given the company is logged in and on the menu for like a job

  Scenario: Verify filter option
    When the company is logged in and on the menu for like a job
    Then the company is liked a job using the like icon
    Then the company is click on the add comment icon
    Then the company add the text
    Then click on post comment button