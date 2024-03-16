from Node import Node
from Tree import Tree


a = Node(5)
b = Node(10)
c = Node(2)
d = Node(8)
e = Node(3)

t = Tree()
t.__init__(a)


t.put(a,c,True)
t.put(a,e,False)
t.put(c,d,True)
t.put(c,b,False)

print(a.get_imbalance())
print(e.get_imbalance())
print(t.find_max_imbalance())



t.move_subtree(c,e,True)

print(a.get_imbalance())
print(e.get_imbalance())
print(t.find_max_imbalance())


t.move_subtree(d,a,True)

print(a.get_imbalance())
print(e.get_imbalance())
print(t.find_max_imbalance())

