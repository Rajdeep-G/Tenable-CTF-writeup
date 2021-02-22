Simple code 
(use python2)
```py
import math


def ar(a, b, c):
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))
    if area > 0:
        area = (math.sqrt(area))
        return area
    else:
        return 0


def length(a1, a2, a3, a4, a5, a6):
    v1 = (abs(a1-a4)**2)+(abs(a2-a5)**2)+(abs(a3-a6)**2)
    v1 = math.sqrt(v1)
    return v1


def area(s1, s2, s3):
    s1_n1 = s1[0]
    s1_n2 = s1[1]
    s1_n3 = s1[2]
    s2_n1 = s2[0]
    s2_n2 = s2[1]
    s2_n3 = s2[2]
    s3_n1 = s3[0]
    s3_n2 = s3[1]
    s3_n3 = s3[2]
    d1 = length(s1_n1, s1_n2, s1_n3, s2_n1, s2_n2, s2_n3)
    d2 = length(s1_n1, s1_n2, s1_n3, s3_n1, s3_n2, s3_n3)
    d3 = length(s2_n1, s2_n2, s2_n3, s3_n1, s3_n2, s3_n3)
    an = ar(d1, d2, d3)
    return an


def FindLargestTriangleArea(points):
    ans = []
    n = len(points)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                ans.append(area(points[i], points[j], points[k]))
    return max(ans)


# Reading space delimited points from stdin
# and building list of 3D points
points_data = raw_input()
points = []
for point in points_data.split(' '):
    point_xyz = point.split(',')
    points.append([int(point_xyz[0]), int(point_xyz[1]), int(point_xyz[2])])

# Compute Largest Triangle and Print Area rounded to nearest whole number
area = FindLargestTriangleArea(points)
print int(round(area))

```