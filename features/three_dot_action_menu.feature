Feature: Three-Dot Action Menu for Applicant Management

  Background:
    Given the company is viewing an applicant's profile with the three-dot action menu

  Scenario: Visit the applicant's detailed profile
    When the company clicks on "Visit Profile"
    Then the detailed applicant profile should be displayed

  Scenario: Block an applicant
    When the company clicks on "Block User"
    Then the applicant should be blocked from future interactions or applications

  Scenario: Report inappropriate content
    When the company clicks on "Report Content"
    Then the content should be reported successfully

  Scenario: Share applicant profile
    When the company clicks on "Share"
    Then a shareable link should be generated for sharing the profile or job post
