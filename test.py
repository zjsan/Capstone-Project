#dfs traversal
def maze(graph,start,end):

    
    search_stack = []#creating an empty stack for the traversal
    search_stack.append(start)
    visited = []#list for visited rooms
    

    #continue traversing all rooms
    #until the stack is empty
    while search_stack:

        currentRoom = search_stack.pop()#popping recently added element --> LIFO RULE
        goalRoom = currentRoom[-1]#will use to search a path from current room to goalroom
        nextRooms = graph[goalRoom]

        #traversing all rooms
        #adding possible paths
        for nextRoom in nextRooms:
            if nextRoom not in visited:
                path = list(currentRoom)#creating a list of possbile path and appending rooms that leads to goal room
                path.append(nextRoom)
                search_stack.append(path)#appending path in the stack
                visited.append(nextRoom)#marking down visited rooms

                #checking if currentRoom is the goalRoom
                #if goal room is found break loop
                if nextRoom == end:
                    return(path)
                
#creating the graph using dictionary

#A-> LOBBY
#B-> DEPARTMENT CHAIR OFFICE
#C-> FACULTY ROOM A
#D-> FACULTY ROOM B
#E-> STAIR 1
#F-> ITSOC OFFICE
#G-> COMFORT ROOM 1
#H-> LECTURE ROOM 1
#I-> LECTURE ROOM 2
#J-> CONFERENCE ROOM
#K-> STAIR 2
#L-> LECTURE ROOM 4
#M-> COMSOC OFFICE
#N-> COMFORT ROOM 2
#O-> LECTURE ROOM 3
graph = {
        'A' : ['B','C'],
        'B' : ['D'],
        'C' : ['J'],
        'D' : ['E','H'],
        'E' : ['F', 'H'],
        'F' : ['G','H'],
        'G' : [],
        'H' : ['I'],
        'I' : [],
        'J' : ['K', 'L'],
        'K' : ['M', 'L'],
        'L' : ['O'],
        'M' : ['N','L'],
        'N' : [],
        'O' : [],
}


print("PLEASE SELECT ROOM: ")
select = input()

if select == "LOBBY":
    select = 'A'
elif select == "DEPARTMENT CHAIR OFFICE":
    select = 'B'    
elif select == "FACULTY ROOM A":
    select = 'C'
elif select == "FACULTY ROOM B":
    select = 'D'
elif select == "STAIR 1":
    select = 'E'
elif select == "ITSOC OFFICE":
    select = 'F'
elif select == "COMFORT ROOM 1":
    select = 'G'
elif select == "LECTURE ROOM 1":
    select = 'H'
elif select == "LECTURE ROOM 2":
    select = 'I'
elif select == "CONFERENCE ROOM":
    select = 'J'
elif select == "STAIR 2":
    select = 'K'
elif select == "LECTURE ROOM 4":
    select = 'L'
elif select == "COMSOC OFFICE":
    select = 'M'
elif select == "COMFORT ROOM 2":
    select = 'N'
elif select == "LECTURE ROOM 3":
    select = 'O'
    
startPosition = 'A'

if startPosition == select:
    print("you are already at that position")
    exit()
    
myList = []
myList = maze(graph,startPosition,select)

newList = []
for x in myList:
    if x == 'A':
        newList.append("LOBBY")
    if x == 'B':
        newList.append("DEPARTMENT CHAIR OFFICE")
    if x == 'C':
        newList.append("FACULY ROOM A")
    if x == 'D':
        newList.append("FACULTY B")
    if x == 'E':
        newList.append("STAIR 1")
    if x == 'F':
        newList.append("ITSOC OFFICE")
    if x == 'G':
        newList.append("COMFORT ROOM 1")
    if x == 'H':
        newList.append("LECTURE ROOM1")
    if x == 'I':
        newList.append("LECTURE ROOM2")
    if x == 'J':
        newList.append("CONFERENCE ROOM")
    if x == 'K':
        newList.append("STAIR 2")
    if x == 'L':
        newList.append("LECTURE ROOM 4")
    if x == 'M':
        newList.append("COMSOC OFFICE")
    if x == 'N':
        newList.append("COMFORT ROOM 2")
    if x == 'O':
        newList.append("LECTURE ROOM 3")
        
for x in newList:
    print(x)
