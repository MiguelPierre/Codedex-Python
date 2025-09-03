# PIN Verification

"""print('BANK OF CODÉDEX')

pin = int(input('Enter your PIN: '))

while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 1234:
  print('PIN accepted!')"""
  
# Guess number

"""guess = 0
tries = 0

while guess != 6 and tries < 3:
  guess = int(input("Guess the number:  "))
  tries += 1

if guess == 6:
  print("You got it!")
else:
  print("Sorry, you've used all your tries.")"""
  
# Detention

"""for i in range(100):
  print("I will not use Snapchat in class")"""
  
# 99 Bottles of beer

"""for i in range(99, 0, -1):
  print(i, "bottles of beer on the wall,", i, "bottles of beer.")
  print("Take one down, pass it around,", i-1, "bottles of beer on the wall.")"""
  
# Fizz Buzz

"""for i in range(1, 101):
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)"""
    
# Bucles anidados

"""i = 0

while i < 6:
  j = 0
  while j < 6:
    print(i * j) # j=0 * i=0, j=1 * i=0, j=2 * i=0, j=3 * i=0, j=4 * i=0, j=5 * i=0
    j = j + 1
  i = i + 1"""

"""import random

lucky_number = random.randint(1, 9)
not_found = True

while not_found:
  for i in range(1, 10):
    if i == lucky_number:
      not_found = False
      break
    else:
      print(i)

print("Yay I got my lucky number {lucky_number}! 🍀")"""

# Challenge

# Are we there yet?

answer = input("Are we there yet? ")

while answer != "yes":
    answer = input("Are we there yet? ")

# New year countdown

"""new_year_countdown = 10

for i in range(new_year_countdown, 0, -1):
    print(i)

print("Happy New Year! 🥳")"""

#Snake eyes

"""import random

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total = die1 + die2

while total != 2:
    print("Nope")
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

print("Snake eyes!")"""

# Asteriks

"""for i in range(24):
    print("* " * (i + 1))"""
    
# Sum of squares

"""number = int(input("Enter a number: "))
total = 0

for i in range(1, number + 1):
    total += i ** 2

print(total)"""

