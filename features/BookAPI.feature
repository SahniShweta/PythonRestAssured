# Created by dell at 23-02-2021
Feature: Verify if books are added and deleted using Library API
  # Enter feature description here

  @library
  Scenario: Verify AddBook API functionality
    Given The book details that are needed to be added to the Library
    When we execute the AddBook POSTAPI method
    Then book is successfully added
    And status code of response should be 200


  @library
  Scenario Outline: Verify AddBook API functionality
    Given The book details with <isbn> and <aisle> added to the Library
    When we execute the AddBook POSTAPI method
    Then book is successfully added
    Examples:
      |isbn  |aisle|
      |sahni4|279  |
      |sahni5|263  |