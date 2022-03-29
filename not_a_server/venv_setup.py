#!/usr/bin/python3

import os

os.system("python3 -m venv venv &&\
        source venv/bin/activate &&\
        pip install -r requirements.txt")
print("Activate: source venv/bin/activate")
print("Deactivate: deactivate")
