from os.path import abspath, normpath, join, commonpath, isdir, getsize, isfile
from config import MAX_CHARS
from functions.utils import validate_path
from google.genai import types


def get_file_content(working_directory, file_path):
    try:
        target_file_path = validate_path(working_directory, file_path)

        if isfile(target_file_path) == False:
            return (
                f'Error: File not found or is not a regular file: "{target_file_path}"'
            )

        with open(target_file_path, "r") as f:
            content = f.read(MAX_CHARS)

            if f.read(1):
                content += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )

            return content

    except Exception as e:
        return f"Error: {e}"


schema_get_files_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Gets the contents of a specified file. Allows for reading of the first {MAX_CHARS} characters. If the file contains more than the quota, it returns metadata at the end that is inclosed within  [...File $file_path truncated at $max_char characters]",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file whose contents are to be read, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)
