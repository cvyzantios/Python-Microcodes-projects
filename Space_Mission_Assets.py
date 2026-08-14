Spaceships = [("cruisers", "mothership", "starfighters", "Unmaned")]
Rovers = [("transportation", "exploration", "tank", "Ground Drone")]
People = [("Scientist", "warriors", "pilots", "Personel")]

while True:

    Kinds = {
        's': Spaceships,
        'p': People,
        'r': Rovers
    }

    # Take the user's choice
    print('**************SPACE MISSION ASSETS**************************** ')
 
    user_input = input(
        "Choose the asset of mission "
        "(s: Spaceships, p: People, r: Rovers): "
    ).lower()

    # Get the selected list
    selected_Kinds = Kinds.get(user_input, [])

    # Display the selected category
    for Kind in selected_Kinds:
        print(Kind)

    # Ask if the user wants to try again
    repeat = input(
        "\nDo you want to try again? (y/n): "
    ).lower()

    if repeat != 'y':
        print("Goodbye!!!! :)")
        break