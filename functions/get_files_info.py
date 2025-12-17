import os
def get_files_info(working_directory, directory="."):
    absolute_working_directory = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(absolute_working_directory, directory))
    # Will be True or False
    valid_target_dir = os.path.commonpath([absolute_working_directory, target_dir]) == absolute_working_directory
    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    try:
        contents_directory = os.listdir(target_dir)
        returned_string = ""
        for item in contents_directory:
                returned_string += f"  - {item}: file_size={os.path.getsize(target_dir + '/'+ item)}, is_dir={os.path.isdir(target_dir+ '/'+ item)} \n"

    except Exception as e:
        return f"Error: {e}"
    return returned_string

