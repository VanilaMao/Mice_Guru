import functools
from typing import Dict
from pyqtribbon.panel import RibbonPanel
from qtpy.QtWidgets import QWidget, QLabel, QCheckBox,QLineEdit,QToolButton
from qtpy.QtCore import Qt
from qtpy.QtGui import QKeySequence,QShortcut
from di.di import DI
from services.context_service import ContextService

def initializer(widget: QWidget, *args, **kwargs):
    if isinstance(widget, QLabel) or isinstance(widget, QCheckBox):
        widget.setText(*args)
    if isinstance(widget, QCheckBox):
        slot = kwargs.pop("slot", None)
        if slot:
            widget.stateChanged.connect(slot(widget))
    if isinstance(widget,QLineEdit):
        slot = kwargs.pop("slot", None)
        if slot:
            slot(widget)

def addWidgetsBy(self, data: Dict[str, Dict]) -> Dict[str,QWidget]:
    widgets = {}  # type: Dict[str, QWidget]
    for key, widget_data in data.items():
        name = widget_data.pop("type", "")  # type: str
        type = name[0].upper() + name[1:]
        if hasattr(self, "add" + type):
            method = getattr(self, "add" + type)  # type: Callable
            if method is not None:
                args = widget_data.get("args", None)
                if args is not None:
                    widgets[key] = method(
                        args,
                        **widget_data.get("arguments", {}),
                        initializer=initializer
                    )
                else:
                    widgets[key] = method(**widget_data.get("arguments", {}))
    ctx = DI.get_di_instance().get(ContextService)
    ctx.widgets.update(widgets)
    handle_shortcuts(widgets)
    return widgets

def handle_shortcuts(widgets:Dict[str,QWidget]):
    for key in widgets:
        widget = widgets[key]
        if isinstance(widget,QToolButton):
            qk:QKeySequence = widget.shortcut()
            short_cut =  QShortcut(qk,widget)
            short_cut.setContext(Qt.ShortcutContext.ApplicationShortcut)
            short_cut.activated.connect(widget.click)

class LabRibbon:
    def __init__(self) -> None:
        pass

    @staticmethod
    def patch_panel_addWidgetsBy():  # addWidgetsBy(self, data: Dict[str, Dict]) -> Dict[str, QtWidgets.QWidget]:
        RibbonPanel.addWidgetsBy = addWidgetsBy
        RibbonPanel.addCheckBox = functools.partialmethod(
            RibbonPanel._addAnyWidget,
            cls=QCheckBox,
            initializer=QCheckBox.setText,
        )
        RibbonPanel.addLineEdit = functools.partialmethod(
            RibbonPanel._addAnyWidget,
            cls=QLineEdit,
            initializer = initializer
        )