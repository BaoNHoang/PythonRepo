# FIXME 1: Complete the compare_answers function
def compare_answers(u1, u1a, u2, u2a):
    if (u1a == 'rock' or u1a == 'scissors' or u1a == 'paper') and (u2a == 'rock' or u2a == 'scissors' or u2a == 'paper'):
        if u1a == u2a:
            return "It's a tie!"
        elif u1a == 'rock' and u2a == 'paper':
            return "Paper wins! Good job " + u2
        elif u1a == 'paper' and u2a == 'rock':
            return "Paper wins! Good job " + u1
        elif u1a == 'paper' and u2a == 'scissors':
            return "Scissors win! Good job " + u2
        elif u1a == 'scissors' and u2a == 'paper':
            return "Scissors win! Good job " + u1
        elif u1a == 'scissors' and u2a == 'rock':
            return "Rock wins! Good job " + u2
        elif u1a == 'rock' and u2a == 'scissors':
            return "Rock wins! Good job " + u1
    else:
        return "Max made an invalid choice! You have not entered rock, paper or scissors."

if __name__ == "__main__":
    # FIXME 2a: Prompt the user to input the name of player 1
    name1 = input("What's the first player's name? ")
    # FIXME 2b: Prompt the user to input the name of player 2
    name2 = input("And the second player's name? ")
    # FIXME 2c: Prompt the user to input the choice of player 1
    choice1 = input(f"{name1}, do you want to choose rock, paper or scissors? ")
    # FIXME 2d: Prompt the user to input the choice of player 2
    choice2 = input(f"{name2}, do you want to choose rock, paper or scissors? ")
    # FIXME 2e: Call the function and print the result of the game
    print(compare_answers(name1, choice1, name2, choice2))

