# Linkedin-visualization
## Demo
https://linkedin-visualizer.herokuapp.com/

## Usage (for Development)
```
git clone https://github.com/camsenec/linkedIn-visualization.git
cd linkedIn-visualization
pip3 install -r requirements.txt
python3 app/app.py
open http://127.0.0.1:8050 (Default) on your browser
Drag and Drop your Connection.csv to the given form
```

Note: How to obtain your Connections.csv data             
https://www.linkedin.com/help/linkedin/answer/66844/export-connections-from-linkedin?lang=en

**NB!** If note is included in the first three lines, delete the lines and make the line with "First line", "Last Name", ..., "Connected on" to the beggining.

## Project Description 
### Overview
Visualization of data gives us a lot of inspiration and reveal new aspects of the data. We focus on LinkedIn, which is a employment-oriented SNS service, and visualize the connection of LinkedIn users, the change of the follower's changes.
LinkedIn provides APIs to retrieve profile, search for people and get brief information of connected users. With the retrieved data, we visualize it with a python library. The well-known library involves matplotlib and seaborn, but we use plotly in this project. The plotly generate beautiful visualization and support various functions. Besides, as an advanced version, we offer the visualization function by web application using Dash developed by the plotly community. 
 
### Development Flow
Our development plan involves 3 steps:
1. Interact with LinkedIn API and obtain some data by python scripts
2. visualize the obtained set of data by various ways using plotly 
3. implement web application which generate charts based on the user input (e.g. When user request her/his connection visualization, our web app returns a illustration the represents the user's co-relation with other users).
4. The following is the list of future works
- Add more interactive function. 
  (e.g. Can see a list of people with whom a user connected during a certain period, where the period is determined by a move of slider (GUI component))
- Add more graph to visualize Connection data
- Add other visualization such as communicated message analysis using Natural Language processing Technique. Users can select "Connection Vizualization" or "message Visualization"
	
we implement step1 and step2 as the alpha version (Deadline: April 29) and step2 as the beta version (Deadline: May 27). 
 
### Reference
- LinkedIn API Documentation : https://docs.microsoft.com/en-us/linkedin/
- Plotly : https://plotly.com/python/
- Dash Introduction : https://dash.plotly.com/introduction
- Dash Documentation : https://dash.plotly.com/


## Development Rules
These are rules to avoid conflict while developing only at master branch. 
1. Do not edit files the other created 
2. To update, excecute the following command (you can do it using some GUI tools such as sourcetree or vizual studio code)
```
git pull origin master
git add . (git add <edited_file>, where <edited_file> is a file you want add to the staging area)
git commit -m "Commit messsage (e.g. anything is OK)
git push origin master
```
Or, 
```
fork this repository
develop it in your folked repository and make a pull request
```

## Contributors
Yusef Ward             
Tomoya Tanaka
