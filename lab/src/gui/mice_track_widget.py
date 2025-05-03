# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mice_track.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_2)

        self.LeftCount = QLabel(Widget)
        self.LeftCount.setObjectName(u"LeftCount")

        self.horizontalLayout.addWidget(self.LeftCount)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(608, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.RightCount = QLabel(Widget)
        self.RightCount.setObjectName(u"RightCount")
        self.RightCount.setStyleSheet(u"margin-right: 10px")

        self.horizontalLayout_2.addWidget(self.RightCount)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.Data = QLabel(Widget)
        self.Data.setObjectName(u"Data")

        self.horizontalLayout_4.addWidget(self.Data)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Label_2 = QLabel(Widget)
        self.Label_2.setObjectName(u"Label_2")
        sizePolicy.setHeightForWidth(self.Label_2.sizePolicy().hasHeightForWidth())
        self.Label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.Label_2)

        self.TouchWidth = QLineEdit(Widget)
        self.TouchWidth.setObjectName(u"TouchWidth")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.TouchWidth.sizePolicy().hasHeightForWidth())
        self.TouchWidth.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.TouchWidth)

        self.Label_1 = QLabel(Widget)
        self.Label_1.setObjectName(u"Label_1")
        sizePolicy.setHeightForWidth(self.Label_1.sizePolicy().hasHeightForWidth())
        self.Label_1.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.Label_1)

        self.TouchHeight = QLineEdit(Widget)
        self.TouchHeight.setObjectName(u"TouchHeight")
        sizePolicy1.setHeightForWidth(self.TouchHeight.sizePolicy().hasHeightForWidth())
        self.TouchHeight.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.TouchHeight)

        self.Apply = QPushButton(Widget)
        self.Apply.setObjectName(u"Apply")
        sizePolicy1.setHeightForWidth(self.Apply.sizePolicy().hasHeightForWidth())
        self.Apply.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.Apply)

        self.Clear = QPushButton(Widget)
        self.Clear.setObjectName(u"Clear")
        sizePolicy1.setHeightForWidth(self.Clear.sizePolicy().hasHeightForWidth())
        self.Clear.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.Clear)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.Track = QWidget(Widget)
        self.Track.setObjectName(u"Track")
        self.Track.setStyleSheet(u"background-color:rgb(16, 16, 16)")

        self.verticalLayout.addWidget(self.Track)

        self.verticalLayout.setStretch(4, 1)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Left Total:", None))
        self.LeftCount.setText(QCoreApplication.translate("Widget", u"0", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Right Total:", None))
        self.RightCount.setText(QCoreApplication.translate("Widget", u"0", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Current Track:", None))
        self.Data.setText("")
        self.label.setText(QCoreApplication.translate("Widget", u"Touch Screen Resolution", None))
        self.Label_2.setText(QCoreApplication.translate("Widget", u"Width:", None))
        self.Label_1.setText(QCoreApplication.translate("Widget", u"Height:", None))
        self.Apply.setText(QCoreApplication.translate("Widget", u"Apply", None))
        self.Clear.setText(QCoreApplication.translate("Widget", u"Clear", None))
    # retranslateUi

