
#!/usr/bin/env python
# Generated by pykdeuic4 from ID3v2Encoding.ui on Fri Apr 25 21:03:42 2008
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui
from PyKDE4.kdeui import KComboBox

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(QtCore.QSize(QtCore.QRect(0,0,285,170).size()).expandedTo(Widget.minimumSizeHint()))

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)

        self.centralwidget = QtGui.QWidget(Widget)
        self.centralwidget.setGeometry(QtCore.QRect(0,0,285,170))
        self.centralwidget.setObjectName("centralwidget")

        self.vboxlayout = QtGui.QVBoxLayout(self.centralwidget)
        self.vboxlayout.setObjectName("vboxlayout")

        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")

        self.titlelabel = QtGui.QLabel(self.centralwidget)
        self.titlelabel.setObjectName("titlelabel")
        self.gridlayout.addWidget(self.titlelabel,0,0,1,1)

        self.artistlabel = QtGui.QLabel(self.centralwidget)
        self.artistlabel.setObjectName("artistlabel")
        self.gridlayout.addWidget(self.artistlabel,1,0,1,1)

        self.v2artist = QtGui.QLineEdit(self.centralwidget)
        self.v2artist.setObjectName("v2artist")
        self.gridlayout.addWidget(self.v2artist,1,1,1,1)

        self.albumlabel = QtGui.QLabel(self.centralwidget)
        self.albumlabel.setObjectName("albumlabel")
        self.gridlayout.addWidget(self.albumlabel,2,0,1,1)

        self.v2album = QtGui.QLineEdit(self.centralwidget)
        self.v2album.setObjectName("v2album")
        self.gridlayout.addWidget(self.v2album,2,1,1,1)

        self.genrelabel = QtGui.QLabel(self.centralwidget)
        self.genrelabel.setObjectName("genrelabel")
        self.gridlayout.addWidget(self.genrelabel,3,0,1,1)

        self.v2genre = QtGui.QLineEdit(self.centralwidget)
        self.v2genre.setObjectName("v2genre")
        self.gridlayout.addWidget(self.v2genre,3,1,1,1)

        self.commentlabel = QtGui.QLabel(self.centralwidget)
        self.commentlabel.setObjectName("commentlabel")
        self.gridlayout.addWidget(self.commentlabel,4,0,1,1)

        self.v2comment = QtGui.QLineEdit(self.centralwidget)
        self.v2comment.setObjectName("v2comment")
        self.gridlayout.addWidget(self.v2comment,4,1,1,1)

        self.v2title = KComboBox(self.centralwidget)
        self.v2title.setModelColumn(0)
        self.v2title.setObjectName("v2title")
        self.gridlayout.addWidget(self.v2title,0,1,1,1)
        self.vboxlayout1.addLayout(self.gridlayout)
        self.vboxlayout.addLayout(self.vboxlayout1)
        self.titlelabel.setBuddy(self.v2title)
        self.artistlabel.setBuddy(self.v2artist)
        self.albumlabel.setBuddy(self.v2album)
        self.genrelabel.setBuddy(self.v2genre)
        self.commentlabel.setBuddy(self.v2comment)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)
        Widget.setTabOrder(self.v2artist,self.v2album)
        Widget.setTabOrder(self.v2album,self.v2genre)
        Widget.setTabOrder(self.v2genre,self.v2comment)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(kdecore.i18n("ID3EncodingConverter"))
        self.titlelabel.setText(kdecore.i18n("&Title"))
        self.artistlabel.setText(kdecore.i18n("A&rtist"))
        self.albumlabel.setText(kdecore.i18n("A&lbum"))
        self.genrelabel.setText(kdecore.i18n("&Genre"))
        self.commentlabel.setText(kdecore.i18n("&Comment"))
        self.v2title.setToolTip(kdecore.i18n("Choose correct representation of song title"))
        self.v2title.setWhatsThis(kdecore.i18n("Choose the correct encoding of the ID3v2 tag. All tags beneath will be updated according to the selection. If the actual encoding is unknown, choose the string that makes sense."))
