from PyQt6.QtWidgets import QTableWidgetItem

from games.basewindow import BaseWindow
from games.database import rate_person_by_win, rate_person_by_loss


class Rating(BaseWindow):
    def __init__(self, name, path):
        super().__init__(name, path)

        self.form.winButton.clicked.connect(self.rate_for_win)
        self.form.lossButton.clicked.connect(self.rate_for_loss)
        self.form.drawButton.clicked.connect(self.rate_for_draw)


    def open(self, user_id):
        self.user_id = user_id
        self.windows.show()

    def rate_for_win(self):
        winning = rate_person_by_win(self.user_id)

        self.form.tableWidget.setRowCount(len(winning))
        for i, info_progress in enumerate(winning):
            self.form.tableWidget.setItem(i, 0, QTableWidgetItem(info_progress.user.FIO))


    def rate_for_loss(self):
        lossing = rate_person_by_loss(self.user_id)

        self.form.tableWidget.setRowCount(len(lossing))
        for i, info_progress in enumerate(lossing):
            self.form.tableWidget.setItem(i, 0, QTableWidgetItem(info_progress.user.FIO))



    def rate_for_draw(self):
        drawing = rate_person_by_loss(self.user_id)

        self.form.tableWidget.setRowCount(len(drawing))
        for i, info_progress in enumerate(drawing):
            self.form.tableWidget.setItem(i, 0, QTableWidgetItem(info_progress.user.FIO))

