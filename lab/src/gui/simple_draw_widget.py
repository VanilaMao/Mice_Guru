from qtpy.QtWidgets import QWidget
from qtpy.QtGui import QPainter,QPen,QColor,QPaintEvent
from qtpy.QtCore import Qt, QRect
from models.location import Point

class SimpleDrawWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._dots=[]
        self._draw_all_points = False
        self._draw_sperator = False
        self._x_factor =1.0
        self._y_factor = 1.0
        self._map_width = 1.0
        self._map_height = 1.0

    def paintEvent(self, event:QPaintEvent):
        painter = QPainter(self)
        rect = event.rect()
        painter.setPen(QPen(QColor(255, 0, 0), 5, Qt.PenStyle.SolidLine))
        if self._draw_all_points or rect.size().width()>20:
            for point in self._dots:
                painter.drawEllipse(point.x, point.y, 1, 1)
            self._draw_all_points = False
        else:
            last = self._dots[-1]
            painter.drawEllipse(last.x, last.y, 1, 1)
        if self.draw_sperator:
            painter.drawLine(self.width()/2,0,self.width()/2,self.height())
        painter.end()

    def draw_dot(self,point:Point):
        local_point = Point(int(point.x*self._x_factor), int(point.y*self._y_factor))
        self._dots.append(local_point)
        self.update(QRect(local_point.x-5,local_point.y-5,10,10))

    def draw_dots(self, points):
        self._dots.extend([Point(int(point.x*self._x_factor),int(point.y*self._y_factor)) for point in points])
        self.update()
    
    def draw_sperator(self):
        self._draw_sperator = True
        self.update()

    def resizeEvent(self, event):
        self._draw_all_points = True
        self._draw_sperator = True
        self._x_current_factor = self.width()/self._map_width
        self._y_current_factor = self.height()/self._map_height
        print(f"x factor in resize event {self._x_factor}")
        for point in self._dots:
            point.x = int(point.x*self._x_current_factor/self._x_factor) 
            point.y= int(point.y*self._y_current_factor/self._y_factor)
        self._x_factor = self._x_current_factor
        self._y_factor = self._y_current_factor
        self.update()
    
    def redraw(self,width=None, height=None, data=None):
        if width is not None and height is not None:
            w = float(width)
            self._map_width = width
            h = float(height)
            self._map_height = height
            self._x_factor = self.width()/w
            print(f"x factor in redraw {self._x_factor}")
            self._y_factor = self.height()/h
            if data is not None:
                self._dots.clear()
                for point in data:
                    self._dots.append(Point(int(point.x*self._x_factor), int(point.y*self._y_factor)))
            else:
                for point in self._dots:
                    point.x = int(point.x*self._x_factor)
                    point.y= int(point.y*self._y_factor)
        else:
            self._dots.clear()
        self._draw_all_points = True
        self.update()