import sys
pie=int(sys.stdin.readline())
people=int(sys.stdin.readline())

distributions=[0 for i in range(pie+1)]
combin=[[] for i in range(pie+1)]
last_served=[[] for i in range(pie+1)]
last_served[people+1].append(people-1)
combin[people+1]=[[1 for i in range(people-1)]+[2]]

def distribute(pie, distributions, last_served):
    for p in range(people+2, pie+1):
        i=0
        m=last_served[p-1][len(last_served[p-1])-1]
        if m>0:
            last_served[p-1].append(m-1)
        else:
            last_served[p-1].append(people-1)
        i=0
        for c in combin[p-1]:
            for s in last_served[p-1]:
                c[s]+=1
                if c not in combin[p]:
                    order=c[:]
                    order.sort()
                    if c==order:
                        combin[p].append(c[:])
                        c[s]-=1
                        if s not in last_served[p]:
                            last_served[p].append(s)
                        distributions[p]+=1
                    else:
                        c[s]-=1
                else:
                    c[s]-=1
            i+=1
    return distributions[pie]
        
print(distribute(pie, distributions, last_served))