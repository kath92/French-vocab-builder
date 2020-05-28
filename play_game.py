import csv

def read_csv(filename):
    """
    Takes a .csv file and loades it into a dictionary
    """
    dict = {}
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for line in reader:
                # Ignore empty lines if they exist
                if len(line[0]) > 1 and len(line[1]) > 1:
                    dict[line[0]] = line[1]
    except:
        print("File not found!")
    return dict


def print_choice():
    """
    This will have to be updated by the user whilst new vocab list will be uploaded
    """
    statement = "Choose a set. Press 'my' for my vocab,'b' for basic,'n' for nature,'p' for places: "
    return statement


def choose_dict():
    """
    Chooses vocabulary set based on user input
    """
    chosen_dict = {}
    statement = print_choice()

    while True:
        dict_choice = input(statement)
        dict_choice = dict_choice.lower()
        if dict_choice == "n":
            chosen_dict = read_csv("nature.csv")
        elif dict_choice == "b":
            chosen_dict = read_csv("basic.csv")
        elif dict_choice == "p":
            chosen_dict = read_csv("places.csv")
        elif dict_choice == "my":
            chosen_dict = read_csv("vocab.csv")
        else:
            print("Incorrect input! Try again!")
            continue
        return chosen_dict


# if __name__ == '__main__':
#     my = choose_dict()
#     print(my)


def is_verified_word(chosen_dict, key, user_answer):
    flag = False
    try:
        correct_answer = chosen_dict[key]
    except:
        print("Cannot get the value by this key")
        return flag
    if user_answer == correct_answer:
        flag = True
        print(f"Bon travail! Tu connais les mots: {key} -> {chosen_dict[key]}")
    return flag


# if __name__ == '__main__':
#     d = {'un cerf': 'jelen', 'etre faché': 'obrazac sie', 'Ca prend': 'To zajmuje'}
#     verified_word = verify_word(d, "Ca prend", "To zajmuje")
#     if verified_word:
#         print("It is working ;p")


def language_is_reversed(chosen_dict):
    reversed_dictionary = dict((v, k) for k, v in chosen_dict.items())
    return reversed_dictionary


# if __name__ == '__main__':
#     d = {'un cerf': 'jelen', 'etre faché': 'obrazac sie', 'Ca prend': 'To zajmuje'}
#     d2 = language_is_reversed(d)
#     print(d2)


def play_game():
    chosen_dict = choose_dict()
    print("Loading the chosen subject for you...")
    print()
    if not chosen_dict:
        print("Oups, something went wrong. Vocabulary bank not found!")
        return

    language_choice = ""
    while True:
        language_choice = input("Press 'f' to translate from French to English or 'e' for English - French: ")
        if language_choice == 'e':
            chosen_dict_copied = chosen_dict.copy()
            chosen_dict = language_is_reversed(chosen_dict_copied)
            break
        elif language_choice == 'f':
            break
        else:
            print("Incorrect input. Press 'f'/'e' ")

    while True:
        print("Enter word translation, press 'q' to exit, 'h' to see a hint or 's' to skip current word")
        print()
        for french_word, english_word in chosen_dict.items():
            current_word_asked = french_word
            ans = ""
            while True:
                ans = input(f"{current_word_asked}: ")
                verified_word = is_verified_word(chosen_dict, current_word_asked, ans)
                if verified_word:
                    break
                elif ans == 'q':
                    print("Quitting the game!\nGoodbye!")
                    return
                elif ans == "s":
                    print(f"Skipping {current_word_asked}...")
                    break
                elif ans == "h":
                    print(f"Here are the first 2 letters of the word: {chosen_dict[current_word_asked][:2]}")
                else:
                    print("Incorrect input! Try again")
                    continue


if __name__ == '__main__':
    play_game()
