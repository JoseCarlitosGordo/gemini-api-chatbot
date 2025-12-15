import os
from config import MAX_CHAR
def get_file_content(working_directory, file_path):
    absolute_working_directory = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(absolute_working_directory, file_path))
    # Will be True or False
    valid_target_dir = os.path.commonpath([absolute_working_directory, target_dir]) == absolute_working_directory
    if not valid_target_dir:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_dir):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
       with open(target_dir, "r") as f:
          file_content_string = f.read(MAX_CHAR+1)
          if len(file_content_string) > MAX_CHAR:
              returned_string = file_content_string[0:MAX_CHAR-1] + '[...File "{file_path}" truncated at 10000 characters]'
          else:
              returned_string = file_content_string

          return returned_string 

    except Exception as e:
        return f"Error: {e}"
   