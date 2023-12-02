import os

# INPUT_FILE = "sample_input.txt"
INPUT_FILE = "input.txt"

script_dir = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(script_dir, INPUT_FILE)

NUM_IN_WORDS = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
    ]

with open(file=file) as f:
    calibration_vals_sum = 0
    for line in f:
        # process a line
        digits = []
        for i, char in enumerate(line):
            if char.isdigit():
                digits.append(int(char))
            else:
                for num, word in enumerate(NUM_IN_WORDS):
                    if line[i:].startswith(word):
                        digits.append(num+1)
         
        calibration_val = digits[0]*10 + digits[-1]
        calibration_vals_sum += calibration_val
    print(calibration_vals_sum)