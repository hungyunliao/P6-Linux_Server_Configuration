import sys
sys.path.append('/var/www/catalog/catalog')

from functools import wraps
from models import Base, User, Category, Item
from flask import (Flask,
                   request,
                   url_for,
                   abort,
                   g,
                   render_template,
                   redirect)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, exc
from flask import session as login_session

import json

from login.controller import login
from oauth.controller import oauth
app = Flask(__name__)
@app.route("/")
def hello():
	return "Hello!!!, I love Digital Ocean!"
if __name__ == "__main__":
	app.run()
