import sys
distance=int(sys.stdin.readline())
n=int(sys.stdin.readline())
clubs=[]
for i in range(n):
    clubs.append(int(sys.stdin.readline()))
strokes=[0]*(distance+1)
usedClubs=[0]+[0]*(distance)

def hole_minimum(clubs, distance, strokes, usedClubs):
    checked=False
    for dist in range(distance+1):
        sc=5281
        newClub=0
        for club in [c for c in clubs if c<=dist]:
            #testing the current club, so change the last club used for this distance. 
            usedClubs[dist]=club
            #If the strokes needed for the current distance minus the current club's distance plus one extra stroke (to represent the current club) is less, and the distance matches all the previous clubs' sums combined, change the number of strokes needed for this distance. 
            if strokes[dist-club]+1<sc and dist==find_distance(usedClubs, dist):
                checked=True
                sc=strokes[dist-club]+1
                newClub=club
        #only modify if checked, as it is necessary to keep the values smaller than the smallest club as 0 in order to achieve the proper values for the larger values.
        if checked:
            strokes[dist]=sc
            #sets the optimal club to add on for this distance, or resets it to 0 if this distance is unreachable.
            usedClubs[dist]=newClub
    return strokes[distance]

def find_distance(usedClubs, dist):
    club=dist
    totalDist=0
    while club>0 and usedClubs[club]>0:
        currentClub=usedClubs[club]
        totalDist+=currentClub
        club-=currentClub
    return totalDist

conclusion=hole_minimum(clubs, distance, strokes, usedClubs)
print(strokes)
print(usedClubs)
if conclusion < 5281:
    print("Roberta wins in " + str(conclusion) + " strokes.")
else:
    print("Roberta acknowledges defeat.")