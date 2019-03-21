import pickle
from math import sqrt
import numpy as np


#with open('./data/data.pkl', 'rb') as f:
#    points_list = pickle.load(f)

#test points tuple imported with pickle
#points_list = [(-107, 630), (-790, -305), (-564, -387), (-181, -68), (330, -474), (-295, -803), (407, -920), (-640, 20), (943, 177), (428, -391), (-62, -335), (964, -98), (-306, -540), (-103, -979), (393, 208), (-94, -689), (497, -273), (201, 903), (965, 416), (-204, -928), (-809, -521), (116, -442), (56, 292), (-1, -604), (-241, 54), (-473, -996), (-61, -70), (-496, -354), (443, 539), (-786, 905), (620, 581), (-547, 588), (320, 102), (643, 964), (-696, 219), (-449, -941), (685, 640), (-763, -178), (120, 638), (-419, -894), (826, -216), (-583, -731), (-909, 170), (848, -749), (156, 946), (595, -172), (436, 93), (561, 48), (535, -868), (-507, 424)]


# We first need to define a Point class with all the operations of a 3D point.
class Point(object):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return 'Point(%s, %s, %s)' % (self.x,self.y,self.z)

    def __add__(self, point):

        return Point(self.x + point.x, self.y + point.y, self.z + point.z)

    def __sub__ (self, point):

        return Point(self.x - point.x, self.y - point.y, self.z - point.z)

    def __mul__ (self, p):
        if type(p) == int or type(p) == float:
            return Point(p*self.x, p*self.y, p*self.z)
        if type (p) == Point:
            return int((self.x * p.x) + (self.y*p.y) + (self.z*p.z))

    def distance (self, other):

        return sqrt((self.x - other.x)**2 +(self.y - other.y)**2 + (self.z - other.z)**2)


class Cluster(object):
    def __init__(self, x, y, z):
        self.center = Point(x, y, z)
        self.points = []

    def update(self):
        temp = Point(0, 0, 0)
        for point in self.points:
            temp += point
        self.center =  temp * (1/float(len(self.points)))
        self.points = []


    def add_point(self, point):
        self.points.append(point)

# We convert the list of tuples representing points to a list of Point Objects.
#points = [Point(points_list[i][0],points_list[i][1]) for i in range(len(points_list))]

def basic_knn(X, nclusters):
    clusters = []
    for i in range(nclusters):
        index = np.random.choice(X.shape[0], 2, replace=False)
        clusters.append(Cluster(X[index]))

    _old = []
    dist_list = []
    for _ in range(10000): # max iterations
        for point in X:

            for cluster in clusters:
                dist_list.append(point.distance(cluster.center))

            min_index = dist_list.index(min(dist_list))
            cluster[min_index].add_point(point)


        if _old == clusters[0].points:
            break
        _old = []
        for cluster in clusters:
            cluster.update()


    return [cluster.center for cluster in clusters]
