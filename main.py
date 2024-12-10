from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt6 Multi-Platform App")
        self.setGeometry(100, 100, 300, 200)

        self.label = QLabel("Hello, PyQt6!")
        self.button = QPushButton("Click Me")
        self.button.clicked.connect(self.change_text)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def change_text(self):
        self.label.setText("You clicked the button!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
