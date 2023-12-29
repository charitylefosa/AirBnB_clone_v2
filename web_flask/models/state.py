#!/usr/bin/python3
"""Defines the State class."""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    """Represent a state."""

    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship(
            'City', backref='state', cascade='all, delete-orphan')

    else:
        name = ""

        @property
        def cities(self):
            """Return the list of City objects from storage linked to the current State."""
            return [obj for key, obj in models.storage.all(models.City).items()
                    if obj.state_id == self.id]
