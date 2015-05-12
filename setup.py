#!/usr/bin/env python

from setuptools import setup

setup(
    name='datadoc',
    version='0.1.0',
    author='Lazaro Gamio',
    author_email='lazaro.gamio@gmail.com',
    url='http://www.lazarogamio.com',
    description='A command-line tool that fetches data from google spreadsheets and saves it in a *variety* of formats.',
    long_description='Still under Development',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    packages=[
        'datadoc'
    ],
    entry_points = {
        'console_scripts': [
            'datadoc = datadoc.datadoc:launch_new_instance',
        ],
    },
    install_requires = [
        'gdata==2.0.18',
        'xmltodict==0.9.1'
    ]
    # test_suite = 'tests.test_binify',
)

