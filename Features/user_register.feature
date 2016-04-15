# Created by shirasaki at 8/04/2016
Feature: User Registration
  As the System Owner
  I want users to be able to create new account
  so that new user can set up their own profile
  and personalise it when needed. 

  Scenario Outline: New User Registration
    Given at the main page
    When user click "register" link
    Then the system should display a form which users will fill basic info to create a new account.
    Examples:
  
  Scenario Outline: Submit Form
    Given at the registration page
    When user click "Submit" link
    Then the system should display "Submission Successful".
    Examples: username: test; password: test12345; email: example@contoso.com;
    
  Scenario Outline: Username Contains Special Characters
    Given at the username field
    When username contains special characters
    Then the system should display "Invalid Username" error message
    Examples: u$ern@me, !@#$user
  
  Scenario Outline: Password Contains Only Numbers
    Given at the password field
    When user enter a password with only numbers
    Then the system should display "Password too simple" error message
    Examples: 123456, 456789546
  
