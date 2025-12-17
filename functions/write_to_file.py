import os
def write_file(working_directory, file_path, content):
    absolute_working_directory = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(absolute_working_directory, file_path))
    # Will be True or False
    valid_target_dir = os.path.commonpath([absolute_working_directory, target_file]) == absolute_working_directory
    if not valid_target_dir:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(target_file):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    
    os.makedirs(name=absolute_working_directory, exist_ok=True)

    try:
        with open(target_file, 'w') as w:
            w.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'


    except Exception as e:
        return f"Error: {e}"