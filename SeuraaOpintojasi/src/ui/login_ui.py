from tkinter import ttk, constants
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
        self._frame = None # pylint: disable=duplicate-code

        self._initialize()

    def pack(self): # pylint: disable=duplicate-code
        """ Tkinter toiminnallisuus
        """
        self._frame.pack(fill=constants.X)

    def destroy(self): # pylint: disable=duplicate-code
        """ Tkinter toiminnallisuus
        """
        self._frame.destroy() # pylint: disable=duplicate-code

    def _initialize(self):
        """ Alustaa graafisen näkymän
        """
        self._frame = ttk.Frame(master=self._root) # pylint: disable=duplicate-code
        self._login()

    def _login_click(self):
        """ Sisäänkirjautumiseen liittyvä toiminto
        """
        username = self._username_entry.get()
        password = self._password_entry.get()
        login = services.login(username, password)

        if login:
            self._handle_show_tracking_view()

    def _login(self):
        """ Sisäänkirjautumisen näkymän graafiset elementit. Tekstit ja painikkeet.
        """

        headertext = "Tervetuloa seuraamaan opintojasi"
        logintext = "Kirjaudu sisään"
        signuptext = "Luo uusi tunnus"
        usernametext = "Käyttäjätunnus" # pylint: disable=duplicate-code
        passwordtext = "Salasana" # pylint: disable=duplicate-code

        welcome_label = ttk.Label(master=self._frame, text=headertext) # pylint: disable=duplicate-code
        welcome_label.grid(row=0, column=0) # pylint: disable=duplicate-code

        username_label = ttk.Label(master=self._frame, text=usernametext) # pylint: disable=duplicate-code
        self._username_entry = ttk.Entry(master=self._frame) # pylint: disable=duplicate-code
        username_label.grid(row=1, column=0) # pylint: disable=duplicate-code
        self._username_entry.grid(row=1, column=1) # pylint: disable=duplicate-code

        password_label = ttk.Label(master=self._frame, text=passwordtext) # pylint: disable=duplicate-code
        self._password_entry = ttk.Entry(master=self._frame) # pylint: disable=duplicate-code
        password_label.grid(row=2, column=0) # pylint: disable=duplicate-code
        self._password_entry.grid(row=2, column=1) # pylint: disable=duplicate-code

        login_button = ttk.Button(
            master=self._frame, text=logintext, command=self._login_click)
        login_button.grid(row=3, column=0, columnspan=2)

        sign_up_button = ttk.Button(
            master=self._frame, text=signuptext, command=self._handle_show_sign_up_view)
        sign_up_button.grid(row=3, column=1, columnspan=2)
