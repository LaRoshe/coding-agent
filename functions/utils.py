from os.path import abspath, normpath, join, commonpath, isdir, getsize, isfile

def validate_path(working_directory, path, error_action="read"):
    abs_working_dir = abspath(working_directory)
    target_path = normpath(join(abs_working_dir, path))
    is_valid_path = commonpath([abs_working_dir, target_path]) == abs_working_dir

    if is_valid_path == False:
        raise Exception(f'Error: Cannot {error_action} {path} as it is outside the permitted working directory')

    if isdir(abs_working_dir) == False:
        raise Exception(f'Error: "{working_directory}" is not a directory')
    
    return target_path