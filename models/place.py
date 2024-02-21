#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from os import getenv
from sqlalchemy.orm import relationship
import models

place_amenity = Table(
    'place_amenity', Base.metadata,
    Column('place_id',
           String(60),
           ForeignKey('places.id'),
           primary_key=True,
           nullable=False),
    Column('amenity_id',
           String(60),
           ForeignKey('amenities.id'),
           primary_key=True,
           nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    aminity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review",
                               backref='place',
                               cascade='all, delete')
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")

    else:

        @property
        def reviews(self):
            """ This is a getter method to get all linked reviews
                                     of this place"""
            from engine import db_storage
            related_reviews = []
            for review in db_storage.all(Review).values():
                if review.place_id == self.id:
                    related_reviews.append(review)
            return related_reviews

        @property
        def amenities(self):
            """ This is a getter method to get all linked amenities
            of this place"""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj):
            """ This is a setter method to set the amenities
            of this place"""
            if isinstance(obj, Amenity) and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj)
            else:
                pass
