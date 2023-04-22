from app import index




#dictionary that contains the different rooms of the building
rooms = {'0':'LOBBY','1':'DEPARTMENT CHAIR OFFICE','2':'FACULTY ROOM B','3':'FACULTY ROOM A'
             ,'4':'CONFERENCE ROOM','5':'STAIR','6':'ITSOC OFFICE','7':'LECTURE ROOM 100C','8':'LECTURE ROOM 100B'
             ,'9':'COMSOC OFFICE','10':'STAIR','11':'COMFORT ROOM','12':'VACANT ROOM','13':'LECTURE ROOM 100A','14':'COMFORT ROOM',
             '15':'WEARTHER FORECAST','16':'METEOROLOGY FACULTY','17':'ROOM 101','18':'ROOM 102',
             '19':'STAIR','20':'VACANT ROOM','21':'ROOM 103','22':'ROOM 104','23':'ROOM 105','24':'ROOM 106',
             '25':'ROOM 107','26':'ROOM 108','27':'ROOM 109','28':'ROOM 110','29':'ROOM 111','30':'VACANT ROOM',
             '31':'STAIR','32':'ROOM 112','33':'ROOM 113'}


#creating search tree of the AI using dictionary
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
#17-> ROOM 101
#18-> ROOM 102
#19-> STAIR
#20-> VACANT ROOM 
#21-> ROOM 104
#22-> ROOM 103
#23-> ROOM 105 
#24-> ROOM 106
#25-> ROOM 107
#26-> ROOM 108
#27-> ROOM 109
#28-> ROOM 110
#29-> ROOM 111
#30-> VACANT ROOM
#31-> STAIR
#32-> ROOM 112
#33-> COMFORT ROOM
#34-> ROOM 113

#AI knowledge set(search space)
#still on the building's ground floor
#makauma agdebug :)
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

#converting user input into AI pre-defined knowledge(search space)
def check_input(selected):

    input = selected

    #input name condition is based on the HTML forms

    #cisrooms
    if input == 'dept_chair':
        input = '1'
        return input
    elif input == 'facultyb':
        input = '2'
        return input
    elif input == 'facultya':
        input = '3'
        return input
    elif input == 'conference':
        input = '4'
        return input
    #skip input 5 -> need to work first on the ground floor 
    elif input == 'itsoc':
        input = '6'
        return input
    elif input == 'lectureC':
        input = '7'
        return input
    elif input =='lectureB':
        input = '8'
        return input
    elif input == 'comsoc':
        input = '9'
        return input
    elif input == 'lectureA':
        input = '13'
        return input
    #cab
    else:
        return "hello" #for debugging purposes
    

#main algorithm for the room direction
#BFS algorithm
def path_generator(graph,start,end):

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
                return(path)
        #traversing all neighbor nodes if goal is not yet reached
        visited.append(node)#marking the node as visited
    return False   

def ai_trigger(goal_node):
    
    start_node = '0'
    target_node = goal_node

    direction_list = []#empty list to contain the generated path
    direction_list = path_generator(graph,start_node,target_node)
    return direction_list

#converting AI search space into user inputs
def convert_node(my_list):

    room_list = []

    #iterating through every values in rooms and graphs as well as the generated path
    for a,b in rooms.items():
        for path in my_list:

            #checks if the generated path is equal to the keys in rooms
            if path == a:
                room_list.append(b)#appending user readable room names
    return room_list

            

def main_ai(selected):
    
    node = check_input(selected)

    initial_list = []#initial list to be use for containing the generated path/direction
    new_list = []#list to contain the room names of the generated path/direction

    initial_list = ai_trigger(node)
    new_list = convert_node(initial_list)
    
    return new_list
