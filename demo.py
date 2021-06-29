# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 21:18:30 2021

@author: Baburam chhetri
"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def intro():
    return 'Hello everyone my name is baburam and this is a demo app to be deployed in kubernete'

if __name__ == '__main__':
    app.run()