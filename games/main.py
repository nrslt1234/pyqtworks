from PyQt6.QtWidgets import QApplication

from games.check_code import Checker
from games.guess_the_number import Game_guess_the_number
from games.history_guess import History
from games.login import Log
from games.menu import Menu
from games.rating import Rating
from games.show_the_result import ShowTheResult
from games.sps import StonePaperScissors

app = QApplication([])
game = StonePaperScissors("game", "ui/untitled.ui")
# game.windows.show()
game_new = Game_guess_the_number("new_game", "ui/guess.ui")
menu = Menu("menu", "ui/menu.ui")
log = Log("login", "ui/login.ui")
res = ShowTheResult("result", "ui/result.ui")
history = History("history", "ui/history_guess.ui")
rating = Rating("rating", "ui/rating.ui")


checker = Checker("checker", "ui/check_my_code.ui")
log.windows.show()
app.exec()
