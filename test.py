from app import index


#dictionary that contains the different rooms of the building
rooms = {'0':'LOBBY','1':'GO LEFT','2':'GO RIGHT','3':'FACULTY ROOM A'
             ,'4':'CONFERENCE ROOM','5':'GO UP STAIR','6':'ITSOC OFFICE','7':'LECTURE ROOM 100C','8':'LECTURE ROOM 100B'
             ,'9':'COMSOC OFFICE','10':'GO UP STAIR','11':'COMFORT ROOM','12':'VACANT ROOM','13':'LECTURE ROOM 100A','14':'COMFORT ROOM',
             '15':'WEATHER FORECAST & SIMULATION LABORATORY','16':'METEOROLOGY FACULTY','17':'ROOM 101','18':'ROOM 102',
             '19':'GO UP STAIR','20':'VACANT ROOM','21':'ROOM 104','22':'ROOM 103','23':'ROOM 105','24':'ROOM 106',
             '25':'ROOM 107','26':'ROOM 108','27':'ROOM 109','28':'ROOM 110','29':'ROOM 111','30':'VACANT ROOM',
             '31':'STAIR','32':'ROOM 112','33':'ROOM 113'}

target = "GO STRAIGHT FORWARD"#for room destination is ROOM 108
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
#15-> WEARTHER FORECAST & MODELING LABORATORY
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
#35-> ROOM 7-COMPUTER LABORATORY ROOM
#36-> ROOM 6
#37-> ROOM 1
#38-> ROOM 200 B
#39-> VACANT ROOM
#40-> ROOM 2
#41-> ROOM 200A
#42-> CLIMATOLOGY LABORATORY
#43-> ROOM 3
#44-> REMOTE SENSING LABORATORY
#45-> ROOM 4
#46-> VACANT ROOM
#47-> ROOM 5
#48-> ROOM 211
#49-> ROOM 210
#50-> ROOM 209
#51-> ROOM 208
#52-> ROOM 207
#53-> ROOM 206
#54-> ROOM 205
#55-> ROOM 204
#56-> ROOM 203
#57-> COMFORT ROOM
#58-> ROOM 202
#59-> ROOM 201
#60-> COMFORT ROOM

#AI knowledge set(search space)
#still on the building's ground floor
#there is a problem when inserting a predecessor node in a succesor node
#backtracking problem
graph = {
    
    '0': ['1','26','2'], #ADDED 108
    "1": ['3'],
    '2': ['4'],
    '3': ['5','6','7'],
    '4': ['8','9','10'],
    '5': ['60','35','36'],#stair
    '6': ['11'],
    '7': ['12'],
    '8': ['13'],
    '9': ['14'],
    '10': [],#stair
    '11': [],#cr
    '12': ['15'],
    '13': [],
    '14': [],#cr
    '15': ['16'],
    '16': ['17'],
    '17': ['18'],
    '18': ['19','20','21'],
    '19': ['49','48'],#stair
    '20': ['22'],
    '21': ['23'],
    '22': [],
    '23': ['24'],
    '24': ['25'],
    '25': ['24','26'],
    '26': ['25','27'],#ADDED 107 -> 25
    '27': ['28'],
    '28': ['29'],
    '29': ['30','31','32'],
    '30': ['33'],
    '31': [],#stair
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
    #cab - lecture rooms and offices only
    #didnt include stairs, crs yet
    elif input == 'forecast':
        input = '15'
        return input
    elif input == 'meteo':
        input = '16'
        return input
    elif input == 'lecture101':
        input = '17'
        return input
    elif input == 'lecture102':
        input = '18'
        return input
    elif input == 'lecture104':
        input = '21'
        return input
    elif input == 'lecture103':
        input = '22'
        return input
    elif input == 'lecture105':
        input = '23'
        return input
    elif input == 'lecture106':
        input = '24'
        return input
    elif input == 'lecture107':
        input = '25'
        return input
    elif input == 'lecture108':
        input = '26'
        return input
    elif input == 'lecture109':
        input = '27'
        return input
    elif input == 'lecture110':
        input = '28'
        return input
    elif input == 'lecture111':
        input = '29'
        return input
    elif input == 'lecture112':
        input = '32'
        return input
    elif input == 'lecture113':
        input = '34'
        return input
    #2nd floor
    elif input == 'lab7':
        input = '35'
        return input
    elif input == 'lab6':
        input = '36'
        return input
    elif input == 'lab1':
        input = '37'
        return input
    elif input == 'lecture200B':
        input = '38'
        return input
    elif input == 'lab2':
        input = '40'
        return input
    elif input == 'lecture200A':
        input = '41'
        return input
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
                print(search_queue)
                print(visited)
                print(*path)
                return(path)
        #traversing all neighbor nodes if goal is not yet reached
        visited.append(node)#marking the node as visited
    return False   

def ai_trigger(goal_node):

    direction_list = []#empty list to contain the generated path
    start_node = '0'#lobby
    
    direction_list = path_generator(graph,start_node,goal_node)#generate direction/path
    return direction_list

#converting AI search space into user inputs
#room 108 and 107 are in incorrect placement when target is 107
#although in the console the nodes are in proper placement 
#temporary solution -> used list.insert() instead of list.append for room 108
def convert_node(my_list):

    room_list = []

    #iterating through every values in rooms and graphs as well as the generated path
    #a -> key
    #b -> values 
    for a,b in rooms.items():
        for path in my_list:
            #checks if the generated path is equal to the keys in rooms
            if path == a:
                if path == '26':#26 -> room 108 then go straight forward
                    #print(b)
                    room_list.insert(1,target)
                else:
                    print(b)
                    room_list.append(b)#appending user readable room names
    print(room_list)#for debugging
    return room_list

            
def main_ai(selected):
    
    node = check_input(selected)#user input into ai input 

    initial_list = []#initial list to be use for containing the generated path/direction
    new_list = []#list to contain the room names of the generated path/direction

    initial_list = ai_trigger(node)#starts the initial state to goal state of ai
    print(initial_list)#for debugging
    new_list = convert_node(initial_list)#ai input to user input
    return new_list
