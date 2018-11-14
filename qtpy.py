from PyQt5 import QtWidgets
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from datfile_convert_smpa import smart_life_data_process

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CHOOSE FILE")
        self.resize(300,300)
        self.dir = "."
        self.file_name = ""


        self.btn_choosefile = QPushButton(self)
        self.btn_choosefile.setObjectName("btn_choosefile")
        self.btn_choosefile.setText("Choose file")
        
        self.file_contents = QLineEdit()
        self.dir_contents = QLineEdit()

        self.btn_save_as = QPushButton(self)
        self.btn_save_as.setObjectName("btn_save_as")
        self.btn_save_as.setText("Save as")
        


        self.btn_file_convert = QPushButton(self)
        self.btn_file_convert.setObjectName("btn_file_convert")
        self.btn_file_convert.setText("Convert")

        layout = QVBoxLayout()
        layout.addWidget(self.btn_choosefile)
        
        layout.addWidget(self.file_contents)
        layout.addWidget(self.btn_save_as)
        layout.addWidget(self.dir_contents)
        layout.addWidget(self.btn_file_convert)
        self.setLayout(layout)

        self.btn_choosefile.clicked.connect(self.slot_choose_file)
        self.btn_save_as.clicked.connect(self.slot_save_as)
        self.btn_file_convert.clicked.connect(self.slot_convert)


    def slot_choose_file(self):

        self.file_name, filetype = QFileDialog.getOpenFileName(self,
                                    "Choose file",
                                    "D:\\Raw_data\\",
                                    "All Files (*);;Text Files ();;Python Files ()")
        self.file_contents.setText(self.file_name)

        
   
    def slot_save_as(self):

        self.dir = QFileDialog.getExistingDirectory(self, "Save as", "D:\\")
        self.dir_contents.setText(self.dir)

    def slot_convert(self):
        
        if ("ACC" in self.file_name) or ("DAILLY" in self.file_name) or ("ECG" in self.file_name):
            smart_life_data_process(self.file_name, self.dir) 
            reply = QMessageBox.about(self, "轉檔結果", "轉檔成功")
        else:
            reply = QMessageBox.about(self, "轉檔結果", "轉檔失敗, 檔名錯誤")

        

        


        
if __name__ == "__main__":  
    import sys  
  
    app = QtWidgets.QApplication(sys.argv)  
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())  

