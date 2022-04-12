import sqlite3
import unittest
from entities.users import Users
from repositories.users_repository import UsersRepository
from repositories.users_repository import repository


class TestUsersRepository(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect("test.db")
        self.db.isolation_level = None
        repository.initialize_database()
        self.user = Users('Erkki', 'Esimerkki')

    def test_sign_up_db(self):
        result = repository.sign_up_db(self.user)
        self.assertEqual(True, result)



    
