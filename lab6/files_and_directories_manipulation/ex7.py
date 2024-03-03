source_file_path = 'source.txt'
destination_file_path = 'destination.txt'

with open(source_file_path, 'r') as source_file, open(destination_file_path, 'w') as destination_file:
    content = source_file.read()

    destination_file.write(content)

print("Copied")