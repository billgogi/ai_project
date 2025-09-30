import os

def get_files_info(working_directory, directory="."):
    new_path = os.path.join(working_directory, directory)
    abs_working_directory = os.path.abspath(working_directory)
    abs_new_path = os.path.abspath(new_path)
    path_list = os.listdir(abs_new_path)
    output_lines = []
    
    if not abs_new_path.startswith(abs_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_new_path):
        return f'Error: "{directory}" is not a directory'
    
    try:
        path_list = os.listdir(abs_new_path)
    except PermissionError as e:
        return f"Error: No permission to access {abs_new_path}"
    
    for item in path_list:
        full_item_path = os.path.join(abs_new_path, item)
        is_dir = os.path.isdir(full_item_path)
        try:
            file_size = os.path.getsize(full_item_path)
        except OSError as e:
            return f'Error: {full_item_path} is either inaccessible or no longer exists'
        formatted_line = f"- {item}: file_size={file_size} bytes, is_dir={is_dir}"
        output_lines.append(formatted_line)
    return "\n".join(output_lines)