import os 
from config import str_input

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.abspath(os.path.join(working_directory, file_path))
        if os.path.commonpath([abs_working_dir, target_file]) != abs_working_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f"Error: '{file_path}' is not a file"

        file_content = str_input(target_file)  # function to read the file content with a maximum character limit // in config.py
        return file_content
    except Exception as e:
        return f"Error: reading file: {e}"
       

        
        
        