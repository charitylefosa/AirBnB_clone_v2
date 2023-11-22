#!/usr/bin/python3
""" State Module for HBNB project """
from base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from place import place_amenity


class Amenity(BaseModel, Base):
    """Amenity class that inherits from BaseModel and Base"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
