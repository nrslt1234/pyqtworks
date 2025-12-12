from PyQt6 import uic


class BaseWindow:
    open_windows = {}
    def __init__(self, name, path):
        self.name = name
        Form, Windows = uic.loadUiType(path)
        self.windows = Windows()
        self.form = Form()
        self.form.setupUi(self.windows)
        BaseWindow.open_windows[self.name] = self

    def open(self):
        self.windows.show()

    def close(self):
        self.windows.hide()



