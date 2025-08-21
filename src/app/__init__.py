'''
CS3250 - Software Development Methods and Tools - Spring 2024
Instructor: Thyago Mota
Team: BadButter
Description: Project 1 - Sol Systems Web App
'''

from datetime import date, datetime

import bcrypt
from flask import Flask
from flask_wtf.csrf import CSRFProtect
import os

app = Flask("Authentication Web App")
app.secret_key = 'do not share'
app.config['USER SIGN UP']= 'User Sign Up"'
app.config['USER SIGNIN']= 'User Sign In"'
csrf = CSRFProtect()
csrf.init_app(app)

# cache setup
from flask_caching import Cache
cache = Cache()
cache.init_app(app, config={
    'CACHE_TYPE': 'simple',
    'CACHE_DEFAULT_TIMEOUT': 5
})

# db initialization
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)


from app import models
with app.app_context(): 
    db.create_all()

# login manager
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

from app.models import User

# user_loader callback
@login_manager.user_loader
def load_user(user_id):
    try:
        #print(db.session.scalars(db.select(User).filter_by(id=user_id)).all())
        return db.session.execute(db.select(User).filter_by(id=user_id)).scalar_one()
        #print('User logged in')
    except:
        #print('User not logged in')
        return None

# create initial required data for grading stuff
from app.models import Offer, UserType, Review, Reply
import uuid, csv
with app.app_context():
    print("offer creation needed" if Offer.query.first() is None else "offers already created")
    if Offer.query.first() is None:
        with open('..\data\catalog.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == 'code':
                    continue
                new_offer = Offer(
                code = row[0],
                description = row[1],
                year = row[2],
                productType = row[3], 
                brand = row[4],
                price = 0.01,
                status = 'opened',
                buyer_id = 9999,
                seller_id = 'test user'
                )
                db.session.add(new_offer)
                db.session.commit()
    
    print("tmota admin creation needed" if db.session.scalars(db.select(User).filter_by(id='tmota')).first() is None else "tmota admin exists")
    if db.session.scalars(db.select(User).filter_by(id='tmota')).first() is None:
        hash_password = bcrypt.hashpw('1'.encode('utf-8'), bcrypt.gensalt())  # Hash the password
        TMota = User(
            id = 'tmota',
            name = 'tmota',
            password = hash_password,
            user_type = UserType.administrator,
            creationDate = date.today(),
            email = 'j',
            description = 'j',
            address = 'j',
            city = 'j',
            state = 'j',
            website = 'j',
            phone = 'j'
        )

        hash_password = bcrypt.hashpw('1'.encode('utf-8'), bcrypt.gensalt())  # Hash the password
        TUser = User(
            id = 'test user',
            name = 'j',
            password = hash_password,
            user_type = UserType.administrator,
            creationDate = date.today(),
            email = 'j',
            description = 'j',
            address = 'j',
            city = 'j',
            state = 'j',
            website = 'j',
            phone = 'j'
        )

        print("tmota admin created")
        print("creating reviews for users")
        r1 = Review(
            user_id = TMota.id,
            id = str(uuid.uuid1()),
            star_rating = 4,
            comment = "Amazingly good stuff! Just a little slow on delivery.",
        )

        r2 = Review(
            user_id = TMota.id,
            id = str(uuid.uuid1()),
            star_rating = 5,
            comment = "good! ",
        )

        rep1 = Reply (
            review_id = r1.id,
            id = str(uuid.uuid1()),
            comment = "Thanks for the great review!"
        )

        rep2 = Reply (
            review_id = r2.id,
            id = str(uuid.uuid1()),
            comment = "Thanks for the [other] great review!"
        )

        db.session.add(TMota)
        db.session.add(TUser)
        db.session.add(r1)
        db.session.add(r2)
        db.session.add(rep1)
        db.session.add(rep2)
        db.session.commit()

from app import routes