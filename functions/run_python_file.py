import os 
import subprocess

def run_python_file(working_directory: str, file_path: str, args:list[str] | None = None) -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)
        absolut_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))
        if os.path.commonpath([abs_working_dir, absolut_file_path]) != abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(absolut_file_path):
            return f'Error: Cannot run "{file_path}" as it is a directory'
        if not file_path.endswith('.py'):
            return f'Error: Cannot run "{file_path}" is not a Python file'
        if not os.path.isfile(absolut_file_path):
            return f'Error: Cannot run "{file_path}" does not exist'

        command =["python3" , absolut_file_path]
        if args:
            command.extend(args)

        subprocess_result = subprocess.run(command, capture_output=True, text=True, timeout=30)

        output = ""
        if subprocess_result.returncode != 0:
            output += f"Process exited with code {subprocess_result.returncode}\n"  
        if subprocess_result.stdout:
            output += f"STDOUT:\n{subprocess_result.stdout}\n"                
        if subprocess_result.stderr:
             output += f"STDERR:\n{subprocess_result.stderr}\n"
        if not subprocess_result.stdout and  not subprocess_result.stderr:
            output += f"No output produced"

        return output 
            
           
        
    except Exception as e:
        return f"Error: running file: {e}"



schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a specified Python file within the working directory and returns its output",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python file to run, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Optional list of arguments to pass to the Python script",
                },
            },
            "required": ["file_path"],
        },
    },
}
  
        
          
            




    
                                  
                         
                       
                    
                   
     