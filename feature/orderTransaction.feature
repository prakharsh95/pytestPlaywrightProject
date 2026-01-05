Feature: Order Transaction
  As a user
  I want to create and view orders

  Scenario Outline: View order details after creating an order
    Given I create an order via API with "<userName>" and "<password>"
    When I login to the application with "<userName>" and "<password>"
    And I navigate to the orders page
    And I view the order with order ID
    Then I should see the order details matching the order ID
    And I delete the order via API
    And I logout from the application

    Examples:
      | userName                | password      |
      | prakhar.sh95@gmail.com | Password@123 |

