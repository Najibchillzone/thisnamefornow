import os 
import Stick_figure 
import random
import Words
import pygame
from blessed import Terminal

pygame.mixer.init()





def play_music():
    pygame.mixer.music.load('TETRIS.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(loops=-1)

def stop_music():
    pygame.mixer.music.stop()   
# Generate a random word

global random_number
random_number = random.randint(0, 9)
def getword():
    secret_word = random.choice(Words.word_list)
    return secret_word

# Function to clear terminal after input
def clear_terminal():
    # Clear the terminal (cross-platform)
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

def welcome():
    print("\033[92mHello and Welcome to the HANGMAN GAME!\033[0m")
    # Wait for the user to press "Enter"
    user_input = input("\033[92mPress Enter to continue...\033[0m")
    # Check if the input string is empty (only "Enter" was pressed)
    if user_input == "":
        clear_terminal()
        print("\033[92mYour job is to guess the secret word within 6 tries")
        print("If you fail to do so the man will be hung :( \033[0m")
        input("\033[92mPress Enter to continue...\033[0m")
        if user_input == "":
            clear_terminal()
            print("\033[92mGuess one letter at a time")
            print("Letters can't be guessed twice")
            input("Press Enter to continue...")
            if user_input == "":
                clear_terminal()
                print("If you think you know the word you can type it out")
                print("If you guess wrong the game will end!")
                print("However you will get the chance to play again\033[0m")
    else:
        print("Invalid input: Pressed key other than Enter")

# Define the well_done function
def well_done():
    print("Well done!!!")
    play_again = input("Play again ? (Y/N)")
    while len(play_again) != 1:
        play_again = input("Play again ? (Y/N)")
    if play_again.upper() == "Y":
        play_game()
    else:
        clear_terminal()
        print("Thank you for playing!")
        print("BYE...")
def try_again():
    Words.lost_response(random_number)
    play_again = input("Play again ? (Y/N)")
    while len(play_again) != 1:
        play_again = input("Play again ? (Y/N)")
    if play_again.upper() == "Y":
        play_game()
    else:
        clear_terminal()
        print("Thank you for playing!")
        print("BYE...")

def play_game():
    play_music()
    rand_word = getword()
    attempts = 6
    count = 0
    astr = "*" * len(rand_word)
    
    print(astr)
    
    while attempts > 0:
        guess = input("Guess a letter: ")
        
        # Handle one letter guesses
        if len(guess) == 1:
            if guess in rand_word:  
                updated_word = ""
                for i in range(len(rand_word)):
                    if rand_word[i] == guess:
                        updated_word += guess
                    else:
                        updated_word += astr[i]  
                astr = updated_word  
                Stick_figure.draw_stick_figure(count)
                print(astr)
                if astr == rand_word:
                    well_done()
                    return
            else:
                attempts -= 1
                count += 1
                Stick_figure.draw_stick_figure(count)
                if attempts == 0:
                    try_again()

        
        # Handle word guess
        elif len(guess) > 1:
            if guess == rand_word:
                well_done()
                return
            else:
                Words.lost_response(random_number)
                play_again = input("Play again ? (Y/N)")
                while len(play_again) != 1:
                    play_again = input("Play again ? (Y/N)")
                if play_again.upper() == "Y":
                    rand_word = getword()
                    attempts = 6
                    count = 0
                    astr = "*" * len(rand_word)
                    clear_terminal()
                    print("\033[92mLet's play again!\033[0m")
                    print(astr)
                else:
                    clear_terminal()
                    print("Thank you for playing!")
                    print("BYE...")
                    break
        else:
            print("Invalid input")
            try_again()




welcome()
play_game()

