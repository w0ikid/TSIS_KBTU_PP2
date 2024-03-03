import os

def test_path_and_extract_details(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")

        directory_name = os.path.dirname(path)
        file_name = os.path.basename(path)
        
        print(f"Directory: {directory_name}")
        print(f"Filename: {file_name}")
    else:
        print(f"The path '{path}' does not exist.")

path = "C:\\KBTU\\sem2\\pp2\\labs\\lab6\\files_and_directories_manipulation\\text.txt"

test_path_and_extract_details(path)
