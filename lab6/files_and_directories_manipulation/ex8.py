def delete_file(file_path : str) -> None:
    import os

    if os.path.exists(file_path):
        print("File exist.")
        if os.access(file_path, os.W_OK):
            print("File is accessible.")
            try:
                os.remove(file_path)
                print("File is deleted.")
            except Exception as e:
                print(f"Could not delete the file.\nError: {e}")
        else:
            print("File is not accessible.")
    else:
        print("File does not exist.")

    return None

delete_file("file_to_delete.txt")
