import unittest
from entities.users import Users
from repositories.users_repository import repository
from services.users_services import services
import sqlite3


class TestUsersServices(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect("test.db")
        self.db.isolation_level = None
        repository.initialize_database()
        self.user = Users('Erkki', 'Esimerkki')
        self.user2 = Users('Valmis', 'Kayttaja')
        repository.sign_up_db(self.user2)
        self._user = None

    def test_logout(self):
        result = services.logout()
        self.assertEqual(True, result)

    def test_login_correct_credentials(self):
        username = self.user2.username
        password = self.user2.password
        result = services.login(username, password)
        self.assertEqual(True, result)

    def test_login_wrong_credentials(self):
        username = self.user2.username
        password = self.user.password
        result = services.login(username, password)
        self.assertEqual(False, result)

    def test_sign_up_existing(self):
        username = self.user2.username
        password = self.user2.password
        result = services.sign_up(username, password)
        self.assertEqual(False, result)

    def test_sign_up_new(self):
        username = self.user.username
        password = self.user.password
        result = services.sign_up(username, password)
        self.assertEqual(True, result)
