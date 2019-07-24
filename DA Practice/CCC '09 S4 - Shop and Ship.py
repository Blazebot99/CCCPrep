import sys

class PriorityQueue():
    
    def __init__(self):
        self.items=[]
        
    def isempty(self):
        return self.items==[]
    
    def insert(self, item):
        pos=0
        if self.isempty():
            self.items.append(item)
            
        while item > self.items[pos]:
            pos+=1
        self.items.insert(pos, item)
    
    def remove(self):
        return self.items.pop(0)

def transport(cities, dest):
    mincost=10**6
    queue=PriorityQueue()
    queue.items.append(dest)
    print(queue.items)
    while queue:
        city=queue.remove()
        print(city)
        if cities[city][1] and cities[city][1]+cities[city][0]<mincost:
            mincost=cities[city][1]+cities[city][0]
        for neighbor in cities[city][2]:
            adj=neighbor
            if not cities[adj][3]:
                if adj not in queue.items:
                    queue.insert(adj)
                if not cities[adj][0] or cities[city][0]+edges[city][adj]<cities[adj][0]:
                    cities[adj][0]=cities[city][0]+edges[city][adj]
        cities[city][3]=True
    return mincost

data=sys.stdin.read().split('\n')
edges=[[0 for i in range(n)] for i in range(int(data[0]))]
cities=[[0, 0, [], False] for i in range(int(data[0]))]
count=2
for i in range(int(data[1])):
    x, y, c=[int(i) for i in data[count].split()]
    edges[x-1][y-1]=c
    cities[x-1][2].append(y-1)
    edges[y-1][x-1]=c
    cities[y-1][2].append(x-1)
    count+=1

p=int(sys.stdin.readline())
for i in range(p):
    z, c=[int(i) for i in data[count].split()]
    cities[z-1][1]=c
    count+=1

d=int(sys.stdin.readline())-1
print(transport(cities, d))