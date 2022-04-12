from tkinter import Tk, ttk, constants
from services.users_services import services

class LoginUi:
    def __init__(self, root, handle_show_tracking_view, handle_show_sign_up_view):
        self._root = root
        self._username_entry = None
        self._password_entry = None
        self._handle_show_tracking_view = handle_show_tracking_view
        self._handle_show_sign_up_view = handle_show_sign_up_view
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
             self._frame = ttk.Frame(master=self._root)
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

        login_button = ttk.Button(master=self._frame, text=logintext, command=self._login_click)
        login_button.grid(row=3, column=0, columnspan=2)

        sign_up_button = ttk.Button(master=self._frame, text=signuptext, command=self._handle_show_sign_up_view)
        sign_up_button.grid(row=3, column=1, columnspan=2)