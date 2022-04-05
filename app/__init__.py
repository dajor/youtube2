# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

from flask            import Flask, request,g



# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
import sys

sys.path.append(".")


from app.app import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=8080)
