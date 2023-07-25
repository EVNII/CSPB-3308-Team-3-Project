# SQL Design
## MusicVerse by The Lightning Bolts
### CSPB 3308 Group 3

#### Requirements for Milestone 5
#### Create 3 tables that include:
+ Table Name
+ Table Description
+ For each field of the table, provide name and short description.
+ List of tests for verifying each table

#### You must also provide the following for each data access method (at least one access method for each table or query required to get the data to display):
+ Name
+ Description
+ Parameters
+ return values
+ List of tests for verifyiing each access method

### Customer Orders Table
*A SQL table containing all orders placed by customers.*

*example layout:*
| Order ID        | Customer ID | Order Date               | Product ID  | Product Name                        |
| :-------------: | :---------: | :---------------------:  | :---------: | :---------------------------------: |
| 00001           | A10001      | June 1, 2023 09:00AM MST | SC-1234     | "Oliloqui Valley" by Herbie Hancock |
| 00002           | A10002      | June 1, 2023 09:00AM MST | SC-2345     | "Coral" by Keith Jarrett            |
| 00003           | A10003      | June 1, 2023 09:00AM MST | SC-3456     | "Blue in Green" by Miles Davis      |
| 00004           | A10004      | June 1, 2023 09:00AM MST | SC-4567     | "Time Remembered" by Bill Evans     |

| Field Name       | Description (data type)                                                                         |
| :--------------: | :-------------------------------------------------------------:                                 |
| Order ID         | A unique alphanumeric identifier for each order placed. (int)                                   | 
| Customer ID      | A unique alphanumeric identifier for each customer.  (varchar)                                  | 
| Order Date       | The date and time when the order was placed.         (timestamp)                                | 
| Product ID       | A unique alphanumeric identifier for each product in the company's product database. (varchar)  |
| Product Name     | The musical score name and artist name.    (text)                                               |
| Unit Price       | The price to download the PDF of the specific score. (float)                                    |
| Total Price      | The combined price of all score's purchased within the order. (float)                           |
| Payment Method   | Visa, MasterCard, AMEX, PayPal, ApplePay, etc.  (enum)                                          |
| Billing Address  | The billing address connected to the provided Payment Method. (text)                            |
| Customer E-mail  | The customer's email address tied to the specific order.   (text)                               |
| Order Notes      | Any additional notes or comments related to the order.    (text)                                |

*To display the customer orders table, you can use the following:*

**SELECT** * **FROM** customer_orders;

*To display a specific customers orders, you can use the following:*

**SELECT** * **FROM** customer_orders WHERE customer_id = XXX;

**TEST CASE: Verify Retrieval of all orders from a specific customer**
*intended use for a customer to see their past order history*

**Use case name:** Verify order history
**Description:** Show all past orders from a specific customer
**Pre-condition:** user has a valid account and has purchased at least 1 score
**Test steps:**
+ Navigate to account page
+ Select 'Order History'
**Expected result:** User should be able to see all past orders
**Actual result:** User is viewing only their orders
**Status:** Pass/Fail
