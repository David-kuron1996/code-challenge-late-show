# project Name:
`Late Show API` A RESTful API built with Flask and SQLAlchemy for managing data related to The Late Show episodes, guests, and their appearances.

This project implements a data model that connects Episodes, Guests, and Appearances, allowing you to retrieve information about show episodes and the guests who appeared on them, as well as add new appearances with ratings.

# projects models:

The API is built around three core models that represent the entities of our application:

1. Episode
Represents a single episode of the show.

id: Primary key (Integer)
date: The air date of the episode (String, e.g., "1/11/99")
number: The episode number (Integer)

2. Guest
Represents a guest who appears on the show.

id: Primary key (Integer)
name: The guest's full name (String)
occupation: The guest's profession (String)



