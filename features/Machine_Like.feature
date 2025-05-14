Feature:  Machinery Filter option

  Background:
    Given the company is logged in and on the menu for like a job

  Scenario: Verify filter option
    When the company is logged in and on the menu for like a job
    Then the company is liked a machine using the like icon
    Then the company is click on the add comment icon
    Then the company adds the text
    Then click on post comment button
    Then click on close button
    Then click on like machine list
    Then view the machine details
