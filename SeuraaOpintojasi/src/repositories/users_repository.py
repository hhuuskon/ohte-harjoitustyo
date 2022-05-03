import sqlite3


class UsersRepository:
    """ Tietokannan toiminnallisuuksien luokka
    """

    def __init__(self, connection):
        """
        Args:
        conncetion: Tietokantayhteyden luominen
        """
        self.db = sqlite3.connect(connection)
        self.db.isolation_level = None

        self.initialize_database()

    def drop_tables(self):
        """ Poistaa olemassaolevat tietokannat
        """
        self.db.execute('''DROP TABLE IF EXISTS users;''')
        self.db.execute('''DROP TABLE IF EXISTS courses;''')
        self.db.commit()

    def initialize_database(self):
        """ Luo uudet tietokannat
        """
        self.drop_tables()
        self.db.execute('''
        CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT
        );
        ''')

        self.db.execute('''
        CREATE TABLE courses (
        id SERIAL PRIMARY KEY,
        course TEXT,
        time INTEGER,
        date TEXT,
        user_id INTEGER REFERENCES users
        );
        ''')

        self.db.commit()

    def sign_up_db(self, user):
        """ Uuden käyttäjän tallentaminen tietokantaan
        Args:
        user: olio, joka sisältää
            username: Käyttäjätunnus jonka käyttäjä syöttää
            password: Salasana jonka käyttäjä syöttää
        """
        try:
            sql = "INSERT INTO users (username, password) VALUES (:username,:password)"
            self.db.execute(
                sql, {"username": user.username, "password": user.password})
            self.db.commit()
        except TypeError as error:
            print(error)
            return False
        return True

    def login_db(self, username, password):
        """ Käyttäjän tietojen tarkistaminen tietokannasta sisäänkirjautumista varten.
        Args:
            username: Käyttäjätunnus jonka käyttäjä syöttää
            password: Salasana jonka käyttäjä syöttää
        """

        try:

            sql = "SELECT username, password FROM users WHERE username=:username"
            result = self.db.execute(sql, {"username": username})
            user_check = result.fetchone()
            if user_check[0] == username and user_check[1] == password:
                return True
            return False
        except TypeError as error:
            print(error)
            return False
        return True


    def existing_user_db(self, username):
        """ Käyttäjänimen tarkistaminen tietokannasta tunnusten luomista varten.
        Args:
            username: Käyttäjätunnus jonka käyttäjä syöttää
        """

        try:

            sql = "SELECT username FROM users WHERE username=:username"
            result = self.db.execute(sql, {"username": username})
            existing_check = result.fetchone()
            if existing_check[0] == username:
                return True
        except TypeError as error:
            print(error)
            return False

    def add_data_db(self, course, time, date):
        """ Kurssiin käytetyn ajan syöttö
        Args:
        course: Kurssin tunniste jonka käyttäjä syöttää
        time: Kurssiin käytetty aika jonka käyttäjä syöttää
        date: Päivämäärä jonka käyttäjä syöttää
        """
        try:
            sql = "INSERT INTO courses (course, time, date) VALUES (:course,:time,:date)"
            self.db.execute(
                sql, {"course": course, "time": time, "date": date})
            self.db.commit()
        except TypeError as error:
            print(error)
            return False
        return True


repository = UsersRepository("db.db")
