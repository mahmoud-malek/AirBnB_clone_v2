#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import unittest
from models.base_model import BaseModel


class test_Amenity(test_basemodel):
    """ Is a testing class for Amenity"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)


class test_Amenity2(unittest.TestCase):
    """ Test the Amenity class """

    def test_inheritance(self):
        """ Test if Amenity inherits from BaseModel """
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attributes(self):
        """ Test the attributes of Amenity """
        amenity = Amenity()
        self.assertEqual(type(amenity.name), str)

    def test_place_amenities_property(self):
        """ Test the place_amenities property of Amenity """
        amenity = Amenity()
        self.assertEqual(type(amenity.place_amenities), list)

    def test_place_amenities_setter(self):
        """ Test the place_amenities setter of Amenity """
        amenity = Amenity()
        place_amenity = PlaceAmenity()
        amenity.place_amenities = place_amenity
        self.assertIn(place_amenity, amenity.place_amenities)


class test_Amenity(unittest.TestCase):
    """ Test the Amenity class """

    def test_inheritance(self):
        """ Test if Amenity inherits from BaseModel """
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attributes(self):
        """ Test the attributes of Amenity """
        amenity = Amenity()
        self.assertEqual(type(amenity.name), str)

    def test_amenity_ids(self):
        """ Test the amenity_ids property of Amenity """
        amenity = Amenity()
        self.assertEqual(type(amenity.amenity_ids), list)
