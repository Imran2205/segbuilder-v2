"""Filesystem storage helpers for the local application."""

import logging
import os
import shutil
from pathlib import Path
from urllib.parse import quote

from .local_resources import get_local_folder


def _full_path(path):
    return Path(get_local_folder()) / path


def load_file(path):
    try:
        return _full_path(path).read_bytes()
    except OSError as error:
        logging.debug("Could not read %s: %s", path, error)
        return None


def write_file(path, data):
    full_path = _full_path(path)
    full_path.parent.mkdir(parents=True, exist_ok=True)
    full_path.write_bytes(data)


def file_exists(path):
    return _full_path(path).exists()


def serve_file(path):
    """Return the URL exposed by the Flask local-storage route."""
    return "/local-storage/" + quote(str(path).replace(os.sep, "/"))


def get_files_in_directory(directory_path):
    full_path = _full_path(directory_path)
    if not full_path.exists():
        return []
    return [
        str(path.relative_to(full_path))
        for path in full_path.rglob("*")
        if path.is_file()
    ]


def file_download(remote_file, local_file):
    try:
        shutil.copy(_full_path(remote_file), local_file)
    except OSError as error:
        logging.error("Could not copy %s: %s", remote_file, error)
