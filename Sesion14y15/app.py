import PyQt5.QtWidgets as pyqt
from PyQt5 import uic
import sys

class Principal(pyqt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGUI()
    
    def initGUI(self):
        uic.loadUi('calculo.ui',self)
        #self.pushButton.clicked.connect(self.imprimir)
        self.show()

        self.boton_calcular.clicked.connect(lambda :
                                            self.operaciones
                                            (int(self.num1.text()),
                                             int(self.num2.text())))

    def operaciones(self,num1,num2):
        if self.suma.isChecked():
            txt=str(num1+num2)
        elif self.resta.isChecked():
            txt=str(num1-num2)
        elif self.producto.isChecked():
            txt=str(num1*num2)
        elif self.division.isChecked():
            txt=str(round((num1/num2),4))
        else:
            txt='Error'
        self.resultado.setText(txt)

   

def main():
    app = pyqt.QApplication([])
    window = Principal()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()