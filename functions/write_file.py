import os

def write_file(working_directory, file_path, content):
    new_path = os.path.join(working_directory, file_path)
    abs_new_path = os.path.abspath(new_path)
    abs_working_directory = os.path.abspath(working_directory)
    parent = os.path.dirname(abs_new_path)

    if not abs_new_path.startswith(abs_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        if parent and not os.path.exists(parent):
            os.makedirs(parent, exist_ok=True)

        with open(abs_new_path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"        