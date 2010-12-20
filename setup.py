#!/usr/bin/env python
import os

from setuptools import setup

from scss import VERSION, PROJECT, LICENSE


def read( fname ):
    try:
        return open( os.path.join( os.path.dirname( __file__ ), fname ) ).read()
    except IOError:
        return ''


META_DATA = dict(
    name=PROJECT,
    version=VERSION,
    license=LICENSE,
    description=read( 'DESCRIPTION' ),
    long_description=read( 'README.rst' ),

    author='Kirill Klenov',
    author_email='horneds@gmail.com',
    url='http://github.com/klen/python-scss',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: Russian',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Programming Language :: Python',
        'Environment :: Console',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Text Processing :: Markup',
    ],

    platforms=('Any'),

    install_requires = [ 'pyparsing' ],
)


if __name__ == "__main__":
    setup( **META_DATA )


