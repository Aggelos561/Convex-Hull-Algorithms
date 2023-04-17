import numpy as np
from quickHull import *
import matplotlib.pyplot as plt

def upper_bridge(cPoints1, cPoints2):

    c1_size = len(cPoints1)
    c2_size = len(cPoints2)

    first_iter = True
    flag_a = False
    flag_b = False

    while True:

        if first_iter:
            a_index = cPoints1.index(max(cPoints1, key=lambda p : p[0]))
            b_index = cPoints2.index(min(cPoints2, key=lambda p : p[0]))
            first_iter = False
        
        else:
            if flag_a:
                a_index = (a_index + 1) % c1_size
                flag_a = False
            if flag_b:    
                b_index = b_index - 1 if b_index - 1 >= 0 else c2_size - 1
                flag_b = False

        a_index_next = (a_index + 1) % c1_size
        b_index_prev = b_index - 1 if b_index - 1 >= 0 else c2_size - 1

        a_random = cPoints1[0]
        while True:
            a_random = random.choice(cPoints1)
            if a_random != cPoints1[a_index] and a_random != cPoints1[a_index_next]:
                break

        b_random = cPoints2[0]
        while True:
            b_random = random.choice(cPoints2)
            if b_random != cPoints2[b_index] and b_random != cPoints2[b_index_prev]:
                break


        if not (is_CCW(cPoints1[a_index], cPoints1[a_index_next], a_random) and is_CCW(cPoints1[a_index], cPoints1[a_index_next], cPoints2[b_index])):
            flag_a = True
        
        if not (is_CW(cPoints2[b_index], cPoints2[b_index_prev], b_random) and is_CW(cPoints2[b_index], cPoints2[b_index_prev], cPoints1[a_index])):
            flag_b= True

        if flag_a or flag_b:
            continue
        else:
            print(cPoints1[a_index])
            print(cPoints2[b_index])
            break


def lower_bridge(cPoints1, cPoints2):

    c1_size = len(cPoints1)
    c2_size = len(cPoints2)

    first_iter = True
    flag_a = False
    flag_b = False

    while True:

        if first_iter:
            a_index = cPoints1.index(max(cPoints1, key=lambda p : p[0]))
            b_index = cPoints2.index(min(cPoints2, key=lambda p : p[0]))
            first_iter = False
        
        else:
            if flag_a:
                a_index = a_index - 1 if a_index - 1 >= 0 else c1_size - 1
                flag_a = False
            if flag_b:    
                b_index = (b_index + 1) % c2_size
                flag_b = False

        a_index_next = a_index - 1 if a_index - 1 >= 0 else c1_size - 1
        b_index_prev = (b_index + 1) % c2_size

        a_random = cPoints1[0]
        while True:
            a_random = random.choice(cPoints1)
            if a_random != cPoints1[a_index] and a_random != cPoints1[a_index_next]:
                break

        b_random = cPoints2[0]
        while True:
            b_random = random.choice(cPoints2)
            if b_random != cPoints2[b_index] and b_random != cPoints2[b_index_prev]:
                break


        if (is_CW(cPoints1[a_index], cPoints1[a_index_next], a_random) and is_CCW(cPoints1[a_index], cPoints1[a_index_next], cPoints2[b_index])):
            print('iteration for a')
            flag_a = True
        
        if (is_CCW(cPoints2[b_index], cPoints2[b_index_prev], b_random) and is_CW(cPoints2[b_index], cPoints2[b_index_prev], cPoints1[a_index])):
            print('iteration for b')
            flag_b= True

        if flag_a or flag_b:
            continue
        else:
            print(cPoints1[a_index])
            print(cPoints2[b_index])
            break



def divideAndConquer(points):

    points_list = sort_points(points)
    grouped_points = np.array_split(points_list, 2)
    points1, points2 = list(tuple(p) for p in grouped_points[0]), list(tuple(p) for p in grouped_points[1])

    convexPoints1 = quickHull(points1)
    convexPoints2 = quickHull(points2)

    lower_points = lower_bridge(convexPoints1, convexPoints2)

    show_convexHull(convexPoints1, points1)
    show_convexHull(convexPoints2, points2)
    plt.show()

    return None


if __name__ == '__main__':
    # [[1, 2], [4, 5], [3, 0], [9, 7], [11, 6], [14, 13], [15, 7], [18, 8]]
    points_list = gen_random_points(random.randint(8, 30), 2)
    vertices = divideAndConquer(points_list)
    # show_convexHull(vertices, points_list)