from tkinter import ttk, constants, StringVar
from services.users_services import services


class LoginUi:
    """ Sisäänkirjautumisen käyttöliittymän luokka
    """

    def __init__(self, root, handle_show_tracking_view, handle_show_sign_up_view):
        self._root = root
        self._username_entry = None
        self._password_entry = None
        self._handle_show_tracking_view = handle_show_tracking_view
        self._handle_show_sign_up_view = handle_show_sign_up_view
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
        self._login()

    def _login_click(self):
        """ Sisäänkirjautumiseen liittyvä toiminto
        """
        username = self._username_entry.get()
        password = self._password_entry.get()
        if len(password) == 0 or len(username) == 0:
            self.error_message(
                "Yritit syöttää tyhjän merkkijonon. Syötä käyttäjätunnus ja salasana.")
            return
        login = services.login(username, password)

        if login:
            self._handle_show_tracking_view()
        else:
            self.error_message(
                "Syötit väärän salasanan tai tunnusta ei ole olemassa.")
            return

    def _login(self):
        """ Sisäänkirjautumisen näkymän graafiset elementit. Tekstit ja painikkeet.
        """

        headertext = "Tervetuloa seuraamaan opintojasi"
        logintext = "Kirjaudu sisään"
        signuptext = "Luo uusi tunnus"
        usernametext = "Käyttäjätunnus"
        passwordtext = "Salasana"

        welcome_label = ttk.Label(master=self._frame, text=headertext)
        welcome_label.grid(columnspan=2, sticky=constants.W, pady=10)

        login_label = ttk.Label(master=self._frame, text=logintext)
        login_label.grid(row=2, sticky=constants.W)

        username_label = ttk.Label(master=self._frame, text=usernametext)
        self._username_entry = ttk.Entry(master=self._frame)
        username_label.grid(row=3, column=0, sticky=constants.W)
        self._username_entry.grid(row=3, column=1, sticky=constants.W)

        password_label = ttk.Label(master=self._frame, text=passwordtext)
        self._password_entry = ttk.Entry(master=self._frame)
        password_label.grid(row=4, column=0, sticky=constants.W)
        self._password_entry.grid(row=4, column=1, sticky=constants.W)

        login_button = ttk.Button(
            master=self._frame, text=logintext, command=self._login_click)
        login_button.grid(row=5, column=0, columnspan=2,
                          pady=5, sticky=constants.W)

        sign_up_button = ttk.Button(
            master=self._frame, text=signuptext, command=self._handle_show_sign_up_view)
        sign_up_button.grid(row=6, column=0, columnspan=2, sticky=constants.W)
