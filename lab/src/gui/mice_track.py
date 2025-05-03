from qtpy.QtWidgets import QWidget,QVBoxLayout
from gui.mice_track_widget import Ui_Widget
from models.serializable import Serializable,EnhancedJSONEncoder,PointClassDecoder
from gui.simple_draw_widget import SimpleDrawWidget
import json

class MiceTrack(Ui_Widget, QWidget, Serializable):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._canvas = SimpleDrawWidget()
        layout = QVBoxLayout()
        layout.addWidget(self._canvas)
        self.Track.setLayout(layout)
        self._canvas.draw_sperator()
        self.Apply.clicked.connect(lambda: self.apply_resolution())
        self.Clear.clicked.connect(lambda:self.clear())
        self._data = []
        self._resolution_height = 600
        self._resolution_width= 800
        self._left_count =0 
        self._right_count = 0
    
    def accept_tracking_data(self,points):
        if len(points) > 1:
            self._data.extend(points)
            self._canvas.draw_dots(points)
        else:
            point = points[0]
            self._data.append(point)
            self._canvas.draw_dot(point)
            if point.x>self._resolution_width/2:
                self._right_count = self._right_count+1
                self.RightCount.setText(str(self._right_count))
            else:
                self._left_count = self._left_count+1
                self.LeftCount.setText(str(self._left_count))
        self.Data.setText(f"X: {points[0].x}  Y:{points[0].y}")

    def apply_resolution(self):
        self._resolution_width = int(self.TouchWidth.text())
        self._resolution_height = int(self.TouchHeight.text())
        self._canvas.redraw(self._resolution_width,self._resolution_height, self._data)

    def clear(self):
        self._left_count = 0
        self._right_count = 0
        self.RightCount.setText(str(self._right_count))
        self.LeftCount.setText(str(self._left_count))
        self._data.clear()
        self._canvas.redraw()

    def serialize(self):
        export = {}
        export["resolution_width"]= self._resolution_width
        export["resolution_height"] = self._resolution_height
        export["left_count"]=self._left_count
        export["right_count"]=self._right_count
        export["data"] = self._data
        return json.dumps(export,cls=EnhancedJSONEncoder)
    
    def deserialize(self, data):
        dict = json.loads(data,cls = PointClassDecoder)
        self._resolution_width = dict["resolution_width"]
        self._resolution_height = dict["resolution_height"]
        self._left_count =dict["left_count"]
        self._right_count = dict["right_count"]
        self._data = dict["data"]
        self.TouchWidth.setText(str(self._resolution_width))
        self.TouchHeight.setText(str(self._resolution_height))
        self.LeftCount.setText(str(self._left_count))
        self.RightCount.setText(str(self._right_count))
        self._canvas.redraw(self._resolution_width,self._resolution_height, self._data)