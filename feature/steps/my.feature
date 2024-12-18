Feature: Pikaboo Testing

Background: Open Website With Valid url
    Given Open Browser and Visit Website

@cartproduct
Scenario: Verify that Product cart is successful
    When Click on Mobile Number/Email Section
    Then Input Mobile Number
    When Click on Password Section
    Then Input Password
    When Click on Log In button
    When Click on Smartphone option
    Then Click on Camera Phone option
    When Click on First phone option
    Then Click on Color Phone option
    When Click on Add To Cart option
    Then Check that Product cart is successfull

@shoppingproduct
Scenario: Verify that Shopping product is proceed successful
    When Click on Mobile Number/Email Section
    Then Input Mobile Number
    When Click on Password Section
    Then Input Password
    When Click on Log In button
    When Click on Shopping option
    Then Click on Proceed to Checkout option
    When Click on Continue option
