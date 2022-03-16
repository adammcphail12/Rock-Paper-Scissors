
def results(won, lost):

    result = input("result? ")

    if result == "win":
        won += 1
    elif result == "loss":
        lost += 1

    score = [won, lost]

    return score

# ***** Main routine ******

var_won = 0
var_lost = 0

for item in range(0, 3):
    current_score = results(var_won, var_lost)

    # print(current_score)

    var_won = current_score[0]
    var_lost = current_score[1]

print("You have {} wins and {} losses".format(var_won, var_lost))