import os 



def write_file(working_directory: str, file_path: str, content: str) -> str:
     try:
            abs_working_dir = os.path.abspath(working_directory)
            target_file = os.path.abspath(os.path.join(abs_working_dir, file_path))
            if os.path.commonpath([abs_working_dir, target_file]) != abs_working_dir:
                return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
            
            if os.path.isdir(target_file):
                return f'Error: Cannot write to {file_path} as it is a directory'
            parent_directory = os.path.dirname(target_file)
            os.makedirs(parent_directory, exist_ok=True)

            with open(target_file,'w') as f:
                f.write(content)
            return f"Successfully wrote to '{file_path}' ({len(content)} characters written)"

     except Exception as e:
          return f"Error: writing file: {e}"



schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes content to a file in the specified working directory and returns a success or error message",
        "parameters": {
            "type": "object",
            "properties": {
                "working_directory": {
                    "type": "string",
                    "description": "The working directory"
                },
                "file_path": {
                    "type": "string",
                    "description": "The path to the file to write"
                },
                "content": {
                    "type": "string",
                    "description": "The content to write to the file"
                }
            },
            "required": ["working_directory", "file_path", "content"]
        }
    }
}
