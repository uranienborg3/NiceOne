Feature: Menu navigation

         As a customer of the store
         I wish to be able to navigate the store with the menu
         in order to access products by categories

Scenario: Navigate to a category of products
   Given  I can see menu on the home page
    When  I hover over Women in menu
     And  I click T-shirts
    Then  I can see products of this category