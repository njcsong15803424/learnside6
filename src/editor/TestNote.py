
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from  vg_node import GraphNode
from vg_editor import VisualGraphEditor

import sys




if __name__=='__main__':
    app=QApplication(sys.argv)
    window=VisualGraphEditor()
    window.show()
    sys.exit(app.exec())
