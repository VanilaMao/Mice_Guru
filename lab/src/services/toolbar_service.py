from typing import Dict, List
from gui.image_tools import ImageToolsEnum
from injector import inject, singleton
from qtpy.QtCore import Signal, QObject, QSignalBlocker
from qtpy.QtWidgets import QWidget
from services.context_service import ContextService

@singleton
class ToolbarService(QObject):
    start=Signal(int)
    config_set:Dict[str,callable]={
    }
       
    starting_disable_list=["Start","Pause","Stop","Continue","TouchScreen"] #they should be disbaled when process is not starting
    
    @inject
    def __init__(self, context_service:ContextService) -> None:
        super().__init__() 
        self._context_service = context_service
        self._slot_dict = {
            "Start": lambda:  self.start
        }
        self.config_widgets ={}

    def update_to_ui(self, value, element):
        signal= self._slot_dict[element]
        signal().emit(value)

    def update_to_ui(self, dict:Dict[str,int]):
        for element in dict:
            signal= self._slot_dict[element]
            signal().emit(dict[element])

    def add_signal_connect(self,element, widget, slot:callable):
        self.config_widgets[element] = widget
        signal= self._slot_dict[element]
        signal().connect(slot)

    def update_config(self, element, value):
        print(f"{element}|{value}")
        config = self._context_service.config
        if isinstance(value, str):
            value = int(value)
        self.config_set[element](config, value)
        self._context_service.update_config()
        
        # TODO define __call__ function in processconfig class instead

    def disable(self, element:str):
        widget:QWidget = self._context_service.widgets[element]
        widget.setEnabled(False)

    def disable_elements(self, elements:List[str]):
        for element in elements:
            self.disable(element)

    def enable(self, element:str):
        widget:QWidget = self._context_service.widgets[element]
        widget.setEnabled(True)

    def enable_elements(self, elements:List[str]):
        for element in elements:
            self.enable(element)
    
    def check_element(self,element:str, value:bool, update_config:bool=True, block_signal:bool = False):
        widget  = self._context_service.widgets[element]
        blocker = None
        if block_signal:
            blocker = QSignalBlocker(widget)
        widget.setChecked(value)
        if update_config:
            config = self._context_service.config
            self.config_set[element](config,value)
        if blocker is not None:
            blocker.unblock()

    def init(self):
        self.disable_elements(self.starting_disable_list)
        config = self._context_service.config
        # self.update_to_ui({
        #               "LeftMax":config.left_max,
        #               "LeftMin":config.left_min,
        #               "RightMin":config.right_min,
        #               "RightMax": config.right_max,
        #               "Min": config.particle_size_min,
        #               "Max": config.particle_size_max,
        #               "Background": config.background
        #               })