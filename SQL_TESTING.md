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

*partial example layout:*  
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
```sqlite3
SELECT * FROM customer_orders;
```
*To display a specific customers orders, you can use the following:*
```sqlite3
SELECT * FROM customer_orders WHERE customer_id = XXX;
```
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

### Scores Table
*A SQL table containing all scores, their specific information, and price*

*partial example layout:*  
| Score_ID | Track Title | Author             | Instrument    | Genre         | Downloads | Price |
| :------: | :---------: | :----------------- | :-----------: | :-----------:| :-------:| :----:|
| 00001    | Yesterday   | The Beatles        | Bass Guitar   | Classic Rock | 1200000   | 4.99  |
| 00002    | Piano Man   | Billy Joel         | Piano         | Classic Rock | 567000    | 2.99  |
| 00003    | Hallelujah  | Leonard Cohen     | String Guitar | Folk Rock    | 546777    | 0.00  |
| 00004    | Fur Elise   | Ludwig van Beethoven | Violin      | Classical    | 4555542   | 0.00 |


| Field Name       | Description (data type)                                                                        |
| :--------------: | :-------------------------------------------------------------:                                 |
| Score_ID         | A unique alphanumeric identifier for each score. (int) (Primary Key)                            | 
| Track Title      | The title of the musical track. (varchar)                                  | 
| Author           | The author or composer of the musical score. (varchar)                                | 
| Instrument       | The instrument associated with the musical score. (varchar)                                  |
| Genre            | The genre of the musical score. (text)                                               |
| Downloads        | The number of times the score has been downloaded. (int)                                    |
| Price            | The price of the score for purchase. (float)                           | 

**To Test Table Verification:**

*To display the scores table, you can use the following:*
```sqlite3
SELECT * FROM scores;
```
*To display a specific score, you can use the following:*
```sqlite3
SELECT * FROM scores WHERE Score_ID = XXX;
```
**Data Access Methods:**    
Name: Search feature   
Description: It needs to return the score information depending on certain criteria      
Parameters: Either an artist, title, or genre   
return values: The score information    

Name: Popular tracks    
Description: It needs to return the popular tracks for the menu        
Parameters: The total dowloads for each track    
return values: The score information    


**TEST CASES:**  

**Use case name:** Search Feature   
**Description:** Show all relevant scores based on a search   
**Pre-condition:** user has hit enter on the search box to find a score   
**Test steps:**    
+ Type into search   
+ Hit enter or hit search button   

**Expected result:** User should be able to see all relevant scores whether that be from searching a genre, title, or author   
**Actual result:** User is displayed all the relevant scores   
**Status:** Pass/Fail    
**Post-conditions:** User is shown all the relevant scores on the screen and can then navigate to one for purchase    
 <br>
**Use case name:** Browse on main menu   
**Description:** Shows populat scores on main menu page   
**Pre-condition:** user has navigated to the menu page (don't need to be logged in)   
**Test steps:**    
+ Hit the main menu button   
+ Or visit the website normally   

**Expected result:** User should be able to see a few popular scores in the main feed   
**Actual result:** User is displayed song title and information on the main page   
**Status:** Pass/Fail    
**Post-conditions:** User is then able to click and browse each popular song from the main page   

### Users Table
*This table contains information about users of the system.  This includes customers, sellers and operators.*

*partial example layout:*  
| UserID          | Username    | Created                  | Surname     | FirstName | Active | Password | RecoveryQuestion  | RecoveryAnswer |
| :-------------: | :---------: | :---------------------:  | :---------: | :-------: |:------:| :------: | :---------------: | :------------: |
| 00001           | Me          | June 1, 2023 09:00AM MST | Who         | Herbie    | True   | Pass123  | Favorite color    | Blue           |
| 00002           | You         | June 1, 2023 10:00AM MST | What        | Keith     | False  | Pass321  | Pet Name          | Marley         |
| 00003           | They        | June 1, 2023 11:00AM MST | Why         | Miles     | True   | 321Pass  | Mom's middle name | Elmo           |
| 00004           | Us          | June 1, 2023 04:00PM MST | Because     | Bill      | True   | 123 Pass | College Mascot    | Buff           |

| Field Name       | Description (data type)                                                                         |
| :--------------: | :-------------------------------------------------------------:                                 |
| UserID           | A unique numeric identifier representing the user.  Primary key, auto-generated. (int)          | 
| Username         | A unique alphanumeric identifier representing the login credential.  (varchar)                  | 
| Created          | The date and time when the user was created; defaults to current time.       (timestamp)        | 
| Surname          | String containing user's family name. (varchar)                                                 |
| FirstName        | string containing user's first name.    (varchar)                                               |
| Active           | Boolean indicating whether user has been disabled; defaults to true. (Boolean)                  |
| Password Price   | The combined price of all score's purchased within the order. (float)                           |
| RecoveryQuestion | Security question to use if password is forgotten.  (text)                                      |
| RecoveryAnswer   | Security question answer for password reset. (text)                                             |

*To display the customer orders table, you can use the following:*
```sqlite3
SELECT * users;
```
*To display a specific customers orders, you can use the following:*
```sqlite3
SELECT * FROM users WHERE UserID = 1;
```

**Use case name:** Verify login with valid username and password 

**Description:** Test the Google login page 

**Pre-conditions** (Given): User has valid username and password 

**Test steps (When):** 
+ Navigate to login page 
+ Provide valid user name 
+ Provide valid password 
+ Click login button 
 
**Expected result (Then):** User should be able to login

**Actual result :** User is navigated to myscores page with successful login 

**Status :** Pass/Fail

**Fail Notes: ** Login page will come back with an error message to allow user to retry.

Post-conditions: User is authenticated and successfully signed into their account. The account session details are aded to an in-memory cache.

