# CleanArchitectureTemplate

Template for software architecture proposed by `Robert C. Martin` in his
[Clean Architecture concept](https://www.amazon.com/Clean-Architecture-Craftsmans-Software-Structure/dp/0134494164).

## Prerequisites

Running of this project locally requires the following tools to be
present on the host system:

* `docker` (version 20.10.0+)
* `docker-compose` (version 1.27.0+)

## Development environment

To run development environment
1. Go into `docker/development` folder.
2. Execute `docker-compose up`.
3. Open `http://localhost:8000` in browser.

#### Admin Panel

Admin Panel is a tool for managing records in a database.
The panel is available at
[http://localhost:8000/admin](http://localhost:8000/admin).

Username: `admin`  
Password: `admin`

#### API Documentation

API Documentation is available at
[http://localhost:8000/api/swagger/](http://localhost:8000/api/swagger/).
