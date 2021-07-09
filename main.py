from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import qrcode
import pathlib
from datetime import date, datetime

class Image(qrcode.image.base.BaseImage):
    def __init__(self, border, width, box_size):
        self.border = border
        self.width = width
        self.box_size = box_size
        size = (width + border * 2) * box_size
        self.image_file = QImage(size, size, QImage.Format_RGB16)
        self.image_file.fill(Qt.white)

    def pixmap(self):
        return QPixmap.fromImage(self.image_file)

    def drawrect(self, row, col):
        painter = QPainter(self.image_file)
        painter.fillRect(
			(col + self.border) * self.box_size,
			(row + self.border) * self.box_size,
			self.box_size, self.box_size,
			Qt.black)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel(self)
        self.lineEdit = QLineEdit(self)
        self.pushButton = QPushButton('Generate')

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)     
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.pushButton)   

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.creating_menubars()
        self.updating_ui()
        self.pushButton.clicked.connect(self.generate_qr_code)

    def updating_ui(self):
        self.lineEdit.setFont(QFont('Times', 13))
        self.lineEdit.setAlignment(Qt.AlignCenter)
        information = 'Enter a Text/URL...'
        self.lineEdit.setPlaceholderText(information)
        self.pushButton.setFont(QFont('Times', 13))

    def generate_qr_code(self):
        self.text = self.lineEdit.text()
        if self.text == '':
            self.error_message_box()
        else:
            qr_image = qrcode.make(self.text, image_factory=Image).pixmap()
            self.label.setPixmap(qr_image)
            self.label.setAlignment(Qt.AlignCenter)

    def creating_menubars(self):
        file_menu = self.menuBar().addMenu('&File')

        save_file_menu = QAction(QIcon('Images/Save.png'), 'Save...', self)
        save_file_menu.setStatusTip('Save')
        save_file_menu.setShortcut(QKeySequence.Save)
        save_file_menu.triggered.connect(self.save_qr_code)
        file_menu.addAction(save_file_menu)

        file_menu.addSeparator()

        quit_file_menu = QAction(QIcon('Images/Quit.png'), 'Quit...', self)
        quit_file_menu.setStatusTip('Quit')
        quit_file_menu.setShortcut(QKeySequence.Close)
        quit_file_menu.triggered.connect(self.quit_window)
        file_menu.addAction(quit_file_menu)

    def save_qr_code(self):
        text = self.lineEdit.text()
        if text == '':
            self.error_message_box()
        else:
            folder_name = 'QR Codes'
            today = date.today()
            date_stamp = today.strftime("%d-%m-%Y")
            now = datetime.now()
            time_stamp = now.strftime("%H-%M-%S")
            file_name = f'{time_stamp}_{date_stamp}.png'
            base_dir = pathlib.Path() / folder_name
            base_dir.mkdir(parents=True, exist_ok=True)
            save_path = f'{folder_name}\{file_name}'
            qr_code_image = qrcode.make(text)
            qr_code_image.save(save_path, scale=6)

    def error_message_box(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Proccessing Error!")
        msg.setWindowIcon(QIcon('Images/Logo.png'))
        msg.setText("Warning!")
        msg.setInformativeText("Text/URL Field is Empty")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

    def quit_window(self):
        exit(0)

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(192, 192, 192))
    palette.setColor(QPalette.WindowText, Qt.yellow)
    palette.setColor(QPalette.Base, QColor(255, 255, 0))
    palette.setColor(QPalette.AlternateBase, QColor(64, 128, 128))
    palette.setColor(QPalette.ToolTipBase, Qt.black)
    palette.setColor(QPalette.ToolTipText, Qt.darkMagenta)
    palette.setColor(QPalette.Text, Qt.black)
    palette.setColor(QPalette.Button, QColor(255, 128, 128))
    palette.setColor(QPalette.ButtonText, Qt.black)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)
    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

    main = MainWindow()
    main.setWindowTitle('QR Code Generator')
    main.setWindowIcon(QIcon('Images/Logo.png'))
    main.resize(300,300)
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()