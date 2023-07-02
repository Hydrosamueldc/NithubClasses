
from random import choice 
user_score = 0
computer_score = 0
options = ["rock", "paper", "scissors"]

while True:
    computer = choice(options) # get computer play
    user = input("\nEnter any one of this 'rock, paper , scissors' And use 'q' or 'quit' to end the game : ").lower()
    if user in ["q", "quit"] :
        print("Thanks for playing.... The end")
        if user_score == computer_score:
            print(f"No victor No vanquish... \nyour final score is = {user_score} and\ncomputer final score = {computer_score} ")
        elif user_score > computer_score:
            print(f"WINNER....\nyour final score is = {user_score} and\ncomputer final score = {computer_score} ")
        elif user_score < computer_score: 
            print(f"YOU LOSE TRY AGAIN NEXT TIME....\nyour final score is ={user_score} and\ncomputerfinal score ={computer_score} ")
        break

    elif user not in  options :
         print("INVALID INPUT")

    else:
        if user == computer:
            print("it's is a tie")
            updated_score = f"computer:{computer}\nuser:{user}\ncomputer score = {computer_score}\nyour score = {user_score}"
            print(updated_score)

        if user == "rock" and computer == "scissors":
            print("you win")
            user_score += 10
            updated_score = f"computer:{computer}\nuser:{user} \ncomputer score = {computer_score} \nyour score = {user_score}"
            print(updated_score)

        if user == "rock" and computer == "paper":
            print("you lose")
            computer_score+=10
            updated_score = f"computer:{computer}\nuser:{user}\ncomputer score = {computer_score}\nyour score = {user_score}"
            print(updated_score)
            
        if user == "scissors"  and computer == "paper":
            print("you win")
            user_score += 10
            updated_score = f"computer:{computer}\nuser:{user}\ncomputer score = {computer_score}\nyour score = {user_score}"
            print(updated_score)
           
        if user == "scissors"  and computer == "rock":
            print("you lose")
            computer_score += 10
            updated_score =f"computer:{computer}\nuser:{user}\ncomputer score = {computer_score}\nyour score = {user_score}"
            print(updated_score)

           
        if user == "paper"  and computer == "rock":
            print("you win")
            user_score += 10
            updated_score = f"computer:{computer}\nuser:{user}\ncomputer score = {computer_score}\nyour score = {user_score}"
            print(updated_score)

           
        if user == "paper"  and computer == "scissors":
            print("you lose")
            computer_score += 10
            updated_score = f"computer:{computer}\nuser:{user} \ncomputer score = {computer_score}\nyour score = {user_score}"
            print(updated_score)









