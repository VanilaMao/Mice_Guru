from processes.lab_process import LabProcess

# model is the datastream from touch window, view is the micetrack widget
class MiceRecordProcess(LabProcess):
    def __init__(self,model_in, view_out):
        self._start = False
        self._stop = False
        self._pause = False
        self._model_in =model_in
        self._view_out = view_out
        self._stream_connection = False

    def start(self):
        if self._start:
            return
        if not self._stream_connection:
            self._model_in(lambda data: self.stream(data))
            self._stream_connection = True
        self._start = True
        self._stop = False

    def stop(self):
        if self._start and not self._stop:
            self._stop = True
            self._start = False
            self._pause = False

    def pause(self):
        if not self._pause:
            self._pause = True

    def resume(self):
        if self._pause:
            self._pause = False

    def stream(self, data):
        if self._start and not self._pause:
            self._view_out(data)
    
    def update(self):
      self._stream_connection = False  
      self._start = False
      self._pause = False