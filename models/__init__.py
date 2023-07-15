#!/usr/bin/python3
"""Initialising the package to create a unique file storage instance.
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
