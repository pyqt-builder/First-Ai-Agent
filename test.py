import os 

def get_files_info(working_directory: str, directory: str = ".") -> str:
   import os 

def get_files_info(working_directory: str, directory: str = ".") -> str:
    working_directory = "calculator"
    directory = "pkg"
    combined_path = os.path.normpath(os.path.join(working_directory, directory))
    path = os.path.abspath(combined_path)
    valid_path = os.path.commonpath([combined_path, path]) == os.path.abspath(working_directory)
