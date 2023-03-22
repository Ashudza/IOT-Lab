#Display the time 10 times is the internal of 10 seconds#
import time
for i in range(10):
	d=time.localtime()
	time.sleep(3)
	print(d.tm_hour,d.tm_min,d.tm_sec)
