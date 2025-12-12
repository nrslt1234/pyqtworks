from PyQt6.QtWidgets import QTableWidgetItem

from games.basewindow import BaseWindow
from games.database import select_add_history_from_guess_the_number


class History(BaseWindow):
    def __init__(self, name, path):
        super().__init__(name, path)

        self.form.pushButton.clicked.connect(self.back_again)








    def open(self, user_id):
        self.user_id = user_id

        res = select_add_history_from_guess_the_number(user_id)

        self.form.tableWidget.setRowCount(len(res))
        for i, guess_prog in enumerate(res):

            self.form.tableWidget.setItem(i,0, QTableWidgetItem(guess_prog.user.FIO))
            self.form.tableWidget.setItem(i, 1, QTableWidgetItem(str(guess_prog.history)))
            self.form.tableWidget.setItem(i, 2, QTableWidgetItem(str(guess_prog.my_choice)))

        self.windows.show()

    def back_again(self):
        self.open_windows["new_game"].open(self.user_id)
        self.close()