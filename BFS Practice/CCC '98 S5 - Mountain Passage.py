import sys

def climb(mountain, size):
    x=0
    y=0
    queue=[(x, y)]
    visited=[(x, y)]
    steps=[[None for i in range(size)] for i in range(size)]
    se=mountain[x][y]
    steps[x][y]=0
    while queue:
        vertex=queue.pop()
        x,y=vertex
        if vertex==(size-1, size-1):
            return steps[x][y]
        ce=mountain[x][y]
        if x > 0:
            ne=mountain[x-1][y]
            if (x-1, y) not in visited and abs(ce-ne) <= 2:
                queue.insert(0, (x-1, y))
                visited.append((x-1, y)) 
                if ce > se or ne > se:
                    steps[x-1][y]=steps[x][y]+1
                else:
                    steps[x-1][y]=steps[x][y]
        if x < size-1:
            ne=mountain[x+1][y]
            if (x+1, y) not in visited and abs(ce-ne) <= 2:
                queue.insert(0, (x+1, y))
                visited.append((x+1, y))  
                if ce > se or ne > se:
                    steps[x+1][y]=steps[x][y]+1
                else:
                    steps[x+1][y]=steps[x][y]
        if y > 0:
            ne=mountain[x][y-1]
            if (x, y-1) not in visited and abs(ce-ne) <= 2:
                queue.insert(0, (x, y-1))
                visited.append((x, y-1))   
                if ce > se or ne > se:
                    steps[x][y-1]=steps[x][y]+1
                else:
                    steps[x][y-1]=steps[x][y]
        if y < size-1:
            ne=mountain[x][y+1]
            if (x, y+1) not in visited and abs(ce-ne) <=2:
                queue.insert(0, (x, y+1))
                visited.append((x, y+1))   
                if ce > se or ne > se:
                    steps[x][y+1]=steps[x][y]+1
                else:
                    steps[x][y+1]=steps[x][y]        
    return "CANNOT MAKE THE TRIP"
        
trips=int(sys.stdin.readline())
for i in range(trips):
    n=int(sys.stdin.readline())
    mountain=[]
    for i in range(n):
        column=[]
        for i in range(n):
            elevation=int(sys.stdin.readline())
            column.append(elevation)
        mountain.append(column)
    print(climb(mountain, n))