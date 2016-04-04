**This is currently alpha material**

ID3EncodingConverter is a simple ID3 tag viewer for KDE written in Python which
supports conversion of tags from different character sets to Unicode with ID3v2.
Its goal is fast and simple conversion for multiple files, letting the user
compare between ID3v1 and ID3v2 tags and choose the correct encoding.

![http://www.stud.uni-karlsruhe.de/~uyhc/files/images/id3encodingconverter_about.png](http://www.stud.uni-karlsruhe.de/~uyhc/files/images/id3encodingconverter_about.png)

See http://en.wikipedia.org/wiki/ID3 on ID3 tags.

# Features #
  * Conversion of ID3v1 to ID3v2 tags
  * Simple side by side comparison of ID3v1 and ID3v2 tags
  * Highlighting of differences between both versions
  * Selection of encoding based on comparison of encoded versions of ID3v1 tag or encoding names
  * Batch conversion of several files
  * Intelligent guessing of encoding
  * Automatic conversion mode

# Dependencies #
  * [Python](http://www.python.org/) Programming Language
  * [Qt4](http://trolltech.com/products/qt) Cross-Platform GUI and Framework
  * [KDE4](http://www.kde.org) KDE4 libraries including kdecore, kdeui, kio
  * [PyKDE4](http://www.riverbankcomputing.co.uk/pykde/) Python bindings for KDE
  * [TagLib](http://developer.kde.org/~wheeler/taglib.html) Audio Meta-Data Library
  * [TagPy](http://news.tiker.net/software/tagpy) Python bindings for TagLib
## Optional ##
  * [libTextCat](http://software.wise-guys.nl/libtextcat/) library primarily developed for language guessing

If you use [Amarok](http://amarok.kde.org/) or KDE itself you should already have the basic libraries. You might have to install the Python bindings additionally.

# Screenshot #
![http://www.kde-apps.org/CONTENT/content-pre1/78854-1.png](http://www.kde-apps.org/CONTENT/content-pre1/78854-1.png)