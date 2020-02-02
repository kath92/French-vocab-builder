#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

def read_csv(filename):
    """
    Takes a .csv file and loades it into a dictionary
    """
    dict = {}
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for line in reader:
            # Ignore empty lines if they exist
            if len(line[0]) > 1 and len(line[1]) > 1:
                dict[line[0]] = line[1]
    file.close()
    return dict


def print_choice():
    """
    This will have to be updated by the user whilist new vocab list will be uploaded
    """
    statement = "Which set would you like to chose? \n Press 'my' for my elementary vocabulary, 'b' for basic, 'n' for nature, 'p for places: "
    return statement


def choose_dict():
    """
    Chooses vocabulary set based on user input
    """
    chosen_dict = {}
    statement = print_choice()

    while True:
        dict_choice = input(statement)

        if dict_choice.lower() == "n":
            chosen_dict = read_csv("nature.csv")
            return chosen_dict

        elif dict_choice.lower() == "b":
            chosen_dict = read_csv("basic.csv")
            return chosen_dict

        elif dict_choice.lower() == "p":
            chosen_dict = read_csv("places.csv")
            return chosen_dict

        elif dict_choice.lower() == "my":
            chosen_dict = read_csv("vocab.csv")
            return chosen_dict

        else:
            print("Incorrect input! Try again!")
            dict_choice = input("")


# learnt_words = {} # words will be appended here after 3rd correct answer occurence for this word
# skipped_words = {} # words that were skipped might be stored so that user can preview them
# favourite_dict = {} # a list of fav vocabulary?


def ask(dict_name):
    """
    Asking for the translation of a given word and verifying if correct
    """
    user_lg_choice = ""
    user_ans = ""

    while user_lg_choice.lower() != 'f' or user_lg_choice.lower() != 'e':
        user_lg_choice = input("Press 'f' if you chose to translate from French to English or 'e' to translate from English to French: ")

        if user_lg_choice.lower() == 'q':
            break

        elif user_lg_choice.lower() == 'f':
            while user_ans.lower() != 'q':
                for word, translation in chosen_dict.items():
                    print(word)

                    while True:
                        user_ans = input("")
                        if user_ans.lower() == "q":
                            return "Quitting the program... Salut!"
                        elif user_ans.lower() == "c":
                            print("The first two letters of this word are:", translation[:2], "\n", word)
                        elif user_ans.lower() == "s":
                            print("You requested to skip the word {0} which is {1}".format(word, translation))
                            break
                        elif user_ans == translation:
                            print("Bon travail! Tu connanis {0} - {1} :)".format(word, translation))
                            break
                        else:
                            print("Try again!")

        elif user_lg_choice.lower() == 'e':
                while user_ans.lower() != 'q':
                    for word, translation in chosen_dict.items():
                        print(translation)
                        while True:
                            user_ans = input("")
                            if user_ans.lower() == "q":
                                return "Quitting the program... Salut!"
                            elif user_ans.lower() == "c":
                                print("The first two letters of this word are:", word[:2], "\n", translation)
                            elif user_ans.lower() == "s":
                                print("You requested to skip the word {0} which is {1}".format(translation, word))
                                break
                            elif user_ans == word:
                                print("Bon travail! Tu connanis {0} - {1} :)".format(translation, word))
                                break
                            else:
                                print("Try again!")
        else:
            user_lg_choice = input("Invalid input. Press 'f' or 'e' to make the choice: ")


# ######### PROGRAM ##########
print("""Welcome to vocabulary builder. \nYour task is to translate the words between English (or Polish in my list) and French!
You can always press 'q' to exit,
if you feel you need a clue - press 'c'.
If you give up and want to want to skip a given word and see the answer, press 's'.
Have fun!""")

chosen_dict = choose_dict()
print(ask(chosen_dict))
