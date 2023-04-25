points = []
curr = 290797
limit = 2*(10**6)
from collections import deque
for i in range(1,limit+1):
    next = pow(curr,2,50515093)
    points.append((curr, next))
    curr = pow(next,2,50515093)

print(len(points))
def dist(p1, p2):
    return (p1[0] - p2[0])*(p1[0] - p2[0]) + (p1[1] - p2[1])*(p1[1] - p2[1])

def bruteForce(P, startIndex, endIndex):
    min_dist = float("inf")
    for i in range(startIndex, endIndex):
        for j in range(i+1, endIndex):
            if dist(P[i], P[j]) < min_dist:
                min_dist = dist(P[i], P[j])
    return min_dist
 
 
def min(x, y):
    return x if x < y else y
 
 
def stripClosest(strip, size, d):
    min_dist = d
    strip = sorted(strip, key=lambda point: point[1])
    #594.461941590881
    for i in range(size):
        for j in range(i+1, min(i+7,size)):
            if (strip[j][1] - strip[i][1]) >= min_dist:
                break
            if dist(strip[i], strip[j]) < min_dist:
                min_dist = dist(strip[i], strip[j])
    return min_dist
 
 
def closestUtil(P, startIndex, endIndex):
    if endIndex-startIndex <= 3:
        return bruteForce(P, startIndex, endIndex)
    mid = startIndex+(endIndex-startIndex)//2
    midPoint = P[mid]
    dl = closestUtil(P, startIndex, mid)
    dr = closestUtil(P, mid, endIndex)
    d = min(dl, dr)
    strip = deque()
    
    left, right = mid-1, mid+12
    while(left>=startIndex and abs(P[left][0] - midPoint[0])<d):
        strip.appendleft(P[left])
        left-=1
    strip.append(midPoint)
    while(right<endIndex and abs(P[right][0] - midPoint[0])<d):
        strip.append(P[right])
        right+=1
    # for i in range(n):
    #     if abs(P[i][0] - midPoint[0]) < d:
    #         strip.append(P[i])
    return min(d, stripClosest(strip, len(strip), d))
 
 
def closest(P, n):
    P = sorted(P, key=lambda point: point[0])
    return closestUtil(P, 0, n)
print(closest(points, len(points))**0.5)

# def dist(p1, p2):
#     # without sqrt
#     return ((p2[1]-p1[1])**2)+((p2[0]-p1[0])**2)


# def closest_brute_force(points):
#     min_dist = float("inf")
#     p1 = None
#     p2 = None
#     for i in range(len(points)):
#         for j in range(i+1, len(points)):
#             d = dist(points[i], points[j])
#             if d < min_dist:
#                 min_dist = d
#                 p1 = points[i]
#                 p2 = points[j]
#     return p1, p2, min_dist

# def rec(xsorted, ysorted):
#     n = len(xsorted)
#     if(n<3):
#         return closest_brute_force(xsorted)
#     else:
#         midPoint = xsorted[n//2]
#         xsorted_left = xsorted[:n//2]
#         xsorted_right = xsorted[n//2:]
#         ysorted_left = []
#         ysorted_right = []
#         for point in points:
#             ysorted_left.append(point) if point[0]<= midPoint[0] else ysorted_right.append(point)
#         (p1_left, p2_left, delta_left) = rec(xsorted_left, ysorted_left)
#         (p1_right, p2_right, delta_right) = rec(xsorted_right, ysorted_right)
#         (p1, p2, delta) = (p1_left, p2_left, delta_left) if delta_left<delta_right else (p1_right, p2_right, delta_right)
#         in_band = [point for point in ysorted if midPoint[0]-delta <point[0]<midPoint[0]+delta]
#         for i in range(len(in_band)):
#             for j in range(i+1, min(i+7, len(in_band))):
#                 d = dist(in_band[i], in_band[j])
#                 if d< delta:
#                     (p1, p2, delta) = (in_band[i], in_band[j], d)
#         return p1, p2, delta
        


# def closest(points):
#     xsorted = sorted(points, key=lambda x:x[0])
#     ysorted = sorted(points, key=lambda x:x[1])
#     return rec(xsorted, ysorted)
# result = closest(points)
# print(dist(result[0], result[1])**0.5)