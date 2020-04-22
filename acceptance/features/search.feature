Feature: Search for an item

         As a customer of the store
         I wish to be able to search for a product by name
         in order to make my shopping faster and easier

Scenario Outline: Search for an item
           Given  I am on the home page
            When  I enter <term> into search field
             and  I click search button
            Then  I can see <number> search results

Examples: By category
            |term           |number |
            |t_shirt        |1      |
            |dress          |7      |
            |summer dress   |4      |