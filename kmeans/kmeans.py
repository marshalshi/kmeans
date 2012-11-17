from random import *
import sys


def random_choose( pts, k):
    s = []
    numran = []
    while len(numran) < k:
        x = randrange( 0, len(pts))
        if x not in numran:
            numran.append(x)
        else:
            pass

    for i in numran:
        s.append(pts[i])

    return s

def kcenter( pts, k):
    s = []
    pts_min_dist = zero( len(pts))
    for i in range(k):
        if not s:
            s.append(pts[randrange(0,len(pts))])
        else:
            for m in range(len(pts)):
                for n in range(len(s)):
                    if dist( pts[m], s[n]) < pts_min_dist[m]:
                        pts_min_dist[m] = dist( pts[m], s[n])
            s.append(pts[pts_min_dist.index(max(pts_min_dist))])
    return s

def kmeansplus(pts,k):
    s = []
    pts_min_dist = zero( len(pts))
    while len(s) < k:
        if not s:
            s.append(pts[randrange(0,len(pts))])
        else:
            for m in range(len(pts)):
                for n in range(len(s)):
                    if dist( pts[m], s[n]) < pts_min_dist[m]:
                        pts_min_dist[m] = dist( pts[m], s[n])
        sum = 0
        for i in pts_min_dist:
            sum += i
        randomsum = random() * sum
        i = -1
        while randomsum > 0:
            randomsum -= pts_min_dist[i]
            i -= 1
            nextpt = pts[pts_min_dist.index(pts_min_dist[i])]
        s.append(nextpt)
    return s

def zero(l):
    lst = []
    for i in range(l):
        lst.append(sys.maxint)
    return lst

def init_group(k):
    x = []
    for i in range(k):
        x.append([])
    return x

def init_groupid(l):
    lst = []
    for i in range(l):
        lst.append(-1)
    return lst

def recompute(group):
    ss = []

    for each in group:
        all_x = 0
        all_y = 0
        for i in each:
            all_x += i[0]
            all_y += i[1]
        ss.append(( all_x/len(each), all_y/len(each)))
    return ss

def dist(x,y):
    import math
    return math.sqrt( (abs(float(x[0])-y[0]))**2 + (abs(float(x[1])-y[1]))**2 )

def kmeans(pts, k, function):
    if int(function) == 1:
        s = random_choose( pts, k)
    elif int(function) ==2:
        s = kcenter( pts, k)
    else:
        s = kmeansplus( pts, k)
    pts_min_dist = zero( len(pts))
    pts_groupid = init_groupid( len(pts))
    kchange = True
    while kchange:
        group = init_group(k)
        pts_min_dist = zero( len(pts))
        for i in range(len(pts)):
            for j in range(len(s)):
                if dist( pts[i], s[j]) < pts_min_dist[i]:
                    pts_min_dist[i] = dist( pts[i], s[j])
                    pts_groupid[i] = j

        for i in range(len(pts)):
            group[pts_groupid[i]].append(pts[i])

        ss = recompute(group)

        if s == ss:
            kchange = False
        else:
            s = ss[:]
    return group, s
