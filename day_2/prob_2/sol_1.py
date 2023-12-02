import os

# INPUT_FILE = "sample_input.txt"
INPUT_FILE = "input.txt"

script_dir = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(script_dir, INPUT_FILE)

def parse_line(line:str):
    game, sets_string = line.strip().split(':')
    game_id = int(game.split()[-1])
    sets_list = sets_string.split(';')
    return game_id, sets_list

def parse_set(subset:str):
    all_cubes = subset.strip().split(',')
    all_cubes = [cubes.split() for cubes in all_cubes]
    return all_cubes
    
with open(file=file) as f:
    power_sum = 0
    for line in f:
        print(line)
        # parse
        game_id, all_sets = parse_line(line=line)
        print(game_id, all_sets)
        # loop sets
        bag = dict()
        for subset in all_sets:
            all_cubes = parse_set(subset)
            print(all_cubes)
            for cubes in all_cubes:
                cube_cnt = int(cubes[0])
                color = cubes[1]
                if not bag.get(color):
                    bag[color] = cube_cnt
                else:
                    if cube_cnt > bag[color]:
                        bag[color] = cube_cnt                       

        power = 1
        for cnt in bag.values():
            power *= cnt
        
        power_sum += power
    print(power_sum)