import random
def hangman():
    word = random.choice(['abuja', 'rivers', 'lagos', 'jos', 'calabar', 'imo'])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    gueses = ''
    while len(word) > 0:
        main = ""

        for letter in word:
            if letter in gueses:
                main = main + letter
            else:
                main = main + "_" + ""

        if main == word:
            print(main)
            print("You won!!!")
            break

        print("Guess the word: ", main)
        guess = input()

        if guess in validLetters:
            gueses = gueses + guess
        else:
            print("enter a valid character")
            guess = input()

        if guess not in word:
            turns -= 1
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break
name = input("Type your name: ")
print("Welcome ", name)
print("---------------")
print("Guess the right word in less than 10 entries ")
hangman()
print()