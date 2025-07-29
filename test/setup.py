# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe

setup(
    name="etiquetas",
    version="1.0",
    description="esto sirve para imprimir",
    author="onedte",
    author_email="ivanandres.hj@gmail.com",
    url="www.onedte.cl",
    license="MIT",
    scripts=["main.py"],
    console=["main.py"],
    options={"py2exe": {"bundle_files": 1}},
    zipfile=None,
)