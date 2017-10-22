"""
Given a collection of intervals, find the minimum number of intervals
you need to remove to make the rest of the intervals non-overlapping.

1. You may assume the interval's end point is always bigger than its start point.
2. Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
"""
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        Time Complexity: O(NlogN) for sorting
        Space Complexity: O(N) for holding temporary array

        Sort by endpoint. Then take the next segment whose startpoint doesn't overlap with the largest end point
        that you have added to your list.

        The intuition is that you are always picking the smallest interval that doesn't overlap with the last valid
        interval.


        :type intervals: List[Interval]
        :rtype: int
        """
        sorted_intervals = sorted(intervals, key=lambda x: x.end)


        curr_end = -float('inf')
        number_erased = 0
        for interval in sorted_intervals:
            if curr_end > interval.start:
                number_erased += 1
            else:
                curr_end = interval.end
        return number_erased


if __name__ == "__main__":
    l = [[1,2],[2,3],[3,4],[-100,-2],[5,7]]

    inters = []
    for i in l:
        new_inter = Interval(s=i[0], e=i[1])
        inters.append(new_inter)
    print(Solution.eraseOverlapIntervals(Solution(), intervals=inters))