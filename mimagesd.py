import time
import os
import timeit

start = timeit.default_timer() 
os.system('fswebcam -d /dev/video0 -r 800x720 --no-banner /media/ubuntu/"UBUNTU 16_0"/img-0/"%Y-%m-%d_%H%M".jpg')
stop = timeit.default_timer() 
time = stop-start

print "Time taken for the calculation to write image in SD card img 0  {} seconds".format(time)


import time
import os
import timeit

start = timeit.default_timer() 
os.system('fswebcam -d /dev/video1 -r 800x720 --no-banner /media/ubuntu/"UBUNTU 16_0"/img-0/"%Y-%m-%d_%H%M".jpg')
stop = timeit.default_timer() 
time = stop-start

print "Time taken for the calculation to write image in SD card img 1 {} seconds".format(time)

import time
import os
import timeit

start = timeit.default_timer() 
os.system('fswebcam -d /dev/video2 -r 800x720 --no-banner /media/ubuntu/"UBUNTU 16_0"/img-0/"%Y-%m-%d_%H%M".jpg')
stop = timeit.default_timer() 
time = stop-start

print "Time taken for the calculation to write image in SD card img 2 {} seconds".format(time)

----------------------------------

https://www.raspberrypi.org/forums/viewtopic.php?t=96706

import os
import datetime

os.system ("fswebcam -d/dev/video0 -r640x480 /home/pi/Documents%s.jpeg" %datetime.datetime.utcnow().strftime ("%Y-%m-%d- -%H-%M-%S"))