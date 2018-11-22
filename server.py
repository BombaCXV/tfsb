# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 03:21:58 2018

@author: Denis
"""

from os import environ
from flask import Flask

app = Flask(__name__)
app.run(environ.get('PORT'))
