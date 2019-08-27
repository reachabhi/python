import threading
x = 0

'''
Suppose we want to increment a value x using 2 threads. SInce 2 threads are accessing the same resource i.e. x we can hit thread sync issues
To avoid this, we need to make use of locks. In below example try removing locks and see the result.
'''

def thread_task(lock):
	global x
	for i in range(1000000): 
		lock.acquire()		 
		x+=1				 
		lock.release()

def main_task():
	lock = threading.Lock() #Create a lock instance which will be passed to the method which needs to be called by that thread

	t1=threading.Thread(target=thread_task, args = (lock,))
	t2=threading.Thread(target=thread_task, args = (lock,))

	t1.start()
	t2.start()

	t1.join()
	t2.join()

if __name__ == '__main__':
	main_task()
	print(x)