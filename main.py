import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from designs import WelcomeWindow, InputPoints, VuzWindow, ProfessionsWindow, FinalScoreWindow
from find_my_vuzes import find_my_VUZes


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
    @staticmethod
    def btn_no_clicked():
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
        self.fourWindow = FourWindow()
        self.fourWindow.show()
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
        self.fourWindow = FourWindow()
        self.fourWindow.show()

    def btn_done_clicked(self):
        # считываем данные с textedit
        try:
            mathematics = int(self.math.text())
            russian_language = int(self.russian.text())
            informatics = int(self.informatics.text())
            physics = int(self.fizika.text())
            additional = int(self.dopolnitelno.text())
            all_ = [mathematics, russian_language, informatics, physics]
            profession = open('_profession_.txt').read()
            self.summa = mathematics + russian_language + physics + informatics + additional
            passed_disciplines = []   # [+ + - +]
            for d in [russian_language, mathematics, physics, informatics]:
                if d != 0:
                    passed_disciplines.append('+')
                else:
                    passed_disciplines.append('-')

            # Получаем ВУЗы, в которые можно пройти
            VUZes = find_my_VUZes(profession, passed_disciplines, self.summa)

            if mathematics < 27 or russian_language < 36 or informatics != 0 and informatics < 40 or physics != 0 and physics < 36:
                self.warning_1()
                return
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

        # Вносим в QListWidget данные о доступных ВУЗах
        with open('VUZes.txt', 'w') as file:
            for key in VUZes:
                file.write(' | '.join([str(v) for v in VUZes[key].values()]))
                file.write('\n')

        vuzes = [line.split(' | ')[1] for line in open('VUZes.txt')]

        self.threeWindow.listWidget.addItems(vuzes)
        self.threeWindow.listWidget.itemClicked.connect(self.selection_VUZ)
        self.threeWindow.show()
    
    def selection_VUZ(self, item):
        vuz = item.text()
        for line in open('VUZes.txt'):
            line = line.split(' | ')
            if line[1] == vuz:
                direction = line[2]
                score = line[-2]
                link = line[-1]
                chances = self.get_chances(int(score), self.summa)
                break
        self.fiveWindow = FiveWindow()
        self.fiveWindow.textEdit_Vuz.setText(vuz)
        self.fiveWindow.textEdit_Score.setText(score)
        self.fiveWindow.textEdit_Direction.setText(direction)
        self.fiveWindow.textEdit_Site.setText(link)
        self.fiveWindow.textEdit_Chances.setText(chances)
        self.fiveWindow.show()

    @staticmethod
    def warning():
        # Создаём окно и добавляем туда различные атрибуты
        my_window = QMessageBox()
        my_window.setText('Введите реальные значения или 0')
        my_window.setDetailedText('Значения баллов за каждый предмет должны быть от 0 до 100. Дополнительные баллы от 0 до 10')
        my_window.setIcon(QMessageBox.Information)
        my_window.setWindowTitle('Предупреждение')
        my_window.setStandardButtons(QMessageBox.Ok)
        my_window.exec_()

    @staticmethod
    def warning_1(self):
        # TODO переделать
        # Создаём окно и добавляем туда различные атрибуты
        my_window = QMessageBox()
        my_window.setText('Введите реальные значения или 0')
        my_window.setDetailedText('Значения баллов за каждый предмет должны быть от 0 до 100. Дополнительные баллы от 0 до 10')
        my_window.setIcon(QMessageBox.Information)
        my_window.setWindowTitle('Предупреждение')
        my_window.setStandardButtons(QMessageBox.Ok)
        my_window.exec_()

    @staticmethod
    def get_chances(last_year_score, student_score):
        percents = round((student_score - last_year_score) / 30, 1) * 100 + 12
        if percents > 99:
            percents = 99
        return f'{percents}%'


class ThreeWindow(QtWidgets.QMainWindow, VuzWindow.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_back_clicked)

    def btn_back_clicked(self):
        self.close()
        self.twoWindow = TwoWindow()
        self.twoWindow.show()


class FourWindow(QtWidgets.QMainWindow, ProfessionsWindow.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Back.clicked.connect(self.btn_back_clicked)
        self.Astronaut.clicked.connect(lambda ch, btn=self.Astronaut: self.pressed_btn(btn))
        self.Astronomer.clicked.connect(lambda ch, btn=self.Astronomer: self.pressed_btn(btn))
        self.Communication_engineer.clicked.connect(lambda ch, btn=self.Communication_engineer: self.pressed_btn(btn))
        self.Space_balistics.clicked.connect(lambda ch, btn=self.Space_balistics: self.pressed_btn(btn))
        self.Robotics_engineer.clicked.connect(lambda ch, btn=self.Robotics_engineer: self.pressed_btn(btn))
        self.Engineer_constructor.clicked.connect(lambda ch, btn=self.Engineer_constructor: self.pressed_btn(btn))
        self.Programmer_engineer.clicked.connect(lambda ch, btn=self.Programmer_engineer: self.pressed_btn(btn))

    def btn_back_clicked(self):
        self.close()
        self.oneWindow = OneWindow()
        self.oneWindow.show()

    def pressed_btn(self, btn):
        self.close()
        file = open('_profession_.txt', 'w')
        file.write(btn.text())
        self.twoWindow = TwoWindow()
        self.twoWindow.show()


class FiveWindow(QtWidgets.QMainWindow, FinalScoreWindow.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


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
# pyuic5 /Users/Wolfram_3387/Downloads/ProfessionsWindow.ui -o /Users/Wolfram_3387/Downloads/ProfessionsWindow.py
# pyuic5 /Users/Wolfram_3387/Downloads/FinalScoreWindow.ui -o /Users/Wolfram_3387/Downloads/FinalScoreWindow.py
