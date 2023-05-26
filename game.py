import random
user_point=0
computer_point=0

while True:
 possible_choices=["rock","scissors","paper"]
 user_input=input("Enter your choice(rock,paper,scissors)")
 computer_choice=random.choice(possible_choices)

 print(f"you choose {user_input}, computer choose {computer_choice}")

 if user_input==computer_choice:
    print(f"It's draw because both selected {user_input}")
 elif user_input=="rock":
    if computer_choice=="scissors":
        print("User wins, rock will break the scissors")
        user_point +=1
    else:
        print("User lose, Paper will cover the rock")
        computer_point +=1

 elif user_input=="paper":
    if computer_choice=="rock":
        print("User wins, Paper will cover rock")
        user_point +=1

    else:
        print("User lose, Scissors will cut paper")
        computer_point +=1


 elif user_input=="scissors":
    if computer_choice=="paper":
        print("User wins, Scissors will cut paper")
        user_point +=1
    else:
        print("User lose, rock will break scissors")
        computer_point +=1

 play_again = input("Do you want to play more?(y/n)")
 if play_again.lower() != "y":
   break
print("Game over")
print(f"Points are : User points {user_point}, Computer points {computer_point}")
