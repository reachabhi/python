# https://www.youtube.com/watch?v=D__VCSj4o6U
import threading, time

def print_epoch(ThreadName, delay):
	count = 0
	while count < 5:
		time.sleep(delay)
		count+=1
		print(ThreadName, '--------', time.time())


class MyThread(threading.Thread): #SUBCLASS of Thread class
	def __init__(self, name, delay):
		threading.Thread.__init__(self)
		self.name = name
		self.delay = delay

	def run(self): #Entry point for thread . We are overridding run method of class Thread. Actually t1.start() internally calls the run method.
		print(f"start thread: {self.name}")
		print_epoch(self.name, self.delay)
		print(f"End Thread: {self.name}")


if __name__ == '__main__':
	t1 = MyThread("Thread1", 1)
	t2 = MyThread("Thread2", 2)
	
	t1.start()
	t2.start()
	
	print(t1.getName()) #getName is a method in Thread class which is accessible in MyThread subclass
	print(t2.getName()) 
	print(threading.activeCount()) #Number of active threads
	print(threading.currentThread())  
	print(threading.enumerate()) #Enumerates all All the threads

	t1.join() #Waits for thread t1 to complete
	t2.join()

	print("Done")

	''' OUTPUT'
	abhishek@abhishekPC:~/python/practice_exercises/multithreading$ python3 thread2.py 
	start thread: Thread1
	start thread: Thread2
	Thread1
	Thread2
	3
	<_MainThread(MainThread, started 140607844841280)>
	[<_MainThread(MainThread, started 140607844841280)>, <MyThread(Thread1, started 140607812208384)>, <MyThread(Thread2, started 140607803815680)>]
	Thread1 -------- 1563872568.9329765
	Thread1 -------- 1563872569.93349
	Thread2 -------- 1563872569.933938
	Thread1 -------- 1563872570.9343863
	Thread2 -------- 1563872571.9342952
	Thread1 -------- 1563872571.9348104
	Thread1 -------- 1563872572.9359622
	End Thread: Thread1
	Thread2 -------- 1563872573.9359593
	Thread2 -------- 1563872575.9381208
	Thread2 -------- 1563872577.9383662
	End Thread: Thread2
	Done

	'''