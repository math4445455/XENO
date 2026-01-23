import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtGui import QIcon
from PySide6.QtCore import QUrl

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
HTML_PATH = os.path.join(BASE_DIR, "publish", "index.html")
ICON_PATH = os.path.join(BASE_DIR, "publish", "icon.png")

app = QApplication(sys.argv)
app.setApplicationName("XENO")
app.setWindowIcon(QIcon(ICON_PATH))

view = QWebEngineView()
view.setWindowTitle("XENO")
view.setWindowIcon(QIcon(ICON_PATH))
view.resize(1100, 700)

view.load(QUrl.fromLocalFile(HTML_PATH))
view.show()

sys.exit(app.exec())