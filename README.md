# My Weather

A single-page web app to display real time data received by synchronizing with
a [NodeMCU][1] controller, which in turn employs a network of sensors to measure
weather data in real time.

## Technologies

### Back-end

- [Flask](https://palletsprojects.com/p/flask/)

### Database

- [SQLite](https://sqlite.org/) (database)
- [SQLAlchemy](https://www.sqlalchemy.org/) (ORM)

### Front-end

- [Bootstrap](https://getbootstrap.com/)
- [jQuery](https://jquery.com/)

[1]: https://www.nodemcu.com/index_en.html

## Installation

### Prerequisites

- Python installed on system (3.6 or newer)

### Setup

Open a command line terminal and `cd` into the project folder. All the commands
have to be run from that folder.

#### Setting up a virtual environment (first time only)

```
> py -m venv venv
> venv\Scripts\activate
> py -m pip install --upgrade pip setuptools
> pip install -r requirements.txt
> deactivate
```

This will set up a virtual Python environment in the `venv` folder and install
the libraries that this project depends upon. In case the command `py` doesn't
work, try one of the following:

- use `python` instead of `py`
- use the full path to your installed Python (eg. `C:\Python36\python`) instead
    of `py`

From here on, before working in the project folder, you must activate your
virtual environment with `venv\Scripts\activate`. You can deactivate it after
you are done with `deactivate`.

#### Setting up the database

```
> py
```

This will start a Python shell. Enter the following commands to set up the
database.

```python
>>> from myweather import db
>>> db.create_all()
```

#### Running the project

To start the server, run the following commands:

```
> set FLASK_APP=myweather.py
> py -m flask run
```

Now open a browser and go to http://localhost:5000 to view your web app. After
you are done, go back to the command line and exit the running server with
Ctrl-C.

## Making changes

- All the back-end logic is in `myweather.py`. This includes the database model
    and the server logic.
- The HTML is in `templates\index.html`.
- The CSS and JS are inside the `static` folder.
