class Node:
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next


class BinTree:
    def __init__(self, key=None):
        self.root = Node(key)
        self.cur = 0

    def creatNext(self,key):
        n = self.cur
        self.cur = self.cur + 1
        nowNode = self.root
        for i in range(n):
            nowNode = nowNode.next
        nowNode.next = Node(key)
        return nowNode.next

    def getLChild(self, i):
        nowNode = self.root
        n = i*2+1
        if n>self.cur:
            return None
        for i in range(n):
            nowNode = nowNode.next
        return nowNode

    def getRChild(self, i):
        n = i*2+2
        if n>self.cur:
            return None
        nowNode = self.root
        for i in range(n):
            nowNode = nowNode.next
        return nowNode

    def getParent(self, i):
        n = ((i-0.1)//2)
        n = int(n)
        nowNode = self.root
        for i in range(n):
            nowNode = nowNode.next
        return nowNode

    def print(self):
        n = self.cur
        nowNode = self.root
        for i in range(n):
            nowNode = nowNode.next

    def geti(self,i):
        nowNode = self.root
        for i in range(i):
            nowNode = nowNode.next
        return nowNode

class PriorityQueue:
    def __init__(self,key):
        self.q=BinTree(key)

    def insert(self,key):
        nowNode = self.q.creatNext(key)
        n = self.q.cur
        while n>0:
            if key>self.q.geti(int((n - 0.1) // 2)).key:
                break
            n = int((n - 0.1) // 2)
        nowNode.key=self.q.geti(n).key
        self.q.geti(n).key = key

    def print(self):
        nowNode = self.q.root
        while nowNode:
            print(nowNode.key,end=' ')
            nowNode = nowNode.next
        print()

    def delMin(self):
        nowNode = self.q.root
        for i in range(self.q.cur - 1):
            nowNode = nowNode.next
        key = nowNode.next.key
        nowNode.next = None
        self.q.root.key = key
        #Start to sink
        nowNode = self.q.root
        n=0
        while nowNode:
            if self.q.getLChild(n) and self.q.getRChild(n):
                if self.q.getLChild(n).key >= self.q.getRChild(n).key:
                    key1 = self.q.getRChild(n).key
                    new = self.q.getRChild(n)
                    ne = n*2+2
                else:
                    key1 = self.q.getLChild(n).key
                    new = self.q.getLChild(n)
                    ne = n * 2 + 1
            elif self.q.getLChild(n) and not self.q.getRChild(n):
                key1 = self.q.getLChild(n).key
                new = self.q.getLChild(n)
                ne = n * 2 + 1
            else:
                break
            if key1 < key:
                nowNode.key = key1
                nowNode = new
                nowNode.key = key
                n = ne



pq = PriorityQueue(4)
pq.insert(0)
pq.insert(5)
pq.insert(2)
print("Now the priority quene is")
pq.print()
pq.delMin()
print("The priority quene after del is")
pq.print()

