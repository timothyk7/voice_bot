#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "pyaudio",
    "SpeechRecognition",
    "argparse",
    "requests",
    "wit"
]

test_requirements = [
    # TODO: put package test requirements here
    "nose"
]

setup(
    name='voice_bot',
    version='0.1.0',
    description="Voice bot that can perform various tasks. ",
    long_description=readme + '\n\n' + history,
    author="Timothy Kua",
    author_email='timothyk7@gmail.com',
    url='https://github.com/timothyk7/voice_bot',
    packages=[
        'voice_bot',
    ],
    package_dir={'voice_bot':
                 'voice_bot'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='voice_bot',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
