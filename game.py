import random
import time
import sys

from draw import draw_d20, draw_d6, draw_d4

def print_dramatic_text(text: str, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def check_player_alive(lives: int) -> None:
    if lives <= 0:
        print_dramatic_text('You died')
        sys.exit()

if __name__ == '__main__':
    # create character by collecting user input (name + class)
    # print character sheet
    # specify roll that must be beat and enemy initiative by collecting user input
    # any buffs / debuffs?
    # any critical success / failure?

    print_dramatic_text('Welcome to my random trivia game!')

    # the player starts with three lives and loses one for each wrong answer
    lives = 3
    answer = input('What is 12 times 6? ')
    if answer == '72':
        print_dramatic_text('correct')
    else:
        print_dramatic_text('Incorrect')
        lives -= 1
        check_player_alive(lives)
    answer = input('What is the fastest animal in the world? ')
    if answer.lower() == 'falcon':
        print_dramatic_text('correct')
    else:
        print_dramatic_text('Incorrect')
        lives -= 1
        check_player_alive(lives)
    answer = input('What color is the sky? ')
    if answer.lower() == 'blue':
        print_dramatic_text('correct')
    else:
        print_dramatic_text('Incorrect')
        lives -= 1
        check_player_alive(lives)
    
    questions = [
        'What is the largest planet?',
        'What is the slowest animal in the world?'
    ]

    answers = [
        'jupiter',
        'banana slug'
    ]

    position = random.randint(0, 1)
    answer = input(questions[position] + ' ')
    if answer.lower() == answers[position]:
        print_dramatic_text('correct')
    else:
        lives -= 1
        check_player_alive(lives)
        print_dramatic_text('incorrect')

    print_dramatic_text('Congratulations you have completed the trivia game!')