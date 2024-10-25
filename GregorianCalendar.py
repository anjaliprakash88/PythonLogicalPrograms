# given a string date representing a calendar date formatted as YYYY-MM-DD, return the day number of the year
# input: "2019-02-10"
# output: 41
from datetime import datetime
date_str = "2019-01-09"
date = datetime.strptime(date_str, "%Y-%m-%d")
print(date.timetuple().tm_yday)



