import random

points = 0
chances = 5
def start():
    print("Hi everyone. Lets play rock paper siccors.")
start()
i = 0
while i <= chances:
    
    game = ["rock", "paper", "scissors"]
    pc = random.choice(game)
    player = input("enter your choice")
    if player not in game:
        print("invalid input")
        
    else:
        i+=1
        print("PC played", pc)
        if pc == "rock":
            if player == "rock":
                pass
            if player == "paper":
                points += 1
            if player == "scissors":
                points -= 1
        elif pc == "paper":
            if player == "rock":
                points -= 1
            if player == "paper":
                pass
            if player == "scissors":
                points += 1
        elif pc == "scissors":
            if player == "rock":
                points += 1
            if player == "paper":
                points -= 1
            if player == "scissors":
                pass
    
else:
    print("gameover ")
    print("you scored ", points)
