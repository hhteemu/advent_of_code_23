import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'data', 'cubes.txt')
with open(file_path) as f:
    lines = f.readlines()

multiplied = []
for line in lines:
    red = 0
    green = 0
    blue = 0
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
                red_num = int(j.split(' ')[0])
                red = max(red, red_num)
            elif 'green' in j:
                green_num = int(j.split(' ')[0])
                green = max(green, green_num)
            elif 'blue' in j:
                blue_num = int(j.split(' ')[0])
                blue = max(blue, blue_num)
    x = red * green * blue
    multiplied.append(x)

print(sum(multiplied))