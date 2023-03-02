#coding:utf-8


from PySide6.QtWidgets import QWidget,QBoxLayout
from vg_view import  VisualGraphView
from vg_scene import  VisualGraphScene
from vg_node import GraphNode
from vg_node_port import  *
class VisualGraphEditor(QWidget):

    def __init__(self,parent=None):
        super().__init__(parent)
        self.setup_editor()


    def setup_editor(self):

        #窗口位置以及大小
        #self.setGeometry(50,50,1000,720)

        self.setWindowTitle('Visual Graph')

        self.layout=QBoxLayout(QBoxLayout.LeftToRight,self)
        self.layout.setContentsMargins(0,0,0,0)

        #初始化scene
        self.scene=VisualGraphScene()
        self.view=VisualGraphView(self.scene,self)
        self.layout.addWidget(self.view)

        self.debug_add_node()


        self.show()

    def debug_add_node(self):

        port=ExecPort()

        node=GraphNode(title="123")
        node.add_port(port)
        self.view.add_graph_node(node,[0,0])
