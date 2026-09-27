import time

def count_time (end, start=0):
    for x in range (start, end+1):
        print (x)
        time.sleep(1)
    print ("Done!")

print (count_time(6, 3))