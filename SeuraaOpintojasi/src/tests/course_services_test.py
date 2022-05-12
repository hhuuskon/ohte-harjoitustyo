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
        result = courseservices.add_data("TKT20002", 4, "20.03.2022", 1)
        self.assertEqual(True, result)

    def test_create_summary(self):
        courseservices.add_data("TKT20002", 4, "20.03.2022", 1)
        courseservices.add_data("TKT20002", 4, "20.03.2022", 1)
        result = courseservices.create_summary(1)
        self.assertEqual([('TKT20002', 8)], result)

    def test_create_summary_all(self):
        courseservices.add_data("TKT20002", 4, "20.03.2022", 1)
        courseservices.add_data("TKT20005", 10, "21.04.2022", 1)
        result = courseservices.create_summary_all(1)
        self.assertEqual([(1, 'TKT20002', 4, '20.03.2022', 1),
                         (2, 'TKT20005', 10, '21.04.2022', 1)], result)
