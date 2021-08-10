my_set = {1, 2, 3, 4}
my_set.remove(2)
my_set.add(0)
# print(my_set)

# for item in my_set:
#     print(item)

class LList:

    def __init__(self):
        self.first = None
        self.last = None

    def append(self, val):
        node = LLNode(val)

        if self.last != None:
            self.last.nxt = node
        else:
            self.first = node
        self.last = node

    # def __getitem__(self, index):
    #     node = self.first
    #     for _ in range(index):
    #         node = node.nxt

    #     return node.val

class LLNode:

    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

llist = LList()
llist.append(1)
llist.append(2)
llist.append(3)
# print(llist[1])
print(llist.__getitem__(1))