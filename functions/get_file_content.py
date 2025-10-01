import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    new_path = os.path.join(working_directory, file_path)
    abs_new_path = os.path.abspath(new_path)
    abs_working_dir = os.path.abspath(working_directory)

    if not abs_new_path.startswith(abs_working_dir + os.sep):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_new_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(abs_new_path, "r") as f:
            content = f.read(MAX_CHARS + 1)
    except Exception as e:
        return f"Error: {e}"

    if len(content) > MAX_CHARS:
        content = content[:MAX_CHARS] + f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    return content
    
