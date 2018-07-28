import time
import os
import timeit
import datetime

#from datetime import datetime

#d = datetime.now("%Y-%m-%d_%H%M") 

#or

#d = str(datetime.now())  

start = timeit.default_timer() 

os.system('streamer -q -c /dev/video0 -f rgb24 -r 3 -t 00:00:05 -o /media/ubuntu/"UBUNTU 16_0"/video0/d.avi')

stop = timeit.default_timer() 

time = stop-start

print "Time taken for the calculation to write video 0 in SD card was {} seconds".format(time)

text_file = open("/media/ubuntu/UBUNTU 16_0/video-read.txt","a")

with open("/media/ubuntu/UBUNTU 16_0/video-read.txt","a") as text_file:

   #text_file.write('Printed string %s. Recorded at: %s\n' % video-read %datetime.now())
   text_file.write('\n' % time)
   text_file.close()
   
   
   
   
 
--------------------------------------------------------------------------------------
#import sys
#from datetime import datetime  
   
## filename = '/path/to/output/myfile-%s.txt'%datetime.now().strftime('%Y-%m-%d_%H%M')
##f = open(filename,'w')
##f.write(out)
##f.close()

------------------------------------

python /path/to/script/myscript.py > /path/to/output/myfile$(date "+%b_%d_%Y").txt

https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/7
https://www.raspberrypi.org/forums/viewtopic.php?t=49530
https://wolfpaulus.com/embedded/raspberrypi_webcam/


import time
import os
import datetime
os.system ("streamer -q -c /dev/video0 -f rgb24 -r 3 -t 00:00:05 -o /media/ubuntu/"UBUNTU 16_0"/video0/%s.avi" %datetime.datetime.utcnow().strftime ("%Y-%m-%d- -%H-%M-%S"))