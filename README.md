# Linkedin-visualization
https://linkedin-visualizer.herokuapp.com/

## Usage
1. Access the link shown above
2. Select graphs you want to see and upload a Connection.csv file (The sample file or the file you obtained from linkedin)

##### Sample File
https://linkedin-visualizer.s3.eu-north-1.amazonaws.com/Connections-sample.csv

##### How to obtain your Connections.csv data          
https://www.linkedin.com/help/linkedin/answer/66844/export-connections-from-linkedin?lang=en\

<img src=https://linkedin-visualizer.s3.eu-north-1.amazonaws.com/home2.png>

## Development
```
git clone https://github.com/camsenec/linkedIn-visualization.git
cd linkedIn-visualization
pip3 install -r requirements.txt
python3 app/app.py
open http://127.0.0.1:8050 (Default) on your browser
For test, Drag and Drop your Connection.csv to the given form
```

## Project Description 
### Overview
Visualization of data gives us a lot of inspiration and reveal new aspects of the data. We focus on LinkedIn, which is a employment-oriented SNS service, and visualize the connection of LinkedIn users, the change of the follower's changes.
LinkedIn provides APIs to retrieve profile, search for people and get brief information of connected users. With the retrieved data, we visualize it with a python library. The well-known library involves matplotlib and seaborn, but we use plotly in this project. The plotly generate beautiful visualization and support various functions. Besides, as an advanced version, we offer the visualization function by web application using Dash developed by the plotly community. 
 
### Development Flow
Our development plan involves 4 steps:
1. Interact with LinkedIn API and obtain some data by python scripts
2. Visualize the obtained set of data by various ways using plotly 
3. Implement web application which generate charts based on the user input (e.g. When user request her/his connection visualization, our web app returns a illustration the represents the user's co-relation with other users).
4. Improvements
  - Bug fix in csv file processing so that users do not have to remove "NOTE" included in the original connections.csv
  - Improve the feature of interaction by adding checkbox and allow users to select graphs they want to see       
  - Add some graphs and update visualization methods so that the output fits considered use cases               
  - (Preparation of sample data so that everyone can try this application)    
  - Deployment to a server        

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
