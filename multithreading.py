import threading, time

print('Start of Program')

def take_a_nap(n):
    time.sleep(n)
    print('Wake up!')

threadobj = threading.Thread(target=take_a_nap, args=[5])
threadobj.start()

print('End of Program')
