# -*- coding: utf-8 -*-

#   This library is free software; you can redistribute it and/or
#   modify it under the terms of the GNU Lesser General Public
#   License as published by the Free Software Foundation; either
#   version 2.1 of the License, or (at your option) any later version.
#
#   This library is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#   Lesser General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public
#   License along with this library; if not, write to the 
#      Free Software Foundation, Inc., 
#      59 Temple Place, Suite 330, 
#      Boston, MA  02111-1307  USA

# This file was part of urlgrabber, a high-level cross-protocol url-grabber
# Copyright 2002-2004 Michael D. Stenner, Ryan Tomayko
# Copyright 2015 Sergio Fernández

from setuptools import setup
import sys

try:
    import six
    py3 = six.PY3
except:
    py3 = sys.version_info[0] >= 3

# metadata
if py3:
    import re
    _version_re = re.compile(r'__version__\s*=\s*"(.*)"')
    for line in open('keepalive/__init__.py', encoding='utf-8'):
        version_match = _version_re.match(line)
        if version_match:
            _version = version_match.group(1)
else:
    import keepalive
    _version = keepalive.__version__

setup(
      name = 'keepalive',
      version = _version,
      description = 'urllib keepalive support for python',
      long_description = 'An HTTP handler for `urllib2` that supports HTTP 1.1 and keepalive.',
      license = 'GNU LGPL',
      author = "mstenner, rtomayko",
      maintainer = 'Sergio Fernández',
      maintainer_email = 'sergio@wikier.org',
      url = 'https://github.com/wikier/keepalive',
      download_url = 'https://github.com/wikier/keepalive/releases',
      platforms = ['any'],
      packages = ['keepalive'],
      requires = [],
      install_requires = [],
      classifiers =  [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
      ],
      keywords = 'python http urllib keepalive',
      use_2to3 = True
)
