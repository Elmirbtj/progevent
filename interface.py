import sys
from PyQt5.QtWidgets import QApplication, QWidget , QGridLayout , QLabel , QLineEdit , QPushButton , QMainWindow
from PyQt5.QtCore import QCoreApplication

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.resize(325,200)
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        self.__lab = QLabel("Saisir votre nom")
        self.__text = QLineEdit("")
        self.__ok = QPushButton("Ok")
        self.__quit = QPushButton("Quitter")
        self.__labNom = QLabel(f'{str(self.__text.text())}')
        # Ajouter les composants au grid ayout
        grid.addWidget(self.__lab, 0, 0)
        grid.addWidget(self.__text, 1, 0)
        grid.addWidget(self.__ok, 2, 0)
        grid.addWidget(self.__quit, 4, 0)
        grid.addWidget(self.__labNom,3 ,0)


        self.__ok.clicked.connect(self.__actionOk)
        self.__quit.clicked.connect(self.__actionQuitter)
        self.setWindowTitle("Exercice-1")


    def __actionOk(self):
        return self.__labNom.setText(f'Bonjour {self.__text.text()}')



    def __actionQuitter(self):
        QCoreApplication.exit(0)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()