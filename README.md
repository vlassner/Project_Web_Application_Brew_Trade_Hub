[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LVxkObDO)
# Overview 

COMING SOON! **Brew Trade Hub** will be the ultimate hub for breweries of all sizes to connect, collaborate, and thrive in the world of craft beer creation. Our vision is to provide a FREE dynamic online marketplace where commercial and craft breweries can FREE-ly buy, sell, trade, and barter for everything they need to brew exceptional beer – from hops and grains to yeast, flavorings, spices, packaging, and brewing equipment. But **Brew Trade Hub** will be more than just a FREE marketplace. We hope it will become a vibrant community where brewers come together to share their expertise, knowledge, and passion for brewing. Whether you're looking for industry news, seeking collaboration opportunities, or simply wanting to connect with fellow brewers, **Brew Trade Hub** is your go-to destination. Join us SOON to help us shape the future of a FREE brewery marketplace.

# User Stories 

This section describes key **user stories** identified for **Brew Trade Hub**. 

## US#1: User Registration

As a brewery representative, I want to be able to register a user on the platform, so that I can sell items like hops. Given that all the required information is given, like the name of the brewery, a short description, the name of the representative, and their contact information, when the brewery representative clicks on "submit", then a new user is created. 

```
TODO: estimate of effort in terms of user story points: 5
```

## US#2: Item Catalog Viewing

As registered user on the platform, I want to be able to view the item catalog, including (at a minimum), sorting by description, year, type, and brand. 

```
TODO: estimate of effort in terms of user story points: 8
```

## US#3: Item Catalog Maintenance

As registered user on the platform, I want to be able to maintain the item catalog. Given that the required information is given, like the description of the item, their year, type, and brand, when the user clicks on "submit" a new item is added to the catalog. Users should also be able to update items that they created.

```
TODO: estimate of effort in terms of user story points: 13
```

## US#4: Offering Items for Sale

As a registered user on the platform, I want to offer items for sale, so that I can get rid of excess (or no longer needed) inventory. Given that an item is offered for sale for a given price, when an offer is made and accepted, then a business transaction is started; when the item is received by the buyer, then the transaction is concluded. The possible status of an offer are: 'opened', 'accepted', 'shipped', and 'received'.

```
TODO: estimate of effort in terms of user story points: 20
```

## US#5: Searching and Accepting Offers

As a registered user on the platform, I want to be able to search offers by their statuses. 
* Given than I selected the 'opened' status, I should be able to see ALL offers with that status. I should then be able to accept any offer from other users. Then, the offer status should change to 'accepted'.
* Given than I selected the 'accepted' status, I should be able to see all of
my offers that were accepted by other users. I should then be able to change the status of those offers to 'shipped'. 
* Given than I selected the 'shipped' status, I should be able to see all of
the offers that I accepted that were shipped. I should then be able to change the status of those offers to 'received'. 

```
TODO: estimate of effort in terms of user story points: 13
```

## US#6: Rating/Reviewing Users (optional)

As a registered user on the platform, I want to be able to rate/review other users with whom I interacted with in a business transaction. Given that I interacted with other users in the past, I should be able to rate them, write new reviews about them, edit/delete past reviews, and also comment on reviews written about me.

```
TODO: estimate of effort in terms of user story points: 8
```

# Design 

An initial design for the project can be found in the [UML](/uml) folder. The design is given as a suggestion. Feel free to come up with your own design.  

# Implementation 

You are expected to implement user stories 1-5. User story #6 is optional (bonus points will be given). You are required to use Python in your implementation, with two possible options to choose for this web app: 

* Flask with SQL Alchemy. 
* [Square API](https://developer.squareup.com/reference/square). 

Finally, you are also required to incorporate caching into your project. **Flask-Caching** is a module that adds caching support to Flask. The following lines were added to **__init__.py**, which sets the caching timeout to 5 minutes. 

```
# cache setup
from flask_caching import Cache
cache = Cache()
cache.init_app(app, config={
    'CACHE_TYPE': 'simple',
    'CACHE_DEFAULT_TIMEOUT': 300
})
```

The example below illustrates how to use caching to query for the item catalog. 

```
from app import cache

catalog = cache.get("catalog")
if not catalog: 
    # cache miss!
    catalog = Item.query().all() # or a call to Square API
    cache.set("catalog", catalog)
```

You **must** use the following structure to organize your project. 

```
src
uml
scrum
tests
Dockerfile
README.md
requirements.txt
```

# Testing 

You are required to implement four *white box* testings using Selenium that together simulate the complete cycle of an offer being 'opened', 'accepted', 'shipped', and 'received'. 

# Deployment 

Commit and push your project using "final submission" as the commit message. You should also create a Docker image that would allow the instructor to run your project as a container. For that requirement, you should create a Dockerfile that allows the instructor to create the image of your project and from that image to run your project as a container. 

# Scrum 

Your team will be evaluated on how close you managed this project according to the Scrum framework and how well you worked as a member of a Srcum team. Each unit of work (user story) must have a clear estimate of effort in terms of points. Each sprint must have a clear goal statement. The team must record notes of their daily scrum meetings. There should also be notes for the sprint review and retrospective meetings at the end of each sprint. See the [Scrum](/scrum) folder for a sprint documentation template. You should create one file for each sprint, named *sprint#.md* replace the pound with the number of the sprint. 

The project progress should be recorded at the end of each sprint. Also, at the end of the project you should be able to produce burn down report using the provided template: in "/scrum/Burndown Chart Template.xlsx". 

# Rubric 

```
+10 for each required user story successfully implemented (up to 50 points)
+2 using cache 
+2 for each of the required white box testings (up to 8 points)
+25 scrum project management
    +5 sprint planning 
    +5 daily scrum meetings 
    +5 sprint review 
    +5 sprint retrospective
    +5 burn down chart showing steady progress
+15 team/self evaluation
+10 bonus points for US#6
+5 implementation was based on the Square API
+5 catalog is searchable
```
