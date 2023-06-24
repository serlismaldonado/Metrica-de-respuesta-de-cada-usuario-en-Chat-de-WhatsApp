import datetime
def secondsBetween(start, end):

    yearS = int(start['year'])
    monthS = int(start['month'])
    dayS = int(start['day'])
    hoursS = int(start['hours'])
    minutesS = int(start['minutes'])
    secondsS = int(start['seconds'])

    yearE = int(end['year'])
    monthE = int(end['month'])
    dayE= int(end['day'])
    hoursE = int(end['hours'])
    minutesE = int(end['minutes'])
    secondsE = int(end['seconds'])

    beggins = datetime.datetime(yearS, monthS, dayS, hoursS, minutesS, secondsS)
    ended = datetime.datetime(yearE, monthE, dayE, hoursE, minutesE, secondsE)

    if ended > beggins:
        res = ended - beggins
        return res.total_seconds()
    else:
        res = -1
        return res

