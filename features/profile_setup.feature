Feature: Company Profile Setup

  Background:
    Given the company is on the profile setup page

  Scenario: Mandatory fields must be filled to complete profile
    When the company fills in all mandatory fields
    Then the company fills the username
    Then the company add the establishedSince

    Then the company add the address
    Then the company adds the city
    Then the company add the email address


    Then the company add the Type of Establishment
    Then the company add Size Of Your Establishment
    Then the company select Currently Hiring For

    Then the company add the description
    Then click on save button

  #Scenario: Successful profile setup completion
    Given the company has filled in all required fields
    When the company submits the profile
    Then the company's account should be marked as successfully created


