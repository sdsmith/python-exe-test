#!/usr/bin/python3
from setuptools import setup
from Cython.Build import cythonize

setup(
    name="python-exe-test",
    python_requires=">=3.9",
    ext_modules = cythonize('hello.pyx'),
    console=['main.py']
)