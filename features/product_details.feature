Feature: Product details page

         As a customer of the store
         I wish to be able to see product details
         in order to facilitate decision making while browsing the store

Scenario: Check out the product details
   Given  I found a certain product
    When  I hover over the product block
     And  I click the More button
    Then  I can see product details page