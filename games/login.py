import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from PyQt6.QtWidgets import QMessageBox

from games.basewindow import BaseWindow
from games.database import check_user, check_registration, check_user_his_email

my_email = "ss3t9n@gmail.com"
my_password = "eaox txrj ftwn jxwy"

my_mail_ru = "ivan_ivanov_ivanovich1234@mail.ru"
password_for_mail_ru = "h1sLwMu2BqPwPGs4ZynU"
class Log(BaseWindow):
    def __init__(self, name, path):
        super().__init__(name, path)
        self.form.pushButton.clicked.connect(self.log_check)
        self.form.pushButton_3.clicked.connect(self.check_registration)
        self.form.forgotButton.clicked.connect(self.forgot_my_password)

    def check_registration(self):
        login = self.form.lineEdit.text()
        passport = self.form.lineEdit_2.text()
        check_registration(login, passport)

        dlg = QMessageBox(self.windows)
        dlg.setWindowTitle("Успешно")
        dlg.setText("Успешно")
        dlg.setStandardButtons(
            QMessageBox.StandardButton.Ok
        )
        dlg.setIcon(QMessageBox.Icon.Information)
        dlg.exec()

    def log_check(self):
        login = self.form.lineEdit.text()
        passport = self.form.lineEdit_2.text()

        res, user = check_user(login, passport)
        print(res)

        if res == True:
            BaseWindow.open_windows["menu"].open(user.id)
            self.close()
        else:
            dlg = QMessageBox(self.windows)
            dlg.setWindowTitle("Нужно зарегистророваться")
            dlg.setText("Неверный логин или пароль")
            dlg.setStandardButtons(
                QMessageBox.StandardButton.Ok
            )
            dlg.setIcon(QMessageBox.Icon.Information)
            dlg.exec()



    def forgot_my_password(self):
        self.new_code = random.randint(100_000, 999_999)
        login = self.form.lineEdit.text()
        current_user = check_user_his_email(login)
        if current_user is not None:
            message = MIMEMultipart()
            message["From"] = my_mail_ru
            message["To"] = login
            message["Subject"] = "Код для восстановления пароля"

            text = f"Код для восстановления пароля: {self.new_code} "
            mime = MIMEText(text, "plain")
            message.attach(mime)
            # server = smtplib.SMTP("smtp.gmail.com", 587)
            # server.close()
            with smtplib.SMTP("smtp.mail.ru", 587) as server:
                server.starttls()
                server.login(my_mail_ru, password_for_mail_ru)
                server.sendmail(my_mail_ru, login, message.as_string())
            print("Письмо успешно отправлено")

            self.open_windows["checker"].open(self.new_code, current_user)
            self.close()


