import numpy as np
from geomKernel import *
from quickHull import *


def get_bridge(cPoints1, cPoints2, mode):

    c1_size = len(cPoints1)
    c2_size = len(cPoints2)

    first_iter = True
    flag_a = False
    flag_b = False

    while True:

        if first_iter:
            a_index = get_rightmost_index(cPoints1)
            b_index = get_leftmost_index(cPoints2)
            first_iter = False
        
        else:
            if flag_a:
                a_index = get_next_index_a(a_index, c1_size, mode)
                flag_a = False
            if flag_b:    
                b_index = get_next_index_b(b_index, c2_size, mode)
                flag_b = False

        a_index_next = get_next_index_a(a_index, c1_size, mode)
        b_index_prev = get_next_index_b(b_index, c2_size, mode)

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

        flag_a, flag_b = check_subspace(cPoints1, cPoints2, a_index, a_index_next, a_random, b_index, b_index_prev, b_random, mode)

        if flag_a or flag_b:
            continue
        else:
            return [cPoints1[a_index], cPoints2[b_index]]


def merge(convexPoints1, convexPoints2):
    
    upper_points = get_bridge(convexPoints1, convexPoints2, 'upper')
    lower_points = get_bridge(convexPoints1, convexPoints2, 'lower')

    convex = []

    p_left = convexPoints1[get_leftmost_index(convexPoints1)]

    upper_in = False

    found_start = False
    stop_circle = False
    while True:

        for p1 in convexPoints1:

            if p1 == p_left and not found_start:
                found_start = True
                if p_left == upper_points[0]:
                    upper_in = True

            if found_start:

                convex.append(p1)

                if p1 == lower_points[0]:
                    convex.append(lower_points[1])
                    stop_circle = True
                    break
        
        if stop_circle:
            break
    

    found_start = False
    stop_circle = False
    while True:

        for p2 in convexPoints2:

            if p2 == lower_points[1] and not found_start:
                found_start = True
                continue
            
            if found_start:
                
                if (upper_points[1] == lower_points[1]):
                    
                    if not upper_in:
                        convex.append(upper_points[0])
                        
                    stop_circle = True
                    break
                
                if p2 != upper_points[0]:
                    
                    convex.append(p2)
                   
                
                if p2 == upper_points[1]:
 
                    if not upper_in:
                        convex.append(upper_points[0])

                    stop_circle = True
                    break
        
        if stop_circle:
            break


    found_start = False
    stop_circle = False
    while True:

        for p1 in convexPoints1:

            if p1 == upper_points[0] and not found_start:
                
                if p1 == convex[0]:
                    stop_circle = True
                    break

                found_start = True
                continue

            if found_start:
                if p1 != convex[0]:
                    convex.append(p1)
                else:
                    stop_circle = True
                    break
                    
        if stop_circle:
            break
    
    return convex

def split(points):

    grouped_points = np.array_split(points, 2)
    points1, points2 = list(tuple(p) for p in grouped_points[0]), list(tuple(p) for p in grouped_points[1])

    if len(points1) <= 6 or len(points2) <= 6:
        convexPoints1 = quickHull(points1)
        convexPoints2 = quickHull(points2)

        return merge(convexPoints1, convexPoints2)
    
    convex1 = split(points1)
    convex2 = split(points2)

    return merge(convex1, convex2)



def divideAndConquer(points):

    points_list = sort_points(points)
    return split(points_list)




if __name__ == '__main__':

    points_list = gen_random_points(random.randint(100000, 100000), 2)
    vertices = divideAndConquer(points_list)
    show_convexHull(vertices, points_list)



# Debugging convex hull:

# points_list = [(0.41404594897748737, 0.6419518873391884), (0.6708764685717089, 0.3935920311252178), (0.3189099147350093, 0.5232479360424155), (0.9815240676330101, 0.38311851613534786), (0.48708492153388816, 0.6907076828680275), (0.43568224526358035, 0.8234158919701465), (0.31749623163820795, 0.6781961027163272), (0.9980161626980715, 0.41251084857312637), (0.6782359550894603, 0.9046641973491251), (0.8373831702140869, 0.2065624101832394), (0.8719603158487957, 0.8929523698159376), (0.4355467544868493, 0.3327811573528645), (0.1222023745942421, 0.11311013672610382), (0.8422235624014605, 0.38172006033463646), (0.6245825763786401, 0.8407737146847024), (0.4267668266092133, 0.5943748412242799), (0.9732261473197905, 0.8640417077784159), (0.6363554168561432, 0.5470143203250895), (0.1961571045392172, 0.8570119783623936), (0.30482676944382736, 0.39472114578705264), (0.9428211974866336, 0.07716100325846686), (0.9401481758500437, 0.4853017259138619), (0.3187484327930261, 0.4935714970656788), (0.43886765243697123, 0.8050006407663407), (0.9824772327425415, 0.1139981129938974), (0.7520714941435228, 0.2651244336185261), (0.24259896850675722, 0.2842253667017711), (0.2958202928274124, 0.8577712153037694), (0.6186376603915757, 0.9019077414415764), (0.4202624215132693, 0.5843805950388319), (0.7565686450062045, 0.9599836738983141), (0.6513442344135933, 0.7479509622518332), (0.6505328572070767, 0.34062838247105565), (0.04284493444668247, 0.24564785248658716), (0.5739804588486093, 0.32360705553437163), (0.7159009506954931, 0.34771484919998663), (0.25461994013471423, 0.7177456872465011), (0.5915606738235368, 0.7837450826561212), (0.4212633264418294, 0.4632754430976447), (0.07666511357986106, 0.7295876412443079), (0.46725916972342285, 0.5718144853977064), (0.7267747517469053, 0.38008235641914956), (0.6564283820660491, 0.6174606768095245), (0.6446149657773363, 0.2778273707862461), (0.6766248514715895, 0.9112031696185325), (0.7222563985987844, 0.9980414772784165), (0.6771674402154525, 0.4382854448226311), (0.6482517883216391, 0.32773696466018243), (0.5023472760785785, 0.7310591426665817), (0.06887859430676879, 0.08441120570351368), (0.7299787678335043, 0.7445630774332166), (0.5192399245361555, 0.5370514006681399), (0.5332181527010192, 0.7698600508394121), (0.021794219216318744, 0.8370365713048983), (0.5684566875492356, 0.10051832724751009), (0.7978519698493683, 0.41646369811481143), (0.03608259343493936, 0.11115277850179017), (0.48249702320453514, 0.3746771165593029), (0.011879405463260606, 0.3085581438258711), (0.7568161275263784, 0.6983930432229444), (0.6725242965715461, 0.7228496090158628), (0.27334812880441994, 0.49528953557157807), (0.5745190454329634, 0.4132576462740709), (0.5949231624134976, 0.20447722168787297), (0.2834435859824648, 0.87273607788619), (0.9333702900838532, 0.6241991657203451), (0.6081141940885422, 0.08610089362823758), (0.5756370512346848, 0.6255632692998498), (0.7063096263072683, 0.48302581832731817), (0.014820269324303692, 0.7362472640707532), (0.05431811292923483, 0.08556378446201218), (0.6793432417647542, 0.9329127928427844), (0.1388097803043825, 0.17751892153298465), (0.2750889485456768, 0.5514450176313425), (0.2405921714568393, 0.6240814477606214), (0.42563241798873874, 0.7023595905808987), (0.39893782564364366, 0.6754929265512435), (0.4380325245007809, 0.43193189525940434), (0.6775609891127373, 0.11071667046280187), (0.9749256395381979, 0.5227675929661064), (0.8502893225273735, 0.34732619518078733), (0.01105012230941338, 0.5235355272699292), (0.059606754146981356, 0.8681767427106457), (0.5665308993120882, 0.013830322007802431), (0.9887623119364652, 0.6446883317646878), (0.9298056045101893, 0.4988677840865551), (0.702171783412245, 0.3031000083848796), (0.7886494503800003, 0.006051721283726219), (0.3414341372516615, 0.6928861415757853), (0.8225566921100361, 0.22151067815934078), (0.8999161778864738, 0.21501944544280827), (0.6767818379966997, 0.16591939005363454), (0.39099215876957916, 0.6328925702414403), (0.3022145836388912, 0.13496651709142127), (0.9372289396025022, 0.5577040665903208), (0.5458992661470514, 0.49444144141936386), (0.8996452440099848, 0.09021210931636825), (0.20598697966134394, 0.4210172724266834), (0.41057284329318966, 0.8927611241482579), (0.7538656409016835, 0.6007131029210909), (0.27602134370001874, 0.01576037040283873), (0.00701372085695251, 0.8127289924830948), (0.23762656944998806, 0.5671653943372382), (0.09713993118983177, 0.4199100920965365), (0.5734606193402613, 0.17826998777940617), (0.27133017325306297, 0.35961791917823205), (0.048020479058381804, 0.8883872428309159), (0.6394027375078878, 0.558026268309261), (0.4010711783897384, 0.001334402391640288), (0.8511097475868414, 0.7727243252642397), (0.3581952535910016, 0.8716657542264585), (0.2517151973152574, 0.9503424965318447), (0.6758597510341848, 0.11827813919727392), (0.6895598465018882, 0.872684968941236), (0.23792156931973296, 0.37744732981457685), (0.42362887444083586, 0.7102210917723363), (0.7894389288820927, 0.8549759313916119), (0.3025127981523015, 0.16947058709060692), (0.18255721136693015, 0.31417775860570063)]
# points_list = [(0.3022145836388912, 0.13496651709142127), (0.3025127981523015, 0.16947058709060692), (0.30482676944382736, 0.39472114578705264), (0.31749623163820795, 0.6781961027163272), (0.3187484327930261, 0.4935714970656788), (0.3189099147350093, 0.5232479360424155), (0.3414341372516615, 0.6928861415757853), (0.3581952535910016, 0.8716657542264585)]
        