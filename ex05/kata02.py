import datetime

h = (3, 30, 2019, 9, 25)
d = datetime.datetime(h[2], h[3], h[4], h[0], h[1])

print(d.strftime("%m/%d/%Y %H:%M"))
