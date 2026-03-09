"""
Guest the random number

Steps:
- Number of players
- User enter their name
- How many turns do you want to play, min 1 max 3
- Each user starts with 50pts in total.
- In each turn the user has 1 attemp to put a number between 1 to 10
- If the random number is equal to user number, the user wins the double randon number points
- If not, the user loss the random number generate point 
- When the game end, the console shows a table with the total points from each user

Author: Hernan Araya Lopez
Date: 8-03-2026
"""

# Import random library
import random 
 


# Initialize variables
user_option = 0
players_number = 0
players_dictionary = {}
players_final_results = {}
player_points = []
copy_player_points = []




while user_option != 2:
    
    try:
        print("""
            Welcome to Guess the Random Number..
            1. Start the game
            2. Exit
            Please select an option:
            """)
        user_option = int(input())

        if user_option == 1:
            print("How many players want to play?: ")
            players_number = int(input())

            # Loop for the players to enter their names
            for player in range(players_number) :
                print(f"\nPlayer# {player+1}")
                name = input("Enter your name: ")
                print(f"\nHello {name}, try to guess the number!")

                # Save the name of the player and value into dictionary
                players_dictionary[name] = int(50)

            
            # Loop for iterate the dictionary of players
            for key, value in players_dictionary.items():
                
                # Loop for turns
                for turn in range(1, 4):

                    # Generate the random number
                    rand_num = random.randint(1, 10)  


                    print(f"\nTurn # {turn}, Player: {key}")
                    print("Please enter a number: ")
                    user_number = int(input())

                    # Condition to compare the user_number and Random number generated
                    if user_number == rand_num:
                        print(f"You win {rand_num * 2}pts")
                        print(f"Random number is {rand_num}")
                        value = value + (rand_num * 2)
                    else:
                        print(f"You loss {rand_num}pts")
                        print(f"Random number is {rand_num}")
                        value = value - rand_num
                        
                    print(f"total points: {value}")
                    player_points.append(value) # Add values into list

                    copy_player_points = player_points.copy() # Generate a copy of list
             
                players_final_results[key] = copy_player_points
                player_points.clear() # Clear all list

            print("\n")

            #Loop for showing the final results
            for keys, values in players_final_results.items():
                print(f"player: {keys}, points: {values}")

        elif user_option == 2:
            print("Exit the game....")
            break
        
       
    except Exception as e:
       print(f"Incorrect value. Please try again {e}")



