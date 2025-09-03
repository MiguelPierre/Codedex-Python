# File Handling

# This opens diaries file for writing
file = open('diaries.txt', 'w')

file.write('Hello, World! 🌎\n') # \n means new line
file.write('Tengo hambre! 🌎\n')
file.write('Bye, World! 🌎')

file.close()

# Opening Files

file = open(file_path, mode)  # Open the file with the specified mode

# Modes: 'r' (read), 'w' (overwrite), 'a' (append), 'b' (binary), 't' (text)

lines = ['This is a line.\n', 'This is the next line.\n']

file.writelines(lines)  # Write multiple lines to the file

