import sys
from heapq import heappush, heappop

#The key is to have an extra parameter when using dijkstra's, to note the minimum distance to get to a given island while taking h damage to the hull. This way we can disregard any paths that would damage the hull more than allowed, as they would be out of the list indices regardless.
def sail(a, b, k):
    queue=[(0, 0, a)]
    paths[a][0]=0
    while queue:
        dist, dmg, loc=heappop(queue)
        tbv[loc]=False
        for place in adjs[loc]:
            if not vis[place]:
                for path in adjs[loc][place]:
                    if dmg+path[1]<k and dist+path[0]<paths[place][dmg+path[1]]:
                        paths[place][dmg+path[1]]=dist+path[0]
                if not tbv[loc]:
                    heappush(queue, (min(paths[place]), paths[place].index(min(paths[place])), place))
                tbv[loc]=True
        vis[loc]=True
    distance=min(paths[b])
    if distance==10**6:
        return -1
    else:
        return distance
                        
k, n, m=[int(i) for i in sys.stdin.readline().split()]
paths=[[10**6 for i in range(k)] for i in range(n)]
vis=[False for i in range(n)]
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