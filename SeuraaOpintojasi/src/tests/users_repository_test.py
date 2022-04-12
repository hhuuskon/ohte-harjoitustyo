import unittest
from repositories.users_repository import UsersRepository
from entities.users import Users


class TestUsersRepository(unittest.TestCase):
    def setUp(self):
        UsersRepository.drop_tables()
        UsersRepository.initialize_database()
        self.user = Users('Erkki', 'Esimerkki')

    def test_sign_up_db(self):
        UsersRepository.sign_up_db(self.user)
