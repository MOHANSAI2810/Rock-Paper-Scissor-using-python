import random
print("-----------------------------------")
print("Welcome to Rock Paper Scissor game")
print("To start the game press 1 and enter")
a=int(input())
if a==1:
    print("Read each and every instruction carefully")
    print("If you won the game your score will be increase by 1")
    print("If computer won the game your score will be decrease by 1")
    print("If it's a tie the score remains constant")
    count=0
    def game():
        global count
        while True: 
            print("--------The game starts now-----------")
            print("Select any one of the follwing")
            print("Rock\nPaper\nScissor")
            print("note:If your answer is rock type rock and \npress enter similarly to paper and scissor")
            print("Enter your choice")
            a=input().lower()
            d=("rock","paper","scissor")
            b=("rock","paper","scissor")
            c=random.choice(b)
            if a in d:
                if a==c:
                    print("It's a tie")
                elif(a=="rock" and c=="scissor"):
                    print("You won")
                    count+=1
                elif(a=="scissor" and c=="paper"):
                    print("You won")
                    count+=1
                elif(a=="paper" and c=="rock"):
                    print("You won")
                    count+=1
                else:
                    print("Computer has won")
                    count-=1
            else:
                print("Please select only from the above given")
            print("To play the game again press 1 and to exit the game press 2")
            z=int(input())
            if z==1:
                game()
            else:
                print("Your score is",count)
                print("Thanks for playing the game \U0001F601")
                break
            break

    game()
else:
    print("Thank you visit again!")

