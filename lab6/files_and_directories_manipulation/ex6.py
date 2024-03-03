for char in range(65, 91):
    filename = f"{chr(char)}.txt"
    with open(filename, 'w') as file:
        file.write(f"This is the file {chr(char)}.txt")


