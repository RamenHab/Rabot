import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QDialogButtonBox
from PyQt5.QtCore import QDateTime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Information Viewer")
        
        main_widget = QWidget()
        layout = QVBoxLayout()

        self.label_6 = QLabel("Author: ")
        self.label_7 = QLabel("Name: ")
        self.label_8 = QLabel("Extension: ")
        self.label_9 = QLabel("Creation Date: ")
        self.label_10 = QLabel("Last Modified Date: ")

        layout.addWidget(self.label_6)
        layout.addWidget(self.label_7)
        layout.addWidget(self.label_8)
        layout.addWidget(self.label_9)
        layout.addWidget(self.label_10)

        self.button_box = QDialogButtonBox(QDialogButtonBox.Open | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.open_file_dialog)
        self.button_box.rejected.connect(self.close)
        layout.addWidget(self.button_box)

        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

    def open_file_dialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*)", options=options)
        
        if file_name:
            self.update_labels(file_name)

    def update_labels(self, file_name):
        file_info = os.stat(file_name)
        
        base_name = os.path.basename(file_name)
        name, ext = os.path.splitext(base_name)
        
        creation_date = QDateTime.fromSecsSinceEpoch(int(file_info.st_ctime))
        modification_date = QDateTime.fromSecsSinceEpoch(int(file_info.st_mtime))
        
        author = "Unknown" 
        

        self.label_6.setText(f"Author: {author}")
        self.label_7.setText(f"Name: {name}")
        self.label_8.setText(f"Extension: {ext}")
        self.label_9.setText(f"Creation Date: {creation_date.toString('yyyy-MM-dd HH:mm:ss')}")
        self.label_10.setText(f"Last Modified Date: {modification_date.toString('yyyy-MM-dd HH:mm:ss')}")