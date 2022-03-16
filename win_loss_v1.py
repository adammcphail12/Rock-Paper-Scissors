from unittest import result


def results(score):

    result = input("result? ")

    if result == "win":
        score += 1

    return score

# ***** Main routine ******

current_score = 0

for item in range(0, 3):
    current_score = results(current_score)

print("You got", current_score)