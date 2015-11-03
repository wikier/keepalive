from setuptools import setup

setup(
      name = 'keepalive',
      version = 0.1,
      description = 'urllib keepalive support',
      long_description = 'An HTTP handler for `urllib2` that supports HTTP 1.1 and keepalive.',
      license = 'GNU GPL',
      author = "Benjamin Woodruff",
      author_email = "github@benjam.info",
      url = 'https://github.com/wikier/keepalive',
      download_url = 'https://github.com/wikier/keepalive/releases',
      platforms = ['any'],
      packages = ['keepalive'],
      requires = [],
      install_requires = [],
      classifiers =  [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
      ],
      keywords = 'python http urllib keepalive',
      use_2to3 = True,
)
