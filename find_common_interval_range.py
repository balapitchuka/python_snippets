# Find Intersection of all Intervals
# Given N intervals of the form of [l, r], the task is to find the intersection of all the intervals. An intersection is
# an interval that lies within all of the given intervals. If no such intersection exists then print -1.
# refer https://www.geeksforgeeks.org/find-intersection-of-all-intervals/


def common_interval(intervals):
    if len(intervals) == 0:
        print("-- empty interval list provided")
        return
    else:
        max_left = intervals[0][0]
        min_right = intervals[0][1]
        for left, right in intervals[1:]:
            if right < max_left or left > min_right:
                print("-- no common interval found")
                return
            else:
                max_left = max(max_left, left)
                min_right =  min(min_right, right)
        print(f"-- common interval range is [{max_left},{min_right}]")


if __name__ == "__main__":
    intervals = [[1,6],[2,8],[3,10],[5,8]]
    common_interval(intervals)
    intervals = [[1,6],[2,8],[3,10],[5,8],[2,4]]
    common_interval(intervals)