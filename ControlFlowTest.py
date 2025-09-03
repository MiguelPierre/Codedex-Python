# Restaurant Review

"""rating = float(input("Enter your rating (1-5): "))

if rating > 4.5:
    print("Extraordinary")
elif rating > 4:
    print("Excellent")
elif rating > 3:
    print("Good")
elif rating > 2:
    print("Fair")
else:
    print("Poor")"""

# Grade Evaluation

"""grade = int(input("Enter your grade (9-12): "))

if grade == 9:
    print("Freshman")
elif grade == 10:
    print("Sophomore")
elif grade == 11:
    print("Junior")
elif grade == 12:
    print("Senior")
else:
    print("TBD")"""
    
# Snapple Facts

"""import random

fact = random.randint(0, 5)
if fact == 0:
    print("Flamingos turn pink from eating shrimp")
elif fact == 1:
    print("The only food that doesn't spoil is honey.")
elif fact == 2:
    print("Shrimp can only swim backwards.")
elif fact == 3:
    print("A taste bud's life span is about 10 days.")
elif fact == 4:
    print("It is impossible to sneeze while sleeping.")
elif fact == 5:
    print("It is illegal to sing off-key in North Carolina.")"""
    
# Seasons of the year

"""month = int(input("Enter a month (1-12): "))

if month == 1 or month == 2 or month == 3:
    print("Winter 🌨️")
elif month == 4 or month == 5 or month == 6:
    print("Spring 🌱")
elif month == 7 or month == 8 or month == 9:
    print("Summer 🌻")
elif month == 10 or month == 11 or month == 12:
    print("Autumn 🍂")
else:
    print("Invalid")"""
    
# Planet weights

earth_weight = float(input("Enter your weight on Earth: "))
planet_number = int(input("Enter a planet number (1-7): "))

if planet_number == 1:
    destination_weight = earth_weight * 0.38
    print(f"Your weight on Mercury is: {destination_weight} kg")
elif planet_number == 2:
    destination_weight = earth_weight * 0.91
    print(f"Your weight on Venus is: {destination_weight} kg")
elif planet_number == 3:
    destination_weight = earth_weight * 0.38
    print(f"Your weight on Mars is: {destination_weight} kg")
elif planet_number == 4:
    destination_weight = earth_weight * 2.53
    print(f"Your weight on Jupiter is: {destination_weight} kg")
elif planet_number == 5:
    destination_weight = earth_weight * 1.07
    print(f"Your weight on Saturn is: {destination_weight} kg")
elif planet_number == 6:
    destination_weight = earth_weight * 0.89
    print(f"Your weight on Uranus is: {destination_weight} kg")
elif planet_number == 7:
    destination_weight = earth_weight * 1.14
    print(f"Your weight on Neptune is: {destination_weight} kg")
else:
    print("Invalid planet number.")