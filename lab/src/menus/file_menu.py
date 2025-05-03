from pyqtribbon import RibbonCategoryStyle, RibbonButtonStyle
from qtpy.QtGui import QIcon,QKeySequence
from qtpy.QtCore import Qt
from icons.constants import *
from actions.file_actions import *
from icons.icon_utilities import *
file_menu = lambda :  {
            "File": {
                "style": RibbonCategoryStyle.Normal,
                "panels": {
                    "Project": {
                        "showPanelOptionButton": True,
                        "widgets": {
                            "New": {
                                "type": "Button",
                                "arguments": {
                                    "icon":   QIcon(new_icon),
                                    "text": "New",
                                    "tooltip": "Create a new mice track file",
                                    "rowSpan": RibbonButtonStyle.Large,
                                    "colSpan": 2,
                                    "slot": lambda: new_file()
                                },
                            },
                            "Open": {
                                "type": "Button",
                                "arguments": {
                                    "icon":  QIcon(open_icon),
                                    "text": "Open",
                                    "tooltip": "Open a mice track file",
                                    "rowSpan": RibbonButtonStyle.Large,
                                    "colSpan": 2,
                                    "alignment": Qt.AlignmentFlag.AlignLeft,
                                    "slot": lambda: open_file()
                                },
                            },
                            "Save": {
                                "type": "Button",
                                "arguments": {
                                    "icon":  QIcon(save_icon),
                                    "text": "Save",
                                    "tooltip": "Save mice tracking file",
                                    "rowSpan": RibbonButtonStyle.Large,
                                    "colSpan": 2,
                                    "alignment": Qt.AlignmentFlag.AlignLeft,
                                    "slot": lambda: save_file()
                                },
                            },
                        },
                    },
                    "Mice Control": {
                        "showPanelOptionButton": True,
                        "widgets": {
                            "TouchScreen": {
                                "type": "Button",
                                "text": "Open Track Screen",
                                "arguments": {
                                    "icon":   QIcon(touch_screen_icon),
                                    "text": "Open Screen Track",
                                    "tooltip": "Open Mice Track Touch Screen",
                                    "rowSpan": RibbonButtonStyle.Large,
                                    "alignment": Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom,
                                    "slot": lambda: open_touch_screen()
                                },
                            },
                            "MarginLeft": {
                                "type": "Label",
                                "args": "    ",
                                "arguments": {
                                    "rowSpan": RibbonButtonStyle.Large
                                },
                            },
                            "Continue": {
                                "type": "Button",
                                "arguments": {
                                    "icon":  QIcon(play_icon),
                                    "text": "Resume",
                                    "rowSpan": RibbonButtonStyle.Small,
                                    "tooltip": "Continue the record, Ctrl+Shift+R(esume)",
                                    "alignment": Qt.AlignmentFlag.AlignLeft,
                                    "shortcut": QKeySequence(Qt.KeyboardModifier.ControlModifier|Qt.KeyboardModifier.ShiftModifier|Qt.Key.Key_R),
                                    "slot": lambda: resume_record()
                                },
                            },
                            "Pause": {
                                "type": "Button",
                                "arguments": {
                                    "icon":  QIcon(pause_icon),
                                    "text": "Pause",
                                    "rowSpan": RibbonButtonStyle.Small,
                                    "tooltip": "Pause the record,Ctrl+Shift+P(ause)",
                                    "alignment": Qt.AlignmentFlag.AlignLeft,
                                    "shortcut": QKeySequence(Qt.KeyboardModifier.ControlModifier|Qt.KeyboardModifier.ShiftModifier|Qt.Key.Key_P),
                                    "slot": lambda: pause_record()
                                },
                            },
                            "Stop": {
                                "type": "Button",
                                "arguments": {
                                    "icon":  QIcon(stop_icon),
                                    "text": "Stop",
                                    "rowSpan": RibbonButtonStyle.Small,
                                    "tooltip": "Stop the record, Ctrl+Shift+E(xit)",
                                    "alignment": Qt.AlignmentFlag.AlignLeft,
                                    "shortcut": QKeySequence(Qt.KeyboardModifier.ControlModifier|Qt.KeyboardModifier.ShiftModifier|Qt.Key.Key_E),
                                    "slot": lambda: stop_record()
                                },
                            },
                            "Start": {
                                "type": "Button",
                                "arguments": {
                                    "icon":   QIcon(start_icon),
                                    "tooltip": "Start a new record,Ctrl+Shift+S(tart)",
                                    "rowSpan": RibbonButtonStyle.Large,
                                    "alignment": Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom,
                                    "shortcut": QKeySequence(Qt.KeyboardModifier.ControlModifier|Qt.KeyboardModifier.ShiftModifier|Qt.Key.Key_S),
                                    "slot": lambda: start_record()
                                },
                            },
                        }
                     }
                },
            }
        }