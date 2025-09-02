gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

q1 = int(input("Do you like Dawn or Dusk? \n\t 1) Dawn \n\t 2) Dusk\n"))
q2 = int(input("When I’m dead, I want people to remember me as: \n\t 1) The Good \n\t 2) The Great \n\t 3) The Wise \n\t 4) The Bold\n"))
q3 = int(input("Which kind of instrument most pleases your ear? \n\t 1) The Violin \n\t 2) The Trumpet \n\t 3) The Flute \n\t 4) The Drum\n"))

if q1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif q1 == 2:
    hufflepuff += 1
    slytherin += 1

if q2 == 1:
    hufflepuff += 2
elif q2 == 2:
    slytherin += 2
elif q2 == 3:
    ravenclaw += 2
elif q2 == 4:
    gryffindor += 2

if q3 == 1:
    slytherin += 4
elif q3 == 2:
    hufflepuff += 4
elif q3 == 3:
    ravenclaw += 4
elif q3 == 4:
    gryffindor += 4

if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
    print("You belong to Gryffindor!")
elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
    print("You belong to Ravenclaw!")
elif hufflepuff > gryffindor and hufflepuff > ravenclaw and hufflepuff > slytherin:
    print("You belong to Hufflepuff!")
elif slytherin > gryffindor and slytherin > ravenclaw and slytherin > hufflepuff:
    print("You belong to Slytherin!")