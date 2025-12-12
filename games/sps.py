import random
from PyQt6.QtWidgets import QApplication
from PyQt6 import uic

from games.basewindow import BaseWindow
from games.database import update_new_result, delete


class StonePaperScissors(BaseWindow):
    def __init__(self, name, path):
        super().__init__(name, path)
        self.form.pushStone.clicked.connect(self.on_stone_clicked)
        self.form.pushPaper.clicked.connect(self.on_paper_clicked)
        self.form.pushScissors.clicked.connect(self.on_scissors_clicked)
        self.form.deleteButton.clicked.connect(self.delete_my_progress)

        self.form.pushButton.clicked.connect(self.close_the_window)
        self.form.pushButton_2.clicked.connect(self.go_to_res)
        self.form.ratingButton.clicked.connect(self.go_to_rate)




    def go_to_rate(self):
        self.open_windows["rating"].open(self.user_id)
        self.close()

    def our_choices(self, my_choice):
        comp_choices = ["камень", "ножницы", "бумага"]
        computer_choice = random.choice(comp_choices)
        self.form.label.setText(f"Вы выбрали: {my_choice}. Компьютер выбрал: {computer_choice}")
        self.result(my_choice, computer_choice)

    def winner(self, my_choice, computer_choice):
        if my_choice == computer_choice:
            update_new_result(self.user_id, draw=1)
            return "Ничья!"

        elif my_choice == "камень" and computer_choice == "ножницы":
            update_new_result(self.user_id, wins = 1)
            return "Вы выиграли"
        elif my_choice == "ножницы" and computer_choice == "бумага":
            update_new_result(self.user_id, wins = 1)
            return "Вы выиграли"
        elif my_choice == "бумага" and computer_choice == "камень":
            update_new_result(self.user_id, wins=1)
            return "Вы выиграли"
        else:
            update_new_result(self.user_id, loss = 1)
            return "Вы проиграли"

    def result(self, my_choice, computer_choice):
        my_result = self.winner(my_choice, computer_choice)
        self.form.label_2.setText(f"Ваш результат: {my_result}")

    def on_stone_clicked(self):
        self.our_choices("камень")


    def on_paper_clicked(self):
        self.our_choices("бумага")


    def on_scissors_clicked(self):
        self.our_choices("ножницы")


    def close_the_window(self):
        self.open_windows["menu"].open(self.user_id)

        self.close()

    def delete_my_progress(self):
        delete(self.user_id)


    def go_to_res(self):
        self.open_windows["result"].open(self.user_id)
        self.close()

    def open(self, user_id):
        self.user_id = user_id
        self.windows.show()

    