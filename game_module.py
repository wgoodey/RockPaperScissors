import random

options = ["rock", "paper", "scissors"]


def print_throw(throw):
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    if throw == "rock":
        print(rock)
    elif throw == "paper":
        print(paper)
    else:
        print(scissors)


def get_user_throw():
    user_choice = ""
    while user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
        user_choice = input('What do you want to throw? Type "rock", "paper", or "scissors"\n').lower()
    return user_choice


def get_comp_throw():
    element = random.randint(0, len(options) - 1)
    return options[element]


def get_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a draw. Throw again")
        return False

    if user_choice == "rock":
        if computer_choice == "paper":
            print("You lose!")
        else:
            print("You win!")

    if user_choice == "paper":
        if computer_choice == "scissors":
            print("You lose!")
        else:
            print("You win!")

    if user_choice == "scissors":
        if computer_choice == "rock":
            print("You lose!")
        else:
            print("You win!")

    return True
