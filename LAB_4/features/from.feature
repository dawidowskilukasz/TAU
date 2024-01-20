Feature: Fill out the form

  Scenario: Fill out the form with valid information
    Given User is on the demoqa.com automation practice form page
    When User enters first name as "John"
    And User enters last name as "Smith"
    And User enters email as "john.smith@domain.com"
    And User selects gender
    And User enters phone number as "1234567891"
    And User selects birthdate
    And User enters subject as "Com"
    And User selects hobbies
    And User enters address as "somewhere 15/58"
    Then Test is completed successfully