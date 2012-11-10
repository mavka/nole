# coding: utf-8

import time, os

x = int(raw_input("Сколько отдыхаем? "))
y = 60
print "Отдыхаем %r минуты" %x
time.sleep(x*y)
print "Милая, а не поработать ли тебе?"
for i in range(8):
	os.system("afplay /System/Library/Sounds/Purr.aiff")
#os.system("say go work now!")



# import time
# for i in range(10):
# 	print "asdfsdfasdf"
# 	time.sleep(5.0)

# import threading


# def hello():
#     print "hello, world"

# t = threading.Timer(30.0, hello)
# t.start() # after 30 seconds, "hello, world" will be printed