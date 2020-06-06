# CyberMongo

The purpose of the following project is experimenting with Python hashlib and pymongo libraries. It consists of a simple - yet robust - authentication mechanism that PBKDF2-encrypt (with cryptographic salt) the password in Python and store it together with the username credential on a cloud-hosted Mongo database.

Disclaimer: this is an experimental project, do NOT use any personal or sensitive data. We're just having fun.

## Behaviour

The user is able to:
- Create a new account providing a username and a password
- Login with the created existing credentials

## Setup

The project uses Python 3.7. All external dependencies are listed in the requirements.txt file.

MongoDB is a super cool NoSQL database that provides great out-of-the-box tools and integrated environments that can be setup in no time. In order to make this script work, you first need to setup a new Cluster on the Atlas Cloud.

To do so, you need to create a new MongoDB account on https://cloud.mongodb.com/. To setup properly your Cluster on MongoDB I highly suggest taking M001: MongoDB Basics on https://university.mongodb.com that is an awesome, free, introductory course that provides you with all the necessary information you need here.

I report anyway the basic steps to setup the Cluster. After successfully logging in:

- Click on "Create a New Cluster" and name it. It takes a couple of moments to setup your new Cluster.
- Click on "Database Access" on the left and "Add New Database User". Enter a valid username and password: remember the password as you'll need to connect to the database through the pymongo driver! As "Database User Privileges" select "Read and write to any database".
- Click on "Network Access" -> "Add IP Address" and enter 0.0.0.0. As suggested by MongoDB, it is not a good choice to make your database accessible from any IP; for this project it's absolutely fine as no sensitive data are used.
- Go back to the "Clusters" page and click on "Collections". Click on "Add my Own Data" and type "cybermongo" both for the new database and for the new collection. 
- Now everything is setup and you are ready to connect to your new Cluster from the python application!

Connecting to the Cluster from an external application:

- On the "Clusters" page click on "Connect your application". Select Driver->"Python" and Version->"3.6 or later"
- Copy & Paste the string that looks like "mongodb+srv://<username>:<password>@dbname-n4azf.mongodb.net/<dbname>?retryWrites=true&w=majority" in srv_atlas_path variable of the AccountDao.py constructor. The "username" shall be replaced with the username you've created before and the "password" with the corresponding password.
- Enjoy your Authentication Application!

If you want to dig deep even further, I strongly recommend downloading MongoDB Compass that is an awesome intuitive GUI that helps you manage your database and collections. Create a new Account and see how the Collection is updated on the Atlas Cluster and on Compass as well!





