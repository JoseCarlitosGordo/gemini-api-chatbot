from google.genai import types

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