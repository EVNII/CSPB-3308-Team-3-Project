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

### Order History Table
*A SQL table containing all orders placed by customers.*

* example layout: *
| Order ID        | Customer ID | Order Date               | Product ID  | Product Name                        |
| :-------------: | :---------: | :---------------------:  | :---------: | :---------------------------------: |
| 00001           | A10001      | June 1, 2023 09:00AM MST | SC-1234     | "Oliloqui Valley" by Herbie Hancock |
| 00002           | A10002      | June 1, 2023 09:00AM MST | SC-2345     | "Coral" by Keith Jarrett            |
| 00003           | A10003      | June 1, 2023 09:00AM MST | SC-3456     | "Blue in Green" by Miles Davis      |
| 00004           | A10004      | June 1, 2023 09:00AM MST | SC-4567     | "Time Remembered" by Bill Evans     |

| Field Name       | Description                                                                          |
| :--------------: | :-------------------------------------------------------------:                      |
| Order ID         | A unique alphanumeric identifier for each order placed.                              | 
| Customer ID      | A unique alphanumeric identifier for each customer.                                  | 
| Order Date       | The date and time when the order was placed.                                         | 
| Product ID       | A unique alphanumeric identifier for each product in the company's product database. |
| Product Name     | The musical score name and artist name.                                              |
| Unit Price       | The price to download the PDF of the specific score.                                 |
| Total Price      | The combined price of all score's purchased within the order.                        |
| Payment Method   | Visa, MasterCard, AMEX, PayPal, ApplePay, etc.                                       |
| Billing Address  | The billing address connected to the provided Payment Method.                        |
| Customer E-mail  | The customer's email address tied to the specific order.                             |
| Order Notes      | Any additional notes or comments related to the order.                               |
