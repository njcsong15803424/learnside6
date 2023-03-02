#coding:utf-8

import sys
from PySide6.QtWidgets import *

from PySide6.QtWidgets import QApplication
from vg_editor import VisualGraphEditor
from vg_view import  QGraphicsView
from vg_node import GraphNode
from vg_node_port import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout=QVBoxLayout()
        self.setLayout(layout)
        self.resize(800,800)
        self.show()

        self.view=QGraphicsView()
        self.scene=QGraphicsScene()
        self.scene.setSceneRect(-15000,-15000,30000,30000)
        self.view.setScene(self.scene)
        layout.addWidget(self.view)

        node=GraphNode(title="哈哈")
        self.item=node


        port1=ExecInPort()
        node.add_port(port1)

        port2=ExecOutPort()
        node.add_port(port2)
        self.scene.addItem(self.item)




if __name__=="__main__":
    app=QApplication([])

    window=MainWindow()  #用这个窗体就能显示node
    #window=VisualGraphEditor() #用这个窗体无法显示node
    sys.exit(app.exec())
