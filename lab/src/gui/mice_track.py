from qtpy.QtWidgets import QWidget, QVBoxLayout
from gui.mice_track_widget import Ui_Widget
from models.serializable import Serializable, EnhancedJSONEncoder, PointClassDecoder
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
        self.Apply.clicked.connect(lambda: self.apply_settings())
        self.Clear.clicked.connect(lambda: self.clear())
        self._data = []
        self._resolution_height = 600
        self._resolution_width = 800
        self._pattern_separator = 400
        self._left_count = 0
        self._right_count = 0

    def accept_tracking_data(self, points):
        result = None
        if len(points) > 1:
            self._data.extend(points)
            self._canvas.draw_dots(points)
        else:
            point = points[0]
            self._data.append(point)
            self._canvas.draw_dot(point)
            if point.x > self._pattern_separator:
                self._right_count = self._right_count + 1
                self.RightCount.setText(str(self._right_count))
                result = False
            else:
                self._left_count = self._left_count + 1
                self.LeftCount.setText(str(self._left_count))
                result = True
        self.Data.setText(f"X: {points[0].x}  Y:{points[0].y}")
        return result

    def apply_settings(self):
        resolution_width = int(self.TouchWidth.text())
        resolution_height = int(self.TouchHeight.text())
        separator = int(self.PatternSeparator.text())
        resolution_changed =  self._resolution_height != resolution_height or self._resolution_width != resolution_width
        separator_changed = separator != self._pattern_separator
        redraw = False
        if resolution_changed:
            redraw = True
            self._resolution_width = resolution_width
            self._resolution_height = resolution_height
        if separator_changed:
            redraw = True
            self._pattern_separator = separator
            self.cal_left_right_count()
        if redraw:   
            self._canvas.redraw(width=self._resolution_width if resolution_changed else None,
                                height=self._resolution_height if resolution_changed else None,
                                pattern_separator=self._pattern_separator if separator_changed else None,
                                data=self._data if resolution_changed else None)

    def clear(self):
        self._left_count = 0
        self._right_count = 0
        self.RightCount.setText(str(self._right_count))
        self.LeftCount.setText(str(self._left_count))
        self._data.clear()
        self._canvas.reset()
    
    def cal_left_right_count(self):
        self._left_count = 0
        self._right_count = 0
        for point in self._data:
            if point.x < self._pattern_separator:
                self._left_count = self._left_count + 1
            else:
               self._right_count = self._right_count + 1 
        self.RightCount.setText(str(self._right_count))
        self.LeftCount.setText(str(self._left_count))  
        
    def serialize(self):
        export = {}
        export["resolution_width"] = self._resolution_width
        export["resolution_height"] = self._resolution_height
        export["left_count"] = self._left_count
        export["right_count"] = self._right_count
        export["pattern_separator"] = self._pattern_separator
        export["data"] = self._data
        return json.dumps(export, cls=EnhancedJSONEncoder)

    def deserialize(self, data):
        dict = json.loads(data, cls=PointClassDecoder)
        self._resolution_width = dict["resolution_width"]
        self._resolution_height = dict["resolution_height"]
        self._left_count = dict["left_count"]
        self._right_count = dict["right_count"]
        self._pattern_separator = dict["pattern_separator"]
        self._data = dict["data"]
        self.TouchWidth.setText(str(self._resolution_width))
        self.TouchHeight.setText(str(self._resolution_height))
        self.LeftCount.setText(str(self._left_count))
        self.RightCount.setText(str(self._right_count))
        self._canvas.redraw(self._resolution_width, self._resolution_height, self._pattern_separator, self._data)