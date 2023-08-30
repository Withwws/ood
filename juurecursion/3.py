def deleteIsland(Map,y,x):
    #delete '1' ที่ติดกับค่าxy โดยแทนที่เป็น 0

    Map[y][x]=0
    if y<len(Map)-1 and Map[y+1][x]==1:#down
        a=deleteIsland(Map,y+1,x)
    if x<len(Map[y])-1 and Map[y][x+1] == 1:#right
        b=deleteIsland(Map,y,x+1)
    if x>0 and Map[y][x-1]==1:#left
        c=deleteIsland(Map,y,x-1)
    if y>0 and Map[y-1][x]==1:#up
        d=deleteIsland(Map,y-1,x)

    return True


def countIsland(Map):
    map_count = 0
    for y, map_row in enumerate(Map):
        for x, map_col in enumerate(map_row):
            if map_col == 1:
                deleteIsland(Map, y, x)
                map_count += 1
    return map_count

Input = input("Enter Input : ").split('/')
Map=[] 
for i in Input:
    temp=[*i]
    temp = list(map(int,temp))
    Map.append(temp)
print(f"Island have : {countIsland(Map)}")