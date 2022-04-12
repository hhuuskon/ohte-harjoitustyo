from tkinter import ttk, constants
from services.users_services import services

class SignUpUi:
    """ Käyttäjätunnuksen käyttöliittymän luokka
    """
    def __init__(self, root, handle_show_tracking_view, handle_show_login_view):
        """
        Args:
        handle_show_tracking_view: Ohjaaminen päänäkymään
        handle_show_login_view: Ohjaaminen kirjautumisnäkymään
        """
        self._root = root
        self._username_entry = None
        self._password_entry = None
        self._handle_show_tracking_view = handle_show_tracking_view
        self._handle_show_login_view = handle_show_login_view
        self._frame = None

        self._initialize()

    def pack(self): # pylint: disable=duplicate-code
        """ Tkinter toiminnallisuus
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """ Tkinter toiminnallisuus
        """
        self._frame.destroy()

    def _initialize(self):
        """ Alustaa graafisen näkymän
        """
        self._frame = ttk.Frame(master=self._root)
        self._sign_up()

    def _sign_up_click(self):
        """ Käyttäjätunnuksen luomiseen liittyvä toiminto
        """
        username = self._username_entry.get()
        password = self._password_entry.get()
        login = services.sign_up(username, password)

        if login:
            self._handle_show_tracking_view()

    def _sign_up(self):
        """ Käyttäjätunnuksen luomisen graafiset elementit. Tekstit ja painikkeet.
        """

        headertext = "Luo uusi käyttäjätunnus"
        signuptext = "Luo tunnus"
        alreadyusertext = "Minulla on jo tunnus"
        usernametext = "Käyttäjätunnus"
        passwordtext = "Salasana"

        welcome_label = ttk.Label(master=self._frame, text=headertext)
        welcome_label.grid(row=0, column=0)

        username_label = ttk.Label(master=self._frame, text=usernametext)
        self._username_entry = ttk.Entry(master=self._frame)
        username_label.grid(row=1, column=0)
        self._username_entry.grid(row=1, column=1)

        password_label = ttk.Label(master=self._frame, text=passwordtext)
        self._password_entry = ttk.Entry(master=self._frame)
        password_label.grid(row=2, column=0)
        self._password_entry.grid(row=2, column=1)

        sign_up_button = ttk.Button(
            master=self._frame, text=signuptext, command=self._sign_up_click)
        sign_up_button.grid(row=4, column=0, columnspan=2)

        already_user_button = ttk.Button(
            master=self._frame, text=alreadyusertext, command=self._handle_show_login_view)
        already_user_button.grid(row=5, column=0, columnspan=2)
