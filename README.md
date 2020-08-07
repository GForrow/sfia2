# SFIA2 - Lootbox Generator

<b>Project:</b> Lootbox Generator <br>
<b>Made by:</b> Gary Forrow <br>

## ReadMe Content
* The Brief
* App Overview
* Trello Board
* Data
* Technologies Used
* CI Pipeline
* Front-End Design
* Risk Assessment
* Difficulties Faced
* Current Issues
* Improvements To Be Made
* Authors  

<br>

## The Brief
The brief set out for the DevOps Core Practical Project was to create a simple python/flask application that was deployed to a virtual environment while making use of containerisation. The project must also make use of a VCS, and deployed to a cloud platform by a CI server. 
<br>

### Minimum Requirements:
* Project management and tracking via Trello or equivalent Kanban board tech. 
* Clear documentation.
* User stories and use cases needed to complete the project.
* The project code is to be fully integrated into a Version Control System using Feature-Branch model, subsequently making use of webhooks through a
CI server and deployed to cloud-based virtual machines.
* The project is to follow a Service Oriented architecture.
* The project is to be deployed using containterisation and use an orchestration tool.
* The project is to make use of a reverse proxy.
* The project must make use of an Ansible Playbook to provision the environment the application is to run on.

<br>

## App Overview

I created a lootbox generator app. The application would generate a random piece of equipment, and a random quality for the equipment. An example being "Common Boots" or "Epic Gloves."

 * Service 1 send a GET request to Service 4.
 * Service 4 sends a GET request to Services 2 and 3.
 * Service 2 receives the GET request and generates the item quality.
 * Service 3 receives the GET request and generates the item type. (Gloves, Boots, Helm, etc)
 * Service 4 receives responses from Services 2 and 3, and concatenates them into a single result. 
 * Service 1 receives the result from Service 4 to display it on the page and commit it to the database. 

<p align="center">
  <img src="https://i.imgur.com/vA0TGdI.png">
</p>

<br>

## Trello Board

To keep track of my project and the tasks required for its completion I made us of Trello project management. This was to track the tasks of each sprint and understand the minimum requirements for the MVP. This was broken down to a backlog of tasks which were split into seperate sprints, and user stories to understand the Minimum Viable Product. 
 
<p align="center">
  <img src="https://i.imgur.com/HDrJGm6.png">
</p>

<br>

## Database

The database in use for the application uses a very simple table, as seen below. This was used to hold the result of previously opened loot boxes.

<p align="center">
  <img src="https://i.imgur.com/isvn4OW.png">
</p>

<br>


## Technologies Used

To keep in line with the brief I made us of the following technologies that were learned during my training: 
* Trello - Project Management / Kanban Board
* Google Cloud Platform - Cloud hosting
* mySQL - Database technology implemented via GCP
* Linux - Server OS used for hosting web app in GCP
* Docker - Used for containerisation of application. Making use of Docker Compose and Docker Swarm.
* Python - Application Back-End
* HTML - Application Front-End
* Flask - As applications Web Framework
* Git - Version Control also making use of GitHub
* Jenkins - CI Server
* Ansible - Used as the configuration management, making use of ansible playbooks for deployment configuration. 
* NGINX - Used as web server utilising reverse proxy to access site without specifying ports.

<br>

## CI Pipeline
<p align="center">
  <img src="https://i.imgur.com/kdnrmjG.jpg">
</p>
The image above details the CI Pipeline implemented for this project.
<br>

* Source Code - Written and tested locally while being commited to preestablished GitHub Repo making use of the feature branch model. 
* Project Tracking - We then look to Trello to confirm our previous job from project backlog was complete, and look to take on the next.
* Version Control System - Git is used to branch from the functioning app repository when developing each job from Trello, before being merged back into the main branch. (See screenshot below)
* CI Server - When a new commit has been made, Jenkins will run a job to replace the old version with the new from GitHub, and rerun the Docker Compose and Ansible Playbook. This would also cause new docker images to be built and pushed to Docker Hub.
* NGINX is also implemented at this stage to act as a reverse proxy to allow us to access the web app without requiring to specify a port. 
* This is all deployed on Ubuntu Servers hosted on GCP. 
<p align="center">
  <img src="https://i.imgur.com/ICrcXaN.png">
</p>
<br>

## Front-End Design
The first implementation of the application simply generated a piece of equipment. 
<p align="center">
  <img src="https://i.imgur.com/CQpOk7D.png">
</p>

<br>
The second implementation of the application generated the piece of equipment and saved it to the database. The previous pieces of equipment 
<p align="center">
  <img src="https://i.imgur.com/WuxZ1vt.png">
</p>

<br>

## Risk Assessment
<p align="center">
  <img src="https://i.imgur.com/qeuAEEl.png">
</p>

<br>

## Difficulties Faced
NGINX Reverse Proxy<br>
I had encountered an issue with the NGINX Reverse Proxy with a port conflict which was overhanging from previous configuration during development. This tripped me up for a while and through all my troubleshooting I ended up renaming and mispelling a part of my configuration. I had confirmed all parts of the configuration were correct and in place, but that one spelling mistake cost me a couple of hours. This has really enforced that I need to be diligent in spellchecking myself. 


Environment Variables<br>
Figuring out how to pass environment variables into the docker containers was just within reach for a long time but I couldn't quite figure it out. In this case I tunnel visioned on one approach and spent too long on it, where as trying something just a little different would have lead me to the correct answer. 


<br>

## Current Issues
* List of opened loot currently goes on forever meaning the page can end up incredibly long. This should be limited by only showing the last 50 results in the DB query. 

<br>

## Future Improvements
* User sign in to track individual users luck.
* Colour each quality of item.
* A board showing each item slot and the best quality item found so far for each slot.

<br>

### Author
Gary Forrow

<br>

##### Resources:
* Trello - https://trello.com/b/9hLtft5c/sfia2
* Link to app - http://35.189.124.167
<br>
