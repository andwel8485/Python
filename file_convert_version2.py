import sys
from PyQt5.QtWidgets import*
from file_convert import*
from datfile_convert_smpa import smart_life_data_process


class FileConvert(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)


    def file_choose(self):
        self.file_name, _ = QFileDialog.getOpenFileName(self,
                            "CHOOSE FILE", 
                            "D:\\Raw_data\\", 
                            "All Files (*);;Text Files ();;Python Files ()")
        self.lineEdit_2.setText(self.file_name)

    def file_save(self):
        self.dir = QFileDialog.getExistingDirectory(self, "SAVE AS", "D:\\")
        self.lineEdit_3.setText(self.dir)

    def file_convert(self):
        if ("ACC" in self.file_name) or ("DAILY" in self.file_name) or ("ECG" in self.file_name):
            smart_life_data_process(self.file_name, self.dir) 
            reply = QMessageBox.about(self, "轉檔結果", "轉檔成功")
        else:
            reply = QMessageBox.about(self, "轉檔結果", "轉檔失敗, 檔名錯誤")
        




    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myui = FileConvert()
    myui.show()
    sys.exit(app.exec_())