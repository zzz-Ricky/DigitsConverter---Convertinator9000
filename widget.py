import sys
from PySide6.QtWidgets import QApplication, QWidget
from ui_form import Ui_Widget
from Converterz import*

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Connect buttons to functions
        self.ui.pushButton.clicked.connect(self.button1_clicked)
        self.ui.Input1.returnPressed.connect(self.Input1_returned)

    def update_line_edit(self,bintext,octtext,hextext,graytext):
        self.ui.binout.setText(bintext)
        self.ui.octout.setText(octtext)
        self.ui.hexout.setText(hextext)
        self.ui.grayout.setText(graytext)


    def button1_clicked(self):
        binary = []
        octal=[]
        hexa = []
        gray = []
        Decimal = self.ui.Input1.text()
        if (Decimal.lstrip("-")).isnumeric() != 1:
            self.update_line_edit("error (NaN)","error (NaN)","error (NaN)","error (NaN)")
        else:
            if int(Decimal) < 0:
                self.update_line_edit("error (Negative)","error (Negative)","error (Negative)","error (Negative)")
            else:
                x = int(Decimal)
                bintext = reverser(convertbinary(x,binary))
                octtext = reverser(convertoctal(x,octal))
                hextext = reverser(converthexa(x,hexa))
                graytext = stringer(convertgray(x,binary,gray))
                # graytext = 'work in progress'
                self.update_line_edit(str(bintext),str(octtext),str(hextext),str(graytext))

    def Input1_returned(self):
        self.button1_clicked()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("breeze")  # Set the Breeze style
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
