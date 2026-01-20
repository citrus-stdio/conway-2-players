render = []


def display(item):
    for arr in item:
        print(str(arr))
        
def fillRender(x,y):
    global render
    render = []
    for i in range(0,y+1):
        render.append([])
        for j in range(0,x+1):
            render[i].append("   ")
        render[i].append("\n")
    return render

def fill(canvas,x1,y1,x2,y2):
    for i in range(y1,y2):
        for j in range(x1,x2):
            canvas[i][j] = " "

def displayRender():
    global render
    for i in range(len(render)):
        for j in render[i]:
            if j != "[0]":
                print(j,end="")
            else: 
                print("   ",end="")
        

def placeBoard(canvas,item,x,y):
    for i in range(len(item)):
        for j in range(len(item[i])):
            canvas[y+i][x+j]=item[i][j]
                
def placeRender(canvas,item,x,y):
    for i in range(len(item)):
        for j in range(len(item[i])):
            if str(item[i][j])[0] != "[":
                canvas[y+i][x+j] = f"[{item[i][j]}]"
            else:
                canvas[y+i][x+j] = f"{item[i][j]}"
            
def countNeighbors(canvas,x,y,p1,p2):
    neighbors = 0 
    neighborsp1 = 0
    neighborsp2 = 0
    
    xpath = [1,0,-1,-1,-1,0,1,1]
    ypath = [-1,-1,-1,0,1,1,1,0]
    
    for i in range(0,8):
        nx = x+xpath[i]
        ny = y+ypath[i]

        try:
            if nx>=0 and ny >=0:
                neighbor = canvas[ny][nx]
            else:
                continue
        except:
            continue
        
        if neighbor != 0 and neighbor != "[0]":
            neighbors +=1
        if str(neighbor) == str(p1) or str(neighbor) ==f"[{str(p1)}]":
            neighborsp1 +=1
        if str(neighbor) == str(p2) or str(neighbor) ==f"[{str(p2)}]":
            neighborsp2 +=1

    return [neighbors,neighborsp1,neighborsp2]
    
def fate(canvas,x,y,p1,p2):
    neighborArr = countNeighbors(canvas,x,y,p1,p2)
    #print(neighborArr)
    neighbors = neighborArr[0]
    neighborsp1 = neighborArr[1]
    neighborsp2 = neighborArr[2]
    
    alive = True
    
    if canvas[y][x] == 0:
        alive = False
    else:
        alive = True
    

    if alive and neighbors <2:
        return 0
    elif alive and 2<=neighbors<=3 and canvas[y][x]==p1:
        return p1
    elif alive and 2<=neighbors<=3 and canvas[y][x]==p2:
        return p2
    elif alive and neighbors>3:
        return 0
    elif not alive and neighbors ==3 and neighborsp1<neighborsp2:
        return p2
    elif not alive and neighbors ==3 and neighborsp1>neighborsp2:
        return p1
    else:
        return 0
    '''
    if alive and neighbors <2:
        return 0
    elif alive and 1<=neighbors <= 5 and neighborsp1>neighborsp2:
        return p1
    elif alive and 1<=neighbors <= 5 and neighborsp1<neighborsp2:
        return p2
    elif alive and neighbors >3:
        return 0
    elif not alive and neighbors ==3 and neighborsp1>neighborsp2:
        return p1
    elif not alive and neighbors ==3 and neighborsp2>neighborsp1:
        return p2
    else:
        return 0
    '''
def newBoard (canvas,p1,p2):
    blank = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]] 
    
    for i in range(0,len(blank)):
        for j in range(0,len(blank[i])):
            result = fate(canvas,j,i,p1,p2)
            
            if result ==0:
                blank[i][j] =0
            else:
                blank[i][j] = result
            
    return blank

def check(canvas,item,x,y):
    try:
        for i in range(len(item)):
            for j in range(len(item[i])):
                if canvas[y+i][x+j] !=0 and item[i][j] != 0:
                    return False
    except:
        return False
    return True

def getPlayerInput1 (canvas, blocks):
    while True:
        num = int(input("P1, please select a block to purchase: "))
        x= int(input("P1, input the x coordinate (1-10) where you want to place the block: "))
        y= int(input("P1, input the y coordinate (1-10) where you want to place the block: "))
        
        if (1<=num<=len(blocks)) and (1<=x<=10) and (1<=y<=10) and (check(canvas,blocks[num-1].shape,x-1,y-1)):
            return[num-1,x-1,y-1]
        else:
            print("The block you tried to place is not placable in that location, please try again")
            
def getPlayerInput2 (canvas, blocks):
    while True:
        num = int(input("P2, please select a block to purchase: "))
        x= int(input("P2, input the x coordinate (1-10) where you want to place the block: "))
        y= int(input("P2, input the y coordinate (1-10) where you want to place the block: "))
        
        if (1<=num<=len(blocks)) and (1<=x<=10) and (1<=y<=10) and (check(canvas,blocks[num-1].shape,x-1,y-1)):
            return[num-1,x-1,y-1]
        else:
            print("The block you tried to place is not placable in that location, please try again")
            
            
def texturize(item, texture):
    for i in range(len(item)):
        for j in range(len(item[i])):
            if item[i][j] != 0:
                item[i][j] = texture
                
    return item
    
def p1count(canvas,p1):
    count=0
    for i in range(0,len(canvas)):
        for j in range(0,len(canvas[i])):
            if(canvas[i][j]==p1):
                count+=1
                
    return count
    
def p2count(canvas,p2):
    count=0
    for i in range(0,len(canvas)):
        for j in range(0,len(canvas[i])):
            if(canvas[i][j]==p2):
                count+=1
                
    return count
