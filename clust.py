import pickle
from math import sqrt

with open('./data/data.pkl', 'rb') as f:
    points_list = pickle.load(f)

#test points tuple imported with pickle
#points_list = [(-107, 630), (-790, -305), (-564, -387), (-181, -68), (330, -474), (-295, -803), (407, -920), (-640, 20), (943, 177), (428, -391), (-62, -335), (964, -98), (-306, -540), (-103, -979), (393, 208), (-94, -689), (497, -273), (201, 903), (965, 416), (-204, -928), (-809, -521), (116, -442), (56, 292), (-1, -604), (-241, 54), (-473, -996), (-61, -70), (-496, -354), (443, 539), (-786, 905), (620, 581), (-547, 588), (320, 102), (643, 964), (-696, 219), (-449, -941), (685, 640), (-763, -178), (120, 638), (-419, -894), (826, -216), (-583, -731), (-909, 170), (848, -749), (156, 946), (595, -172), (436, 93), (561, 48), (535, -868), (-507, 424)]


# We first need to define a Point class with all the operations of a 2D point.
class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point(%s, %s)' % (self.x,self.y)

    def __add__(self, point):

        return Point(self.x + point.x, self.y + point.y)

    def __sub__ (self, point):

        return Point(self.x - point.x, self.y - point.y)

    def __mul__ (self, p):
        if type(p) == int or type(p) == float:
            return Point(p*self.x, p*self.y)
        if type (p) == Point:
            return int((self.x * p.x) + (self.y*p.y))

    def distance (self, other):

        return sqrt((self.x - other.x)**2 +(self.y - other.y)**2)
             return int((self.x * p.x) + (self.y*p.y))

class Cluster(object):
    def __init__(self, x, y):
        self.center = Point(x, y)
        self.points = []

    def update(self):
        temp = Point(0, 0)
        for point in self.points:
            temp += point
        self.center =  temp * (1/float(len(self.points)))
        self.points = []


    def add_point(self, point):
        self.points.append(point)

# We convert the list of tuples representing points to a list of Point Objects.
points = [Point(points_list[i][0],points_list[i][1]) for i in range(len(points_list))]

def compute_result():
    a = Cluster(1,0)
    b = Cluster(-1,0)
    a_old = []
    for _ in range(10000): # max iterations
        for point in points:
            if point.distance(a.center) < point.distance(b.center):
                # add the right point
                a.add_point(point)
            else:
                # add the right point
                b.add_point(point)
        if a_old == a.points:
            break
        a_old = []
        a.update()
        b.update()
    return [(a.center.x,a.center.y),(b.center.x,a.center.y)]
