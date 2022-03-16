def rockPaperScissors(question):    
    error = "Please enter either, rock, paper or scissors\nEnter Cancel, if you would like to stop: "

    playerInput = input(question).lower()
    valid = False
    while not valid:

        if playerInput == "r" or playerInput == "rock":
            return playerInput
        elif playerInput == "s" or playerInput ==  "scissors":
            return playerInput
        elif playerInput == "p" or playerInput ==  "paper":
            return playerInput
        elif playerInput == "c" or playerInput ==  "cancel":
            return playerInput
        else:
            print(error)
            



#******** Main Routine ********
round = rockPaperScissors("Which do you choose, rock\npaper or scissors: ")

