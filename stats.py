import os
import time
import subprocess
import statistics

from tabulate import tabulate
from tqdm import tqdm

MAX_RUNS = 10
print(f"Benchmark running over {MAX_RUNS} runs...")

def run_script(filepath:str):
    try:
        subprocess.run(f'python3 {filepath}', shell=True, stdout=subprocess.DEVNULL)
    except Exception as err:
        print(err)
        
results = []
tree_iter = os.walk('.')
next(tree_iter) # skip files in current dir
for dirpath, dirs, files in tree_iter:
    for file in files:
        if file.endswith('.py'):
            filepath = f'{dirpath}/{file}'
            # print(filepath)
            print(f"Running benchmark for : {filepath}")
            runs = []
            for i in tqdm(range(MAX_RUNS)):
                s = time.perf_counter()
                run_script(filepath=filepath)
                e = time.perf_counter()
                runs.append(e-s)
            
            results.append([
                filepath,
                min(runs),
                statistics.mean(runs),
                max(runs)
            ])
            
TABLEFMT = "heavy_grid"
headers = ["File", "Min (s)", "Avg (s)", "Max (s)"]
print(tabulate(sorted(results), headers=headers, tablefmt=TABLEFMT))