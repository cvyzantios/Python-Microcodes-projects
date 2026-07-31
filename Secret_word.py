
secret_word="chupacabra"
guess_word = input("Enter secret word: ")

while guess_word != secret_word:

    if guess_word == '0':
        print("Stop Game")
        break
        

    else:
        print("Wrong word")

    guess_word = input("Enter a word again: ")


if guess_word == secret_word:
    print("You've successfully left the loop.")