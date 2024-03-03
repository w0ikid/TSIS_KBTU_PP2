def count_lines(filename):
    line_count = 0
    with open(filename, 'r') as file:
        for line in file:
            line_count += 1
    return line_count

filename = "C:\\KBTU\\sem2\\pp2\\labs\\lab6\\files_and_directories_manipulation\\text.txt"
print(f"The file has {count_lines(filename)} lines.")
