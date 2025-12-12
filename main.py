import random
from PyQt6.QtWidgets import QApplication
from PyQt6 import uic
Form, Windows = uic.loadUiType('untitled.ui')
win = QApplication([])
windows = Windows()
form = Form()
form.setupUi(windows)



# cnt = 0
# def clicker():
#     global cnt
#     cnt +=1
#     form.button_click.setText(f"{cnt}")
#     form.label.setText(f"{cnt}")
#
# form.button_click.clicked.connect(clicker)
#
# def exit():
#     global cnt
#     cnt = 0
#     form.button_click.setText(f"{cnt}")
# form.exitbutton.clicked.connect(exit)



# def F():
#     while True:
#         if form.pushStone.clicked() or form.pushPaper.clicked() or form.push.scissors.clicked():
#             computer_random_number = random.randint(1, 3)
#             if computer_random_number == 1 and form.pushStone.clicked():
#                 form.label.setText("У вас ничья!")
#             elif computer_random_number == 2 and form.pushStone.clicked():
#                 form.label.setText("Вы победили!")
#             elif computer_random_number == 3 and form.pushStone.clicked():
#                 form.label.setText("Вы проиграли!")
#
#
#             if computer_random_number == 1 and form.pushPaper.clicked():
#                 form.label.setText("Вы выиграли")
#             elif computer_random_number == 2 and form.pushPaper.clicked():
#                 form.label.setText("У вас ничья")
#             elif computer_random_number == 3 and form.pushPaper.clicked():
#                 form.label.setText("Вы проиграли!")
#
#
#             if computer_random_number == 1 and form.pushScissors.clicked():
#                 form.label.setText("Вы проиграли")
#             elif computer_random_number == 2 and form.pushScissors.clicked():
#                 form.label.setText("Вы выиграли")
#             elif computer_random_number == 3 and form.pushScissors.clicked():
#                 form.label.setText("У вас ничья")





import random
from PyQt6.QtWidgets import QApplication
from PyQt6 import uic
Form, Windows = uic.loadUiType('untitled.ui')
app = QApplication([])
windows = Windows()
form = Form()
form.setupUi(windows)




def our_choices(my_choice):
    comp_choices = ["камень", "ножницы", "бумага"]
    computer_choice = random.choice(comp_choices)
    form.label.setText(f"Вы выбрали: {my_choice}. Компьютер выбрал: {computer_choice}")
    result(my_choice, computer_choice)
def winner(my_choice, computer_choice):
    if my_choice == computer_choice:
        return "Ничья!"
    elif my_choice == "камень" and computer_choice == "ножницы":
        return "Вы выиграли"
    elif my_choice == "ножницы" and computer_choice == "бумага":
        return "Вы выиграли"
    elif my_choice == "бумага" and computer_choice == "камень":
        return "Вы выиграли"
    else:
        return "Вы проиграли"


def result(my_choice, computer_choice):
    my_result = winner(my_choice, computer_choice)
    form.label_2.setText(f"Ваш результат: {my_result}")

def on_stone_clicked():
    our_choices("камень")
form.pushStone.clicked.connect(on_stone_clicked)
def on_paper_clicked():
    our_choices("бумага")
form.pushPaper.clicked.connect(on_paper_clicked)
def on_scissors_clicked():
    our_choices("ножницы")
form.pushScissors.clicked.connect(on_scissors_clicked)


windows.show()
app.exec()


