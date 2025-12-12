from games.basewindow import BaseWindow

from games.database import select_my_result


class ShowTheResult(BaseWindow):
    def __init__(self, name, path):
        super().__init__(name, path)


        self.form.pushButton.clicked.connect(self.return_for_sps)

    def open(self, user_id):
        self.user_id = user_id

        res = select_my_result(user_id)
        if res is None:

            self.form.label.setText(f"Побед: {0}, Ничьи: {0}, Поражений: {0} ")

        else:
            self.form.label.setText(f"Побед: {res.wins}, Ничьи: {res.draw}, Поражений: {res.loss} ")

        self.windows.show()



    def return_for_sps(self):
        self.open_windows["game"].open(self.user_id)
        self.close()




