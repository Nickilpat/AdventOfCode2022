input_file = open("02/input2.txt", "r")
rps_rounds = input_file.read().split('\n')
input_file.close()

def points_for_shape(shape_played):
    if shape_played == 'A':
        return 1
    elif shape_played == 'B':
        return 2
    elif shape_played == 'C':
        return 3

def did_you_win(opp, you):
    if opp == 'A' and you == 'B':
        return True
    elif opp == 'B' and you == 'C':
        return True
    elif opp == 'C' and you == 'A':
        return True
    else:
        return False
        

def points_for_result(opp, you):
    if opp == you:
        return 3
    elif did_you_win(opp, you):
        return 6
    else:
        return 0

def convert(shape):
    if shape == 'X':
        return 'A'
    elif shape == 'Y':
        return 'B'
    elif shape == 'Z':
        return 'C'

def solvePartOne():
    for round in rps_rounds:
        round_shapes = round.split()
        opp = round_shapes[0]
        you = convert(round_shapes[1])
        round_score += points_for_shape(you)
        round_score += points_for_result(opp, you)
        print("round score: " + str(round_score))
        total_score += round_score
        round_score = 0

    print(total_score)



total_score = 0
round_score = 0
solvePartOne()
