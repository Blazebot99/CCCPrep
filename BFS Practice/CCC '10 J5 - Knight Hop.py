import sys
sx, sy=[int(i) for i in sys.stdin.readline().split()]
dx, dy=[int(i) for i in sys.stdin.readline().split()]

def hop(sx, sy, dx, dy):
    sx=sx-1
    sy=sy-1
    queue=[(sx, sy)]
    visited=[(sx, sy)]
    board=[[int(i) for i in range(8)] for i in range(8)]
    steps=[[None for i in range(8)] for i in range(8)]
    steps[sx][sy]=0
    while queue:
        x, y=queue.pop()
        if (x, y)==(dx-1, dy-1):
            continue
        else:
            if x>1 and y>0:
                if (x-2, y-1) not in visited:
                    queue.insert(0, (x-2, y-1))
                    visited.append((x-2, y-1))
                    if steps[x-2][y-1] is None or steps[x][y]+1<steps[x-2][y-1]:
                        steps[x-2][y-1]=steps[x][y]+1
            if x>0 and y>1:
                if (x-1 , y-2) not in visited:
                    queue.insert(0, (x-1, y-2))
                    visited.append((x-1, y-2))
                    if steps[x-1][y-2] is None or steps[x][y]+1<steps[x-1][y-2]:
                        steps[x-1][y-2]=steps[x][y]+1
            if x<7 and y>1:
                if (x+1, y-2) not in visited:
                    queue.insert(0, (x+1, y-2))
                    visited.append((x-2, y-1))
                    if steps[x+1][y-2] is None or steps[x][y]+1<steps[x+1][y-2]:
                        steps[x+1][y-2]=steps[x][y]+1
            if x<6 and y>0:
                if (x+2, y-1) not in visited:
                    queue.insert(0, (x+2, y-1))
                    visited.append((x+2, y-1))
                    if steps[x+2][y-1] is None or steps[x][y]+1<steps[x+2][y-1]:
                        steps[x+2][y-1]=steps[x][y]+1
            if x<6 and y<7:
                if (x+2, y+1) not in visited:
                    queue.insert(0, (x+2, y+1))
                    visited.append((x+2, y+1))
                    if steps[x+2][y+1] is None or steps[x][y]+1<steps[x+2][y+1]:
                        steps[x+2][y+1]=steps[x][y]+1
            if x<7 and y<6:
                if (x+1, y+2) not in visited:
                    queue.insert(0, (x+1, y+2))
                    visited.append((x+1, y+2))
                    if steps[x+1][y+2] is None or steps[x][y]+1<steps[x+1][y+2]:
                        steps[x+1][y+2]=steps[x][y]+1
            if x>0 and y<6:
                if (x-1, y+2) not in visited:
                    queue.insert(0, (x-1, y+2))
                    visited.append((x-1, y+2))
                    if steps[x-1][y+2] is None or steps[x][y]+1<steps[x-1][y+2]:
                        steps[x-1][y+2]=steps[x][y]+1
            if x>1 and y<7:
                if (x-2, y+1) not in visited:
                    queue.insert(0, (x-2, y+1))
                    visited.append((x-2, y+1))
                    if steps[x-2][y+1] is None or steps[x][y]+1<steps[x-2][y+1]:
                        steps[x-2][y+1]=steps[x][y]+1
    return steps[dx-1][dy-1]

print(hop(sx, sy, dx, dy))