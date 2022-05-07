from repositories.course_repository import CourseRepository as default_course_repository, repository
from entities.course import Course

class CourseServices:

    def __init__(self, course_repository=default_course_repository):

        self._course = None
        self._course_repository = course_repository

    
    def add_data(self, course, time, date):
        """ Kurssiin käytetyn ajan syöttö
        Args:
        course: Kurssin tunniste jonka käyttäjä syöttää
        time: Kurssiin käytetty aika jonka käyttäjä syöttää
        date: Päivämäärä jonka käyttäjä syöttää
        """
        entry = repository.add_data_db(course, time, date)

        if entry:
            return True
        return False

    def create_summary(self):

        summary = repository.summary_courses_db()

        return summary


    def create_summary_all(self):

        summary = repository.summary_all_courses_db()

        return summary
    
courseservices = CourseServices()