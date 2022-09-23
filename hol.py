import math, random # Importing libraries

while True: 
    maximum = 100
    minimum = 0
    
    rand_num = int(random.randint(minimum, maximum))
    game_mode = input("Let's play higher or lower! Enter 1 to have your number guessed or 2 to guess my number: ") # Setting up a while true loop so you can play again automatically after the first time without having to rerun the program
    
    if game_mode != "1" and game_mode != "2":
        cheating = 2
        print ("invalid input")
        x, y = False, False
    
    elif int(game_mode) == 1:
        x, y = True, False
        rand = input("Press 1 for strategic mode or 2 for randomized mode") # Variables we will use for the gamemode
    
    elif int(game_mode) == 2:
        x, y, = False, True
        player = input("I have a number from " + str(minimum) + " - " + str(maximum) + ", try to guess my number") # Variables we will use for the gamemode
    
    while x == True: # Setting another while true loop for gamemode 1
        if rand == "1":
            computer = (maximum + minimum) / 2 # Sets it up the computer so that it will guess stratgically
        
        elif rand == "2":
            computer = int(random.randint(minimum, maximum)) # Sets up the computer to guess randomly
        
        elif rand != "1" and rand != "2":
            print("Invalid input.")
            cheating, y = 2, False
            break # Fail safe incase there was a misinput during the previous selection
        
        last_num = ""
        guess = input("I guess " + str(math.floor(computer)))
        
        if computer == last_num:
            cheating == 1
            break
        
        elif math.ceil(computer) == int(minimum) and guess == "l" or computer == int(maximum) and guess == "h":
            cheating = 1
            print("Hey, that's cheating! I quit.")
            break # Fail safe against cheaters
        
        elif guess.lower() == 'h' or guess.lower() == 'higher':
            minimum = int(math.floor(computer)) + 1
            last_num = computer # Changes the minimum so the computer will guess more accurately
        
        elif guess.lower() == "l" or guess.lower() == "lower":
            maximum = int(math.floor(computer))
            last_num = computer # Changes the maximum so the computer will guess more accurately
        
        elif guess.lower() == "c" or guess.lower() == "correct":
            print("Yay! I guessed your number!")
            cheating = 0
            x = False # For when the computer guesses your number correctly so it can pass on to the restart part of the program - set cheating to zero so we can go past the cheating barriers - sets x to flase so this while true loop becomes false and doesn't repeat anymore
        elif guess.lower() != "l" and guess.lower() != "h" and guess.lower() != "c" and guess != "n":
            print("That's not a valid input, please try again.")
            cheating = 2 # Failsafe for when there is a invalid input
    
    while y == True: # Sets a while true loop
        if int(player) > rand_num:
            player = int(input("lower, guess again: "))
        
        elif int(player) < rand_num:
            player = int(input("higher, guess again: "))
        
        elif int(player) == rand_num:
            print("You guessed it!")
            cheating = 0
            break
    
    if cheating == 1:
        break # Automatically ends the program if the player is caught cheating
    
    if cheating == 2:
        continue # Used to automatically start the program again if there was an invalid input
    
    check = input("enter r to play again") # Used to decide whether or not to continue the game loop
    
    if check != "r":
        print("bye then.")
        break
