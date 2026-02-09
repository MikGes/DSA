#Description: Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the minimum time (in seconds) to visit all the points in the order given by points.
#Approch: The time taken to move from one point to another is the maximum of the absolute difference of their x-coordinates and the absolute difference of their y-coordinates. We can iterate through the list of points, calculate the time taken to move from the current point to the next point, and accumulate the total time.
class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        x1,y1 = points.pop()
        r=0
        while points:
            x2, y2 = points.pop()
            r += max(abs(x1 - x2), abs(y1 - y2))
            x1,y1 = x2,y2
        return r