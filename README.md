# Table of Contents
* [Heroku](#heroku)
* [Installation](#installation)
* [Running the server](#running-the-server)
* [Superuser](#superuser)

## Heroku 
A deployed version of this project is available at [https://auctions-website.herokuapp.com/](https://auctions-website.herokuapp.com/).

## Installation

The repository tracks only the Django project. To clone it and keep the correct directory structure do the following:

1. Create a virtual environment eg.
	`virtualenv auctions`
2. Enter the directory it creates and activate the environment
	```bash
	cd auctions
	. bin/activate
	```
3. Clone the repository
	* `git clone https://github.com/harveyrandall/auctions.git` or `git clone git@github.com:harveyrandall/auctions.git` depending on whether you use SSH or HTTPS.
4. Enter the directory the repository is cloned into
	```bash
	cd auctions
	```
5. Install the packages the project requires
	```bash
	pip install -r requirements.txt
	```

The project should now be all setup and ready to run.

## Running the server
Run the server like any normal Django project.

```bash
python manage.py runserver
```

To see the progress so far open `127.0.0.1:8000` in your browser.

## Superuser
I have created a superuser with the following details:
* **Username:** admin
* **Password:** password
