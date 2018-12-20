Feature: Google
    Verify basic Google search functionality

Scenario: Searching Google
    Given I navigate to Google
    When I reach the page
    Then the Google logo image will be present and clickable
    And the search input box will be present and clickable
    And the 'Google Search' button will be present and clickable
    Then I click the search button
    And nothing happens, I stay on the Google home page
    Then I type 'True Fit' in the search box
    And the the search box diplay text matches 'True Fit'
    Then I click the search button
    And I go to the search results page
    