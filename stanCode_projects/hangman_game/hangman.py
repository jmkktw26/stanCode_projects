"""
File: hangman.py
Name:
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    word = random_word()
    print("The word looks like:", "-" * len(word))
    num_life = 7
    print("You have", num_life, "guesses left.")
    save_alpha_location = ""
    save_alpha = ""
    while True:
        alphabet = input("Your guess:")
        if alphabet.isalpha():
            if alphabet.upper() in word:
                count = 0
                print("You are correct!")
                num = str(word.find(alphabet.upper()))
                tmp_count = 0
                for i in word:  # find the repeat words
                    if i == alphabet.upper() and str(tmp_count) not in num:
                        num += str(tmp_count)
                    tmp_count += 1
                if num in save_alpha_location:  # save the position where the word you guess right
                    pass
                else:
                    save_alpha_location += num
                for i in range(len(word)):  # test whether you guess every word or not
                    if str(i) in save_alpha_location:
                        count += 1
                    if count == len(word):
                        print("You Win!!")
                        print("The word was:", word)
                save_alpha = ""
                for i in range(len(word)):  # renew the word position
                    if str(i) in num and str(i) in save_alpha_location:
                        save_alpha += word[i]
                    elif str(i) in num and str(i) not in save_alpha_location:
                        save_alpha += word[i]
                    elif str(i) not in num and str(i) in save_alpha_location:
                        save_alpha += word[i]
                    else:
                        save_alpha += "-"
                if count == len(word):
                    break
                print("The word looks like:", save_alpha)
                print("You have", num_life, "guesses left.")
            elif alphabet.upper() not in word:  # you guess the wrong word
                num_life -= 1
                if num_life != 0:
                    print("You have", num_life, "guesses left")
                    print("There is no", alphabet.upper() + "'s", "in the word")
                else:
                    print("There is no", alphabet.upper() + "'s", "in the word")
                if num_life == 0:  # if you are hung
                    print("You are completely hung :(")
                    print("The word was:", word)
                    break
                elif save_alpha_location == "":  # you guess wrong in the first time
                    print("The word looks like:", "-" * len(word))
                else:
                    print("The word looks like:", save_alpha)  # print the correct word before you guess wrong
        else:
            print("Illegal format.")


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
