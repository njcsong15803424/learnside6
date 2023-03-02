#coding:utf-8

from PySide6.QtWidgets import QGraphicsView
from PySide6.QtGui import QPainter,QMouseEvent
from PySide6.QtCore import Qt,QEvent
import PySide6

class VisualGraphView(QGraphicsView):

    def __init__(self,scene,parent=None):
        super().__init__(parent)


        self._scene=scene
        self.setScene(self._scene)

        self.setRenderHints(QPainter.Antialiasing|QPainter.TextAntialiasing|QPainter.SmoothPixmapTransform)
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        #隐藏滚动条
        #self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        #self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        #scale
        self._zoom_clamp=[0.5,5]
        self._zoom_factor=1.05
        self._view_scale=1.0
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

        #画布上拖动
        self._drag_mode =False

    def mousePressEvent(self, event:PySide6.QtGui.QMouseEvent) -> None:

        if event.button()==Qt.LeftButton: #因为我的鼠标没有中键，所以用左键，原视频中这里是中键
            self.middlebuttonPression(event)
        else:
            return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event:PySide6.QtGui.QMouseEvent) -> None:
        if event.button() == Qt.LeftButton: #因为我的鼠标没有中键，所以用左键，原视频中这里是中键
            self.middlebuttonRealeased(event)
        else:
            return super().mouseReleaseEvent(event)

    def mouseDoubleClickEvent(self, event:PySide6.QtGui.QMouseEvent) -> None:
        if event.button()==Qt.LeftButton:
            self.reset_scale()
        else:
            return super().mouseDoubleClickEvent(event)

    def wheelEvent(self, event) -> None:
        if self._drag_mode:
            if event.angleDelta().y()>0:
                zoom_factor =self._zoom_factor
            else:
                zoom_factor = 1 / self._zoom_factor

            self._view_scale *=zoom_factor

            if self._view_scale < self._zoom_clamp[0] or self._view_scale > self._zoom_clamp[1]:
                zoom_factor=1.0
                #self._view_scale=self._last_scale

            #self._last_scale=self._view_scale

            #每一次相对于上一次的进行缩放
            self.scale(zoom_factor,zoom_factor)


    def middlebuttonPression(self,event):
        if (self.itemAt(event.pos()) is not None):
            return
        else:
            #创建虚拟的左键松开事件
            release_event=QMouseEvent(QEvent.MouseButtonRelease,event.localPos(),Qt.LeftButton,Qt.NoButton,event.modifiers())
            super().mouseReleaseEvent(release_event)

            self.setDragMode(QGraphicsView.ScrollHandDrag)
            self._drag_mode=False
            # 创建虚拟的左键点击事件
            check_event=QMouseEvent(QEvent.MouseButtonPress,event.localPos(),Qt.LeftButton,Qt.NoButton,event.modifiers())
            super().mousePressEvent(check_event)

    def middlebuttonRealeased(self,event):
        release_event=QMouseEvent(QEvent.MouseButtonRelease,event.localPos(),Qt.LeftButton,Qt.NoButton,event.modifiers())
        super().mouseReleaseEvent(release_event)
        self.setDragMode(QGraphicsView.NoDrag)
        self._drag_mode = True

    def reset_scale(self):
        self.resetTransform()
        self._view_scale=1.0

    def set_scene(self,scene):
        self._scene=scene

    #添加节点
    def add_graph_node(self,node,pos=[0,0]):
        self._scene.addItem(node)
        node.setPos(pos[0],pos[1])
        node.set_scene(self._scene)







