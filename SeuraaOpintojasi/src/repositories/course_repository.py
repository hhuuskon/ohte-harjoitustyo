import sqlite3


class CourseRepository:

    def __init__(self, connection):

        self.db = sqlite3.connect(connection)
        self.db.isolation_level = None

    def add_data_db(self, course_entry):
        """ Kurssiin käytetyn ajan syöttö
        Args:
        course: Kurssin tunniste jonka käyttäjä syöttää
        time: Kurssiin käytetty aika jonka käyttäjä syöttää
        date: Päivämäärä jonka käyttäjä syöttää
        """
        try:
            sql = "INSERT INTO courses (course, time, date, user_id) "\
                "VALUES (:course,:time,:date,:user_id)"
            self.db.execute(
                sql, {"course": course_entry.course, "time": course_entry.time, "date": course_entry.date, "user_id": course_entry.user_id})
            self.db.commit()
        except TypeError as error:
            print(error)
            return False
        return True

    def summary_courses_db(self, user_id):
        ''' Kurssiin käytetyn ajan yhteenvedon haku tietokannasta
        Args:
        user_id: Käyttäjän yksilöivä numero
        '''
        try:
            sql = "SELECT course, SUM(time) FROM courses C WHERE C.user_id=:user_id GROUP BY course"
            result = self.db.execute(sql, {"user_id": user_id})
            summary = result.fetchall()
            return summary
        except TypeError as error:
            print(error)
            return False

    def summary_all_courses_db(self, user_id):
        ''' Kaikkien käyttäjän syöttämien kurssien haku tietokannasta
        Args:
        user_id: Käyttäjän yksilöivä numero
        '''
        try:
            sql = "SELECT * FROM courses C WHERE C.user_id=:user_id ORDER BY course"
            result = self.db.execute(sql, {"user_id": user_id})
            summary = result.fetchall()
            return summary
        except TypeError as error:
            print(error)
            return False


repository = CourseRepository("db.db")
