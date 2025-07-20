# API Server Documentation

These notes explain how to use **Fast API Server** that we made for EigenSol.

## About this Server

This server:
- is an **API Server**
- is developed in **Python language**
- uses `fast` library
- has **MVC** (Models, Views, Controllers) architecture in it
- has **Advance Routing** mechanism in it
- has **Middlewares** feature in it.
- has **Migrations and Models** feature in it (via `piccolo` library)
- uses **Postgress** database
- has configuration files and `.env` in it

### Why we used `fast` ?

- Because it is fast in speed
- And it automatically generated documentation for API details.
- It automatically does basic API related tasks like:
  - converting to JSON
  - handling client and matching a function against requested url
  - it has basic routing
  - etc.

We also had other options like `django` and `flask`, but we choose `fast` because of above reasons.

### Why we used `piccolo` ?

- Because it has **migraitons** and **seeders** features. And we can make them easily with commands.
- It supports **Models** with **ORM**. So we only call a function and it automatically makes and runs queries for basic CRUD operations.
- It uses **Postgress** (SQL-based) database. That is very fast.

There were other options as well, but we used `piccolo` for above mentioned reasons.

### Why we used `postgress` ?

- Postgress is **faster** than MySQL
- And it is compatible with `piccolo` library we are using.
- MySQL or MariaDB are not compatible with `piccolo`.

## Table of Contents

1. [Setup and Run](01_setup_and_run.md)  
2. [Routing Basics](02_routing_basics.md)  
3. [Advanced Routing](03_advanced_routing.md)  
4. [Controllers Basics](04_controllers_basics.md)  
5. [Techniques for Making good Controllers](05_techniques_for_making_good_controllers.md)  
6. [Migrations and Seeders](06_migrations_and_seeders.md)  
7. [Models](07_models.md)  
8. [Using Models in Controllers](08_using_models_in_controllers.md)  
9. [A Basic CRUD App](09_a_basic_crud_app.md)  
10. [Advance Topics to learn after this course](10_advance_topics_to_learn_after_this_course.md)
