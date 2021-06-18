#!/usr/bin/python3
from setuptools import find_packages, setup
from Cython.Build import cythonize
import py2exe

import sys
from typing import List

setup(
    name="temp-hello",
    python_requires=">=3.9",
    ext_modules = cythonize('hello.py'),
    console=['main.py']
)