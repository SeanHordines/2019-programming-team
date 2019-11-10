#Mercer Binary Bears team D
# Room 251
class Node:
    def __init__(self, a, b, c, s):
        self.large = a
        self.small = b
        self.char = c
        self.size = s
        self.str = ""

    def recurStr(self, c):
        if(self.large is Node):
            self.large.str = c + self.large.str.recurStr(".")
        if(self.small is Node):
            self.small.str = c + self.large.str.recurStr("-")

    def find(self, c):
        if(self.char == c):
            return self
        if(self.large is Node):
            temp = self.large.find(c)
            if(temp != 0):
                return self
        if(self.small is Node):
            temp = self.small.find(c)
            if(temp != 0):
                return self
        return 0


freq = {}
for c in input().upper():
    if not (c in " ,.!?"):
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

nodes = []
for key in freq.keys():
    nodes.append(Node(0, 0, key, freq[key]))

nodes.sort(key = lambda x: x.size)

while(len(nodes) > 1):
    first = nodes.pop(0)
    second = nodes.pop(0)
    curr = Node(first, second, ".", first.size + second.size)

    found = False
    for i in range(len(nodes)):
        if(curr.size > nodes[i].size):
            nodes.insert(i+1, curr)
            found = True
            break
    if not found:
        nodes.append(curr)

root = nodes[0]
root.recurStr("")
length = 0
for key in freq.keys():
    node = root.find(key)
    for d in node.str:
        if(d == "."):
            length += 1
        else:
            length += 3
    length += 1

print(length - 1)
