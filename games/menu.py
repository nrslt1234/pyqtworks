from PyQt6 import uic

from games.basewindow import BaseWindow
from games.guess_the_number import Game_guess_the_number
from games.sps import StonePaperScissors


class Menu(BaseWindow):
    def __init__(self, name, path):
        super().__init__(name, path)
        self.form.menuButton.clicked.connect(self.clicker_for_sps)
        self.form.guessButton.clicked.connect(self.clicker_for_guess_the_number)

    def open(self, user_id):
        self.user_id = user_id
        self.windows.show()

    def clicker_for_sps(self):
        #self.game = StonePaperScissors("game", "ui/untitled.ui")
        #self.game.windows.show()
        self.open_windows["game"].open(self.user_id)
        self.close()







    def clicker_for_guess_the_number(self):
        #self.new_game = Game_guess_the_number("new_game", "ui/guess.ui")
        #self.new_game.windows.show()
        self.open_windows["new_game"].open(self.user_id)
        self.close()

