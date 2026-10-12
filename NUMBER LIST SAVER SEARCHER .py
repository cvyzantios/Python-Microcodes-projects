
#NUMBER LIST SAVER SEARCHER #
# 1. Δημιουργούμε μια κενή λίστα
# 1. Create an empty list
my_list = []

# 2. Επαναλαμβάνουμε τη διαδικασία εισαγωγής αριθμών
# 2. Repeat the process of entering numbers
while True:

    # Ζητάμε έναν αριθμό ή τον χαρακτήρα q για έξοδο
    # Ask for a number or the character q to exit
    user_input = input("Enter an integer (or q to quit): ").strip().lower()

    # Ελέγχουμε αν ο χρήστης θέλει να σταματήσει
    # Check whether the user wants to stop
    if user_input == "q":
        break

    try:
        # Μετατρέπουμε την είσοδο σε ακέραιο αριθμό
        # Convert the input into an integer
        num = int(user_input)

        # Προσθέτουμε τον αριθμό στη λίστα
        # Add the number to the list
        my_list.append(num)

    except ValueError:
        # Εμφανίζουμε μήνυμα λάθους αν η είσοδος δεν είναι ακέραιος
        # Display an error message if the input is not an integer
        print("Error! Please enter a valid integer. Try again!")
        continue

    # Ρωτάμε αν ο χρήστης θέλει να συνεχίσει
    # Ask whether the user wants to continue
    again = input("Do you want to add another number? (y/n): ").strip().lower()

    # Αν η απάντηση δεν είναι y, σταματάμε την εισαγωγή
    # If the answer is not y, stop entering numbers
    if again != "y":
        break

# 3. Εμφανίζουμε τη λίστα που δημιουργήθηκε
# 3. Display the list that was created
print("\nYour list:", my_list)

# 4. Ρωτάμε αν ο χρήστης θέλει να αναζητήσει αριθμό ή να εξέλθει
# 4. Ask whether the user wants to search for a number or exit
while True:

    # Ζητάμε y για αναζήτηση ή q για έξοδο
    # Ask for y to search or q to exit
    search_again = input(
        "\nDo you want to search for a number? (y/q): "
    ).strip().lower()

    # Αν ο χρήστης πληκτρολογήσει q, τερματίζουμε
    # If the user enters q, terminate the program
    if search_again == "q":
        print("Goodbye! :)")
        break

    # Αν η απάντηση δεν είναι y, εμφανίζουμε μήνυμα και ξαναρωτάμε
    # If the answer is not y, display a message and ask again
    if search_again != "y":
        print("Invalid choice! Enter y or q. Try again!")
        continue

    try:
        # Ζητάμε τον αριθμό που θέλει να αναζητήσει
        # Ask for the number the user wants to search for
        search_num = int(input("Enter the number to search for: "))

        # Ελέγχουμε αν ο αριθμός υπάρχει στη λίστα
        # Check whether the number exists in the list
        if search_num in my_list:

            # Ενημερώνουμε τον χρήστη ότι ο αριθμός υπάρχει
            # Inform the user that the number exists
            print(f"The number {search_num} exists in the list.")

        else:

            # Ενημερώνουμε τον χρήστη ότι ο αριθμός δεν υπάρχει
            # Inform the user that the number does not exist
            print(f"The number {search_num} does not exist in the list.")

    except ValueError:
        # Εμφανίζουμε μήνυμα λάθους για μη έγκυρο αριθμό
        # Display an error message for an invalid number
        print("Error! Please enter a valid integer. Try again!")
        continue

    # Ρωτάμε αν θέλει άλλη αναζήτηση ή έξοδο
    # Ask whether the user wants another search or wants to exit
    again = input("Search again? (y/q): ").strip().lower()

    # Αν επιλέξει q, τερματίζουμε το πρόγραμμα
    # If the user chooses q, terminate the program
    if again == "q":
        print("Goodbye! :)")
        break

    # Αν δεν επιλέξει y ή q, εμφανίζουμε μήνυμα λάθους
    # If the user chooses neither y nor q, display an error message
    if again != "y":
        print("Invalid choice! Enter y or q. Try again!")
        
        
        
  """
    # ============================================================
# TECHNIQUE 1: DYNAMIC LIST CREATION
# ΤΕΧΝΙΚΗ 1: ΔΥΝΑΜΙΚΗ ΔΗΜΙΟΥΡΓΙΑ ΛΙΣΤΑΣ
# ============================================================

# Create an empty list to store the elements.
# Δημιουργούμε μια κενή λίστα για να αποθηκεύσουμε τα στοιχεία.
my_list = []

# Use while True to repeatedly ask the user for input.
# Χρησιμοποιούμε while True για να ζητάμε συνεχώς στοιχεία.
while True:

    # Read the user's input as a string.
    # Διαβάζουμε την είσοδο του χρήστη ως συμβολοσειρά.
    user_input = input("Enter an integer (or q to quit): ").strip().lower()

    # If the user enters q, stop the loop.
    # Αν ο χρήστης εισάγει q, σταματάμε τον βρόχο.
    if user_input == "q":
        break

    try:
        # Convert the input into an integer.
        # Μετατρέπουμε την είσοδο σε ακέραιο αριθμό.
        num = int(user_input)

        # Append the number to the end of the list.
        # Προσθέτουμε τον αριθμό στο τέλος της λίστας.
        my_list.append(num)

    except ValueError:
        # Handle invalid input without terminating the program.
        # Διαχειριζόμαστε τη λανθασμένη είσοδο χωρίς να τερματίσουμε το πρόγραμμα.
        print("Error! Please enter a valid integer. Try again!")
        continue

# ============================================================
# TECHNIQUE 2: LIST SEARCH
# ΤΕΧΝΙΚΗ 2: ΑΝΑΖΗΤΗΣΗ ΣΤΗ ΛΙΣΤΑ
# ============================================================

# Ask the user for the number to search for.
# Ζητάμε από τον χρήστη τον αριθμό που θέλει να αναζητήσει.
search_num = int(input("Enter the number to search for: "))

# Check whether the number exists in the list using the 'in' operator.
# Ελέγχουμε αν ο αριθμός υπάρχει στη λίστα με τον τελεστή 'in'.
if search_num in my_list:

    # Confirm that the number was found.
    # Επιβεβαιώνουμε ότι βρέθηκε ο αριθμός.
    print(f"The number {search_num} exists in the list.")

else:

    # Inform the user that the number was not found.
    # Ενημερώνουμε τον χρήστη ότι ο αριθμός δεν βρέθηκε.
    print(f"The number {search_num} does not exist in the list.")
    
    
"""