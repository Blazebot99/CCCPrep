import sys

n, size=[int(i) for i in sys.stdin.readline().split()]
factory=[]
targets=[]
cameras=[]
conveyors=["L", "R", "U", "D"]
testables=[]
steps=[[10**6 for i in range(size)] for i in range(n)]
conpaths={}

def conveyor_test(factory, x, y):
    visited=[(x, y)]
    while True:
        if factory[y][x]=="U":
            if (x, y-1) in visited:
                return (False,)
            elif factory[y-1][x] in conveyors:
                visited.append((x, y-1))
                y=y-1            
            elif steps[y-1][x]==-1:
                return (False,)
            else:
                return (True, x, y-1)
        elif factory[y][x]=="D":
            if (x, y+1) in visited:
                return (False,)
            elif factory[y+1][x] in conveyors:
                visited.append((x, y-1))
                y=y+1            
            elif steps[y+1][x]==-1:
                return (False,)
            else:
                return (True, x, y+1)
        elif factory[y][x]=="L":
            if (x-1, y) in visited:
                return (False,)
            elif factory[y][x-1] in conveyors:
                visited.append((x-1, y))
                x=x-1        
            elif steps[y][x-1]==-1:
                return (False,)
            else:
                return (True, x-1, y)
        elif factory[y][x]=="R":
            if (x+1, y) in visited:
                return (False,)
            elif factory[y][x+1] in conveyors:
                visited.append((x+1, y))
                x=x+1        
            elif steps[y][x+1]==-1:
                return (False,)
            else:
                return (True, x+1, y)    
            
for y in range(n):
    row=sys.stdin.readline()
    row=list(map(str, row[:len(row)-1]))
    for x in range(len(row)):
        if row[x]==".":
            targets.append((x, y))
        elif row[x]=="S":
            start=(x, y)
            steps[y][x]=0
        elif row[x]=="C":
            cameras.append((x, y))
        elif row[x]=="W":
            steps[y][x]=-1
        else:
            testables.append((x, y))
    factory.append(row)
  
for c in cameras:
    for i in range(c[1], n):
        if factory[i][c[0]]=="W":
            break
        elif factory[i][c[0]] not in conveyors:
            steps[i][c[0]]=-1
    i=c[1]-1
    while factory[i][c[0]]!="W":
        if factory[i][c[0]] not in conveyors:
            steps[i][c[0]]=-1
        i-=1
    for i in range(c[0], size):
        if factory[c[1]][i]=="W":
            break
        elif factory[c[1]][i] not in conveyors:
            steps[c[1]][i]=-1
    i=c[0]-1
    while factory[c[1]][i]!="W":
        if factory[c[1]][i] not in conveyors:
            steps[c[1]][i]=-1
        i-=1

for conveyor in testables:
    result=conveyor_test(factory, conveyor[0], conveyor[1])
    if not result[0]:
        steps[conveyor[1]][conveyor[0]]=-1
    else:
        conpaths[(conveyor)]=(result[1], result[2])
        
def escape(factory, targets, start, size, n):
    if steps[start[1]][start[0]]==-1:
        for target in targets:
            print(-1)
        return
    queue=[start]
    visited=[start]
    while queue:
        x, y=queue.pop()
        if steps[y][x]+1<steps[y-1][x] and (x, y-1) not in visited:
            visited.append((x, y-1))
            steps[y-1][x]=steps[y][x]+1
            if (x, y-1) in conpaths:
                if conpaths[(x, y-1)] not in visited and steps[conpaths[(x, y-1)][1]][conpaths[(x, y-1)][0]] > steps[y-1][x]:
                    queue.insert(0, conpaths[(x, y-1)])
                    visited.append(conpaths[(x, y-1)])
                    steps[conpaths[(x, y-1)][1]][conpaths[(x, y-1)][0]]=steps[y-1][x]
            else:
                queue.insert(0, (x, y-1))
        if steps[y][x]+1<steps[y+1][x] and (x, y+1) not in visited: 
            visited.append((x, y+1))
            steps[y+1][x]=steps[y][x]+1
            if (x, y+1) in conpaths:
                if conpaths[(x, y+1)] not in visited and steps[conpaths[(x, y+1)][1]][conpaths[(x, y+1)][0]] > steps[y+1][x]:
                    queue.insert(0, conpaths[(x, y+1)])
                    visited.append(conpaths[(x, y+1)])
                    steps[conpaths[(x, y+1)][1]][conpaths[(x, y+1)][0]]=steps[y+1][x]
            else:
                queue.insert(0, (x, y+1))
        if steps[y][x]+1<steps[y][x-1] and (x-1, y) not in visited:
            visited.append((x-1, y))
            steps[y][x-1]=steps[y][x]+1
            if (x-1, y) in conpaths:
                if conpaths[(x-1, y)] not in visited and steps[conpaths[(x-1, y)][1]][conpaths[(x-1, y)][0]] > steps[y][x-1]:
                    queue.insert(0, conpaths[(x-1, y)])
                    visited.append(conpaths[(x-1, y)])
                    steps[conpaths[(x-1, y)][1]][conpaths[(x-1, y)][0]]=steps[y][x-1]
            else:
                queue.insert(0, (x-1, y))
        if steps[y][x]+1<steps[y][x+1] and (x+1, y) not in visited:
            visited.append((x+1, y))
            steps[y][x+1]=steps[y][x]+1
            if (x+1, y) in conpaths:
                if conpaths[(x+1, y)] not in visited and steps[conpaths[(x+1, y)][1]][conpaths[(x+1, y)][0]]> steps[y][x+1]:
                    queue.insert(0, conpaths[(x+1, y)])
                    visited.append(conpaths[(x+1, y)])
                    steps[conpaths[(x+1, y)][1]][conpaths[(x+1, y)][0]]=steps[y][x+1]                
            else:
                queue.insert(0, (x+1, y))
    for target in targets:
        if steps[target[1]][target[0]]<10**6:
            print(steps[target[1]][target[0]])
        else:
            print(-1) 
            
escape(factory, targets, start, size, n)