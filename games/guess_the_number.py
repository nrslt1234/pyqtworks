import random
from PyQt6 import uic

from games.basewindow import BaseWindow
from games.database import add_history_from_guess_the_number, select_add_history_from_guess_the_number


class Game_guess_the_number(BaseWindow):
    def __init__(self, name, path):
        super().__init__(name, path)
        self.form.pushButton.clicked.connect(self.find_his_num)
        self.comp_choice_numb = random.randint(0, 1000)

        self.form.pushButton_2.clicked.connect(self.close_the_window)

        self.form.historyButton.clicked.connect(self.open_the_history)

    def find_his_num(self):
        person_answer = int(self.form.lineEdit.text())
        add_history_from_guess_the_number(self.user_id, self.comp_choice_numb, person_answer)

        if person_answer == self.comp_choice_numb:
            self.form.label.setText("Поздравляю! Вы угадали, вы выиграли!")
        elif person_answer < self.comp_choice_numb:
            self.form.label.setText("Нет, мое число больше. Попробую еще!")
        else:
            self.form.label.setText("Ошибочка, мое число меньше")






    def open_the_history(self):
        self.open_windows["history"].open(self.user_id)
        self.close()


    def open(self, user_id):
        self.user_id = user_id
        self.windows.show()

    def close_the_window(self):
        self.open_windows["menu"].open(self.user_id)
        self.close()
