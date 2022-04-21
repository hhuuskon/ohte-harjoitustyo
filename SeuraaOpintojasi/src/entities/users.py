
class Users:
    """ Yksittäisen käyttäjän ilmentymää kuvaava luokka
    """

    def __init__(self, username, password):
        """ Uuden käyttäjän luominen
        Args:
            username: Käyttäjätunnus jonka käyttäjä syöttää
            password: Salasana jonka käyttäjä syöttää
        """
        self.username = username
        self.password = password
