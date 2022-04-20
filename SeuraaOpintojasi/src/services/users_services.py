from repositories.users_repository import UsersRepository as default_users_repository, repository
from entities.users import Users

class UsersServices:
    """ Käyttäjien hallinnoinnista vastaava luokka
    """

    def __init__(self, users_repository=default_users_repository):
        """ Käyttäjän kirjautumisen hallintaa.
        """
        self._user = None
        self._users_repository = users_repository

    def sign_up(self, username, password):
        """ Uuden käyttäjän luominen
        Args:
        username: Käyttäjätunnus jonka käyttäjä syöttää
        password: Salasana jonka käyttäjä syöttää
        """
        user = Users(username, password)
        if repository.existing_user_db(username):
            return False    
        login = repository.sign_up_db(user)

        if login:
            self._user = user
            return True
        return False

    def login(self, username, password):
        """ Käyttäjän sisäänkirjautuminen
        Args:
        username: Käyttäjätunnus jonka käyttäjä syöttää
        password: Salasana jonka käyttäjä syöttää
        """
        user = Users(username, password)
        login = repository.login_db(username, password)

        if login:
            self._user = user

            return True
        return False

    def logout(self):
        """ Kirjaa käyttäjän ulos
        """
        self._user = None
        return True



services = UsersServices()
