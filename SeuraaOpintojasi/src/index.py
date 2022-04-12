from tkinter import Tk
from ui.ui import UserInterface

""" Ohjelman käynnistykseen liittyvät toiminnallisuudet.
"""


def main():
    """ Käynnistää graafien käyttöliittymän
    """

    window = Tk()
    window.title("Seuraa Opintojasi -sovellus")
    ui_view = UserInterface(window)
    ui_view.start()
    window.mainloop()


if __name__ == '__main__':
    main()
