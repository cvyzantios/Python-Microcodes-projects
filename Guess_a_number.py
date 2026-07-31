secret_number = 777

print("""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

guess_number = int(input("Enter a number or type 0 to stop: "))

while guess_number != secret_number:

    if guess_number == 0:
        print("Game stopped")
        break

    else:
        print("Wrong number")

    guess_number = int(input("Enter a number again: "))


if guess_number == secret_number:
    print("Congratulations !!!")


