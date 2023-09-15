import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QTextEdit, QPushButton, QLabel
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import Qt
from calculator import hesapla

class HesapMakinesi(QMainWindow):  #main class
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # GUI index
        self.setWindowTitle('Hesap Makinesi')
        self.setGeometry(100, 100, 500, 600)
        icon = QIcon('images/logo.png')
        self.setWindowIcon(icon)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Arka plan rengini ayarla (örneğin pembe)
        background_color = 'lightgrey'
        central_widget.setStyleSheet(f'background-color: {background_color};')

        # Layout oluştur
        main_layout = QVBoxLayout()
        button_layout = QGridLayout()  # 3x3 matris için QGridLayout kullanın


        
   

        # Girdi alanı (input area) oluştur
        self.input_area = QTextEdit(self)
        self.input_area.setReadOnly(True)  # Girdi alanını sadece okunabilir yap
        self.input_area.setFont(QFont("Arial", 14))  # Yazı tipi ve boyutu ayarlayın

        self.input_label = QLabel(self)
        self.input_label.setText('Input Data')
        self.input_label.setFont(QFont("Arial", 10, QFont.Bold))

        # Sonuç alanı (result area) oluştur
        self.result_area = QTextEdit(self)
        self.result_area.setReadOnly(True)  # Sonuç alanını sadece okunabilir yap
        self.result_area.setFont(QFont("Arial", 14))  # Yazı tipi ve boyutu ayarlayın

        self.result_label = QLabel(self)
        self.result_label.setText('Result Data')
        self.result_label.setFont(QFont("Arial", 10, QFont.Bold))

        # Log alanı (log area) oluştur
        self.log_area = QTextEdit(self)
        self.log_area.setReadOnly(True)
        self.log_area.setFont(QFont("Arial", 12))  # Yazı tipi ve boyutu ayarlayın
        self.log_area.setStyleSheet("background-color: black; color: white;")  # Arka plan ve metin rengini ayarlayın

        self.log_label = QLabel(self)
        self.log_label.setText('Pytest result section is below: ')
        self.log_label.setFont(QFont("Arial", 10,  QFont.Bold))
        
        # For button, button dictionary
        buttonlar = [
               '7', '8', '9',
               '4', '5', '6',
               '1', '2', '3',
               '0', 'C', '=', '+', '-', '*', '/'
          ]
        row, col = 0, 0
        for button in buttonlar:  #click the button and take text input 
            btn = QPushButton(button)
            btn.clicked.connect(self.on_button_clicked)
            btn.setFont(QFont("Arial", 12 , QFont.Bold))  # Düğme yazı tipi ve boyutu
            button_layout.addWidget(btn, row, col)
            col += 1
            if col > 2:
                col = 0
                row += 1
        #add main layout all the widgets
        main_layout.addWidget(self.input_label)
        main_layout.addWidget(self.input_area)
        main_layout.addLayout(button_layout)  # GridLayout'u ana layouta ekleyin
        main_layout.addWidget(self.result_label)
        main_layout.addWidget(self.result_area)
        main_layout.addWidget(self.log_label)
        main_layout.addWidget(self.log_area)  # Log alanını ana layouta ekleyin
        central_widget.setLayout(main_layout)

        self.clear() #call clear method

    def on_button_clicked(self):
        sender = self.sender()
        button_text = sender.text()

        if button_text == "=":
            try:
                expression = self.input_area.toPlainText()
                result = hesapla(expression)
                self.result_area.setPlainText(str(result))
                self.log_area.append(f"Input: {expression}, Result: {result}")  # Log alanına ekleyin
            except Exception as e:
                self.result_area.setPlainText("Hata")
        elif button_text == "C":
            self.clear()
        else:
            current_text = self.input_area.toPlainText()
            new_text = current_text + button_text
            self.input_area.setPlainText(new_text)

    def clear(self):   #temizleme function
        self.input_area.setPlainText("")
        self.result_area.setPlainText("")

def main():  #main function definition
    app = QApplication(sys.argv)
    hesap_makinesi = HesapMakinesi()
    hesap_makinesi.show()
    sys.exit(app.exec_())

if __name__ == '__main__':  #start the main
    main()
