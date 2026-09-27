"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort by start date
        smeetings = sorted(intervals, key = lambda x: x.start)

        # compare endings with next start
        for i in range(1, len(smeetings)):
            nxtm = smeetings[i]
            lstm = smeetings[i - 1]
            if lstm.end > nxtm.start:
                return False
        return True