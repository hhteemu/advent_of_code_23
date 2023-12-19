import os
import re

current_dir  = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'data', 'calibration.txt')
with open(file_path) as f:
    lines = f.readlines()

def keep_numbers(input_string):
    result = ''
    i = 0
    while i < len(input_string):
        if input_string[i].isdigit():
            result += input_string[i]
            i += 1
        else:
            if input_string[i:i+3] == 'one':
                result += '1'
                i += 1
            elif input_string[i:i+3] == 'two':
                result += '2'
                i += 1
            elif input_string[i:i+5] == 'three':
                result += '3'
                i += 1
            elif input_string[i:i+4] == 'four':
                result += '4'
                i += 1
            elif input_string[i:i+4] == 'five':
                result += '5'
                i += 1
            elif input_string[i:i+3] == 'six':
                result += '6'
                i += 1
            elif input_string[i:i+5] == 'seven':
                result += '7'
                i += 1
            elif input_string[i:i+5] == 'eight':
                result += '8'
                i += 1
            elif input_string[i:i+4] == 'nine':
                result += '9'
                i += 1
            else:
                i += 1

    return result

nums = []
for line in lines:
    new_num = keep_numbers(line)[0] + keep_numbers(line)[-1]
    nums.append(int(keep_numbers(new_num)))

print(sum(nums))