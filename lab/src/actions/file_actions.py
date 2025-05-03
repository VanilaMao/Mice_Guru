from pathlib import Path
from qtpy.QtWidgets  import QFileDialog
from di.di import DI
from processes.mice_record_process import MiceRecordProcess
from services.dialog_service import *
from services.context_service import ContextService
from services.toolbar_service import ToolbarService
from services.screen_service  import ScreenService,ScreenIdentifier
from gui.mice_track import MiceTrack
from gui.touch_window import TouchWindow
from processes.lab_process import LabProcess
import global_vars.global_windows as g

def open_file():
    context_service = DI.get_di_instance().get(ContextService)
    fileName = QFileDialog.getOpenFileName(None, "Open Mice Files", "/home/lab", "Mice Record File (*.mice)")
    file= fileName[0]
    print(file)
    if not not file:
        context_service.fileName = file
        sc = DI.get_di_instance().get(ScreenService)
        sc.open_screen(ScreenIdentifier.MICE,widget_loader= lambda:MiceTrack(), force=True) #forbid touch window record, if need to record, create a new file
        sc.set_title(ScreenIdentifier.MICE,file)
        if g.touch_window is not None:
            g.touch_window.close()  # close touch window
        tb = DI.get_di_instance().get(ToolbarService)
        tb.disable_elements(["TouchScreen","Continue","Pause","Stop","Start"])

def save_file():
    context_service = DI.get_di_instance().get(ContextService)
    sc = DI.get_di_instance().get(ScreenService)
    file:str = context_service.fileName
    if "untitled" in file:
        fileName, _ = QFileDialog.getSaveFileName(None,"Save Mice Record File","/home/lab","Mice Record File (*.mice)")
        if not not fileName:
            sc.set_title(ScreenIdentifier.MICE,fileName)
            context_service.fileName =fileName
            file = fileName
        else:
            return #click cancel button in dialog
    sc.save_screen(ScreenIdentifier.MICE, file)

def new_file():
    context_service = DI.get_di_instance().get(ContextService)
    context_service.fileName ="untitled.mice"
    widget = MiceTrack()
    context_service.process = MiceRecordProcess(lambda func:g.touch_window.connect_touch(func), lambda points: widget.accept_tracking_data(points))
    sc = DI.get_di_instance().get(ScreenService)
    sc.open_screen(ScreenIdentifier.MICE,widget_loader =lambda:widget,force=True)
    sc.set_title(ScreenIdentifier.MICE,context_service.fileName)
    tb = DI.get_di_instance().get(ToolbarService)
    tb.enable_elements(["TouchScreen"])

def open_touch_screen():
    tb = DI.get_di_instance().get(ToolbarService)
    context_service = DI.get_di_instance().get(ContextService)
    process:LabProcess = context_service.process
    touch_window = TouchWindow()
    touch_window.setMinimumSize(800,600)

    touch_window.touchclosed.connect(lambda: close_touch_window(tb,process))
    g.touch_window = touch_window
    touch_window.show()
    tb.disable_elements(["TouchScreen"])
    tb.enable_elements(["Start"])

def start_record():
    context_service = DI.get_di_instance().get(ContextService)
    process:LabProcess = context_service.process
    if process is not None:
        tb = DI.get_di_instance().get(ToolbarService)
        tb.enable_elements(["Pause","Stop"])
        tb.disable_elements(["Continue","Start"])
        process.start()
        

def stop_record():
    context_service = DI.get_di_instance().get(ContextService)
    process:LabProcess = context_service.process
    if process is not None:
        process.stop()
        tb = DI.get_di_instance().get(ToolbarService)
        tb.enable_elements(["Start"])
        tb.disable_elements(["Pause","Stop","Continue"])

def pause_record():
    context_service = DI.get_di_instance().get(ContextService)
    process:LabProcess = context_service.process
    if process is not None:
        process.pause()
        tb = DI.get_di_instance().get(ToolbarService)
        tb.enable_elements(["Continue"])
        tb.disable_elements(["Pause"])

def resume_record():
    context_service = DI.get_di_instance().get(ContextService)
    process:LabProcess = context_service.process
    if process is not None:
        process.resume()
        tb = DI.get_di_instance().get(ToolbarService)
        tb.enable_elements(["Pause"])
        tb.disable_elements(["Continue"])

def close_touch_window(tb:ToolbarService,process:LabProcess):
    tb.enable_elements(["TouchScreen"])
    tb.disable_elements(["Start","Continue","Pause","Stop"])
    process.update()
    g.touch_window = None