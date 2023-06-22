import time
from beneathBeyond import beneathBeyond
from giftWrapping import gift_wrapping
from divideAndConquer import divideAndConquer
from quickHull import quickHull
from geomKernel import *
import pandas as pd
from tabulate import tabulate


algorithms_list = [(beneathBeyond, 'Beneath Beyond') , (gift_wrapping, 'Gift Wrapping'), 
                   (divideAndConquer, 'Divide and Conquer'), (quickHull, 'Quick Hull')]

df_times = pd.DataFrame(columns=['Size'] + [algo[1] for algo in algorithms_list])

size = 10
while size <= 100000:

    algorithm_times = []
    points_list = gen_random_points(size, 2)

    for algorithm, name in algorithms_list:
        start = time.perf_counter()

        hull_points = algorithm(points_list)

        end = time.perf_counter()
        total_time = end - start

        algorithm_times.append(total_time)
    
    new_row = {'Size' : size}
    for algo_name, t in zip(algorithms_list, algorithm_times):
        new_row[algo_name[1]] = t

    df_times = pd.concat([df_times, pd.DataFrame([new_row])], ignore_index=True)

    size *= 10

print(tabulate(df_times, headers='keys', tablefmt='fancy_grid', showindex=False))
