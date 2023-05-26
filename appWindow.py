import random
from PyQt5 import QtWidgets, QtGui, QtCore
import subprocess
import time
from PyQt5.QtWidgets import QMessageBox

class GradientProgressBar(QtWidgets.QProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimum(0)
        self.setMaximum(100)
        self.setTextVisible(True)
        self.color1 = None
        self.color2 = None
        self.color3 = None

    def generate_random_colors(self):
        self.color1 = QtGui.QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.color2 = QtGui.QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.color3 = QtGui.QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def paintEvent(self, event):
        painter = QtWidgets.QStylePainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)

        if self.color1 is None or self.color2 is None or self.color3 is None:
            self.generate_random_colors()

        # Create the gradient colors
        gradient = QtGui.QLinearGradient(QtCore.QPointF(0, 0), QtCore.QPointF(self.width(), 0))
        gradient.setColorAt(0, self.color1)
        gradient.setColorAt(0.5, self.color2)
        gradient.setColorAt(1, self.color3)

        # Set the gradient as the background
        painter.setBrush(QtGui.QBrush(gradient))

        # Calculate the progress rect
        progress_rect = QtCore.QRectF(0, 0, self.width() * (self.value() / self.maximum()), self.height())

        # Draw the progress bar
        painter.drawRoundedRect(progress_rect, 5, 5)

        # Draw the text
        painter.drawText(QtCore.QRectF(0, 0, self.width(), self.height()), QtCore.Qt.AlignCenter, self.text())

class InstallerWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.installation_complete = False

    def initUI(self):
        # Create the install button
        self.install_button = QtWidgets.QPushButton("Install")
        self.install_button.clicked.connect(self.run_silent_install)

        # Create the progress bar
        self.progress_bar = GradientProgressBar()

        # Create the progress label
        self.progress_label = QtWidgets.QLabel("Install Progress")

        # Create the additional text label
        self.additional_label = QtWidgets.QLabel("")

        # Set the font size for the buttons and labels
        font = QtGui.QFont()
        font.setPointSize(12)  # Set the desired font size
        self.install_button.setFont(font)
        self.progress_label.setFont(font)
        self.additional_label.setFont(font)

        # Create a vertical layout for the progress bar, labels, and button
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.progress_label)
        layout.addWidget(self.additional_label)
        layout.addWidget(self.install_button)

        # Set the layout for the window
        self.setLayout(layout)

        self.setWindowTitle("Silent Installer")

    def run_silent_install(self):
        if self.installation_complete:
            return

        # Path to the installer executable
        installer_path = r"C:\kidztownfiles\repairfiles\DLS8Setup.8.5.1.exe"

        # Execute the installer with silent parameters
        process = subprocess.Popen([installer_path, "/S"])

        # Update the progress bar as the installation progresses
        while process.poll() is None:
            self.progress_bar.setValue(self.progress_bar.value() + 1)
            QtCore.QCoreApplication.processEvents()
            time.sleep(0.1)

            if self.progress_bar.value() == 100:
                self.additional_label.setText("Verifying Install")
                QtCore.QTimer.singleShot(2000, self.update_additional_label)

        # Check the exit code of the process
        if process.returncode == 0:
            self.installation_complete = True
            self.show_installation_complete_message()
        else:
            QMessageBox.critical(self, "Installation Error", "An error occurred during the silent installation.")

    def update_additional_label(self):
        sayings = [
            "Checking Version",
            "Saying a Prayer it works",
            "Go get a coffee",
            "Checking System Requirements",
            "A few more moments"
        ]

        if not self.installation_complete:
            saying = random.choice(sayings)
            self.additional_label.setText(saying)
            QtCore.QTimer.singleShot(2000, self.update_additional_label)

    def show_installation_complete_message(self):
        QMessageBox.information(self, "Installation Complete", "Silent installation completed successfully!")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = InstallerWindow()
    window.show()
    app.exec_()


'''
from PyQt5 import QtWidgets, QtGui, QtCore
import subprocess
import time
from PyQt5.QtWidgets import QMessageBox

class InstallerWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create the install button
        self.install_button = QtWidgets.QPushButton("Install")
        self.install_button.clicked.connect(self.run_silent_install)

        # Create the progress bar
        self.progress_bar = QtWidgets.QProgressBar()
        self.progress_bar.setTextVisible(False)

        # Create the progress label
        self.progress_label = QtWidgets.QLabel("Installation Progress")

        # Set the font size for the buttons and label
        font = QtGui.QFont()
        font.setPointSize(16)  # Set the desired font size
        self.install_button.setFont(font)
        self.progress_label.setFont(font)

        # Create a vertical layout and add the elements
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.install_button)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.progress_label)

        # Set the layout for the window
        self.setLayout(layout)

        self.setWindowTitle("Silent Installer")

    def run_silent_install(self):
        # Path to the installer executable
        installer_path = r"C:\kidztownfiles\repairfiles\DLS8Setup.8.5.1.exe"

        # Execute the installer with silent parameters
        process = subprocess.Popen([installer_path, "/S"])

        # Update the progress bar as the installation progresses
        while process.poll() is None:
            self.progress_bar.setValue(self.progress_bar.value() + 1)
            QtCore.QCoreApplication.processEvents()
            time.sleep(0.1)

        # Check the exit code of the process
        if process.returncode == 0:
            QMessageBox.information(self, "Installation Complete", "Silent installation completed successfully!")
        else:
            QMessageBox.critical(self, "Installation Error", "An error occurred during the silent installation.")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = InstallerWindow()
    window.show()
    app.exec_()
'''


'''
from tkinter import *
import tkinter as tk
from tkinter import ttk
import subprocess
import time
from tkinter import messagebox
import ctypes
# conda activate ktvenv
 #ALT + SHIFT + A for multi - line comment

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_silent_install():
    installer_path = r"C:\kidztownfiles\repairfiles\DLS8Setup.8.5.1.exe"
    if is_admin():
        try:
            subprocess.run([installer_path, "/S"], check=True)
            messagebox.showinfo("Installation Complete", "Silent installation completed successfully!")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Installation Error", f"An error occurred during the silent installation:\n{e}")
    else:
        messagebox.showerror("Administrator Privileges Required", "This operation requires administrator privileges.")

root = tk.Tk()
root.geometry("200x100")
root.title("Silent Installer")

install_button = tk.Button(root, text="Install", command=run_silent_install)
install_button.pack(pady=10)
        
root.mainloop()

'''