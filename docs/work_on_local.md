# Working on a local environment


## Prerequisites
- python 3.11
- postgres (my suggestion is to run it in a docker container)

Create an empty database:
```
> psql -U <username>
$ create database wordcounter;
$ grant all privileges on database wordcounter to <username>;
$ exit;
```

## Setup the project

### 1 - clone the project:

```
> git clone git@gitlab.com:mostaBG/wordcounter.git
> cd wordcounter/django-prj
> touch core/.env
```

In the `.env` file put something like

```
DEBUG=True
SECRET_KEY=*bk*!o+-z+^jhgnp81z4r&rr!-m-g8-4u-b3)naj6=wnl4drg1
ALLOWED_HOSTS="*"
DATABASE_URL="postgres://myusername:mypassword@localhost:5432/wordcounter"
```


### 2 - create a virtual environment
```
> python3.11 -m venv ../venv
> source ../venv/bin/activate
```


### 3 - install the required packages
```
> python -m pip install -r ../requirements/requirements-dev.txt
```

### 4 - apply the migrations
```
> export DJANGO_SETTINGS_MODULE=core.settings.dev
> ./manage.py migrate
```


### 5 - start the dev server & open the browser
```
> ./manage.py runserver
```
Open the browser at `http://localhost:8000`.


## Running the tests
Activate the virtual env and then run
```
pytest
```


## Update requirements
Install `pip-tools` after activating the environment:
```
(venv) > python -m pip install pip-tools
```

Now you can run commands like:
```
> pip-compile
> pip-compile requirements-dev.in
> pip-sync requirements-dev.txt
```

Command `pip-compile` creates the file called `requirements.txt` using the packages found in `requirements.in`. Since
we are using the `-dev` version, we have to run also `pip-compile requirements-dev.in`.

At this point, instead of running `pip-sync` (that would install the packages in `requirements.txt`) we
run `pip-sync requirements-dev.txt`.

See `https://github.com/jazzband/pip-tools` for more details.
