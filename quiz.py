import random

name = input("please enter you name")
print("welcome",name,"to the math quiz")
quistions = 0
score =0
while quistions <=3:
    n1 = random.randint(1,25)
    n2 = random.randint(1, 25)
    op = random.randint(1,3)
    if op == 1:
        print("whats ",n1, " * ", n2)
        answer = int(input("please solve the question above"))
        if answer == (n1 * n2):
            print("you are right")
            score+=1
            quistions +=1
        else:
            print("you are wrong")
            quistions += 1
    if op == 2:
        print("whats ",n1, " - ", n2)
        answer = int(input("please solve the question above"))
        if answer == (n1 - n2):
            print("you are right")
            score += 1
            quistions +=1
        else:
            print("you are wrong")
            quistions +=1
    if op == 3:
        print("whats ",n1, " + ", n2)
        answer = int(input("please solve the question above"))
        if answer == (n1 + n2):
            print("you are right")
            score += 1
            quistions +=1
        else:
            print("you are wrong")
            quistions +=1
print("your score is ", score,"/4")