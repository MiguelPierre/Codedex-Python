# File operations
"""
file_path = 'example.txt'

try:
    file = open(file_path, 'r')
    # Perform operations on the file
finally:
    file.close()
# Reading from a file using read() method
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
  
# File cursor
  
# Moving the file cursor using seek()
with open('example.txt', 'r') as file:
    file.seek(10)  # Move to the 10th byte
    content = file.read()
  
# Truncating a file
with open('example.txt', 'a') as file:
    file.truncate(20)  # Limit the file size to 20 bytes
    print("File truncated to 20 bytes.")
"""  
# Exercises

sent_message = 'Hey there! This is a secret message.'

with open('sent_message.txt', 'w') as file:
    file.write(sent_message)
  
with open('sent_message.txt', 'r+') as file:
    # Read the sent message from the file
    original_message = file.read()
      
    # Move the cursor to the beginning of the file
    file.seek(0)
  
# Modify the message to simulate unsending
unsent_message = 'This message has been unsent.'

with open('sent_message.txt', 'a') as file:
    file.truncate(29)
    file.write(unsent_message)
    print(unsent_message)