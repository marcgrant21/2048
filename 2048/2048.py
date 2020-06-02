import gui
import random
from copy import deepcopy



# Give grid the appropriate value
#problem 1#
grid = [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]


# Values to represent the directions the tiles could move
UP = 1
DOWN = 2
RIGHT = 3
LEFT = 4

# Dictionarcol that might be useful
helper = {"count": 0, "Right": RIGHT, "Up": UP, "Left": LEFT, "Down": DOWN}

# Used to store the available keyboard controls
controls = ["<Right>", "<Left>", "<Up>", "<Down>"]

# used to help animate the movement from one tile to another, if functions are implemented correctlcol increasing
# this will increase the speed at which the tiles move and decreasing it will also cause the tiles to move slower
transition_value = 20

#problem 2#
def empty_slots():
    mcol=[]
    for row in range(4):
        for col in range(4):
            if grid[row][col] == 0:
                mcol.append((row,col))
    return mcol

#problem 3#
def random_position():
    return random.choice(empty_slots())

#problem 4#
def add_random_number(board):
    key="NumberTile"+str(helper["count"])
    helper["count"]+=1
    p=random_position()
    row=p[0]
    col=p[1]
    t=gui.random_number()
    gui.put(board,key,t,row,col)
    grid [row][col] = t.value
    return (row,col)

#problem 5#
def find_identifier(board, row, col):
    slot = (row, col)
    for key, value in board.numbers.items():
        if value == slot:
            return key

#problem 6#
def update_grid(row,col,direction):
    for key in helper:
        if helper[key]==direction:
            position = helper[key]
#------------------------------------------------------------------------
    if grid[row][col]!=0 and position==4:
        if row<=3 and col==0:
            return (row,col)
        else:
            if grid[row][col-1]==0 or grid[row][col-1]==grid[row][col]:
                if grid[row][col-1]==0:
                    grid[row][col-1]=grid[row][col]
                    grid[row][col]=0
                    return (row,col-1)
                if grid[row][col]==grid[row][col-1]:
                    grid[row][col-1]= grid[row][col-1]+grid[row][col]
                    grid[row][col]=0
                    return (row,col-1)
            else:
                return (row,col)
#--------------------------------------------------------------------------
    if grid[row][col]!=0 and position==3:
        if row<=3 and col==3:
            return (row,col)
        else:
            if grid[row][col+1]==0 or grid[row][col+1]==grid[row][col]:
                if grid[row][col+1]==0:
                    grid[row][col+1]=grid[row][col]
                    grid[row][col]=0
                    return (row,col+1)
                if grid[row][col]==grid[row][col+1]:
                    grid[row][col+1]= grid[row][col+1]+grid[row][col]
                    grid[row][col]=0
                    return (row,col+1)
            else:
                return (row,col)
#--------------------------------------------------------------------------
    if grid[row][col]!=0 and position==1:
        if row==0 and col<=3:
            return (row,col)
        else:
            if grid[row-1][col]==0 or grid[row-1][col]==grid[row][col]:
                if grid[row-1][col]==0:
                    grid[row-1][col]=grid[row][col]
                    grid[row][col]=0
                    return (row-1,col)
                if grid[row-1][col]==grid[row][col]:
                    grid[row-1][col]= grid[row][col]+grid[row][col]
                    grid[row][col]=0
                    return (row-1,col)
            else:
                return (row,col)
#---------------------------------------------------------------------------
    if grid[row][col]!=0 and position==2:
        if row==3 and col<=3:
            return (row,col)
        else:
            if grid[row+1][col]==0 or grid[row+1][col]==grid[row][col]:
                if grid[row+1][col]==0:
                    grid[row+1][col]=grid[row][col]
                    grid[row][col]=0
                    return (row+1,col)
                if grid[row+1][col]==grid[row][col]:
                    grid[row+1][col]= grid[row][col]+grid[row][col]
                    grid[row][col]=0
                    return (row+1,col)
            else:
                return (row,col)
    else:
        return (row,col)


#problem 7#
'''def animate_movement(board,key,horizontal_distance,vertical_distance,direction):  
    def helper_horizontal(transition, distance):
        if distance < transition_value:
            gui.move_tile(board, kecy, distance * transition_value/transition, 0)
            return True
        else:
            gui.move_tile(board, key, transition, 0)
            return helper_horizontal(transition, distance - transition_value)
    def helper_vertical(transition, distance):
        if distance < transition_value:
            gui.move_tile(board, key,0,distance * transition_value/transition)
            return True
        else:
            gui.move_tile(board, key, 0, transition)
            return helper_vertical(transition, distance - transition_value)    
    if direction == 1:
        return helper_vertical(-1 * transition_value, vertical_distance)   
    elif direction == 2:
        return helper_vertical(transition_value, vertical_distance)
    elif direction == 3:
        return helper_horizontal(transition_value, horizontal_distance) 
    elif direction == 4:
        return helper_horizontal(-1 * transition_value, horizontal_distance)'''

#problem 8#
def move(board,key,direction):
    if direction == 1:
        position = 1
        if gui.move_number(board,key,position,update_grid,animate_movement) == True:
            move(board,key,direction)
    elif direction == 2:
        position = 2
        if gui.move_number(board,key,position,update_grid,animate_movement) == True:
            move(board,key,direction)
    elif direction == 3:
        position = 3
        if gui.move_number(board,key,position,update_grid,animate_movement) == True:
            move(board,key,direction)
    elif direction == 4:
        position = 4
        if gui.move_number(board,key,position,update_grid,animate_movement) == True:
            move(board,key,direction)

#Problem 9#
def move_all_down(board):
    holder=[]
    for i in board.numbers:
        holder.append(board.numbers[i])
    holder.sort()
    for M in reversed(holder):
        if grid[M[0]][M[1]]!=0:
            move(board,find_identifier(board,M[0],M[1]),DOWN)

#Problem 10#
def move_all_up(board):
    holder=[]
    for i in board.numbers:
        holder.append(board.numbers[i])
    holder.sort()
    for M in (holder):
        if grid[M[0]][M[1]]!=0:
            move(board,find_identifier(board,M[0],M[1]),UP)

#Problem 11#
def move_all_right(board):
    holder=[]
    for i in board.numbers:
        holder.append(board.numbers[i])
    holder.sort()
    for M in reversed(holder):
        if grid[M[0]][M[1]]!=0:
            move(board,find_identifier(board,M[0],M[1]),RIGHT)

#Problem 12#
def move_all_left(board):
    holder=[]
    for i in board.numbers:
        holder.append(board.numbers[i])
    holder.sort()
    for M in (holder):
        if grid[M[0]][M[1]]!=0:
            move(board,find_identifier(board,M[0],M[1]),LEFT)
            
#Problem 13#
def move_all(board,event):
        if event==3:
            move_all_right(board)
        elif event == 1:
            move_all_up(board)
        elif event == 2:
            move_all_down(board)
        elif event == 4: 
            move_all_left(board)
            
#problem 14#
'''def keyboard_callback(event,frame,board):
    old_state = deepcopcol(grid)
    move_all(board, event)
    new_state = deepcopcol(grid)
    if old_state != new_state:
        add_random_number(board)'''

#problem 15#
def bind(frame,board):
    map(lambda x:frame.bind(x,lambda event:keyboard_callback(helper[event.keysym],frame,board)),controls)

#Problem 16#
def unbind(frame):
    map(frame.unbind(lambda event:keyboard_callback(helper[event.keysym],frame,board)),controls)
      

#problem 18#           
def merge(board,key):
    f=0
    for i in board.numbers:
        if i!=key and board.numbers[key] and board.numbers[i]==board.numbers[key]:
            gui.remove_number(board,i)
            gui.remove_number(board,key)
            del board.numbers[i]
            x=board.numbers[key]
            f=grid[x[0]][x[1]]
            board.score=board.score+f
            gui.update_score(board)
            c=gui.find_number(f)
            gui.put(board,key,c,x[0],x[1])
            is_game_over(board)
            return True
    else:
        return False
    
#problem 19#
def animate_movement(board,key,hor_dis,ver_dis,direction):
#-----------------------------------------------------------------------------------
    def helper_horizontal(transition, distance):
        if distance < transition_value:
            gui.move_tile(board, key, distance * transition_value/transition, 0)
            if merge(board,key)==True:
                return False
            else:
                return True
        else:
            gui.move_tile(board, key, transition, 0)
            return helper_horizontal(transition, distance - transition_value)
#------------------------------------------------------------------------------------
    def helper_vertical(transition, distance):
        if distance < transition_value:
            gui.move_tile(board, key,0,distance * transition_value/transition)
            if merge(board,key)==True:
                return False
            else:
                return True
        else:
            gui.move_tile(board, key, 0, transition)
            return helper_vertical(transition, distance - transition_value)   
    if direction == 1:
        return helper_vertical(-1 * transition_value, ver_dis)   
    elif direction == 2:
        return helper_vertical(transition_value, ver_dis)
    elif direction == 3:
        return helper_horizontal(transition_value, hor_dis) 
    elif direction == 4:
        return helper_horizontal(-1 * transition_value, hor_dis)
    
#problem 20#
def is_game_over(board):
    def c():
        for i in board.numbers:
            row,col=gui.find_position(board,i)
            if grid[row][col] ==2048:
                gui.game_over(board,True)
                return True
        return False
    if empty_slots()==[]:
        gui.game_over(board,c())
    return c()
   
#problem 21#           
def keyboard_callback(event,frame,board):
    old_state=deepcopy(grid)
    unbind(frame)
    is_game_over(board)
    move_all(board,event)
    bind(frame,board)
    new_state=deepcopy(grid)
    if old_state!=new_state:
        add_random_number(board)
#-----------------------------------------------------------------------------------------
if __name__ == '__main__':
    frame, board = gui.setup()
    row,col = add_random_number(board)
    row,col = add_random_number(board)
    # Finishing setting up colour GameBoard here, answer to Question 17 should go here
    #problem 17#
    bind(frame,board)
    unbind(frame)
    gui.start(frame)

