from os.path import abspath, normpath, join, commonpath, isdir, getsize, isfile
from config import MAX_CHARS
from functions.utils import validate_path

def get_file_content(working_directory, file_path):
    try:
        target_file_path = validate_path(working_directory, file_path)
        
        if isfile(target_file_path) == False:
            return f'Error: File not found or is not a regular file: "{target_file_path}"'

        with open(target_file_path, "r") as f:
            content = f.read(MAX_CHARS)

            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            
            return content

    except Exception as e:
        return f"Error: {e}"
