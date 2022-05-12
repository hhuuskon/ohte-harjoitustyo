
class Course:
    """ Yksittäisen kurssin ilmentymää kuvaava luokka
    """

    def __init__(self, course, time, date, user_id):
        """ Uuden käyttäjän luominen
        Args:
            course: Kussin tunniste jonka käyttäjä syöttää
            time: Kurssiin käytetty aika jonka käyttäjä syöttää
            date: Käytetyn ajan päivämäärä jonka käyttäjä syöttää
        """
        self.course = course
        self.time = time
        self.date = date
        self.user_id = user_id
