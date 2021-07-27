import sys
from PyQt5 import QtWidgets
import UI.register.background
from UI.register.login import Login_Ui
from UI.register.robot import Robot_Ui
from UI.register.upload import Upload_Ui

from patient import Patient
from chatbot import ChatBot
from config import brain_path

if __name__ == "__main__":
    global patient
    patient = Patient()
    chat_bot = ChatBot(brain_path)

    app = QtWidgets.QApplication(sys.argv)
    Login_window = QtWidgets.QWidget()
    login_ui = Login_Ui(patient)
    login_ui.setupUi(Login_window)

    Robot_window = QtWidgets.QMainWindow()
    robot_ui = Robot_Ui(patient, chat_bot)
    robot_ui.setupUi(Robot_window)

    Upload_window = QtWidgets.QMainWindow()
    upload_ui = Upload_Ui(patient)
    upload_ui.setupUi(Upload_window)

    login_ui.chatbot_button.clicked.connect(Robot_window.show)
    robot_ui.upload_button.clicked.connect(Upload_window.show)

    Login_window.show()
    sys.exit(app.exec_())