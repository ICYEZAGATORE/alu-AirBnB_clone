#!/usr/bin/python3
"""
This module initializes the models package and creates an instance of FileStorage.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
