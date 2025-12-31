from funcs import *
import time
import random

class block:
    def __init__(self,s,w,l,c):
        self.shape = s
        self.width = w
        self.length = l
        self.cost = c
        
plus = block([[0,1,0],[1,1,1],[0,1,0]],3,3,5)
bomb = block([[0,1,1,0],[1,0,1,1],[0,1,1,0]],4,3,7)
carrot = block([[0,1,1,1],[1,0,0,1],[0,1,0,1],[0,0,1,0]],4,4,8)
square = block([[1,1,1],[1,0,1],[1,1,1]],3,3,8)

blocks = [plus,bomb,carrot,square]

p1cells=16
p2cells =16

tminusone = [[0 for i in range(10)]for j in range(10)]
tminustwo = [[0 for i in range(10)]for j in range(10)]


board =[[0 for i in range(10)]for j in range(10)]
ystrip = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
xstrip = [[1,2,3,4,5,6,7,8,9,10]]

render = fillRender(30,11)


p1char = input("Player 1, please choose a non-zero character: ")
p2char = input("Player 2, please choose a non-zero character: ")

#placing things on the render to setup
placeRender(render,xstrip,1,0)
placeRender(render,ystrip,0,1)
placeRender(render,blocks[0].shape,18,1)
placeRender(render,[[1]],16,1)
placeRender(render,blocks[1].shape,25,1)
placeRender(render,[[2]],23,1)
placeRender(render,blocks[2].shape,18,5)
placeRender(render,[[3]],16,5)
placeRender(render,blocks[3].shape,25,5)
placeRender(render,[[4]],23,5)


placeRender(render,"X",0,0)
placeRender(render,[["P",1,"C","E","L","L","S",":",p1cells]],20,9)
placeRender(render,[["P",2,"C","E","L","L","S",":",p2cells]],20,10)



placeRender(render,board,1,1)
displayRender()




while p1cells>4 and p2cells>4:
    if p1cells>4:
        p1 = getPlayerInput1(board,blocks)
        placeBoard(board,texturize(blocks[p1[0]].shape,p1char),p1[1],p1[2])
        
        
        p1cells-=blocks[p1[0]].cost
        placeRender(render,[["P",1,"C","E","L","L","S",":",p1cells]],20,9)
        
        placeRender(render,board,1,1)
        displayRender()
        
    if p2cells>4:
        p2 = getPlayerInput2(board,blocks)
        placeBoard(board,texturize(blocks[p2[0]].shape,p2char),p2[1],p2[2])
        
        p2cells-=blocks[p2[0]].cost
        placeRender(render,[["P",2,"C","E","L","L","S",":",p2cells]],20,10)
        
        placeRender(render,board,1,1)
        displayRender()
        

render = fillRender(30,11)

placeRender(render,xstrip,1,0)
placeRender(render,ystrip,0,1)
placeRender(render,[["X"]],30,11)
placeRender(render,[["X"]],0,0)
placeRender(render,board,1,1)

displayRender()

input("Resize the console until you can see both X's, then press enter to continue")

render = fillRender(30,11)
'''

#testing \/

test = [["X","X","X"],[0,0,0],["Y","Y","Y"]]



p1char = "X"
p2char = "Y"

arr = countNeighbors(test,1,1,p1char,p2char)
print(arr)

placeBoard(board,texturize(blocks[0].shape,"X"),0,0)
placeBoard(board,texturize(blocks[1].shape,"Y"),4,4)
placeBoard(board,texturize(blocks[0].shape,"X"),7,0)


placeRender(render,board,0,0)
displayRender()
