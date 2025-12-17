import os
import subprocess
def run_python_file(working_directory, file_path, args=None):
    try:
        #finds absolute path for parent directory and filepath 
        absolute_working_directory = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(absolute_working_directory, file_path))
        # Will be True or False
        valid_target_dir = os.path.commonpath([absolute_working_directory, target_file]) == absolute_working_directory
        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            f'Error: "{file_path}" is not a Python file'
        command = ["python", target_file]
        if args is not None:
            command = command.extend(args)
        returned_process = subprocess.run(args=command, capture_output=True, text=True, timeout=30)
        output = ''
        if returned_process.returncode != 0:
            output += "Process exited with code X\n"
        if returned_process.stdout is None and returned_process.stderr is None:
            return output + "No output produced"
        if returned_process.stdout is not None:
            output = output + f"STDOUT: {returned_process.stdout}\n"
        if returned_process.stderr is not None:
            output = output + f"STDERR: {returned_process.stderr}\n"
        return output

        

    except Exception as e:
        return f"Error: executing Python file: {e}"
    
