import sys
from heapq import heappush, heappop

def sail(a, b, k):
    queue=[(0, 0, a)]
    paths[a][0]=0
    tbv[a]=True
    while queue:
        print(queue)
        dist, dmg, loc=heappop(queue)
        tbv[loc]=False
        for x in range(len(adjs[loc])):
            for y in range(len(adjs[loc][place])):
                short=dist+path[0]
                if dmg+path[1]<k and short<paths[place][dmg+path[1]]:
                    paths[place][dmg+path[1]]=short
                    if not tbv[place]:
                        heappush(queue, (short, paths[place].index(short), place))
                        tbv[place]=True
    distance=min(paths[b])
    if distance==10**6:
        return -1
    else:
        return distance
                        
k, n, m=[int(i) for i in sys.stdin.readline().split()]
paths=[[10**6 for i in range(k)] for i in range(n)]
adjs=[{} for i in range(n)]
tbv=[False for i in range(n)]

for i in range(m):
    a, b, t, h=[int(i) for i in sys.stdin.readline().split()]
    if adjs[a-1].get(b-1, 0)==0:
        adjs[a-1][b-1]=[]
    adjs[a-1][b-1].append((t, h))
    if adjs[b-1].get(a-1, 0)==0:
        adjs[b-1][a-1]=[]
    adjs[b-1][a-1].append((t, h))

a, b=[int(i) for i in sys.stdin.readline().split()]
print(sail(a-1, b-1, k))
for i in range(n):
    print(str(i+1), paths[i])