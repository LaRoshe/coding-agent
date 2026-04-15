from os.path import abspath, normpath, join, commonpath, isdir, getsize
from os import listdir
from functools import reduce

from functions.utils import validate_path

def get_files_info(working_directory, directory="."):
    try:
        target_dir = validate_path(working_directory, directory)

        if isdir(target_dir) == False:
            return f'Error: "{directory}" is not a directory'
        
        dir_list = listdir(target_dir)

        def aggregate_path_data(acc, path_name):
            abs_path = normpath(join(target_dir, path_name))
            is_path_dir = isdir(abs_path)
            file_size = getsize(abs_path)
            return acc + f"- {path_name}: file_size={file_size} bytes, is_dir={is_path_dir}\n"
            

        return reduce(aggregate_path_data, dir_list, "").rstrip("\n")
    except Exception as e:
        return f"Error: {e}"