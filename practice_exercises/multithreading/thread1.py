import threading, time

def print_epochTime(ThreadName, delay):
	count = 0
	while count < 5:
		time.sleep(delay)
		count+=1
		print(ThreadName, '--------', time.time())

def cube(num):
	print(f'Cube - {num*num*num}')

def square(num):
	print(f'Square - {num*num}')


if __name__ == '__main__':
	t1 = threading.Thread(target = square, args=(2,))
	t2 = threading.Thread(target = cube, args=(2,))
	t3 = threading.Thread(target = print_epochTime, args=("Thread1", 1, ))
	t4 = threading.Thread(target= print_epochTime, args=("Thread2", 2, ))

	t1.start()
	t2.start()
	t3.start()
	t4.start()

	t1.join()
	t2.join()
	t3.join()
	t4.join()
	

	print("Done")