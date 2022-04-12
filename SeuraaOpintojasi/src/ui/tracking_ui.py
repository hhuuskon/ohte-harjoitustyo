from tkinter import ttk, constants
from services.users_services import services


class TrackingUi:
    """ Päänäkymän käyttöliittymän luokka
    """
    def __init__(self, root, handle_show_login_view):
        self._root = root
        self._root.geometry("500x500")
        self._handle_show_login_view = handle_show_login_view
        self._frame = None

        self._initialize()

    def pack(self): # pylint: disable=duplicate-code
        """ Tkinter toiminnallisuus
        """
        self._frame.pack(fill=constants.X)

    def destroy(self): # pylint: disable=duplicate-code
        """ Tkinter toiminnallisuus
        """
        self._frame.destroy()

    def _initialize(self):
        """ Alustaa graafisen näkymän
        """
        self._frame = ttk.Frame(master=self._root)
        self._tracking()

    def _logout_click(self):
        """ Uloskirjautumisen liittyvä toiminto
        """
        logout = services.logout()
        if logout:
            self._handle_show_login_view()

    def _tracking(self):
        """ Päänäkymän graaffiset elementit tulevat tähän myöhemmin.
        """

        logouttext = "Logout"

        test_button = ttk.Button(
            master=self._frame, text=logouttext, command=self._handle_show_login_view)
        test_button.grid(row=3, column=0, columnspan=2)
