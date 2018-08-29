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

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)

app.register_blueprint(login, url_prefix='/')
app.register_blueprint(oauth, url_prefix='/')

FB_APP_ID = json.loads(
        open('/var/www/catalog/catalog/oauth/fb_client_secrets.json', 'r').read()
    )['web']['app_id']
FB_APP_SECRET = json.loads(
        open('/var/www/catalog/catalog/oauth/fb_client_secrets.json', 'r').read()
    )['web']['app_secret']


@app.route('/')
@app.route('/categories')
def showLatest():
    """ Show items in ALL categories """

    session = DBSession()
    categories = session.query(Category).all()
    # list the latest itmes chronologically
    items = session.query(Item).order_by("id desc").all()
    return render_template(
        'showLatest.html',
        categories=categories,
        items=items,
        isLoggedIn=isLoggedIn(login_session)
    )
if __name__ == "__main__":
    app.run()
