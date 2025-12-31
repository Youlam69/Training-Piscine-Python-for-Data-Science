import time
import datetime

timeNow = time.time()

print(f"Seconds since January 1, 1970: \
      {timeNow:,.4f} or {timeNow:.2e} in scientific notation")
print(datetime.date.today().strftime("%b %d %Y"))
