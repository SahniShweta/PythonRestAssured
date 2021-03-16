# Created by dell at 25-02-2021
Feature: Github API Validation
  # Enter feature description here

  Scenario: Session Management check
    Given I have github auth credentials
    When I hit gitRepo API of github
    Then status code of response should be 200