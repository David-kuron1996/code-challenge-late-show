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

3. Appearance
A join table that represents a guest's appearance on a specific episode, including their rating.

id: Primary key (Integer)
rating: The guest's rating from 1 to 5 (Integer)
episode_id: Foreign key linking to an Episode (Integer)
guest_id: Foreign key linking to a Guest (Integer)

Relationships
An Episode has many Guests through Appearance.
A Guest has many Episodes through Appearance.
An Appearance belongs to one Episode and one Guest.
Cascade deletes are configured, meaning if an Episode or Guest is deleted, their associated Appearance records are also deleted.


