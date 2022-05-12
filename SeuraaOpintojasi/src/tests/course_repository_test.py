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
        self.course_test = Course("TKT20002", 4, "20.03.2022", 1)
        self.course_test2 = Course("TKT20004", 2, "20.03.2022", 1)

    def test_add_data_db(self):
        result = Crepository.add_data_db(self.course_test)
        self.assertEqual(True, result)

    def test_summary_courses_db(self):
        Crepository.add_data_db(self.course_test)
        Crepository.add_data_db(self.course_test)
        result = Crepository.summary_courses_db(1)
        self.assertEqual([('TKT20002', 8)], result)

    def test_summary_all_courses_db(self):
        Crepository.add_data_db(self.course_test)
        Crepository.add_data_db(self.course_test2)
        result = Crepository.summary_courses_db(1)
        self.assertEqual([('TKT20002', 4), ('TKT20004', 2)], result)
