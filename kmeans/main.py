#!/usr/bin/python

import matplotlib
import pylab
import kmeans
import numpy
from subprocess import *

def main(filename, k, function):
    file = open(filename)
    pts = []
    for line in file.readlines():
        line = line.split()
        pts.append(( int(line[0]), int(line[1])))
    file.close()

    group, s = kmeans.kmeans(pts, k, function)
    print group
    print s
    f = open(filename +'cluster', 'w')
    for each in range(len(group)):
        f.write( str(group[each])+'\n\n')
        cc = numpy.random.rand(10000)
        for i in group[each]:
            matplotlib.pyplot.scatter(i[0],i[1],s=2, color=cc)
        pylab.plot(s[each][0], s[each][1], '+')
    f.close()

    ll = filename + 'cluster'
    ll = 'gedit '+ ll
    ll = ll.split()
    process = Popen(ll)

    matplotlib.pyplot.show()
