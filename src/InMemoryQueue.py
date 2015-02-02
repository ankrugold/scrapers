from Queue import Queue

class InMemoryQueue:
	queue = Queue()
	def pop(self):
		return self.queue.get()
	def put(self, list):
		for i in list:
			self.queue.put(i)

