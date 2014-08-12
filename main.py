from PyQt4 import QtCore, QtGui, QtSql
from PyQt4.QtSql import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sqlite3
import ctypes
import os, errno

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Database:
    def __init__(self, parent=None):
        self.db = None

    def connect(filename):
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(filename)
        self.db.open()
        if not self.db.open():
            MessageBox = ctypes.windll.user32.MessageBoxA
            MessageBox(None, 'Bukan File SQLite3 Database', 'Alert', 0)

class Model(QtSql.QSqlTableModel):
    def __init__(self, parent=None):
        super(Model, self).__init__(parent)
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable("sqlite_master")
        self.model.select()

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(591, 542)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.read_pushButton = QtGui.QPushButton(self.centralwidget)
        self.read_pushButton.setGeometry(QtCore.QRect(500, 180, 75, 23))
        self.read_pushButton.setObjectName(_fromUtf8("read_pushButton"))
        self.db_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.db_lineEdit.setGeometry(QtCore.QRect(90, 180, 301, 21))
        self.db_lineEdit.setObjectName(_fromUtf8("db_lineEdit"))
        self.db_label = QtGui.QLabel(self.centralwidget)
        self.db_label.setGeometry(QtCore.QRect(20, 180, 51, 16))
        self.db_label.setObjectName(_fromUtf8("db_label"))
        self.db_pushButton = QtGui.QPushButton(self.centralwidget)
        self.db_pushButton.setGeometry(QtCore.QRect(410, 180, 75, 23))
        self.db_pushButton.setObjectName(_fromUtf8("db_pushButton"))
        self.close_pushButton = QtGui.QPushButton(self.centralwidget)
        self.close_pushButton.setGeometry(QtCore.QRect(260, 500, 75, 23))
        self.close_pushButton.setObjectName(_fromUtf8("close_pushButton"))
        self.label_app = QtGui.QLabel(self.centralwidget)
        self.label_app.setGeometry(QtCore.QRect(70, 0, 341, 71))
        self.label_app.setObjectName(_fromUtf8("label_app"))
        self.label_sub = QtGui.QLabel(self.centralwidget)
        self.label_sub.setGeometry(QtCore.QRect(20, 70, 131, 21))
        self.label_sub.setObjectName(_fromUtf8("label_sub"))
        self.groupBox_OS = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_OS.setGeometry(QtCore.QRect(20, 100, 381, 41))
        self.groupBox_OS.setObjectName(_fromUtf8("groupBox_OS"))
        self.radioButton_box = QtGui.QRadioButton(self.groupBox_OS)
        self.radioButton_box.setGeometry(QtCore.QRect(10, 20, 71, 17))
        self.radioButton_box.setObjectName(_fromUtf8("radioButton_box"))
        self.radioButton_drop = QtGui.QRadioButton(self.groupBox_OS)
        self.radioButton_drop.setGeometry(QtCore.QRect(310, 20, 61, 17))
        self.radioButton_drop.setObjectName(_fromUtf8("radioButton_drop"))
        self.radioButton_4sha = QtGui.QRadioButton(self.groupBox_OS)
        self.radioButton_4sha.setGeometry(QtCore.QRect(240, 20, 61, 17))
        self.radioButton_4sha.setObjectName(_fromUtf8("radioButton_4sha"))
        self.radioButton_copy = QtGui.QRadioButton(self.groupBox_OS)
        self.radioButton_copy.setGeometry(QtCore.QRect(160, 20, 71, 17))
        self.radioButton_copy.setObjectName(_fromUtf8("radioButton_copy"))
        self.radioButton_gdrive = QtGui.QRadioButton(self.groupBox_OS)
        self.radioButton_gdrive.setGeometry(QtCore.QRect(90, 20, 61, 17))
        self.radioButton_gdrive.setObjectName(_fromUtf8("radioButton_gdrive"))
        self.lineEdit_loc = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_loc.setGeometry(QtCore.QRect(170, 150, 381, 21))
        self.lineEdit_loc.setText(_fromUtf8(""))
        self.lineEdit_loc.setObjectName(_fromUtf8("lineEdit_loc"))
        self.label_loc = QtGui.QLabel(self.centralwidget)
        self.label_loc.setGeometry(QtCore.QRect(20, 150, 131, 16))
        self.label_loc.setObjectName(_fromUtf8("label_loc"))
        self.logo_app = QtGui.QLabel(self.centralwidget)
        self.logo_app.setGeometry(QtCore.QRect(440, 10, 81, 81))
        self.logo_app.setText(_fromUtf8(""))
        self.logo_app.setPixmap(QtGui.QPixmap(_fromUtf8("../logo2.png")))
        self.logo_app.setObjectName(_fromUtf8("logo_app"))
        self.info_pushButton = QtGui.QPushButton(self.centralwidget)
        self.info_pushButton.setGeometry(QtCore.QRect(10, 500, 75, 23))
        self.info_pushButton.setObjectName(_fromUtf8("info_pushButton"))
        self.comboBox_tabel = QtGui.QComboBox(self.centralwidget)
        self.comboBox_tabel.setGeometry(QtCore.QRect(70, 220, 161, 22))
        self.comboBox_tabel.setObjectName(_fromUtf8("comboBox_tabel"))
        self.tableView_db = QtGui.QTableView(self.centralwidget)
        self.tableView_db.setGeometry(QtCore.QRect(10, 250, 571, 241))
        self.tableView_db.setObjectName(_fromUtf8("tableView_db"))
        self.label_tabel = QtGui.QLabel(self.centralwidget)
        self.label_tabel.setGeometry(QtCore.QRect(20, 220, 46, 13))
        self.label_tabel.setObjectName(_fromUtf8("label_tabel"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 591, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.db_label.setBuddy(self.db_lineEdit)
        self.label_loc.setBuddy(self.lineEdit_loc)
        self.label_tabel.setBuddy(self.comboBox_tabel)

        self.retranslateUi(MainWindow)
        self.radioButton_gdrive.toggled.connect(self.rb_gdrive_clicked)
        self.radioButton_copy.toggled.connect(self.rb_copy_clicked)
        self.radioButton_box.toggled.connect(self.rb_box_clicked)
        self.radioButton_4sha.toggled.connect(self.rb_4sha_clicked)
        self.radioButton_drop.toggled.connect(self.rb_drop_clicked)
        self.db_pushButton.clicked.connect(self.db_clicked)
        self.read_pushButton.clicked.connect(self.read_clicked)
        self.info_pushButton.clicked.connect(self.info_clicked)
        self.close_pushButton.clicked.connect(self.closeApp)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Main Application", None))
        self.read_pushButton.setText(_translate("MainWindow", "Read DB", None))
        self.db_label.setText(_translate("MainWindow", "Pilih file db", None))
        self.db_pushButton.setText(_translate("MainWindow", "Browse", None))
        self.close_pushButton.setText(_translate("MainWindow", "Close", None))
        self.label_app.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:44pt; color:#55aaff;\">OnStoFe app</span></p></body></html>", None))
        self.label_sub.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:13pt;\">Trace You Back!!</span></p></body></html>", None))
        self.groupBox_OS.setTitle(_translate("MainWindow", "Pilih Jenis Online Storage", None))
        self.radioButton_box.setText(_translate("MainWindow", "Box sync", None))
        self.radioButton_drop.setText(_translate("MainWindow", "Dropbox", None))
        self.radioButton_4sha.setText(_translate("MainWindow", "4shared", None))
        self.radioButton_copy.setText(_translate("MainWindow", "Copy.com", None))
        self.radioButton_gdrive.setText(_translate("MainWindow", "G Drive", None))
        self.label_loc.setText(_translate("MainWindow", "Info Lokasi Folder Instalasi", None))
        self.info_pushButton.setText(_translate("MainWindow", "Info", None))
        self.label_tabel.setText(_translate("MainWindow", "Tabel", None))

    def rb_gdrive_clicked(self, enabled):
        if enabled:            
            self.lineEdit_loc.setText('test')

    def rb_copy_clicked(self, enabled):
        if enabled:            
            self.lineEdit_loc.setText('test')

    def rb_box_clicked(self, enabled):
        if enabled:            
            self.lineEdit_loc.setText('test')

    def rb_4sha_clicked(self, enabled):
        if enabled:            
            self.lineEdit_loc.setText('')

    def rb_drop_clicked(self, enabled):
        if enabled:            
            self.lineEdit_loc.setText('tes')

    def db_clicked(self):
        filename = QtGui.QFileDialog.getOpenFileName(MainWindow, "Open File", '',
        'Database (*.db) \nAll File (*.*)', None, QtGui.QFileDialog.DontUseNativeDialog)
        self.db_lineEdit.setText(filename)

        #self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE") >>>>saya pernah mencoba menaruh script db disini
        #self.db.setDatabaseName(filename)
        #self.db.open()
        #if not self.db.open():
         #   MessageBox = ctypes.windll.user32.MessageBoxA
          #  MessageBox(None, 'Bukan File SQLite3 Database', 'Alert', 0)

    def read_clicked(self):
        self.db = Database()
        self.model = Model(self)
        combo = self.comboBox_tabel
        combo.setModel(self.model)
        combo.setModelColumn(self.model.fieldIndex("name"))

        projectView = self.tableView_db
        projectView.setModel(self.model)
        projectView.show()


    def info_clicked(self):
        MessageBox = ctypes.windll.user32.MessageBoxA
        MessageBox(None, 'test', 'Author Message', 0)

    def closeApp(self):
        result = QtGui.QMessageBox.question(self, 'Alert',
            "Keluar Dari Aplikasi?",
            QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if result == QtGui.QMessageBox.Yes:
            MainWindow.close()
        else:
            pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())