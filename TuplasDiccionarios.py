# Intro

"""# Tuple (ordered, immutable)
teams = ('TeamA', 'TeamB')

# Dictionary (unordered, mutable)
basketball_player = {'name': 'LeBron James', 'team': 'Los Angeles Lakers'}

# Set (unordered, unique)
soccer_positions = {'Forward', 'Midfielder', 'Defender', 'Goalkeeper'}"""

"""genz_slang = {
    "lit": "exciting or excellent",
    "bet": "yes or okay",
    "cap": "lie or falsehood",
    "no cap": "truth or honesty",
    "flex": "to show off",
    "slay": "to succeed or impress",
    "savage": "bold or unapologetic",
    "vibe": "atmosphere or feeling",
    "stan": "to be an obsessed fan",
    "ghost": "to suddenly cut off communication"
}

print(genz_slang)"""

# Find my friends tuple

"""almeria = (36.8342, -2.4637)
granada = (37.1882, -3.6066)
bilbao = (43.2630, -2.9340)
madrid = (40.4168, -3.7038)

print("Almeria:", almeria)
print("Granada:", granada)
print("Bilbao:", bilbao)
print("Madrid:", madrid)"""

# Met museum dictionary

"""artifact = {
    "name": "The Starry Night",
    "artist": "Vincent van Gogh",
    "period": "Post-Impressionism",
    "date": 1889
}

print(artifact)"""

# Fruit cart set

"""set_1 = {"apple", "banana", "cherry"}
set_2 = {"banana", "dragonfruit", "elderberry"}

union_set = set_1.union(set_2)
intersection_set = set_1.intersection(set_2)

print("Union:", union_set)
print("Intersection:", intersection_set)"""


# Post-game stats

player_1 = {
    "name": "Jose",
    "position": "Forward",
    "jersey number": 10,
    "goals": 4,
    "assists": 1
}

player_2 = {
    "name": "Pedro",
    "position": "Defender",
    "jersey number": 4,
    "goals": 1,
    "assists": 2
}

player_3 = {
    "name": "Juan",
    "position": "Goalkeeper",
    "jersey number": 1,
    "goals": 0,
    "assists": 0
}

print([player_1["position"], player_2["position"], player_3["position"]])
player_3["goals"] = 1
print(sum([player_1["goals"], player_2["goals"], player_3["goals"]]) / 3)