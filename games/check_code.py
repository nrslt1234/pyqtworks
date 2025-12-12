from games.basewindow import BaseWindow



class Checker(BaseWindow):
    def __init__(self, name, path):
        super().__init__(name, path)

        self.form.pushButton.clicked.connect(self.checker)

    def open(self, code, current_user):
        self.code = code
        self.current_user = current_user
        self.windows.show()
    def checker(self):
        code = self.form.lineEdit.text()

        if code == str(self.code):
            self.open_windows["menu"].open(self.current_user.id)
            self.close()
