# Flask-Login-Template
Flask Login Template System from Tutorial

## Notes
* Tutorial: https://scotch.io/tutorials/authentication-and-authorization-with-flask-login
* To create the database, use:
```python
from project import db, create_app
db.create_all(app=create_app()) # pass the create_app result so Flask-SQLAlchemy gets the configuration.
```
* Install a requirements.txt file, use `sudo pip3 install -r requirements.txt`
* The user database is stored in db.sqlite, and can be viewed locally with a tool like TablePlus on Mac.

## Projects derived from this
* DotWatch App Website
