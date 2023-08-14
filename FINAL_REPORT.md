# Final Project Report **MusicVerse**

	An online collection of easy to read sheet music for a variety of genres.
	
* Team # : **3**
* Team/Product Name: **The Lightning Bolts**

* Team members
  
| Name           	| Git Username    	| Email                 	|
|----------------	|-----------------	|-----------------------	|
| Yuzhou Shen    	| EVNII           	| yush1599@colorado.edu 	|
| Sean Keery     	| skibum55        	| seke4820@colorado.edu 	|
| Mark Wilkening 	| markwilkening21 	| mawi3086@colorado.edu 	|
| Max Panning    	| copa4960        	| copa4960@colorado.edu 	|

### Project Tracking: 
https://trello.com/w/thelightningboltscspb3308group3

### Version Control:
https://github.com/EVNII/CSPB-3308-Team-3-Project

### Deployment:
Front end: https://musicverse.onrender.com/  
API Framework: https://musicverse-api.onrender.com/SwaggerUI/

### Completed
* Navigation Bar
* Login Page
* User Table with Login & Account Information
* Feature - Upload Score
* Feature - User Edit Account Information

### In the middle of implementing

* Feature - Reset Password
* API testing framework

### To be implemented

* Feature - Purchase Score
* Optimize Storage of Score/PDFs (i.e Amazon S3)
* Frontend Username validation
* Frontend Password validation
* Waiting login animation
* Update method for counting downloads/scores/views
* Backend upload files' type validation
* Frontend error message when the files cannot be corretly presented to client
* More Error Message to client

### Any bugs or problems?

* Price is a valid field, but everyone still could download any score without purchasing.
* When user field is edited, and then goes to the user list page, the production environment will show an error in browswer while there is no problem in the development environment.
* When client receives a file which is not in PDF format, the browser still opens a tab trying to show the PDF file. Ref #10.

### Video Demo
https://drive.google.com/file/d/1ZXOOaLVPQ1jqJjEo8NVHFT1qYdaYiIwW/view?usp=drive_link  
