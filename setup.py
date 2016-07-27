#!/usr/bin/env python
from setuptools import setup

def readme():
    with open("README.rst") as f:
        return f.read()

setup (
    name='swupd',
    version='0.1.0',
    description='Python bindings for swupd',
    long_description=readme(),
    author='Guillermo Ponce',
    author_email='guillermo.a.ponce.castneda@intel.com',
    license='Apache-2.0',
    packages=['swupd'],
    platforms='Clear Linux for Intel Architecture',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: System :: Installation/Setup',
    ],
)
