# https://doc.qt.io/qtforpython-6/examples/example_widgets_mainwindows_mdi.html
# https://pypi.org/project/PySide6-QtAds/
from typing import List, Dict
import os
from injector import inject, singleton
from gui.image_tools import ImageToolsEnum
from models.location import Rect
from models.worm import CarbinReport
from screen.screen import *
from screen.screen_identifier import *
from services.context_service import ContextService
from services.document_service import DocumentService,DocType

@singleton
class ScreenService:
    @inject
    def __init__(self, parent: QMainWindow, ses:ScreenEventSub, context_service:ContextService, doc_service:DocumentService) -> None:
        self._conductor: Conductor = Conductor(parent)
        self._parent = parent
        self._doc_service = doc_service
        ses.addEventListener(ScreenEventEnum.close, self.close_screen)
        ses.addEventListener(ScreenEventEnum.select, self.draw_screen_rect)
        self._screen_widgets = {}
        self._title_loaders:Dict[ScreenIdentifier,callable] = {}
        self._context_service:ContextService= context_service

    def open_screen(self, id:ScreenIdentifier, image_loader:callable= None,widget_loader:callable=None, update_tools_bar=False, force = False):
        locations= self._context_service.ui.locations
        file = self._context_service.fileName
        data_loader = None
        if file is not None and os.path.exists(file):
            data_loader = lambda: self._doc_service.load(DocType.Json, file=file)
        title_loader = self._conductor.activate_screen(id,image_loader,widget_loader,data_loader, force, locations.get(id) if locations is not None else None)
        self._title_loaders[id] = title_loader
        if update_tools_bar:
            widget = self._screen_widgets[id]
            widget.setChecked(True)
    
    def hide_screen(self, id:ScreenIdentifier):
        self._conductor.hide_screen(id)

    def set_title(self, id:ScreenIdentifier, title:str):
        title_loader = self._title_loaders[id]
        title_loader(title)

    def get_layout(self):
        return self._conductor.get_layout()
    
    def save_screen(self,id:ScreenIdentifier,file):
        self._conductor.save_screen(id, lambda json: self._doc_service.save(DocType.Json,json, file=file))

    def close_screen(self, event):
        widget = self._screen_widgets.get(event.screen_id,None)
        self.save_screen_location(event.screen_id,event.loc)
        if widget is not None:
            widget.setChecked(False)

    def set_screen_map_widget(self, id:ScreenIdentifier, widget):
        self._screen_widgets[id] = widget
    
    def image_tools(self, tool:ImageToolsEnum):
        self._conductor.image_tools(tool)

    def draw_screen_rect(self, event:ScreenMouseEvent):
        self.draw_screen_rect(event.screen_id,event.start_pos,event.end_pos)
    
    def draw_screen_rect(self,id, start, end):
        self._conductor.draw_screen_rect(id, start, end)

    def clear_screen_rect(self):
        self._conductor.clear_screen_rect()

    def report(self,results:List[CarbinReport]):
        times = list(map(lambda x:x.time,results))
        self._conductor.report("Behavior",times, list(map(lambda x:x.speed,results)))
        self._conductor.report("Ratio",times,list(map(lambda x:x.ratio,results)))
        self._conductor.report("Trajectory",list(map(lambda x:x.trajectory.x,results)),list(map(lambda x:x.trajectory.y,results)))
        
    def show_status_message(self, message):
        status_bar = self._parent.statusBar()
        status_bar.showMessage(message)

    def save_screen_location(self,screen_id, loc):
        locations = self._context_service.ui.locations
        locations[screen_id] = loc
