#coding:utf-8


from PySide6.QtWidgets import QGraphicsItem,QGraphicsTextItem
from PySide6.QtCore import QRect,Qt,QRectF
from PySide6.QtGui import QPainter,QPen,QColor,QBrush,QPainterPath,QFont
from vg_config import EditorConfig
from vg_node_port import NodePort

class GraphNode(QGraphicsItem):
    def __init__(self,title='',scene=None,parent=None):
        super().__init__(parent)

        self._scene=scene

        #定义node的大小
        self._node_width=240
        self._node_height=160
        self._node_radius=10

        #node的边框
        self._pen_default=QPen(QColor('#ffee00'))
        self._pen_selected=QPen(QColor('#aaffee00')) #前2位代表不透明度，后6位代表颜色

        #noder 的背景
        self._brush_background=QBrush(QColor('#aa151515'))

        self.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)

        #节点的
        self._title=title
        self._title_height=25
        self._title_font=QFont('Arial',13)
        self._title_color=Qt.white
        self._title_padding=3
        self._brush_title_back=QBrush(QColor('#aa00003f'))

        self.init_title()

        #port
        self._port_padding=10

    def init_title(self):
        self._title_item=QGraphicsTextItem(self)
        self._title_item.setPlainText(self._title)
        self._title_item.setFont(self._title_font)
        self._title_item.setDefaultTextColor(self._title_color)
        self._title_item.setPos(self._title_padding,self._title_padding)

    def boundingRect(self)->QRectF:
        return QRectF(0,0,self._node_width,self._node_height)

    def paint(self,painter:QPainter,option,wdiget):
        #画背景颜色
        node_outline=QPainterPath()
        node_outline.addRoundedRect(0,0,self._node_width,self._node_height,self._node_radius,self._node_radius)

        painter.setPen(Qt.NoPen)
        painter.setBrush(self._brush_background)
        painter.drawPath(node_outline.simplified())


        #画title的背景颜色
        title_outline=QPainterPath()
        title_outline.setFillRule(Qt.WindingFill)
        title_outline.addRoundedRect(0,0,self._node_width,
                                     self._title_height,self._node_radius
                                     ,self._node_radius)

        title_outline.addRect(0,
                              self._title_height-self._node_radius,
                              self._node_radius,
                              self._node_radius)

        title_outline.addRect(self._node_width - self._node_radius,
                              self._title_height-self._node_radius,
                              self._node_radius,
                              self._node_radius
                              )

        painter.setPen(Qt.NoPen)
        painter.setBrush(self._brush_title_back)
        painter.drawPath(title_outline.simplified())

        if not self.isSelected():
            painter.setPen(self._pen_default)
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(node_outline)
        else:
            painter.setPen(self._pen_selected)
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(node_outline)


    def add_port(self,port):
        if port._port_type == NodePort.PORT_TYPE_EXEC_IN:
            self.add_exec_in_port(port)

        elif port._port_type == NodePort.PORT_TYPE_EXEC_OUT:
            self.add_exec_out_port(port)

    def add_exec_in_port(self,port:NodePort):
        port.add_to_parent_node(self,self._scene)
        port.setPos(self._port_padding,self._title_height)


    def add_exec_out_port(self,port:NodePort):
        port.add_to_parent_node(self,self._scene)
        port.setPos(self._node_width+0.5*port._port_icon_size-port._port_width-self._port_padding,self._title_height)



