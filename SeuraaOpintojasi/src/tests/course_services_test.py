import unittest
from entities.course import Course
from repositories.users_repository import repository as repository
from services.course_services import courseservices
import sqlite3


class TestCourseServices(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect("test.db")
        self.db.isolation_level = None
        repository.initialize_database()


    def test_add_data(self):
        result = courseservices.add_data("TK20002", 4, "20.03.2022")
        self.assertEqual(True, result)