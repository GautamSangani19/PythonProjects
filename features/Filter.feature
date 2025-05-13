Feature:  Machinery Filter option

  Background:
    Given the company is logged in for filter option

  Scenario: Verify filter option
    When click on machine tab list
    #Then Machine details screen for filter
    Then CLick on filter icon for machinery filter
    Then Add the brand name for filter option
    Then select type for filter option
    Then select condition for filter option
    Then select model for filter option
    Then Add the location for filter option
    Then click on apply filter button
    Then Filter applied successfully
    Then Reset filter
    Then Reset filter successfully


