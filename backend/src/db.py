from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    """
    User model

    Has one-to-many relationship with locations
    """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, **kwargs):
        """
        Initialize User object
        """
        self.username = kwargs.get("username")
        self.email = kwargs.get("email")
        self.password = kwargs.get("password")

    def simple_serialize(self):
        """
        Simple serialize User object
        """
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }

    def serialize(self):
        """
        Serialize User object
        """
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password
        }


class Location(db.Model):
    """
    Location model

    Has many-to-one relationship with User model
    """
    __tablename__ = "locations"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    loc_category = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def get_loc_name(self):
        return self.name

    def get_loc_category(self):
        return self.loc_category

    def __init__(self, **kwargs):
        """
        Initialize Library object
        """
        self.name = kwargs.get("name")
        self.loc_category = kwargs.get("loc_category")
        self.user_id = kwargs.get("user_id")

    def serialize(self):
        """
        Simple serialize Library object
        """
        return {
            "id": self.id,
            "name": self.name,
            "loc_category": self.loc_category,
            "user_id": self.user_id
        }


class Food(db.Model):
    """
    Food model

    Has many-to-one relationship with locations model
    """
    __tablename__ = "foods"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    food_category = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    keywords = db.Column(db.String, nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey(
        "locations.id"), nullable=False)
    creation_time = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    expiration = db.Column(db.DateTime)

    def get_food_id(self):
        return self.id

    def get_food_name(self):
        return self.name

    def get_location(self):
        return Location.query.filter_by(id=self.location_id).first()

    def get_keywords(self):
        return self.keywords

    def get_location_name(self):
        location = self.get_location()
        return location.get_name()

    def get_location_category(self):
        location = self.get_location()
        return location.get_loc_category()

    def __init__(self, **kwargs):
        """
        Initialize Food object
        """
        self.food_category = kwargs.get("food_category")
        self.name = kwargs.get("name")
        self.keywords = kwargs.get("keywords")
        self.location_id = kwargs.get("location_id")
        if expiration is not None:
            self.expiration = kwargs.get("expiration")

    def simple_serialize(self):
        """
        Simple serialize Food object
        """
        return {
            "id": self.id,
            "food_category": self.food_category,
            "name": self.name,
            "keywords": self.keywords,
            "location_id" = self.location_id
            "creation_time": self.creation_time,
            "expiration": self.expiration
        }

    def serialize(self):
        """
        Serialize Room object
        """
        location = Location.query.filter_by(id=(self.location_id)).first()
        return {
            "id": self.id,
            "food_category": self.food_category,
            "name": self.name,
            "keywords": self.keywords,
            "location_id" = location.simple_serialize(),
            "creation_time": self.creation_time,
            "expiration": self.expiration
        }
