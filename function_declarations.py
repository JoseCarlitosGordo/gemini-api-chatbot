from google.genai import types
from functions import get_file_content, get_files_info, run_python_file, write_to_file
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the contents of a specified file. Constrained to the working directory and found through a specific file name",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path that specifies which file contents to grab.",
            ),
        },
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the contents of a specified python file (HAS TO BE A PYTHON FILE). Strictly limited to the current working directory and descendants of the directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path that dictates which python file is run.",
            ),
             "args": types.Schema(
                type=types.Type.TYPE_UNSPECIFIED,
                description="A list of arguments to pass into the specified program. If none are provided the program will handle any errors gracefully.",
            ),
        },
    ),
)
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes the provided contents to a specified file path",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative file path that dictates where the contents of the file will be written to.",
            ),
             "content": types.Schema(
                type=types.Type.TYPE_UNSPECIFIED,
                description="The content that will be written into the file. .",
            ),
        },
    ),
)
available_functions = types.Tool(
    function_declarations=[schema_get_files_info, schema_get_file_content, schema_run_python_file, schema_write_file],
)

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    function_dictionary = {
        'get_files_info' : get_files_info.get_files_info, 
        'get_file_content' : get_file_content.get_file_content, 
        'run_python_file' : run_python_file.run_python_file, 
        'write_file' : write_to_file.write_file
                           
                           }
    called_function = function_dictionary.get(function_call_part.name)
    if called_function is None:
        return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_call_part.name,
            response={"error": f"Unknown function: {function_call_part.name}"},
        )
    ],
    )
    returned_results = called_function(working_directory='./calculator', **function_call_part.args)
    return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_call_part.name,
            response={"result": returned_results},
        )
    ],
)
    