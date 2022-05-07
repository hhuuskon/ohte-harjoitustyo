from ui.login_ui import LoginUi
from ui.sign_up_ui import SignUpUi
from ui.tracking_ui import TrackingUi
from ui.summary_ui import SummaryUi

""" Käyttöliittymän osa, joka pitää sisällään eri näkymän.
    Näkymät vaihtelevat sen mukaan mitä osaa ohjelmasta käytetään
"""


class UserInterface:
    """ Käyttöliittymän näkymien hallinnoinnin luokka
    """
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._summary_type = None

    def start(self):
        """ Käynnistää tämän näkymän ensimmäiseksi
        """
        self._show_login_view()

    def _hide_current_view(self):
        """ Näkymän vaihdon yhteydessä piilottaa edellisen näkymän
        """
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_login_view(self):
        """ Näyttää kirjautumisnäkymän
        """
        self._hide_current_view()
        self._current_view = LoginUi(
            self._root, self._show_tracking_view, self._show_sign_up_view)

        self._current_view.pack()

    def _show_sign_up_view(self):
        """ Näyttää käyttäjätunnusten luomisen näkymän
        """
        self._hide_current_view()
        self._current_view = SignUpUi(
            self._root, self._show_tracking_view, self._show_login_view)

        self._current_view.pack()

    def _show_tracking_view(self):
        """ Näyttää toimintojen päänäkymän
        """
        self._hide_current_view()
        self._current_view = TrackingUi(
            self._root, self._show_login_view, self._show_summary_view, self._show_summary_all_view)

        self._current_view.pack()

    def _show_summary_view(self):
        """ Näyttää yhteenvedon syötetyistä tiedoista
        """
        self._summary_type = "summary"
        self._hide_current_view()
        self._current_view = SummaryUi(
            self._root, self._show_login_view, self._show_tracking_view, self._summary_type)

        self._current_view.pack()

    
    def _show_summary_all_view(self):
        """ Näyttää yhteenvedon syötetyistä tiedoista
        """
        self._summary_type = "summary_all"
        self._hide_current_view()
        self._current_view = SummaryUi(
            self._root, self._show_login_view, self._show_tracking_view, self._summary_type)

        self._current_view.pack()
