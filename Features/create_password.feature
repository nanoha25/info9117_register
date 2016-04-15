# Created by hakur at 15/04/2016
Feature: Create User Password
  As the System Owner
  I want user to create a decent password
  So that only that user can log into system

  Scenario: User Enter a Decent Password
    Given at the "Create Password" textbox
    When user enter a decent password
    Then the registration system should accept this password and set as user login password
    Examples: takamachi25, name!@456

   Scenario: User Enter Nothing
     Given at the "Create Password" textbox
     When user does not enter anything
     Then the registration system should show an error message to tell user a password is required
     Examples: "You must enter a password"

   Scenario: User Enter a Password With Only Numbers
     Given at the "Create Password" textbox
     When user enters a password with only numbers
     Then the registration system should show an error message to tell user password is too weak
     Examples: 123456, 445678123