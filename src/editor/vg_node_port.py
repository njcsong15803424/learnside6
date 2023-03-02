#coding:utf-8
from PySide6.QtCore import QPointF
from PySide6.QtGui import QPolygonF
from PySide6.QtWidgets import QGraphicsItem,QGraphicsTextItem
from PySide6.QtCore import QRect,Qt,QRectF
from PySide6.QtGui import QPainter,QPen,QColor,QBrush,QPainterPath,QFont
from vg_config import EditorConfig


class NodePort(QGraphicsItem):
    PORT_TYPE_EXEC_IN = 1001
    PORT_TYPE_EXEC_OUT = 1002
    PORT_TYPE_PARAM = 1003
    PORT_TYPE_OUTPUT = 1004

    def __init__(self,port_lable='',port_class='str',port_color='#ffffff' ,port_type=PORT_TYPE_EXEC_IN,parent=None):
        super().__init__(parent)

        self._port_lable = port_lable
        self._port_class = port_class
        self._port_color = port_color
        self._port_type = port_type

        self._pen_default=QPen(QColor(self._port_color))
        self._pen_default.setWidthF(1.5)
        self._brush_default=QPen(QColor(self._port_color))
        self._font_size=12
        self._port_font=QFont('Consols',self._font_size)

        self._port_icon_size=20
        self._port_lable_size=len(self._port_lable)*self._font_size
        self._port_width=self._port_icon_size+self._port_lable_size

    def boundingRect(self) -> QRectF:
        return QRectF(0,0,self._port_width,self._port_icon_size)

    #将本节点添加到parent node上
    def add_to_parent_node(self,parent_node,scene):
        self.setParentItem(parent_node)
        self._parent_node=parent_node
        self._scene=scene




class ExecPort(NodePort):
    def __init__(self,port_lable='',port_class='str',port_color='#ffffff' ,port_type=NodePort.PORT_TYPE_EXEC_IN,parent=None):
        super().__init__(port_lable,port_class,port_color,port_type,parent)

    def paint(self,painter:QPainter,option,widget)->None:
        port_outline=QPainterPath()
        poly=QPolygonF()
        poly.append(QPointF(0, 0.2 * self._port_icon_size))
        poly.append(QPointF(0.25 * self._port_icon_size,0.2 * self._port_icon_size))
        poly.append(QPointF(self._port_icon_size*0.5,self._port_icon_size*0.5))
        poly.append(QPointF(0.25 * self._port_icon_size,0.8 * self._port_icon_size))
        poly.append(QPointF(0,0.8 * self._port_icon_size))
        port_outline.addPolygon(poly)

        painter.setPen(self._pen_default)
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(port_outline.simplified())



class ExecInPort(ExecPort):
    def __init__(self):
        super().__init__(port_type=NodePort.PORT_TYPE_EXEC_IN)

class ExecOutPort(ExecPort):
    def __init__(self):
        super().__init__(port_type=NodePort.PORT_TYPE_EXEC_OUT)




























