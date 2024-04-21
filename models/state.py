#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
	""" State class """
	__tablename__ = 'states'
	name = Column(String(128), nullable=False)
	cities = relationship("City", backref="state", cascade="all, delete")

	@property
	def cities(self):
		storage = models.storage.all()
		result = []
		for key in storage:
			city = key.replace('.',' ')
			city = city.split(' ')
			if (city[0] == 'City' and storage[key].state_id == self.id):
				result.append(storage[key])
		return (result)
