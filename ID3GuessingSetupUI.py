
#!/usr/bin/env python
# Generated by pykdeuic4 from ID3GuessingSetup.ui on Thu May  1 18:18:30 2008
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyKDE4.kio import KUrlRequester
from PyQt4 import QtCore, QtGui
from kcombolistbox import KComboListBox

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(QtCore.QSize(QtCore.QRect(0,0,508,316).size()).expandedTo(Widget.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(Widget)
        self.vboxlayout.setObjectName("vboxlayout")

        self.groupBox = QtGui.QGroupBox(Widget)
        self.groupBox.setObjectName("groupBox")

        self.gridlayout = QtGui.QGridLayout(self.groupBox)
        self.gridlayout.setObjectName("gridlayout")

        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label,0,0,1,1)

        self.kcfg_textcat_LM_path = KUrlRequester(self.groupBox)
        self.kcfg_textcat_LM_path.setObjectName("kcfg_textcat_LM_path")
        self.gridlayout.addWidget(self.kcfg_textcat_LM_path,0,1,1,1)
        self.vboxlayout.addWidget(self.groupBox)

        self.kcfg_language_encoding_pref = KComboListBox(Widget)
        self.kcfg_language_encoding_pref.setObjectName("kcfg_language_encoding_pref")
        self.vboxlayout.addWidget(self.kcfg_language_encoding_pref)
        self.label.setBuddy(self.kcfg_textcat_LM_path)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(kdecore.i18n("Form"))
        self.groupBox.setTitle(kdecore.i18n("Textcat"))
        self.label.setText(kdecore.i18n("&Textcat language model path"))
