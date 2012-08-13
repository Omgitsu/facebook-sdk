#!/usr/bin/env python
from distutils.core import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='facebooksdk',
    version='0.3.3',
    description='This client library is designed to support the Facebook '
                'Graph API and the official Facebook JavaScript SDK, which '
                'is the canonical way to implement Facebook authentication.',
    author='Facebook',
    url='http://github.com/omgitsu/facebook-sdk',
    license='Apache',
    py_modules=[
        'facebooksdk',
    ],
    long_description=read("readme.md"),
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
    ],
)
