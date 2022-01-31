import random
number=[]
chances=0
def Number():
    for i in range (5):
        a=random.randrange(0,9)
        number.append(a)
def playgames():
    global chances
    chances+=1
    cows=0
    bulls=0
    print(number)
    choice=input("please enter 5 digit number")
    guess=[]
    for i in range(5):
        guess.append(int(choice[i]))
    for i in range(5):
        for j in range(5):
            if (guess[i])==number[j]:
                cows+=1
    for x in range(5):
        if guess[x]==number[x]:
            bulls+=1
    print("bulls",bulls)
    print("cow",cows)
    if bulls==5:
        print("WOW! you won this game")
    if bulls!=5:
      print("sorry please try again")
      playgames()
Number()
playgames()