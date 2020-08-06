import datetime
import uuid

current_time = datetime.now()
year = str(current_time.year)[:2]
month = str(current_time.month)
day = str(current_time.day)
time_mid = uuid.uuid4().time_mid



random_id = "REG-{}{}{}{}".format(
            year, month, day, time_mid)
