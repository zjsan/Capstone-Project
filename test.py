
#creating the graph using dictionary

#0-> LOBBY
#1-> DEPARTMENT CHAIR OFFICE
#2-> FACULTY ROOM A
#3-> FACULTY ROOM B
#4-> CONFERENCE ROOM
#5-> STAIR
#6-> ITSOC OFFICE
#7-> LECTURE ROOM 100C
#8-> LECTURE ROOM 100B 
#9-> COMSOC OFFICE
#10-> STAIR 
#11-> COMFORT ROOM
#12-> LECTURE ROOM
#13-> LECTURE ROOM 100A
#14-> COMFORT ROOM
graph = {
        '0' : ['1','2'],
        '1' : ['3'],
        '2' : ['4'],
        '3' : ['5','6','7'],
        '4' : ['8', '9','10'],
        '5' : [],
        '6' : ['11'],
        '7' : ['12'],
        '8' : ['13'],
        '9' : ['14'],
        '10' : [],
        '11' : [],
        '12': ['15'],
        '13' : [],
        '14' : [],
        '15': [],
}


def pathfinder(graph,start,goal):

    search_queue = []#list to add nodes in the graph
    search_queue.append(start)#adding starting node in the queue
    visited = []#list for marked nodes during the traversal

    #while the queue is not empty
    #continue traversing 
    #until queue is empty
    while search_queue: 
        node = search_queue.pop(0)#getting first element in the queue
        lastNode = node[-1]#will use to search a path from a node to last node
        nextNodes = graph[lastNode]#appending lastnode for nextnode
        
        #traversing a path from current node to goal node
        #adding possible paths to the queue
        for nextNode in nextNodes:
            path = list(node)#list to contain possible paths
            path.append(nextNode)
            search_queue.append(path)#appending goal path in the queue
            #checking if node is goal
            #if goal has reached
            #get out of the loop
            if nextNode == goal:
                #path.pop(0)
                return path #displaying the path
            #traversing all neighbour nodes if goal is not yet reached
            visited.append(node)#marking the node as visited
    return False

print("PLEASE SELECT ROOM: ")
select = input()

if select == "LOBBY" or "lobby":
    select = '0'
if select == "DEPARTMENT CHAIR OFFICE" or "department chair office":
    select = '1'    
if select == "Faculty room B":
    select = '2'
if select == "FACULTY ROOM A":
     select = '3'
if select == "CONFERENCE ROOM":
     select = '4'
if select == "STAIR":
     select = '5'
if select == "ITSOC OFFICE":
     select = '6'
if select == "LECTURE ROOM 100C":
    select = '7'
if select == "LECTURE ROOM 100B":
     select = '8'
if select == "COMSOC OFFICE":
     select = '9'
if select == "STAIR":
     select = '10'
if select == "COMFORT ROOM":
    select = '11'
if select == " ":
     select = '12'
if select == "LECTURE 100A":
     select = '13'
if select == "COMFORT ROOM":
     select = '14'
if select == "WEATHER FORECASTING AND MODELING LABORATORY":
    select = '15'
# else:
#     print("Room Doesn't Exist")
#     exit()


startPosition = '0'
myList = pathfinder(graph,startPosition,select)

if select == startPosition:
    print("you are already at that position")
    exit()
else:
    myList = []
    myList = pathfinder(graph,startPosition,select)

    newList = []
    for x in myList:
        if x == '0':
            newList.append("LOBBY")
        if x == '1':
            newList.append("DEPARTMENT CHAIR OFFICE -> TURN LEFT")
        if x == '2':
            newList.append("FACULY ROOM B -> TURN RIGHT")
        if x == '3':
            newList.append("FACULTY ROOM A")
        if x == '4':
         newList.append("CONFERENCE ROOM")
        if x == '5':
            newList.append("STAIR")
        if x == '6':
            newList.append("ITSOC OFFICE")
        if x == '7':
            newList.append("LECTURE ROOM 100C")
        if x == '8':
            newList.append("LECTURE ROOM 100B")
        if x == '9':
            newList.append("COMSOC OFFICE")
        if x == '10':
            newList.append("STAIR")
        if x == '11':
            newList.append("COMFORT ROOM")
        if x == '12':
            newList.append(" ")
        if x == '13':
            newList.append("LECTURE ROOM 100A")
        if x == '14':
            newList.append("COMFORT ROOM")
        if x == '15':
            newList.append("WEATHER FORECASTING AND MODELING LABORATORY")

    for x in newList:
        print(x)
