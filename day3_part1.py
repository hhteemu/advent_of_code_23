import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'data', 'partnumbers.txt')
with open(file_path) as f:
    lines = f.readlines()

lines_list = []
for line in lines:
    lines_list.append(line)

skip = 0
nums = []
num = ''
symbols = set("!@#$%^&*()_+{}[];\',:/?><~-=`")
previous_line = ''
next_line = ''

def has_symbol_nearby(line, i, end):
    has_symbol = False
    if any(0 <= i + offset < len(line) and line[i+offset] in symbols for offset in range(-1, end)):
        has_symbol = True
    return has_symbol

for index, line in enumerate(lines_list):
    if index > 0:
        previous_line = lines_list[index - 1]
    if index < len(lines_list) - 1:
        next_line = lines_list[index + 1]
    for i in range(len(line)):
        if line[i].isdigit():
            if skip > 0:
                skip -= 1
                continue
            if i + 2 < len(line) and line[i+1].isdigit() and line[i+2].isdigit():
                if line[i+3] in symbols or line[i-1] in symbols or has_symbol_nearby(previous_line, i, 4) or has_symbol_nearby(next_line, i, 4):
                        num = int(line[i] + line[i+1] + line[i+2])
                        nums.append(num)
                skip += 2
            elif i + 1 < len(line) and line[i+1].isdigit():
                if line[i+2] in symbols or line[i-1] in symbols or has_symbol_nearby(previous_line, i, 3) or has_symbol_nearby(next_line, i, 3):
                    num = int(line[i] + line[i+1])
                    nums.append(num)
                skip += 1
            else:
                if line[i+1] in symbols or line[i-1] in symbols or has_symbol_nearby(previous_line, i, 2) or has_symbol_nearby(next_line, i, 2):
                    num = int(line[i])
                    nums.append(num)

print(sum(nums))