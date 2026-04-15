import os
from functions.utils import validate_path
from os.path import abspath, normpath, join, commonpath, isdir, getsize, isfile, dirname


def write_file(working_directory, file_path, content):
    try:
        target_path = validate_path(working_directory, file_path, "write to")

        if isdir(target_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        parent_path = dirname(target_path)
        os.makedirs(parent_path, exist_ok=True)

        with open(target_path, "w") as f:
            f.write(content)
            return f'Succesfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: {e}'