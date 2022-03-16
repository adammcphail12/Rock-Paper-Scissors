import random


valid_options = ["scissors","rock","paper"]
#Computer Gen 
def r_p_s():
    
    number_gen = random.randrange(1,4)
        
        
    if number_gen == 1:
        computer_response = "Rock"
        
    elif number_gen == 2:
        computer_response = "Scissors"
        
    elif number_gen == 3:
        computer_response = "Paper"
    return computer_response 


#yes/no checker
def yes_no(question,yes, no, error):
    
    # Lists Used in Yes_No Checker    
    yes_answers = ["y","yes"]
    no_answers = ["n", "no"]
    
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


#Statement_Gen
def statement_gen(statement, decoration,lines,dec_num,del_num) :
    sides = decoration * dec_num
    statement = ("{} {} {}".format(sides,statement,sides))
    if lines == 3:
        
        
        topbottomlenth = len(statement) - del_num # Number cannot * a string in the same variable
        topbottomv2 = topbottomlenth * decoration 

        print(topbottomv2)
        print(statement)
        print(topbottomv2)

        
    else:
        print(statement)
    
    return ""


#Rock Paper Scissors Checker
def r_p_s_PI(question,Rock_PI, Paper_PI,Scissors_PI, error):
    
    # Lists Used in Yes_No Checker    
    rock = ["rock","r"]
    scissors = ["scissors","s"]
    paper = ["paper","p"]
    cancel = "xxx"
    
    valid = False
    while not valid:

        response = input (question).lower()
        print("\n\n")
        if response not in rock and response not in paper and response not in scissors and response not in cancel:
            print(error)
        elif response in rock:
            
            statement_gen(Rock_PI,"^", 3,5,9)
            return response
        elif response in scissors:
            statement_gen(Scissors_PI,"^", 3,5,9)
            return response
        elif response == cancel:
            if var_win >= 1:    
                win_rate = (var_win / rounds_played) * 100 
                print("\nYou have a win rate of : {}%\nThats all your rounds for today!".format(win_rate))
            print("\n\nThanks For Playing")
            quit()
        else:
            statement_gen(Paper_PI,"^", 3,5,9)
            return response
        
#num check
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


#runs game and odds
def game_console(win,loss,tie,win_count,loss_count,tie_count):
    player_input =  r_p_s_PI("What do you choose?","You Picked \x1B[33mROCK!\x1B[0m","You Picked \x1B[32mPAPER\x1B[0m","You picked \x1B[31mSCISSORS\x1B[0m","Uh oh, Thats not a valid awnser.\nValid awnsers include: Rock, Paper, Scissors, OR XXX to quit")
    com_play = r_p_s()
    input("\n\nBut what did the computer choose? ")
    print("The computer picked \x1B[36m{}\x1B[0m\n\n".format(com_play))
    
    rock_list =["rock","r"]
    scissors_list=["scissors","s"]
    paper_list=["paper","p"]
    
    
    if player_input in rock_list and com_play == "Scissors":
        statement_gen(win,"^",3,10,9)
        win_count += 1
    elif player_input in rock_list and com_play == "Paper":
        statement_gen(loss,"^",3,10,9)
        loss_count += 1
    elif player_input in rock_list and com_play == "Rock":
        statement_gen(tie,"^",3,10,9)
        tie_count += 1
    
    if player_input in scissors_list and com_play == "Paper":
        statement_gen(win,"^",3,10,9)
        win_count+=1
    elif player_input in scissors_list and com_play == "Rock":
        statement_gen(loss,"^",3,10,9)
        loss_count += 1
    elif player_input in scissors_list and com_play == "Scissors":
        statement_gen(tie,"^",3,10,9)
        tie_count += 1
    
    if player_input in paper_list and com_play == "Rock":
        statement_gen(win,"^",3,10,9)
        win_count+=1
    elif player_input in paper_list and com_play == "Scissors":
        statement_gen(loss,"^",3,10,9)
        loss_count += 1
    elif player_input in paper_list and com_play == "Paper":
        statement_gen(tie,"^",3,10,9)
        tie_count += 1
    score = [win_count,loss_count,tie_count]
    return score
    
    
    
    
#--------- Main Routine ---------
rounds = 1
infinite_mode = yes_no("Would you like to play infinte mode?","Infinite mode set to True","Infinte mode set to false","That is a invalid answer.\nValid answers are Yes or No")
print("\n--------------------\n")
if infinite_mode == False:
    rounds = num_check("How many rounds would you like to play?","Sorry that is not a valid answer.\nA valid answer is a whole number greater then one.")
print("\n\n")
statement_gen("Game Begins","^",1,10,0)
print("\n\n")
var_win = 0
var_loss = 0
var_tie = 0
while 0 < rounds or infinite_mode == True:
    score = game_console("You \x1B[32mWin\x1B[0m","You \x1B[31mLose\x1B[0m","You \x1B[33mtie\x1B[0m",var_win,var_loss,var_tie)
    
    var_win = score[0]
    var_loss = score[1]
    var_tie = score[2]
    rounds_played = var_win + var_loss + var_tie
    
    print("\nWins: {}, Losses: {}, Ties: {}.\n---------------------\n\n".format(var_win,var_loss,var_tie))

    if infinite_mode == False:
        rounds = rounds - 1

if var_win >= 1:    
    win_rate = (var_win / rounds_played) * 100 
    print("\nYou have a win rate of : {}%\nThats all your rounds for today!".format(win_rate))
else:
    print("Your win rate is 0%")











        
