#!/usr/bin/python3

""" a module to test the file db_storage.py """

import unittest
import os
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.engine.db_storage import DBStorage


class TestDBStorage(unittest.TestCase):
    """ a class to test the file db_stoarge.py """

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') != 'db', "not testing db storage")
    def setUp(self):
        """ set up for the test """
        self.db = DBStorage()
        self.db.reload()

    def tearDown(self):
        """ tear down for the test """
        self.db.close()

    def test_all(self):
        """ test the all method """
        obj = self.db.all()
        self.assertIsNotNone(obj)
        self.assertNotEqual(type(obj), dict)

    def test_new(self):
        """ test the new method """
        obj = State(name="California")
        self.db.new(obj)
        self.assertEqual(obj, self.db.all()["State.{}".format(obj.id)])

    def test_save(self):
        """ test the save method """
        obj = State(name="California")
        self.db.new(obj)
        self.db.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ test the reload method """
        obj = State(name="California")
        self.db.new(obj)
        self.db.save()
        self.db.reload()
        self.assertIsNotNone(self.db.all())
        self.assertEqual(type(self.db.all()), dict)
        self.assertIsNotNone(self.db.all()["State.{}".format(obj.id)])

    def test_delete(self):
        """ test the delete method """
        obj = State(name="California")
        self.db.new(obj)
        self.db.save()
        self.db.delete(obj)
        self.assertIsNone(self.db.all().get("State.{}".format(obj.id)))


if __name__ == "__main__":
    unittest.main()
