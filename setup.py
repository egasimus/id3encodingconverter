#!/usr/bin/python
# -*- coding: utf8 -*-

from distutils.core import setup
import re
import os

FULLAUTHOR = "Christoph Burgmer <christoph.burgmer@stud.uni-karlsruhe.de>"
LICENSE = 'GNU General Public License v2'
URL = "http://code.google.com/p/id3encodingconverter"
VERSION = "0.1alpha"

(AUTHOR, EMAIL) = re.match('^(.*?)\s*<(.*)>$', FULLAUTHOR).groups()

# get target directories for kde4 files
kde4DataTarget = os.popen("kde4-config --expandvars --install data")\
    .read().strip()
kde4DesktopTarget = os.popen("kde4-config --expandvars --install apps")\
    .read().strip()
kde4IconTarget = os.popen("kde4-config --expandvars --install icon")\
    .read().strip()

setup(name='id3encodingconverter',
    version=VERSION,
    description='ID3 tag viewer for conversion of different character sets',
    long_description="cjklib provides language routines for handling Han " \
        + "id3encodingconverter is a simple ID3 tag viewer for KDE written in" \
        + " Python which supports conversion of tags from different character" \
        + " sets to Unicode with ID3v2. Its goal is fast and simple" \
        + " conversion for multiple files, letting the user compare between" \
        + " ID3v1 and ID3v2 tags and choose the correct encoding.",
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    py_modules=['encoding', 'ngram', 'ID3EncodingConverterUI',
        'ID3EncodingConverterGuessingSetup'],
    packages=[],
    package_data={},
    scripts=['id3encodingconverter'],
    data_files=[(os.path.join(kde4DataTarget, 'id3encodingconverter'),
            ['id3encodingconverterui.rc', 'id3encodingconverter_about.png']),
        (os.path.join(kde4DesktopTarget, 'id3encodingconverter'),
                 ['id3encodingconverter.desktop']),
        ('share/doc/id3encodingconverter/', ['TODO']), # 'README', 'changelog', 'COPYING'
        (kde4IconTarget, ['id3encodingconverter.png']),],
    license=LICENSE,
    classifiers=['Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python',])
