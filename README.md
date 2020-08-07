# SFIA2 - Lootbox Generator

<b>Project:</b> Lootbox Generator <br>
<b>Made by:</b> Gary Forrow <br>

## ReadMe Content
* The Brief
* App Functionality
* Technologies Used
* Project Tracking
* Data
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

<br>

<br>

 * Service 1 send a GET request to Service 4.
 * Service 4 sends a GET request to Services 2 and 3.
 * Service 2 receives the GET request and generates
 * Service 3 receives the GET request and generates
 * Service 4 receives responses from Services 2 and 3, and concatenates them into a single result. 
 * Service 1 receives the result from Service 4 to display it on the page and commit it to the database. 

<p align="center">
  <img src="https://i.imgur.com/vA0TGdI.png">
</p>

<br>

## Trello Board

The user stories I set to meet the above brief were: 
 * As a user I must be able to add a plant to my colleciton
 * As a user I must be able to add details of my plants to differentiate between individuals.
 * As a user I must be able to add notes to individual plants to track particular requirements individuals.
 * As a user I must be able to edit a plant's description.
 * As a user I must be able to edit a plant's name. 
 * As a user I must be able to edit a plant's notes.
 
 See image below for full list of user stories created for the development of this application, as well as the design 
 flow implemented through the development.
 
<p align="center">
  <img src="https://i.imgur.com/DqNqSFl.png">
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
  <img src="https://i.imgur.com/X9uqvFX.png">
</p>
The image above details the CI Pipeline implemented for this project.
<br>

* Source Code - Written and tested locally while being commited to preestablished GitHub Repo
* Project Tracking - We then look to Trello to confirm our previous job was complete, and look to take on the next.
* Version Control System - Git is used to branch from the functioning app repository when developing each job from Trello, before being merged back into the main branch.
* CI Server - When a new commit has been made, Jenkins will run a job to replace the old version with the new from GitHub, and rerun the app service.

<br>

## Front-End Design
A brief walkthrough of the front-end design of the website
<p align="center">
  <img src="https://i.imgur.com/dneOWlo.png">
</p>
The user is welcomed to the site with the homepage
<br>
<p align="center">
  <img src="https://i.imgur.com/A5OIy6M.png">
</p>
The user can choose to sign up to the website by creating an account. 
<p align="center">
  <img src="https://i.imgur.com/yB82yuL.png">
</p>
The user can then sign in to the website
<p align="center">
  <img src="https://i.imgur.com/nlGq4LL.png">
</p>
After signing in, the user is directed to their plant list which initially is empty. They can choose the Add New Plant button to start their diary.
<p align="center">
  <img src="https://i.imgur.com/MmsO6ap.png">
</p>
The user is then directed to the New Plant page where they can enter their plants details.
<p align="center">
  <img src="https://i.imgur.com/3ntikAB.png">
</p>
Once submitted the user is directed back to their plant list with the new entry listed. Each individual entry can be edited or deleted.
<p align="center">
  <img src="https://i.imgur.com/mBFU6a6.png">
</p>
The user also has the option to update their account details or delete their account and posts entirely.

<br>

## Risk Assessment
<p align="center">
  <img src="https://i.imgur.com/mCvxbSo.png">
</p>

<br>

## Difficulties Faced
Page Layout and Design<br>
The original design I had planned would present the user with a splash screen welcoming them to the website with a message in the middle of
the page, with navigation buttons beneath this message. When it came to development I found I did not have the time to develop
my HTML skills enough to achieve this. The ideal design also had tiled plant themed background image present on all pages. 

Database Structure<br>
When the project was planned, one of the "shoulds" was to include the functionality of the user to have individual rooms
which they could organise their plants into. I feel I should have approached this first to avoid having to dismantle some of
the existing functionality to add this. 

<br>

## Current Issues
* Database entries can currently be deleted by navigating directly to the delete post URL in the browser if the post IDs are known

<br>

## Future Improvements
* Implement Splash screen on homepage for a more aesthetically pleasing welcome to the site.
* Implement user rooms for better plant organisation.
* Add plant themed background to pages.
* More consideration in page layout and font styling. 
* Ability to upload images to each plant entry.

<br>

### Author
Gary Forrow

<br>

##### Resources:
* Trello - https://trello.com/b/mWkaYpmy/plant-diary
* Link to app - http://35.189.101.96/
<br>
