import sys
pages=int(sys.stdin.readline())
book={}
for i in range(pages):
    line=sys.stdin.readline().split()
    if len(line)<2:
        book[i+1]=[]
    else:
        paths=[int(i) for i in line[1:]]
        book[i+1]=paths

def read(book, pages):
    to_read=[1]
    alr_read=[1]
    pfo={1:1}
    shortest_path=None
    while to_read:
        page=to_read.pop()
        for new in book[page]:
            if pfo.get(new, None) is None or pfo[new]>pfo[page]+1:
                pfo[new]=pfo[page]+1 
            if book[new]==[]:
                if shortest_path is None or shortest_path>pfo[new]:
                    shortest_path=pfo[new]
            if new not in alr_read: 
                to_read.insert(0, new)
                alr_read.append(new)
    alr_read.sort()
    if alr_read!=[int(i)+1 for i in range(pages)]:
        print("N")
    else:
        print("Y")
    return shortest_path

print(read(book, pages))