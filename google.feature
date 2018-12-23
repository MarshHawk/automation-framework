Feature: Google
    Verify basic Google search functionality

Scenario: Simple Google Search homepage smoke test
    Given I go to Google
    When I reach the page
    Then the Google logo image will be displayed
    And the search box will be displayed
    And the Google Search button will be displayed
    Then I click the search button
    And nothing happens, I stay on the Google home page
    Then I type 'True Fit' in the search box
    And the displayed search box text matches what I typed
    Then I click the search button
    And I arrive at the search results page
    