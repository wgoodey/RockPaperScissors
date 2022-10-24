
import game_module


print("Welcome to Rock, Paper, Scissors!")

game_over = False
while not game_over:
    # get user input
    user = game_module.get_user_throw()
    # print user input
    print(f"You threw {user}")
    game_module.print_throw(user)

    # get computer throw
    computer = game_module.get_comp_throw()
    # print computer throw
    print(f"The computer threw {computer}")
    game_module.print_throw(computer)

    game_over = game_module.get_result(user, computer)
