# Linkedin-vizualization
## Project Description 
### Overview
Visualization of data gives us a lot of inspiration and reveal new aspects of the data. We focus on LinkedIn, which is a employment-oriented SNS service, and visualize the connection of LinkedIn users, the change of the follower's changes.
LinkedIn provides APIs to retrieve profile, search for people and get brief information of connected users. With the retrieved data, we visualize it with a python library. The well-known library involves matplotlib and seaborn, but we use plotly in this project. The plotly generate beautiful visualization and support various functions. Besides, as an advanced version, we offer the visualization function by web application using Dash developed by the plotly community. 
 
### Development Flow
Our development plan involves 3 steps:
1. Interact with LinkedIn API and obtain some data by python scripts
2. visualize the obtained set of data by various ways using plotly 
3. implement web application which generate charts based on the user input (e.g. When user request her/his connection visualization, our web app returns a illustration the represents the user's co-relation with other users).
	
we implement step1 and step2 as the alpha version (Deadline: April 29) and step2 as the beta version (Deadline: May 27). 
 
### Reference
- LinkedIn API Documentation : https://docs.microsoft.com/en-us/linkedin/
- Plotly : https://plotly.com/python/
- Dash Introduction : https://dash.plotly.com/introduction
- Dash Documentation : https://dash.plotly.com/

## Development Rules
These are rules to avoid conflict
we only develop at master branch. 
### First step (in the process to generate various ideas for vizualizing data)
1. Do not edit files the other created 
2. To update, excecute the following command (you can do it using some GUI tools such as sourcetree or vizual studio code)
'''
git pull origin master
git add . (git add <edited_file>, where <edited_file> is a file you want add to the staging area)
git commit -m "Commit messsage (e.g. anything is OK)
git push origin master
'''

### Second step (in the process to combine ideas)
TBD

## Contributors
Yusef Ward
Tomoya Tanaka
