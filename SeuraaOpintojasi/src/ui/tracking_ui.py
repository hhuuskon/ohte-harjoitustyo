from tkinter import ttk, constants, StringVar
from services.users_services import services
from services.course_services import courseservices


class TrackingUi:
    """ Päänäkymän käyttöliittymän luokka
    """

    def __init__(self, root, handle_show_login_view, handle_show_summary_view, handle_show_summary_all_view):
        """
        Args:
        handle_show_login_view: Ohjaaminen kirjautumisnäkymään.
        handle_show_summary_view: Ohjaaminen koostenäkymään.
        """
        self._root = root
        self._couse_entry = None
        self._time_entry = None
        self._date_entry = None
        self._handle_show_login_view = handle_show_login_view
        self._handle_show_summary_view = handle_show_summary_view
        self._handle_show_summary_all_view = handle_show_summary_all_view
        self._frame = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        """ Tkinter toiminnallisuus
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """ Tkinter toiminnallisuus
        """
        self._frame.destroy()

    def error_message(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _initialize(self):
        """ Alustaa graafisen näkymän
        """
        self._frame = ttk.Frame(master=self._root)
        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame, textvariable=self._error_variable, foreground="red")
        self._tracking()

    def _logout_click(self):
        """ Uloskirjautumisen liittyvä toiminto
        """
        logout = services.logout()
        if logout:
            self._handle_show_login_view()

    def _add_data_click(self):
        """ Toiminto kurssin ja ajan syöttämiseksi tietokantaan.
        """
        course = self._course_entry.get()
        time = self._time_entry.get()
        date = self._date_entry.get()
        user_id = services.get_user_id()
        if len(course) == 0 or len(time) == 0 or len(date) == 0:
            self.error_message(
                "Yritit syöttää tyhjän merkkijonon. Täytä kaikki kentät.")
            return
        self._data = courseservices.add_data(course, time, date, user_id)
        if self._data:
            self._handle_show_summary_all_view()
        else:
            self.error_message("Tietojen syöttö tietokantaan ei onnistunut.")

    def _show_summary_view(self, type):
        """ Toiminto ohjaa oikeanlaiseen yhteenvedon näkymään
        """
        if type == "summary":
            self._handle_show_summary_view
        if type == "summary_all":
            self.self._handle_show_summary_all_view

    def _tracking(self):
        """
        Päänäkymän graaffiset elementit.
        Kurssi, siihen käytetty aika ja päivämäärä syötetään tähän.
        """
        logouttext = "Logout"
        headertext = "Syötä kurssin tiedot ja käytetty aika"
        coursetext = "Kurssi (esim. TKT20002)"
        timetext = "Käytetty aika (esim. 4)"
        datetext = "Päivämäärä (esim 30.04.2022)"
        addtext = "Lisää tietokantaan"
        summarytext = "Näytä kooste"
        summaryalltext = "Näytä kaikki merkinnät"

        welcome_label = ttk.Label(master=self._frame, text=headertext)
        welcome_label.grid(row=0, column=0)

        course_label = ttk.Label(master=self._frame, text=coursetext)
        self._course_entry = ttk.Entry(master=self._frame)
        course_label.grid(row=1, column=0)
        self._course_entry.grid(row=1, column=1)

        time_label = ttk.Label(master=self._frame, text=timetext)
        self._time_entry = ttk.Entry(master=self._frame)
        time_label.grid(row=2, column=0)
        self._time_entry.grid(row=2, column=1)

        date_label = ttk.Label(master=self._frame, text=datetext)
        self._date_entry = ttk.Entry(master=self._frame)
        date_label.grid(row=3, column=0)
        self._date_entry.grid(row=3, column=1)

        add_button = ttk.Button(
            master=self._frame, text=addtext, command=self._add_data_click)
        add_button.grid(row=4, column=0, columnspan=2)

        summary_button = ttk.Button(
            master=self._frame, text=summarytext, command=self._handle_show_summary_view)
        summary_button.grid(row=5, column=0, columnspan=2)

        summary_all_button = ttk.Button(
            master=self._frame, text=summaryalltext, command=self._handle_show_summary_all_view)
        summary_all_button.grid(row=6, column=0, columnspan=2)

        logout_button = ttk.Button(
            master=self._frame, text=logouttext, command=self._logout_click)
        logout_button.grid(row=7, column=0, columnspan=2)
