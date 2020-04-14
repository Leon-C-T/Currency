# README - Fiat Crypto Currency Converter 

For SFIA project 2  

## Table of Contents

[Project Brief](#brief)
   * [Proposal](#proposal)

[Planning](#planning)
   * [Initial Trello Board](#initspr)
   * [Sprint 1](#spr1)
   * [Sprint 1 Rolling Changes](#rolling1)
   * [Sprint 1 (end) / Sprint 2 (Start)](#spr1end)
   * [Sprint 2 Rolling Changes](#rolling2)
   * [Sprint 2 (end)](#spr2end)
   * [Issues during the 2 Sprints](#sprissues)

[Risk Assessment](#risk)
   * [Initial Risk Assessment and Matrix](#initialrisk)
   * [Final Updates to Risk Assessment and Matrix](#finalrisk)

[Project Architecture](#architecture)
   * [Entity Relationship Diagrams](#erd)
   * [Docker Swarm / UI Architecture](#dockerarch)
   * [Deployment Pipeline](#deploypipe)
   * [Toolchain](#deploypipe)

[Final Application](#deploypipe)

[Testing](#test)
   * [Pytest](#pytest)

[Deployment](#Deployment)
   * [Technology Used](#techused)
   * [Installation Guide](#install)

[Retrospective](#retrospec)
   * [What Went Well](#wentwell)
   * [Future Improvements](#futureimp)

[Author](#auth)


<a name="brief"></a>
## Project Brief

The main goal of this project was to utilise a number of different technologies to deploy an application that met certain key requirements. These Key Requirements were:

+ Using Python to Develop 4 Micro-Services with a RESTful architecture
+ Services 2, 3 and 4 should have dual implementations
+ The result of Service 4 should be stored in a MySQL Database
+ Docker should be used to containerise the 4 Micro-Services
+ Docker Swarm must be used to deploy the containers over a minimum of 2 nodes
+ Ansible must be used to configure the environment of the Nodes prior to the application being deployed
+ A CI/CD Pipeline using Jenkins will automate the entire process of Build/Test/Deploy

<a name="proposal"></a>
### Proposal

My proposal was to create a Random Cryptocurrency to Fiat Currency Converter (e.g. Bitcoin to Euro). My inital proposal is to have 4 services as follows:

+ Service 1: This will be the front end of my application, and Flask will be used to create this. My database will store the resulting crypto/fiat/price pair that is generated from Service 4, in a MySQL Database on GCP. Only a single index.html page will be used to display the information. Options will be present on Service 1 to enable dual implementation for Services 2, 3 and 4.

+ Service 2: Generates a random fiat currency to return to Service 4. The Fiat Currencies used in the application will be stored as csv files seperated into groups.

+ Service 3: Generates a random crypto currency to return to Service 4. The Cryptocurrencys used in the application will be stored as csv files seperated into groups.

+ Service 4: Returns to Service 1 a price based off of the fiat and crypto currency returned from Service 2 and 3. This services uses an External API to pull live market data provided by CryptoCompare. The mode of Service 4 e.g. (Crypto to Fiat or Fiat to Crypto conversion) is used to determine how to process the conversion using the External API. All Data is formatted and returned to Service 1.

![An Initial Wireframe diagram of my Flask Application (Service 1) ](/images/webblock1.png)

Shown above is an initial Wireframe diagram of my Flask Application (Service 1)

<a name="planning"></a>
## Planning

<a name="initspr"></a>
### Initial Trello Board

Trello, a web-based Kanban board, was used to plan the project while implementing Agile methodology, such as specifying a product and sprint backlog. The project was to be split into 2 sprints 

I utilised MosCoW Prioritisation to give each requirement of the project an importance, so that I can use this to sort the order I should prioritise completing them in. I used a colour labelling method to do this and you can see an example of this below for my Initial Trello Board:

![Initial Trello Board ](/images/initTrel.png) ![Labels](/images/MoSCoWLabels.png)

<a name="spr1"></a>
### Sprint 1 

The main aims in Sprint 1 were to create the 4 micro services and ensure they work together, as well as gain experience using Docker, Docker Swarm and Docker Swarm as early as possible so that the micro-services can be containerised. This is reflected in the Initial Sprint 1 board below:

![Initial Sprint 1 ](/images/initSP1Trel.png)

<a name="rolling1"></a>
#### Rolling Changes During Sprint 1

+ Service 1 Constructed using Flask
+ Service 2 and 3 Randomly Generates Fiat / Crypto
+ Service 4 Successfully makes External API Call and returns data back to Service 1
+ CSV Files implemented for service 2 and 3 to avoid long lists in code
+ Dockerfiles created for each service to enable Containerisation
+ First Version of Application containerised using Docker and pushed to repo on Docker Hub
+ First Version of Application run using Docker Compose with updated Docker-Compose file
+ First version of Application runs on multiple VM's using Docker Swarm
+ Database Successfully integrated with 2 tables
+ 2nd Implementation Successfully Built for Service 2 (Now adds Fiat Region Functionality e.g. Europe, Oceania etc.)
+ 2nd Implementation Successfully Built for Service 3 (Now adds Crypto List Functionality e.g. Top 10, Top 50 etc.)
+ 2nd Implementation Successfully Built for Service 4 (Can now switch between cryp2fiat or fiat2cryp modes)
+ Latest Version of Application runs on multiple VM's using Docker Swarm
+ Exposed TCP/UDP Ports required for Docker Swarm, on GCP VM Instance Firewalls
+ All Docker images version controlled using Docker Hub
+ All work files version controlled using GitHub

<a name="spr1end"></a>
### Sprint 1 (end) / Sprint 2 (start)

All changes during Sprint 1 were explained above. The main aims in Sprint 2 were to create a Ansible Playbook to configure the VM's that would be used in the Swarm, build a Jenkins Pipeline to Build the compose file, conduct testing on the micro-services and deploy the application to multiple seperate VM's. Shown Below is the Trello Board by the Start of Sprint 2:

![End Sprint 1 ](/images/endSP1Trel.png)

<a name="rolling2"></a>
#### Rolling Changes During Sprint 2

+ Nginx implemented as a container for Reverse Proxy
+ URL Tests written and tested locally using Docker-Compose
+ DB Tests written and tested locally using Docker-Compose
+ URL and DB Tests tested on multiple VM's using Docker-Swarm
+ Ansible Playbook written to install Docker on target VM's using inventory file and Tested
+ Ansible Playbook updated to also create Manager/Worker Nodes using inventory file and Tested
+ Ansible Playbook updated to also deploy Docker Swarm Stack Application and Tested
+ Jenkins Pipeline established on seperate Test VM with webhooks from Master branch of Github Repo
+ Jenkinsfile written as well as accompanying sh scripts
+ Jenkins CI/CD Pipeline Build/Test stages successful
+ App Relevant Secret Info + Ansible Files stored on Jenkins Test Server
+ Ansible File update to also copy files during deploy stage, to multiple VM's and deploy the Swarm Stack Application
+ Jenkins CI/CD Pipeline successfully built
+ All work files version controlled using GitHub
+ Webhooks created for Dockerhub Images

<a name="spr2end"></a>
### Sprint 2 (end)

All changes during Sprint 2 were explained above. The Trello board by the end of the Final Sprint is show below:

![End Sprint 2 ](/images/endSP2Trel.png)

By the end of Sprint 2 the key requirements as well as some optional requirements were implemented. However All 'Could Have' labelled features were not implemented due to time constraints, however these would be considered in a future sprint. This will be discussed later in the README.

<a name="sprissues"></a>
#### Issues Faced During The 2 Sprints:

+ Issue passing parameters between services for dual implementation. Get requests using JSON learnt to implement basic requests
+ Had issues with setting up Docker Swarm as Worker Nodes could not pull down image. Fixed by Making Docker Repo Public
+ Had issue where exposing API key as well as DB info needed to be prevented. An Environment File was made and used to store the environment variables so that it can be used on multiple VM's
+ SSH keys are needed to be used for Ansible to execute all instruction in Playbook on other VM's. SSH keys were securely transferred to relevant folders as well as Jenkins Test VM
+ Multiple minor issues with Docker Swarm, however these were fixed by checking the logs of the service or container and identifying potential causes e.g. missing dependecy, Database not on etc

<a name="risk"></a>
## Risk Assessment

<a name="initialrisk"></a>
### Initial Risk Assessment and Matrix

Shown below is the intial risk assessment and accompanying matrix for the project:

![Initial RA](/images/initialrisk.png)

![Initial Matrix](/images/initialmatrix.png)

<a name="finalrisk"></a>
### Final Updates to Risk Assessment and Matrix

Shown below are additions to the risk assessment and matrix after completing the project and encountering a further number of issues:

![Final RA](/images/finalrisk.png)

![Final Matrix](/images/finalmatrix.png)

<a name="Architecture"></a>
## Project Architecture

<a name="erd"></a>
### Entity Relationships

The initial ERD Diagram for my project is shown below. The database consists of a single table called currencylist, in which the pair and price returned to Service 1 is stored.

![Initial ERD](/images/initialerd.png)

The inital ERD was sufficient for a single implementation of Service 4, however to introduce a second implementaion a change to the ERD structure was required. The Main change came in adding a new table to store the results for the two different modes of operation - Crypto to Fiat and Fiat to Crypto, in 2 different tables. This is so that Price Column can have adjusted decimal parameters for storing the results.

The Final ERD Diagram used therefore, is shown below:

![Final ERD](/images/finalerd.png)

<a name="dockerarch"></a>
#### Docker Swarm / UI Architecture

Shown Below is the Docker Swarm architecture for the application. The Swarm Architecture consists of 2 GCP VM Instances, in which one VM instance is configured to be a Manager Node, and the other a Worker Node. An Overlay network is used to deploy the swarm so that the applications can communicate with each other from different VM's. There are a total of 5 Docker Containers used. 4 Containers are for the actual developed service, while the 5th container is an Nginx Image, which is acting as a Reverse Proxy to forward port 80 web traffic to port 5000 of the Flask App and vice versa. Services 2, 3 and 4 are replicated twice, while Service 1 and Nginx are only Replicated once.

![Docker Swarm Architecture Diagram](/images/swarmarch.png)

<a name="deploypipe"></a>
#### Deployment Pipeline

The Pipeline used for deployment is represented as a diagram shown below. The Entire Pipeline utilises 3 GCP VM instances. 1 is used as the Jenkins Test Server, 1 is used for developing the application as well as being the Master node in the swarm, and a spare VN instance is utilised to act as a worker node. All VM instances have access to the GCP SQL Database so that the flask application can retrieve and store data wherever the container may be.

![Deployment Pipeline](/images/deploypipe.png)

<a name="toolchain"></a>
#### Toolchain 

The Toolchain Pipeline is shown below: 

![Toolchain Pipeline](/images/Toolchain.png)

<a name="finalapp"></a>
## Final Application

After Implementing all feature and building the Final Flask Micro-service, an updated Wireframe diagram was produced to show the evolution of the page during the project. The final wireframe includes features for a dual implementation, as well as introduces a read from the 2nd table. This is shown below:

![Final Wireframe Diagram](/images/finalweb.png)

The Final design of the website is shown below.

![Screenshot of Final Webapp](/images/finalapp.png)

<a name="Test"></a>
## Testing

<a name="pytest"></a>
### Pytest

Testing is composed of 2 parts, URL testing to ensure the site is up and running, and Database testing which mimics the entry of a pair into the database.

In the URL Test, the local swarm is pinged and an assert of 200 is made which demonstrates the site is up and running, with a connection established.

The Database Testing loop consists of the following, and is repeated for both tables in the database:

+ Test Data is inserted into the table and an assert is made to check number of records has increased by 1
+ Test Data is read from table and an assert is made to check the data read back is equivalent to the data to be inserted.
+ Test Data is updated with different values and an assert is made after reading the values back, to ensure they match the updated test data.
+ Test Data deleted and the table is reset to its original state before the tests were conducted. An assert is made to ensure the number of records has decreased by 1.

The coverage report is shown below:

![Coverage Report](/images/coverage.png)

The coverage is 99% because none of the routes are being tested, the database functionality of the routes are being mimicked in the testing.py file

<a name="Deployment"></a>
## Deployment

<a name="techused"></a>
### Technology Used

+ 3 GCP VM Instances
+ 1 GCP SQL Server for storing Data
+ Jenkins Pipeline for CI/CD with Github Webhooks
+ Testing using Pytest
+ Ansible to configure the environment of deployment VM's
+ Docker to Containerise the application
+ Docker Swarm (and Compose) To run the Application across multiple VM's
+ Nginx as a reverse proxy
+ Docker Hub as a Version Control Service for Docker Images
+ GitHub as a Version Control Service for the Applications Code
    + Feature Branch Model implemented - Master / Developer Branches
    + Master Branch used to Build Docker Images automatically with Webhooks as well as Webhook with Jenkins
    + Developer Branch used to write out code and fix bugs in application

<a name="install"></a>
### Installation Guide

1. Setup 3 VM's on GCP with Ubuntu 18.04 LTS
2. Setup SSH keys for the 3 VM's and store in a config file in a .ssh folder
3. Install Jenkins on one GCP VM Instance to be used as a Jenkins Test Server. Expose TCP port 8080 in firewall rules
4. Add Jenkins to sudoers group
5. Setup Jenkins pipeline with Webhooks 
6. Copy over .ssh folder to root of jenkins directory as well as Ansible Playbook + inventory and keys.env files to working directory in Jenkins for Pipeline. e.g. var/lib/jenkins/workspace/currencyswarm
7. Add required Docker Swarm ports to Firewall Rules of all VM's: TCP 2376, 2377 and 7946, UDP 4789, and 7946.
8. Request build on Jenkins Pipeline.
9. Scripts should install all dependencies needed for Jenkins to run Swarm stack on Jenkins VM. Ansible Playbook will configure deployment VM's with software needed to ensure application Runs.

<a name="retrospec"></a>
## Retrospective

<a name="wentwell"></a>
### What Went Well

+ Project completed withing timeframe
+ All 'Must Have' Requirements Met
+ Docker, Ansible and Jenkins all Successfully Integrated into a continuous pipeline
+ Application deployed across multiple VM's

<a name="futureimp"></a>
### Future Improvements:

+ Implement Telegram API to enable Chatbot like Functionality
+ Implement Selenium for Front End Testing
+ Implement a 'percentage change' feature that show the percentage change of the price since the last time it appeared
+ Deploy application to more worker nodes
+ Incorporate a second manager node in Swarm to ensure System reliability

A Trello Board was made to show what a future sprint could look like to implement these improvements, as shown below:

![Future Kanban Board](/images/futuresprint.png)

<a name="auth"></a>
## Author

Leon Cresswell Thallapally


