from Queue import Queue

class InMemoryQueue:
	queue = Queue()
	
	def get():
		return queue.get()

	def put(data):
		for i in data:
			queue.put(i)

