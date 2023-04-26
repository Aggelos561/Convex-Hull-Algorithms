from beneathBeyond import beneathBeyond
from giftWrapping import gift_wrapping
from divideAndConquer import divideAndConquer
from quickHull import quickHull
from geomKernel import *


points_collinear_list = [(1, 1), (2, 3), (4, 2), (3, 1), (5, 6), (7, 6), (8, 8), (8, 10), (8, 12), (5, 12), (1, 12)]

# Check collinear for beneath beyond algorithm
hull_points = beneathBeyond(points_collinear_list)
show_convexHull(hull_points, points_collinear_list, "Beneath Beyond", True)


# Check collinear for gift wrapping algorithm
hull_points = gift_wrapping(points_collinear_list)
show_convexHull(hull_points, points_collinear_list, "Gift Wrapping", True)


# Check collinear for divide and conquer algorithm
hull_points = divideAndConquer(points_collinear_list)
show_convexHull(hull_points, points_collinear_list, "Divide and Conquer", True)


# Check collinear for quick hull algorithm
hull_points = quickHull(points_collinear_list)
show_convexHull(hull_points, points_collinear_list, "Quick Hull", True)

