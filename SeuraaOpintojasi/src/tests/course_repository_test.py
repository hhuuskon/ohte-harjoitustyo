import sqlite3
import unittest
from unittest import result
from entities.course import Course
from repositories.course_repository import repository as Crepository
from repositories.users_repository import repository as Urepository


class TestCourseRepository(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect("test.db")
        self.db.isolation_level = None
        Urepository.initialize_database()

    def test_add_data_db(self):
        result = Crepository.add_data_db("TK20002", 4, "20.03.2022")
        self.assertEqual(True, result)
