import random
import itertools
#Computer Gen ( Generates a Value for what the computer pics)
def r_p_s():
    #this function picks a number between 1 and 3. 
    number_gen = random.randrange(1,4)
     #it then returns a Value (R P or S) that is based off ther picked number   
        
    if number_gen == 1:
        computer_response = "Rock"
        
    elif number_gen == 2:
        computer_response = "Scissors"
        
    elif number_gen == 3:
        computer_response = "Paper"
    return computer_response 

#yes/no checker is used whenever a question comes up that needs to be either true or false
def yes_no(question,yes, no, error):
    
    # Lists Used in Yes_No Checker    
    yes_answers = ["y","yes"]
    no_answers = ["n", "no"]
    
    #This runs a loop till it returns a response
    valid = False
    while not valid:

        response = input (question).lower()

        if response not in yes_answers and response not in no_answers:
            print(error)
        elif response in yes_answers:
            print(yes)
            response = True
            return response
        elif response in no_answers:
            print(no)
            response = False
            return response


#Statement_Gen is for all the fancy decorations and and stuff.
def statement_gen(statement, decoration,lines,dec_num,del_num) :
    #(Statement is what you say)(This is the charecter for your lines to be "^")(This is how many rows.)(This is how long the decor4ation is on either side)(This is how many charecters need to be deleted)
    sides = decoration * dec_num
    statement = ("{} {} {}".format(sides,statement,sides))
    if lines == 3:
        #this is what happens when you wantg three rows
        
        topbottomlenth = len(statement) - del_num # Number cannot * a string in the same variable
        topbottomv2 = topbottomlenth * decoration 

        print(topbottomv2)
        print(statement)
        print(topbottomv2)

        #This is what happens when you want only one row
        
    else:
        print(statement)
    
    return ""


#Rock Paper Scissors Checker checks that the users input is valid and then detremines if the pklayer wins or not.
def r_p_s_PI(question,Rock_PI, Paper_PI,Scissors_PI, error,save_data_inner):
    
    # Lists Used in Yes_No Checker    
    rock = ["rock","r"]
    scissors = ["scissors","s"]
    paper = ["paper","p"]
    cancel = "xxx"

    #This code joins all the lists together to see if its a valid answer or not.
    valid_var = ["Valid Answers",]
    valid_var = list(itertools.chain(rock,scissors,paper))
    valid_var.append(cancel)
    
    
    
    valid = False
    while not valid:
        
        response = input (question).lower()
        print("\n\n")
        if response not in valid_var:
            print(error)
        elif response in rock:
            statement_gen(Rock_PI,"^", 3,5,9)
            return response
        elif response in scissors:
            statement_gen(Scissors_PI,"^", 3,5,9)
            return response
        elif response == cancel:
            win_rate = (var_win / rounds_played) * 100 
            print("\nYou have a win rate of : {}%\nThats all your rounds for today!\n".format(win_rate))
            # this is for savig the file if "xxx" is called
            if save_data_inner == True:
                save_or_not = yes_no("would you like to save your score to be loaded again in the future?","Save Data is saved","Save data will not be saved","That is a invalid answer, Valid answers aree Yes or no")
                if save_or_not == True:
                    file = open('read_write_score.txt','w')
                    file.write("{}\n{}\n{}".format(var_win,var_loss,var_tie))



            print("\n\nThanks For Playing")
            quit()
        elif response in paper:
            statement_gen(Paper_PI,"^", 3,5,9)
            return response
        
#num check checks to see if a input is a whole valid number.
def num_check(question, error):

    valid = False
    while not valid:
         try:
             response = int(input(question))
             if 0 < response:
                 return response
             else:
                 print(error)
         except ValueError:
             print(error)


#runs game and odds this determines if you win or not.
def game_console(win,loss,tie,win_count,loss_count,tie_count,save_data_middle):
    player_input =  r_p_s_PI("What do you choose?","You Picked \x1B[33mROCK!\x1B[0m","You Picked \x1B[32mPAPER\x1B[0m","You picked \x1B[31mSCISSORS\x1B[0m","Uh oh, Thats not a valid awnser.\nValid awnsers include: Rock, Paper, Scissors, OR XXX to quit",save_data_middle)
    com_play = r_p_s()
    input("\n\nBut what did the computer choose? ")
    print("The computer picked \x1B[36m{}\x1B[0m\n\n".format(com_play))
    
    rock_list =["rock","r"]
    scissors_list=["scissors","s"]
    paper_list=["paper","p"]
    
    #this is are the conditions for winning and losing. (And tyeing)
    if player_input in rock_list and com_play == "Scissors" or player_input in scissors_list and com_play == "Paper" or  player_input in paper_list and com_play == "Rock":
        statement_gen(win,"^",3,10,9)
        win_count += 1
    elif player_input in rock_list and com_play == "Paper" or player_input in scissors_list and com_play == "Rock" or player_input in paper_list and com_play == "Scissors":
        statement_gen(loss,"^",3,10,9)
        loss_count += 1
    elif player_input in rock_list and com_play == "Rock" or player_input in scissors_list and com_play == "Scissors" or player_input in paper_list and com_play == "Paper":
        statement_gen(tie,"^",3,10,9)
        tie_count += 1
    #Returns the score to the main routine.
    score = [win_count,loss_count,tie_count]
    return score
    
    
    
    
#--------- Main Routine ---------
#These determikne the game modes
rounds = 1
load_data = False
save_data_outer = False
#Woould you like to play infinite m0de or not
infinite_mode = yes_no("Would you like to play infinte mode?","Infinite mode set to True","Infinte mode set to false","That is a invalid answer.\nValid answers are Yes or No")
print("\n--------------------\n")
#If you dont wamt to p[lay infinite mode then they ask how many runds you want to play]
if infinite_mode == False:
    rounds = num_check("How many rounds would you like to play?","Sorry that is not a valid answer.\nA valid answer is a whole number.")
#This asks if you would like to load save data
if infinite_mode == True:
    load_data = yes_no("Would you like to load the previous score for Rock-paper-Scissors in infinite mode? ", "Previous score loaded","Previous score not loaded","That is a invalid answer, Valid answers include Yes or no")
#Loads the save file
if load_data == True:
    file = open('read_write_score.txt')
    contents = file.readlines()
    var_win = int(contents[0])
    var_loss = int(contents[1])
    var_tie = int(contents[2])
    save_data_outer = True
#If not loaded this resets the score.
else:
    var_win = 0
    var_loss = 0
    var_tie = 0
print("\n\n")
statement_gen("Game Begins","^",1,10,0)
print("\n\n")
#Game console loop
while 0 < rounds or infinite_mode == True:
    #Runs a variable that determines if the player wins or not
    score = game_console("You \x1B[32mWin\x1B[0m","You \x1B[31mLose\x1B[0m","You \x1B[33mtie\x1B[0m",var_win,var_loss,var_tie,save_data_outer)
    
    #pullsa the score from the list
    var_win = score[0]
    var_loss = score[1]
    var_tie = score[2]
    rounds_played = var_win + var_loss + var_tie
    
    print("\nWins: {}, Losses: {}, Ties: {}.\n---------------------\n\n".format(var_win,var_loss,var_tie))
 # This slowly removes the rounds, if not in infinite mode.
    if infinite_mode == False:
        rounds = rounds - 1
#Calculates the win rate.
if var_win >= 1:    
    win_rate = (var_win / rounds_played) * 100 
    print("\nYou have a win rate of : {}%\nThats all your rounds for today!".format(win_rate))
else:
    print("Your win rate is 0%")











        
