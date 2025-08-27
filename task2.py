scores ={"Alice":[80,90], "Bob":[70,85], "Charlie":[95]}
running = True
while running:
    print("Enter name and score of student")
    name=input("Enter the student's name: ")
    if name.capitalize()== "Exit":
        running = False
    elif name.capitalize() in scores.keys():
        score=input("Enter the student's score: ")
        scores[name.capitalize()].append(score)
    else:
        score=input("Enter the student's score: ")
        scores[name.capitalize()]=[score]
print(scores)
