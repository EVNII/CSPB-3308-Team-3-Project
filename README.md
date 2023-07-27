# Project title: **MusicVerse**

    An online collection of easy to read sheet music for a variety of genres.
* Team # : **3**
* Team/Product Name: **The Lightning Bolts**
* Team members: list the name, git username, and email for each member.
  
| Name           	| Git Username    	| Email                 	|
|----------------	|-----------------	|-----------------------	|
| Yuzhou Shen    	| EVNII           	| yush1599@colorado.edu 	|
| Sean Keery     	| skibum55        	| seke4820@colorado.edu 	|
| Mark Wilkening 	| markwilkening21 	| mawi3086@colorado.edu 	|
| Max Panning    	| copa4960        	| copa4960@colorado.edu 	|

* Day/Time/TimeZone for the scheduled team weekly meeting (30 minutes via Zoom)
  
	**Mondays at 8 am MST/ 9 am CST/ 3 pm UTC +1/10 pm UTC +8**

### Vision statement:
   
To provide quality sheet music for all the world’s musicians

### Motivation: why are you working on this project?

- 1. Developing proficiency in web-based music score rendering
- 2. Creating a valuable platform for musicians
- 3. Overcoming challenges and completing a complex project
  
### Risks to project completion, possibly including:

- 1. Test pull request permissions
- 2. Getting mulitple programming languages to work together in order to build a successful website
- 3. Creating and managing a database that can be easily added to/edited

### New language or working environment 
HTML, CSS, Java, JavaScript, Python, GitHub, SQL, and Linux

### Possible risk: 

- 1. No experience with certain languages
- 2. Possible licensing music issues
- 3. Errors with formatting music scores

### Lack of some needed resources:
* Render the music score in web
* Generate PDF version for downloading
* Playing the score (potential embeded youtube videos)

### Mitigation Strategy for above risks

* Assign Sreesha as Product Owner
* Focus on Minimum Viable Product for first release
* Work on mountain tops to avoid spring conditions 
* Identify open source software which can be leveraged instead of new software development efforts
* Stands ups and daily summaries in Slack
* Pair programming and peer review 

### Development method: scrum, kanban, waterfall: with specifics!

Scrum: Define epics, create user stories, prioritize work, assign work to pairs, demo work, accept stories, iterate. We will try to first break each feature down to a list of smaller features. Then we can distribute these out and have meetings about any blocks, progress, etc. Once smaller features are done, we can combine these to finish the sprint and have a working feature of the final project. At the end, then we can combine all working prototypes to have a finished project.

### Project Tracking Software link (Trello is most common): 
https://trello.com/w/thelightningboltscspb3308group3

## BackEnd Part
### Setup python Environment.

```shell
pip install -r requirements.txt
```

### Run
```shell
export FLASK_APP=app/main
export FLASK_ENV=development
flask run
```

### Swagger UI
The Back end integered with Swagger UI to check the api usage.

Can access http://127.0.0.1:5000/SwaggerUI/

## FrontEnd Part

### Setup Environment
```shell
cd vite-project
npm install
```

### Run
```shell
echo "VITE_API_URI=http://127.0.0.1:5000" > .env.development
npm run dev
```