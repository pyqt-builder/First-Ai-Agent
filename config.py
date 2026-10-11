import os 

MAX_CHARS = 10000  # Define the maximum number of characters to read
WORKING_DIR = "./calculator"  # Define the working directory for file operations
MAX_ITERATIONS = 20  # Define the maximum number of iterations for the AI agent

def str_input(file_path: str) -> str:
      with open(file_path, 'r', encoding='utf-8') as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1): # Check if there are more characters to read 
                  file_content_string += f'[... File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content_string
        
                    
        
  