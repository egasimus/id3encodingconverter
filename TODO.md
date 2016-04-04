# Introduction #

This page acts as a "To Do" list and collects points that need to be resolved, some urgent, some being of rather minor importance.

# Concept #
  * Currently the main design stipulates the comparison between ID3v1 ad ID3v2. Speaking of my experience, there are many ID3v2 tags not encoded using Unicode which lack the information of the encoding used. As the design relies on one part (the left side) being text in some unknown encoding while the other (the right side) is the actual tag in Unicode, the view suffers from the tags containing badly encoded strings. Currently there is a small button to allow the correction of the encoding, but this brakes the simplicity of reencoding. It might be a better solution to only show one tag (using the union of tags provided by TagLib's tag() method), and let the user operate on this. Optionally the user can view all tags and mix between the different versions.

# Functions #

  * LICENSE, INSTALL, CHANGELOG files
  * Use http://chardet.feedparser.org/
  * Improve guessing, use all possible methods together (match to ID3v2, match to file name, ngrams) and weight.
  * Improve guessing, group songs by artist and album, assume same encoding for all (maybe configurable).
  * Implement asynchronous handling of remote files, set status 'saved' only after uploading.
  * Amarok plugin.
  * Improve encoding.py, substitute top-n with better scoring.
  * Only enable own conversion button for ID3v2 if 1) non-ASCII, 2) convertible?
  * Drag&Drop of files/directories.

# Other #
  * Use the StringHandler class of TagLib.
  * Document source code.
  * Always have a id3v2 dictionary, even when empty. Make this consistent across functions.
  * Localisation currently seems not to work. The language can be choosen through the help menu, but no text is changed.
  * Configuration dialog can't handle preferences [[1](http://www.riverbankcomputing.com/pipermail/pyqt/2008-March/018906.html)].
  * Lack of responsiveness of combo box; once an item was selected by clicking somewhere else and moving the mouse to an entry where the button is released then entries can't be selected by simply clicking any more.
  * Menu text doesn't appear by default, when fixing this, it appears in white [[3](http://www.riverbankcomputing.com/pipermail/pyqt/2008-April/019000.html)].
  * Get proper size of file table view to fit window.
  * Nice colours for diff view, maybe in accordance to Oxygen theme.
  * Small handbook.
  * Proper icon for auto-conversion