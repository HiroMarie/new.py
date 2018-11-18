import random

def hangman():
    word_list = ["music", "baseball", "cat", "france", "bank", "newspaper",
                 "python", "english", "car", "diary", "book", "child"]
    rand_index = random.randint(0, len(word_list) - 1)
    word = word_list[rand_index]
    wrong = 0
    stages = ["",
              "_______       ",
              "|      |      ",
              "|      |      ",
              "|      0      ",
              "|      |      ",
              "|    ／|＼    ",
              "|      |      ",
              "|     /|      ",
              "|             ",
              ]

    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman Game!")
    
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess one letter.\n"
        char = input(msg)

        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"

        else:
            wrong += 1

        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))

        if "_" not in board:
            print("\nYou win!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0:e]))
        print("You lose. The answer is {}.".format(word))

