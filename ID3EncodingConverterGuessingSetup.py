
#!/usr/bin/env python
# Generated by pykdeuic4 from ID3EncodingConverterGuessingSetup.ui on Thu Apr 17 18:04:20 2008
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui
from PyKDE4.kio import KUrlRequester
from PyKDE4.kdeui import KEditListBox

class Ui_EncodingGuessing(object):
    def setupUi(self, EncodingGuessing):
        EncodingGuessing.setObjectName("EncodingGuessing")
        EncodingGuessing.resize(QtCore.QSize(QtCore.QRect(0,0,508,282).size()).expandedTo(EncodingGuessing.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(EncodingGuessing)
        self.vboxlayout.setObjectName("vboxlayout")

        self.kcfg_language_encoding_pref = KEditListBox(EncodingGuessing)
        self.kcfg_language_encoding_pref.setObjectName("kcfg_language_encoding_pref")
        self.vboxlayout.addWidget(self.kcfg_language_encoding_pref)

        self.label = QtGui.QLabel(EncodingGuessing)
        self.label.setObjectName("label")
        self.vboxlayout.addWidget(self.label)

        self.kcfg_textcat_LM_path = KUrlRequester(EncodingGuessing)
        self.kcfg_textcat_LM_path.setObjectName("kcfg_textcat_LM_path")
        self.vboxlayout.addWidget(self.kcfg_textcat_LM_path)

        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.vboxlayout.addLayout(self.vboxlayout1)
        self.label.setBuddy(self.kcfg_textcat_LM_path)

        self.retranslateUi(EncodingGuessing)
        QtCore.QMetaObject.connectSlotsByName(EncodingGuessing)

    def retranslateUi(self, EncodingGuessing):
        EncodingGuessing.setWindowTitle(kdecore.i18n("Form"))
        self.label.setText(kdecore.i18n("&Textcat path"))
