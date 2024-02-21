import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    def test_inheritance(self):
        """ Test if Place inherits from BaseModel """
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attributes(self):
        """ Test the attributes of Place """
        place = Place()
        self.assertEqual(type(place.city_id), str)
        self.assertEqual(type(place.user_id), str)
        self.assertEqual(type(place.name), str)
        self.assertEqual(type(place.description), str)
        self.assertEqual(type(place.number_rooms), int)
        self.assertEqual(type(place.number_bathrooms), int)
        self.assertEqual(type(place.max_guest), int)
        self.assertEqual(type(place.price_by_night), int)
        self.assertEqual(type(place.latitude), float)
        self.assertEqual(type(place.longitude), float)
        self.assertEqual(type(place.amenity_ids), list)

    def test_reviews_property(self):
        """ Test the reviews property of Place """
        place = Place()
        self.assertEqual(type(place.reviews), list)

    def test_amenities_property(self):
        """ Test the amenities property of Place """
        place = Place()
        self.assertEqual(type(place.amenities), list)

    def test_amenities_setter(self):
        """ Test the amenities setter of Place """
        place = Place()
        amenity = Amenity()
        place.amenities = amenity
        self.assertIn(amenity, place.amenities)


if __name__ == '__main__':
    unittest.main()
