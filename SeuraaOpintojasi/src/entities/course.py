
class Course:
    """ Yksittäisen käyttäjän ilmentymää kuvaava luokka
    """

    def __init__(self, course, time, date):
        """ Uuden käyttäjän luominen
        Args:
            username: Käyttäjätunnus jonka käyttäjä syöttää
            password: Salasana jonka käyttäjä syöttää
        """
        self.course = course
        self.time = time
        self.date = date
