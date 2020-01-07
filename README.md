# Django Twitter

## Prerequesites
- Git https://git-scm.com/downloads
- Docker Desktop https://www.docker.com/products/docker-desktop
- Node.JS for NPM https://nodejs.org/en/download/ 

## Setup
- Clone repo
- Make a duplicate of `docker-compose.example.yml` and rename it to `docker-compose.yml`
- Run `./docker-dj.sh up` in bash to bring up the workspace
- Run `./docker-dj.sh ssh` in bash to connect to the workspace
- - When in workspace run `python manage.py createmigrations` to create migrations
- - And run `python manage.py migrate` to apply the migrations
- When in python folder (`cd python`), run 
- - `npm install`
- - `npm run watch` in bash to run compile scripts for app
