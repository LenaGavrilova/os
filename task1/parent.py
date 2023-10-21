#!/usr/bin/python3
import os
import sys
import random

n = int(sys.argv[1])

ch = n
while ch > 0:
    
    child = os.fork()

    if child > 0:
        print("Parent [{os.getpid()}]: I ran children process with PID {child}")
        
    else:
        os.execl("./child.py", "./child.py", str(random.randint(3, 15)))

    if child > 0:
        ch -= 1

ch = n

while ch > 0:
    ch_pid = os.wait()
    status = os.wait()
    
    if status != 0:
        child = os.fork()

        if child > 0:
            print("Parent [{os.getpid()}]: I ran children process with PID {child}")
            
        else:
            os.execl("./child.py", "./child.py", str(random.randint(3, 15)))
    else:
        print("Parent [{os.getpid()}]: Child with PID {ch_pid} terminated. Exit Status {status}")
        ch -= 1

os._exit(os.EX_OK)
