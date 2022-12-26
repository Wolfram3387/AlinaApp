import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from designs import WelcomeWindow, InputPoints, VuzWindow  # Это наш конвертированный файл дизайна


LISTS = [VUZ for VUZ in open('VUZes.txt')]


class OneWindow(QtWidgets.QMainWindow, WelcomeWindow.Ui_Dialog):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле HelloWindow.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.setFixedSize(585, 530)
        self.twoWindow = None
        # Подключаем функции, которые будут обрабатывать нажатия на кнопки:
        self.pushButton.clicked.connect(self.btn_no_clicked)
        self.pushButton_2.clicked.connect(self.btn_yes_clicked)
        # self....clicked.connect(self.btn_done_clicked)

    # Прописываем функции, которые будут обрабатывать нажатия на кнопки:
    def btn_no_clicked(self):
        # Создаём окно и добавляем туда различные атрибуты
        my_window = QMessageBox()
        my_window.setText('Нет-нет, необходимо нажать на кнопку ДА')
        my_window.setDetailedText('Нажимая на кнопку "Да" вы принимаете лицензионное соглашение.')
        my_window.setIcon(QMessageBox.Information)
        my_window.setWindowTitle('Предупреждение')
        my_window.setStandardButtons(QMessageBox.Ok)
        my_window.exec_()

    def btn_yes_clicked(self):
        self.close()
        self.twoWindow = TwoWindow()
        self.twoWindow.show()
        # self.window2 = QtWidgets.QMainWindow()
        # self.ui = InputPoints.Ui_Dialog(self.window2)  # +++ self.window
        # self.ui.setupUi2(self.window2)
        # self.close()
        # self.window2.show()


class TwoWindow(QtWidgets.QMainWindow, InputPoints.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.oneWindow = None
        self.setupUi(self)
        self.pushButton_done.clicked.connect(self.btn_done_clicked)
        self.pushButton_back.clicked.connect(self.btn_back_clicked)

    def btn_back_clicked(self):
        self.close()
        self.oneWindow = OneWindow()
        self.oneWindow.show()

    def btn_done_clicked(self):
        # считываем данные с textedit
        try:
            mathematics = int(self.math.text())
            russian_language = int(self.russian.text())
            informatics = int(self.informatics.text())
            physics = int(self.fizika.text())
            additional = int(self.dopolnitelno.text())
            all_ = [mathematics, russian_language, informatics, physics]
        except:
            self.warning()
            return

        # показать warning, если данные некорректны
        is_correct = all(0 <= i <= 100 for i in all_) and 0 <= additional <= 10

        if not is_correct:
            self.warning()
            return

        self.close()
        self.threeWindow = ThreeWindow()

        # TODO Вносим в QListWidget данные о доступных ВУЗах
        self.threeWindow.listWidget.addItems(LISTS)
        self.threeWindow.listWidget.itemClicked.connect(self.selection_VUZ)
        self.threeWindow.show()
    
    def selection_VUZ(self, item):
        print(f"Вы кликнули: {item.text()}")
        if item.text() == "item2":
            print("Делайте что-нибудь.")

    def warning(self):
        # Создаём окно и добавляем туда различные атрибуты
        my_window = QMessageBox()
        my_window.setText('Введите реальные значения или 0')
        my_window.setDetailedText('Значения баллов за каждый предмет должны быть от 0 до 100. Дополнительные баллы от 0 до 10')
        my_window.setIcon(QMessageBox.Information)
        my_window.setWindowTitle('Предупреждение')
        my_window.setStandardButtons(QMessageBox.Ok)
        my_window.exec_()


class ThreeWindow(QtWidgets.QMainWindow, VuzWindow.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_back_clicked)

    def btn_back_clicked(self):
        self.close()
        self.twoWindow = TwoWindow()
        self.twoWindow.show()


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = OneWindow()  # Создаём объект класса
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()

# pyuic5 /Users/Wolfram_3387/Downloads/HelloWindowNew.ui -o /Users/Wolfram_3387/Downloads/AlinaApp/designs/WelcomeWindow.py
# pyuic5 /Users/Wolfram_3387/Downloads/InputPointsNew.ui -o /Users/Wolfram_3387/Downloads/AlinaApp/designs/InputPoints.py
# pyuic5 /Users/Wolfram_3387/Downloads/VuzWindow.ui -o /Users/Wolfram_3387/Downloads/AlinaApp/designs/VuzWindow.py
