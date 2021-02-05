class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root_node):
	def traverse(node):
		if node:
			lst.append(str(node.val))
			traverse(node.left)
			traverse(node.right)
		else:
			lst.append("-")

	lst = []
	traverse(root_node)
	return ' '.join(lst)

def deserialize(data):
	def construct():
		val = next(lst)
		if val == '-':
			return None

		node = Node(int(val))
		node.left = construct()
		node.right = construct()
		return node

	lst = iter(data.split(' '))
	return construct()


node_h = Node(0)
node_d = Node(1, node_h)
node_e = Node(4)
node_b = Node(3, node_d, node_e)
node_f = Node(7)
node_g = Node(13)
node_c = Node(9, node_f, node_g)
node_a = Node(5, node_b, node_c)

print(serialize(node_a))

print(deserialize(serialize(node_a)).left.val)
