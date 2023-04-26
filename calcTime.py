from time import process_time
from beneathBeyond import beneathBeyond
from giftWrapping import gift_wrapping
from divideAndConquer import divideAndConquer
from quickHull import quickHull
from geomKernel import *
import pandas as pd


algorithms_list = [(beneathBeyond, 'Beneath Beyond') , (gift_wrapping, 'Gift Wrapping'), 
                   (divideAndConquer, 'Divide and Conquer'), (quickHull, 'Quick Hull')
                   ]

df_times = pd.DataFrame(columns=['Size'] + [algo[1] for algo in algorithms_list])

size = 10
while size <= 100000:

    algorithm_times = []
    points_list = gen_random_points(size, 2)

    for algorithm, name in algorithms_list:
        start = process_time()

        hull_points = beneathBeyond(points_list)

        end = process_time()
        total_time = end - start

        algorithm_times.append(total_time)
    
    new_row = {'Size' : size}
    for algo_name, time in zip(algorithms_list, algorithm_times):
        new_row[algo_name[1]] = time

    df_times = pd.concat([df_times, pd.DataFrame([new_row])], ignore_index=True)

    size *= 10

print(df_times.to_markdown(index=False))
