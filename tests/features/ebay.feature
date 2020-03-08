Feature: Ebay

  Scenario Outline: Search the products
    Given  I load the ebay website
    When I enter the "<value>" on search window
    When I select the "<categories>"
    Then I click the search button
    Then I expect search results display "<value>"
    Then I collect the item_name and item_price
    Examples:
      | value             | categories                    |
      | head first python | Books, Comics & Magazines     |
      | iphone 7          | Mobile Phones & Communication |
      | toyota yaris      | Cars, Motorcycles & Vehicles  |




