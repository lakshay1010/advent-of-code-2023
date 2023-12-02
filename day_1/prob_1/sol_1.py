import os

# INPUT_FILE = "sample_input.txt"
INPUT_FILE = "input.txt"

script_dir = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(script_dir, INPUT_FILE)

with open(file=file) as f:
    calibration_vals_sum = 0
    for line in f:
        # process a line
        leftmost, righmost = 0, 0
        for elem in line:
            if elem.isdigit():
                leftmost = elem
                break

        for elem in reversed(line):
            if elem.isdigit():
                rightmost = elem        
                break
            
        calibration_vals_sum += int(leftmost+rightmost)
    print(calibration_vals_sum)       