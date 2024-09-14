#!/usr/bin/python3
"""Initialization of the FileStorage instance."""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
