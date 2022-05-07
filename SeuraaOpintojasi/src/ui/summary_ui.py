from tkinter import ttk, constants, StringVar
from services.course_services import courseservices


class SummaryUi:
    """ Päänäkymän käyttöliittymän luokka
    """
    def __init__(self, root, handle_show_login_view, handle_show_tracking_view, summary_type):
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
        self._summary_type = summary_type


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
        self._error_label = ttk.Label(master=self._frame, textvariable=self._error_variable, foreground="red")
        self._summary()
        if self._summary_type == "summary":
            self._summary_click()
        elif self._summary_type == "summary_all":
            self._summary_all_click()

    def _summary_click(self):
        result = courseservices.create_summary()


        if len(result) == 0:
            self.error_message("Sinulla ei ole vielä merkintöjä. Palaa edelliselle sivulle lisätäksesi niitä.")

        row_variable = 11
        for rivi in result:
            label = ttk.Label(master=self._frame, text=f"Kurssitunniste: {rivi[0]} | Käytetty aika: {rivi[1]} Tuntia")
            label.grid(row=row_variable, column=0)
            row_variable+=1
        

    def _summary_all_click(self):
        result = courseservices.create_summary_all()

        if len(result) == 0:
            self.error_message("Sinulla ei ole vielä merkintöjä. Palaa edelliselle sivulle lisätäksesi niitä.")

        row_variable = 11
        for rivi in result:
            label = ttk.Label(master=self._frame, text=f"Kurssitunniste: {rivi[1]} | Päivämäärä: {rivi[3]} | Käytetty aika: {rivi[2]} Tuntia")
            label.grid(row=row_variable, column=0)
            row_variable+=1

    def _summary(self):
        """
        Koosteen graaffiset elementit.
        Kooste kursseihin käytetystä ajasta esitetään tässä.
        """
        headertext = "Tässä haluamasi kooste:"
        returntext = "Palaa edelliseen"

        welcome_label = ttk.Label(master=self._frame, text=headertext)
        welcome_label.grid(row=2, column=0)

    
        return_button = ttk.Button(
            master=self._frame, text=returntext, command=self._handle_show_tracking_view)
        return_button.grid(row=100, column=0, columnspan=2)