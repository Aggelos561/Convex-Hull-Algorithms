from geomKernel import gen_random_points
from beneathBeyond import beneathBeyond

# Step by step visualization of Beneath Beyond algorithm

points_list = gen_random_points(20, 2)

beneathBeyond(points_list, visualize=True)
