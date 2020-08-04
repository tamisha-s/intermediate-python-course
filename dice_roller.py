# Tamisha Dzifa Segbefia
# August 4th, 2020

import random


def main():
    print(
        "Thank you for coming to this game! This is just a simple dice roller game that compares your roll sum to other roll sums.\n"
        "The winner is determined by the team that has the highest roll. There can be multiple winners.\n"
        "Whatever the case, we hope you have an amazing time!\n")
    
    number_of_teams = int(input('How many teams or people are there? '))

    player_scores = []
    player_names = []
    for i in range(0, number_of_teams):
        player_scores.append(0)
        user_names = input('Please enter your name or your team name: ')
        print(f'Welcome, {user_names}! Your position in the team array is {i}.\n')
        player_names.append(user_names)

    dice_rolls = int(input('How many dice would you like to roll per team? '))
    dice_size = int(input('How many sides has the dice? '))

    for i in range(0, number_of_teams):
        dice_sum = 0
        for j in range(0, dice_rolls):
            roll = random.randint(1, dice_size)
            dice_sum += roll
        player_scores[i] = dice_sum

    highest_score = max(player_scores)

    for i in range(0, number_of_teams):
        if player_scores[i] == highest_score:
            print(f'\nCongratulations, {player_names[i]}! You win this round with an amazing score of {highest_score}!')


if __name__ == "__main__":
    main()
