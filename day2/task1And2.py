import re

with open('input', 'r') as file:
    lines = file.readlines()

def sortGames():
    games = [[0 for x in range(3)] for y in range(len(lines)+1)]

    for line in lines:
        digits = re.findall(r'\d+', line)
        colours = re.findall(r'red|green|blue', line)
        red = 0
        green = 0
        blue = 0
        for i in range(len(colours)):
            if int(digits[i+1]) > red and colours[i] == 'red':
                red = int(digits[i+1])
            elif int(digits[i+1]) > green and colours[i] == 'green':
                green = int(digits[i+1])
            elif int(digits[i+1]) > blue and colours[i] == 'blue':
                blue = int(digits[i+1])
        games[int(digits[0])][0] = red
        games[int(digits[0])][1] = green
        games[int(digits[0])][2] = blue
    return games

def task1(actualRed: int, actualGreen: int, actualBlue: int):
    games = sortGames(1)
    finalSum = 0
    for game in range(1, len(games)):
        if games[game][0] <= actualRed and games[game][1] <= actualGreen and games[game][2] <= actualBlue:
            finalSum += game
    print(finalSum)

def task2():
    games = sortGames()
    finalSum = 0
    for game in games:
        power = game[0] * game[1] * game[2]
        finalSum += power
    print(finalSum)

task2()
