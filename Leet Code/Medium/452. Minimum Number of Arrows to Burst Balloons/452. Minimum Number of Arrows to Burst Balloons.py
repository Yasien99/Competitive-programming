class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sorted_points = points.sort()
        arw = 1
        last = points[0][1]
        for i in range(len(points)):
            if points[i][0] > last:
                arw += 1
                last = points[i][1]
            else:
                last = min(last, points[i][1])
        return arw