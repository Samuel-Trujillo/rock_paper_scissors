import random
comp_options= ["rock", "paper", "scissors"]
your_score=0
cpu_score=0

while your_score or cpu_score < 3:
    choice= input(" BEST OF FIVE! rock, paper, scissors: ")
    comp_choice= random.choice(comp_options)
    print(f"CPU CHOSE {comp_choice}")
    if choice == comp_choice:
        print("TIE!!!")
    elif choice == "rock":
        if comp_choice== "scissors":
            your_score += 1
            print("WINNER!!")
        else:
            cpu_score += 1
            print("LOSER!!")
    elif choice == "paper":
        if comp_choice== "rock":
            your_score += 1
            print("WINNER!!")
        else:
            cpu_score += 1
            print("LOSER!!")
    elif choice == "scissors":
        if comp_choice== "paper":
            print("WINNER!!")
            your_score += 1
        else:
            cpu_score +=1
            print("LOSER!!")
    print(cpu_score)
    print(your_score)
    if cpu_score == 3:
        print("YOU LOSE")
        break
    if your_score == 3:
        print("YOU WIN")
        break





