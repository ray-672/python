import random
import datetime

def random_date(start, end):

    rs = random.randint(0, int ((end - start).total_seconds()))

    rdate = datetime.timedelta(seconds = rs)

    return start + rdate

start = datetime.datetime(2020, 1 ,1)
end = datetime.datetime(2021, 1, 1)
randomdate = random_date(start, end)

print(f'the random date between {start.date()} and {end.date()} is {randomdate.date()}')