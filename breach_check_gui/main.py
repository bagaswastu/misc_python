from checker import ScrapeException, Breach
import utils
import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QPushButton,
    QMessageBox,
    QDialog,
)
import checker
import logging


class BreachDetailDialog(QDialog):
    def __init__(self, breach: Breach):
        super().__init__()

        self.setWindowTitle(f"Breach Detail for {breach.name}")

        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"Name\t\t: {breach.name}"))
        layout.addWidget(QLabel(f"Title\t\t: {breach.title}"))
        layout.addWidget(QLabel(f"Domain\t\t: {breach.domain}"))
        layout.addWidget(QLabel(f"Date\t\t: {breach.date}"))
        layout.addWidget(QLabel(f"Breach total\t: {breach.pwn_count}"))

        formatted_breached_data = "\n- ".join(breach.breached_data)
        layout.addWidget(QLabel(f"Breached data\t:\n- {formatted_breached_data}"))

        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Breach Checker")
        self.list_breach: list[Breach] = []

        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("Email"))

        self.email_input_widget = QLineEdit()
        input_layout.addWidget(self.email_input_widget)

        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)

        send_button = QPushButton(text="Check")
        send_button.clicked.connect(self.check_on_click)

        main_layout.addWidget(send_button)

        result_layout = QHBoxLayout()
        main_layout.addLayout(result_layout)
        self.list_breach_widget = QListWidget()
        self.list_breach_widget.itemClicked.connect(self.clicked_breach_item)
        result_layout.addWidget(self.list_breach_widget)

        self.state_label = QLabel("Status: Ready")
        main_layout.addWidget(self.state_label)

        self.widget = QWidget()
        self.widget.setLayout(main_layout)
        self.setCentralWidget(self.widget)

    def clicked_breach_item(self, item) -> None:
        """
        Function that run when user clcik the item from list breach widget.
        """
        clicked_breach: Breach = [
            breach for breach in self.list_breach if breach.name == item.text()
        ][0]
        BreachDetailDialog(breach=clicked_breach).exec()

    def clear_breach_list(self) -> None:
        self.list_breach_widget.clear()

    def check_on_click(self) -> None:
        """
        Function that run when user click "Check" button.
        """
        email = self.email_input_widget.text()

        # If email is not valid, then show error message box.
        if not utils.is_email_valid(email):
            QMessageBox.information(self.widget, "Information", "Email is not valid.")
            return

        try:
            self.state_label.setText("Status: Loading...")
            self.list_breach = checker.check_breach(email=email)
            list_breach_name = [breach.name for breach in self.list_breach]
            self.list_breach_widget.addItems(list_breach_name)

        except ScrapeException as e:
            QMessageBox.critical(self.widget, "Error", e.message)
            logging.error(e.message)
        except Exception as e:
            QMessageBox.critical(self.widget, "Error", "Unknown error has ben occurred")
            logging.exception(e)
        finally:
            self.state_label.setText("Status: Ready")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
