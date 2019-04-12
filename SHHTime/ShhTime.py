# -*- coding:UTF-8 -*-



from datetime import datetime
import time

class Time(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            origin = super(Time, cls)
            cls._instance = origin.__new__(cls)
        return cls._instance

    def __init__(self):
        pass

    def now(self):
        dateTime = str(datetime.now())
        return dateTime.split('.')[0]

    def timestap(self, ttime):
        ttime = time.strptime(ttime, '%Y-%m-%d %H:%M:%S')
        timeStamp = int(time.mktime(ttime))
        return timeStamp

    def timeDelta(self, ftime, btime):
        deltaTime = self.timestap(btime) - self.timestap(ftime)
        return deltaTime

    def is_same_day(self, ftime, btime):
        time1 = time.strptime(ftime, '%Y-%m-%d %H:%M:%S')
        time2 = time.strptime(btime, '%Y-%m-%d %H:%M:%S')
        dayDelta = time2[2] - time1[2]
        if dayDelta == 0:
            return 1
        else:
            return None

    def dayDelta(self, ftime, btime):
        time1 = time.strptime(ftime, '%Y-%m-%d %H:%M:%S')
        time2 = time.strptime(btime, '%Y-%m-%d %H:%M:%S')
        deltaDay = time2[2] - time1[2]
        return deltaDay


STime = Time()


