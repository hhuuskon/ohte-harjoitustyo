import sqlite3
import unittest
from unittest import result
from entities.users import Users
from repositories.users_repository import UsersRepository
from repositories.users_repository import repository


class TestUsersRepository(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect("test.db")
        self.db.isolation_level = None
        repository.initialize_database()
        self.user = Users('Erkki', 'Esimerkki')
        self.user2 = Users('Valmis', 'Kayttaja')
        repository.sign_up_db(self.user2)

    def test_sign_up_db(self):
        result = repository.sign_up_db(self.user)
        self.assertEqual(True, result)

    def test_login_db(self):
        username = self.user2.username
        password = self.user2.password
        result = repository.login_db(username, password)
        self.assertEqual(True, result)

    def test_existing_user_db(self):
        username = self.user2.username
        result = repository.existing_user_db(username)
        self.assertEqual(True, result)

    def test_no_sign_up_db(self):
        result = repository.sign_up_db(self.user2)
        self.assertEqual(False, result)

    def test_no_login_db(self):
        username = self.user2.username
        password = self.user.password
        result = repository.login_db(username, password)
        self.assertEqual(False, result)

    def test_already_existing_user_db(self):
        username = self.user.username
        result = repository.existing_user_db(username)
        self.assertEqual(False, result)




    
