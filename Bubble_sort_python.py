# 1. Ask the user for the size of the list
size = int(input("Choose the size of the list: "))

# 2. Fill the list with numbers entered by the user
my_list = []
for i in range(size):
    num = int(input(f"Enter element {i + 1}: "))
    my_list.append(num)

print("\nOriginal list:", my_list)

# 3. Sort the list using the Bubble Sort algorithm
swapped = True
while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True

            # Swap the values
            # --- VALUE SWAPPING (SWAP) ---
            # Right side: Python first evaluates the values
            # and creates a temporary tuple in memory.
            # Left side: The values are assigned simultaneously
            # to my_list[i] and my_list[i + 1].
            # This swaps the elements (e.g. [10, 2] -> [2, 10])
            # without the need for a temporary variable.
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# 4. Print the sorted list
print("Sorted list:  ", my_list)

"""
How the swap works:

1. Python creates a temporary tuple containing:
   (my_list[i + 1], my_list[i])

2. The values are assigned simultaneously to the
   variables on the left side.

In other languages such as C++ or Java, you would need:

temp = a;
a = b;
b = temp;
"""