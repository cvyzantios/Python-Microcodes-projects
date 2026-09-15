hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
x = int(input("Choose what position of list you want to change (0-4): "))
# Step 1: replace the middle number with an integer entered by the user.
hat_list[x] = int(input("Enter a new integer: "))


# Step 3: print the length of the existing list.
print(len(hat_list))

print(hat_list)