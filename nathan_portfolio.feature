Feature: Github icon

Scenario: Clicking on the GitHub icon should take the sure to the correct GitHub profile
    Given the user is on the about section
    When the user clicks on the GitHub icon
    Then the user should be taken to "https://github.com/nathanfleet"