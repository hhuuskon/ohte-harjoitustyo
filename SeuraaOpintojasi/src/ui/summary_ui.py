from tkinter import ttk, constants, StringVar
from services.users_services import services


class SummaryUi:
    """ Päänäkymän käyttöliittymän luokka
    """
    def __init__(self, root, handle_show_login_view, handle_show_tracking_view):
        """
        Args:
        handle_show_login_view: Ohjaaminen kirjautumisnäkymään.
        handle_show_tracking_view: Ohjaaminen päätoiminnallisuuden näkymään.
        """
        self._root = root
        self._handle_show_login_view = handle_show_login_view
        self._handle_show_tracking_view = handle_show_tracking_view
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
        self._error_label = ttk.Label(master=self._frame, textvariable=self._error_variable)
        self._summary()

    
    def _logout_click(self):
        """ Uloskirjautumisen liittyvä toiminto
        """
        logout = services.logout()
        if logout:
            self._handle_show_login_view()

    def _summary(self):
        """
        Koosteen graaffiset elementit.
        Kooste kursseihin käytetystä ajasta esitetään tässä.
        """
        logouttext = "Logout"
        headertext = "Tähän tulee koosteen toiminnot myöhemmin"
        coursetext = "Kurssi"
        timetext = "Käytetty aika"
        datetext = "Päivämäärä"
        returntext = "Palaa edelliseen"

        welcome_label = ttk.Label(master=self._frame, text=headertext)
        welcome_label.grid(row=0, column=0)


        summary_button = ttk.Button(
            master=self._frame, text=returntext, command=self._handle_show_tracking_view)
        summary_button.grid(row=5, column=0, columnspan=2)

        logout_button = ttk.Button(
            master=self._frame, text=logouttext, command=self._logout_click)
        logout_button.grid(row=6, column=0, columnspan=2)