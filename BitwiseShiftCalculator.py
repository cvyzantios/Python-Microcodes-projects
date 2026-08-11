var = int(input("Enter a variable: "))
right = int(input("Enter how many bits to shift right: "))
left = int(input("Enter how many bits to shift left: "))

# Μετατοπίσεις
var_right = var >> right
var_left = var << left

# Αποτελέσματα
print()
print("Variable:", var)
print("Binary:", bin(var)[2:])  ## Convert the variable to binary

print()
print("Shift left:", var_left)
print("Binary:", bin(var_left)[2:]) # Convert the variable to binary

print()
print("Shift right:", var_right)
print("Binary:", bin(var_right)[2:])# Convert the variable to binary