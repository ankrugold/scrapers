from Queue import Queue

class InMemoryQueue:
	queue = Queue()
	
	def get():
		return queue.get()

	def put(list):
		for i in list:
			queue.put(i)

