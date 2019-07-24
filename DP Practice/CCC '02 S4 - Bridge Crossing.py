import sys

def cross(crossings, mintimes, queue, size):
    for n in range(1, q+1):
        small=10**6
        current=queue[:n]
        if n<=size:
            group=current
            small=max(current)
        elif n==size+1:
            pass
        crossings[n].append(group)
        mintimes[n]=small
        
m=int(sys.stdin.readline())
q=int(sys.stdin.readline())
time=0
crossings=[[] for i in range(q+1)]
mintimes=[0 for i in range(q+1)]
people={}
queue=[]
for i in range(q):
    name=sys.stdin.readline()
    name=name[:len(name)-1]
    queue.append(name)
    speed=int(sys.stdin.readline())
    people[name]=speed

