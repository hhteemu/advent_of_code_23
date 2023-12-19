import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'data', 'cubes.txt')
with open(file_path) as f:
    lines = f.readlines()

# What games are possible with 12 red, 13 green and 14 blue cubes
red = 12
green = 13
blue = 14
notpossible = []
possible = []
for line in lines:
    separated_strings = line.split(': ')
    game = separated_strings[0]
    game_split = game.split(' ')
    game_id = int(game_split[1])
    
    games = separated_strings[1]
    games_split = games.split('; ')
    for i in games_split:
        i = i.split(', ')
        for j in i:
            if 'red' in j:
                red_num = j.split(' ')
                red_num = int(red_num[0])
                if red_num > red:
                    if game_id not in (notpossible):
                        notpossible.append(game_id)
            elif 'green' in j:
                green_num = j.split(' ')
                green_num = int(green_num[0])
                if green_num > green:
                    if game_id not in (notpossible):
                        notpossible.append(game_id)
            elif 'blue' in j:
                blue_num = j.split(' ')
                blue_num = int(blue_num[0])
                if blue_num > blue:
                    if game_id not in (notpossible):
                        notpossible.append(game_id)
    
x = 1
while x < 101:
    if x not in notpossible:
        possible.append(x)
    x += 1

print(sum(possible))