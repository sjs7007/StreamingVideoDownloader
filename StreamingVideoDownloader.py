# http://www.quora.com/Ankesh-Porwal/Posts/Downloading-buffered-YouTube-videos-on-Ubuntu-using-terminal

import os

# Step 1 : Find flashplayer's pid : 

os.system("pgrep -f flashplayer > pid.txt")
f=open('/home/shinchan/pid.txt','r')
x=int(f.readline())

# Step 2 : Navigate through RAM : 

os.system("ls /proc/%d/fd -l > list.txt" %x) 

# Step 3 : Note down the number associated with '/tmp/FlashXXXXXX (deleted)

s=open('~/list.txt','r').read()
loc=s.find('/tmp/Flash') # will contain loc of '/'

end=loc-5 #end location
temp=end
start=0
while(s[temp]!=' '):
	start=temp	
	temp=temp-1

number = int(s[start:end+1])

# Step 4 : copy video to another location

name=raw_input("Enter Video name : ")
name=name.replace(' ','_')
os.system("cp /proc/%d/fd/%d ~/%s.flv" %(x,number,name))
	



