from qtpy.QtWidgets import QWidget,QPushButton,QVBoxLayout,QSizePolicy
from qtpy.QtGui import QMouseEvent, QTouchEvent, QCloseEvent
from qtpy.QtCore import Signal, Qt
from models.location import Point

class TouchButton(QPushButton):
    touch = Signal(object)
    def __init__(self, top_margin_cal, parent=None):
        super().__init__(parent)
        self._top_margin_cal = top_margin_cal
        self.setAttribute(Qt.WidgetAttribute.WA_AcceptTouchEvents, True)

    def mousePressEvent(self, e: QMouseEvent):
        self.touch.emit([Point(int(e.pos().x()),int(e.pos().y()+self._top_margin_cal()))])
        super().mousePressEvent(e)

    def touchEvent(self, event: QTouchEvent):
        touch_positions = []
        for touch in event.points():
            touch_positions(Point(int(touch.pos().x()),int(touch.pos().y()+self._top_margin_cal())))
            print(f"Touch Coordinates (Multi): {touch.pos()}")
        self.touch.emit(touch_positions)
        super().touchEvent(event)

class TouchWindow(QWidget):
    touchclosed = Signal()
    def __init__(self):
        self._top_margin = 0
        super().__init__()
        self.setWindowTitle("Touch Window")
        layout = QVBoxLayout()
        self._button= TouchButton(lambda: self.geometry().y() - self.frameGeometry().y())
        self._button.setStyleSheet("QPushButton { border: none; }")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        self._button.setSizePolicy(sizePolicy)
        layout.addWidget(self._button)
        layout.setContentsMargins(0, 0, 0, 0) 
        self.setLayout(layout)
        self.setWindowFlags(Qt.WindowType.MaximizeUsingFullscreenGeometryHint)
        self.setContentsMargins(0, 0, 0, 0) 

    def closeEvent(self, event: QCloseEvent):
        self.touchclosed.emit()
        print("close touch window")
        event.accept()
        
    def connect_touch(self,touch_handler:callable):
        self._button.touch.connect(touch_handler)