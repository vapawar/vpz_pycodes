class Tree:
	def __init__(self, data, left=None, right=None):
		self.data=data
		self.left=left
		self.right=right

def add_node(root, data):
	if root == None:
		return
	t = Tree(data, None, None)
	next=root
	prev=None
	while next:
		prev=next
		if data<next.data:
			next=next.left
		else:
			next=next.right
	if data>= prev.data:
		prev.right=t
	else:
		prev.left=t
	
def tinorder( tree):
	if tree == None:
		return
	tinorder(tree.left)
	print(tree.data)
	tinorder(tree.right)

def tpreorder( tree):
	if tree == None:
		return
	print(tree.data)
	tpreorder(tree.left)
	tpreorder(tree.right)

def tpostorder( tree):
	if tree == None:
		return
	tpostorder(tree.left)
	tpostorder(tree.right)
	print(tree.data)

t=Tree(1234, None, None)
add_node(t, 38)
add_node(t, 2468)
add_node(t,46488)
add_node(t,4683)
add_node(t,4823)
add_node(t,48)
tinorder(t)