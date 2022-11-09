# Django Rest framework skeleton app

## Content: ##

1. Quick start setup
2. Manual setup
3. Features

## Quick start setup: ##

1. Setup env variables for local development:

   cp .env.example .env

2. Setup docker-compose override file for local development:

   cp example.docker-compose.override.yml docker-compose.override.yml

3. Run dockerized server:

   docker-compose up

4. After docker image is built and server started, setup migrations/static files/admin access:

   docker-compose exec app sh entrypoint.sh

## Manual setup ##

1. Set .env variables (see comments in env.dev.example and env.local.example for details):
    1. Create .env file from development (env.dev.example) template
    2. Set PROJECT_NAME, FRONTEND_URL
    3. Set local DB credentials
    6. Set admin credentials for script or setup them manually later
2. Set docker-compose.override.yml file:
    1. By default all non-core services (db , ...) are placed remotely, in this case no
       docker-compose.override.yml is needed
    2. To place some services locally add docker-compose.override.yml
3. Run dockerized server: docker-compose up --build
4. After docker image is built and server started, setup migrations/static files/admin access:
    the entrypoint.sh will handel server setup
   
## Features ##

1. Server is served at http://localhost:80
2. Swagger docs are served at http://localhost/docs/all and http://localhost/docs/{app name}
3. Admin panel is served at http://localhost/admin
4. Includes Celery for scheduled and background tasks. See app/core/tasks.py and app/settings.py for examples

# AUTHOR
Created at 🌙 by HamdiAAA
- my profile : [Hamdi Mohamed ](https://github.com/HamdiAAA).
### 2021 FUN FACTS : 
- House of the dragons
- God of war ragnarok is the game of the year.
- the witcher 3 wild hunt is the best game of all times ❤ .
