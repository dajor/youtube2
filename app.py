# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import os
from app import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)