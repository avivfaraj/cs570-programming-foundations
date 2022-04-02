from Node import DoubleNode


class Deque():

	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def is_empty(self) -> bool:
		"""
		Function to check if there are elements in Deque

		Return:
		True if empty, False otherwise.
		"""
		if self.head == None:
			return True

		return False

	def front(self) -> int:
		"""
		Front of the Deque

		Return:
		Value of the front node in the Deque (int)
		"""
		if self.head == None:
			return None

		return self.head.value

	def back(self) -> int:
		"""
		Back of the Deque

		Return:
		Value of the last node in the Deque (int)
		"""
		if self.tail == None:
			return None

		return self.tail.value

	def push_front(self, value: int) -> None:

		"""
		Push a new node in the front of the Deque
		"""

		# New node with value, but next,previous -> None
		newNode = DoubleNode(value)

		if self.head == None:
			self.head = newNode
			self.tail = newNode
		else:
			self.head.previous = newNode
			newNode.next = self.head
			self.head = newNode

		self.size += 1

	def push_back(self, value: int) -> None:

		"""
		Push a new node to the end of the Deque
		"""
		# New node with value, but next,previous -> None
		newNode = DoubleNode(value)

		if self.tail == None:
			self.head = newNode
			self.tail = newNode
		else:
			self.tail.next = newNode
			newNode.previous = self.tail
			self.tail = newNode

		self.size += 1

	def pop_front(self) -> int:
		"""
		Remove the node in the front of the Deque

		Return:
		Value of the item in front (int), None if empty.
		"""
		if self.head == None:
			return

		val = self.head.value

		if self.head == self.tail:
			self.head, self.tail = None, None
			self.size = 0
			return val

		self.head = self.head.next

		if self.head != None:
			self.head.previous = None

		self.size -= 1

		return val

	def pop_back(self) -> int:
		"""
		Remove the node in the end of the Deque

		Return:
		Value of the item in end (int), None if empty.
		"""
		if self.tail == None:
			return

		val = self.tail.value

		if self.head == self.tail:
			self.head, self.tail = None, None
			self.size = 0
			return val

		self.tail = self.tail.previous

		if self.tail != None:
			self.tail.next = None

		self.size -= 1

		return val

	def get_item(self, forward = True, pop = True) -> int:
		"""
		Generator function to iterate over nodes in Deque

		Input:
		forward -> True to start at the Front and move toward the end,
				   False to start at the End and move backward to the front

		pop     -> Remove nodes from Deque while iterating if True. 
		Return:
		Yield value of current node (int).
		"""

		helper_node = self.head if forward else self.tail

		while helper_node != None:
			val = helper_node.value
			helper_node = (helper_node.next
						   if forward
						   else helper_node.previous
							)
			if pop:
				if forward:
					self.pop_front()
				else:
					self.pop_back()

			yield val


	def __repr__(self) -> None:
		"""
		Represent the Deque in a string

		Return:
		String representation of Deque
		"""
		if self.front() == None:
			return "Queue is Empty!"

		output = "Front -> "
		helper_node = self.head

		while helper_node != None:
			output += str(helper_node.value) + " <-> "
			helper_node = helper_node.next

		return output[:-2] + " Tail"


	def __len__(self) -> int:
		"""
		Return:
		Length of the Deque (int)
		"""
		return self.size


if __name__ == "__main__":
	q = Deque()
	q.push_front(10)
	q.push_back(20)
	q.push_back(30)
	print(q)
	print([i for i in q.get_item(pop = False)])
	assert len(q) == 3
