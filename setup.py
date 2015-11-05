from setuptools import setup

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
      license = 'GNU GPL',
      author = "mstenner, rtomayko",
      maintainer = 'Sergio Fernandez',
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
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
      ],
      keywords = 'python http urllib keepalive',
      use_2to3 = True
)
