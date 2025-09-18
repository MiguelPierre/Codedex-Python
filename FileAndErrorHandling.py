# File Handling
""""
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

# Reading files

file = open('filename.txt', 'r')

content = file.read() # Read the entire file content

print('Using read():')
print(content)

lines = file.readlines() # Read all lines into a list

for line in lines:
  print(line, end='')

# Closing files

# Opens file to read
file = open('filename.txt', 'r')

# Closes file
file.close()

# Using 'with' statement
with open('filename.txt', 'r') as file:
  content = file.read() # File is automatically closed after this block
  print(content)
"""  
# Exercises

liked_songs = {
  'title': 'artist'
}

def write_liked_songs_to_file(songs, file_name):
  with open(file_name, 'w') as file:
    file.write('Liked Songs:\n')
    for song, artist in songs.items():
      file.write(f' {song} by {artist}\n')

liked_songs = {
    'Bad Habits': 'Ed Sheeran',
    "I'm Just Ken": 'Ryan Gosling',          
    'Mastermind': 'Taylor Swift',
    'Uptown Funk': 'Mark Ronson ft. Bruno Mars',
    'Ghost': 'Justin Bieber'   
    }