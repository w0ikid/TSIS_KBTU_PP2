import os

def check_path_access(path):
    exists = os.path.exists(path)

    print(f"Path exists: {exists}")
    
    if exists:

        readable = os.access(path, os.R_OK)
        print(f"Path is readable: {readable}")
        
        writable = os.access(path, os.W_OK)
        print(f"Path is writable: {writable}")
        
        executable = os.access(path, os.X_OK)
        print(f"Path is executable: {executable}")
    else:
        print("Path does not exist, cannot check for readability, writability, or executability.")

path = "C:\\KBTU\\sem2\\pp2\\labs\\lab6\\files_and_directories_manipulation\\text.txt"

check_path_access(path)