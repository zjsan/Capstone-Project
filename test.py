from app import index

#creating the graph using dictionary

#0-> LOBBY
#1-> DEPARTMENT CHAIR OFFICE
#2-> FACULTY ROOM B
#3-> FACULTY ROOM A
#4-> CONFERENCE ROOM
#5-> STAIR
#6-> ITSOC OFFICE
#7-> LECTURE ROOM 100C
#8-> LECTURE ROOM 100B 
#9-> COMSOC OFFICE
#10-> STAIR 
#11-> COMFORT ROOM
#12-> VACANT ROOM
#13-> LECTURE ROOM 100A
#14-> COMFORT ROOM
#15-> WEARTHER FORECAST 
#16-> METEOROLOGY FACULTY 
#17-> FACULTY ROOM B
#18-> FACULTY ROOM A
#19-> CONFERENCE ROOM
#20-> STAIR
#21-> ITSOC OFFICE
#22-> LECTURE ROOM 100C
#23-> LECTURE ROOM 100B 
#24-> COMSOC OFFICE
#25-> STAIR 
#26-> COMFORT ROOM
#27-> VACANT ROOM
#28-> LECTURE ROOM 100A
#29-> COMFORT ROOM
#30-> LOBBY
#31-> DEPARTMENT CHAIR OFFICE
#32-> FACULTY ROOM B
#33-> FACULTY ROOM A
#34-> CONFERENCE ROOM

graph = {
    
    '0': ['1','2'], 
    "1": ['3'],
    '2': ['4'],
    '3': ['5','6','7'],
    '4': ['8','9','10'],
    '5': [],
    '6': ['11'],
    '7': ['12'],
    '8': ['13'],
    '9': ['14'],
    '10': [],
    '11': [],
    '12': ['15'],
    '13': [],
    '14': [],
    '15': ['16'],
    '16': ['17'],
    '17': ['18'],
    '18': ['19','20','21'],
    '19': [],
    '20': ['22'],
    '21': ['23'],
    '22': [],
    '23': ['24'],
    '24': ['25'],
    '25': ['26'],
    '26': ['27'],
    '27': ['28'],
    '28': ['29'],
    '29': ['30','31','32'],
    '30': ['33'],
    '31': [],
    '32': ['34'],
    '33': [],
    '34': [],

}

def pathFinder(graph,start,end):

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
            if nextNode == end:
                #displaying the path
                print(*path)
                return True
        #traversing all neighbor nodes if goal is not yet reached
        visited.append(node)#marking the node as visited
    return False  

pathFinder(graph,'0','5')