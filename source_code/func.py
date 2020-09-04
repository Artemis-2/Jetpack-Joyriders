
from scene import *
from person import *
from settings import *


def blitobject(scene, item, x, y):
    """ Blit given item over the scene where specified
    after deleting previous instance"""
    scenematrix = scene.returnmatrix()
    itemmatrix = item.returnmatrix()
    k = 0
    l = 0
    # deleting previous position
    # print("item.x:",item.x)
    # print("item.y:",item.y)
    # print("item.length:",item.length)
    for i in range(item.x, item.x + item.length):
        # print("888888")
        for j in range(item.y, item.y + item.width):
            # print("i:",i,"J:",j)
            scenematrix[i][j] = ' '
    # putting at new position
    # print("***")
    for i in range(x, x + item.length):
        for j in range(y, y + item.width):
            # print("i:",i,"J:",j)
            scenematrix[i][j] = itemmatrix[i-x][j-y]
            
    scene.updatescene(scenematrix)



def clashcheck(scene, item, x, y):
    
    scenematrix = scene.returnmatrix()

    item.in_range=0
    for i in range(y + item.width,y+ item.width+20):
        #magnet in front( on right)
        for q in range(0,32):
            if scenematrix[q][i] in [colors['Cyan']+'0' + RESET]:
                item.in_range=1

    for i in range(y + item.width-20,y+ item.width):
        # magnet behind (on left)
        for q in range(0,32):
            if scenematrix[q][i] in [colors['Cyan']+'0' + RESET]:
                item.in_range=2







    # check left boundary of item
    if y <= scene.start:
        return 1
    for i in range(x, x + item.length):
        if(i >= scene.length):
            return 1
    
    for i in range(x, x + item.length):
        if scenematrix[i][y] in [(colors['Brown']+'#' + RESET)]:
             return 1
    for i in range(x, x + item.length):
        if scenematrix[i][y] in [(colors['Yellow']+'$' + RESET)]:
            return 4
    for i in range(x, x + item.length):
        if scenematrix[i][y] in [(colors['Red']+'@' + RESET)]:
            return 2
    for i in range(x, x + item.length):
        if scenematrix[i][y] in ['+']:
            return 3
    for i in range(x, x + item.length):
        if scenematrix[i][y] in ['@']:
            return 5
    for i in range(x, x + item.length):
        if scenematrix[i][y] in ['~']:
            return 6


    # check right boundary of item
    if y >= scene.fullwidth:
        return 1

    
    for i in range(x, x + item.length):
        if scenematrix[i][y + item.width - 1] in [(colors['Brown']+'#' + RESET)]:
            return 1
        if scenematrix[i][y + item.width - 1] in [(colors['Yellow']+'$' + RESET)]:
            return 4
        if scenematrix[i][y + item.width - 1] in [(colors['Red']+'@' + RESET)]:
            return 2
        if scenematrix[i][y + item.width - 1] in ['+']:
            return 3
        if scenematrix[i][y + item.width - 1] in ['@']:
            return 5
        if scenematrix[i][y + item.width - 1] in ['~']:
            return 6

    # check top
    for i in range(y, y + item.width):
        if(x <= 0):
            return 1
        # elif scenematrix[x][i] in barriers:
        elif scenematrix[x][i] in [(colors['Brown']+'#' + RESET)]:
            # print("!!!333")
            item.status = 1
            return 1

    # check bottom
    for i in range(y, y + item.width):
        if scenematrix[x + item.length - 1][i] in [(colors['Brown']+'#' + RESET)]:
            return 1
        if scenematrix[i][y + item.width - 1] in [(colors['Yellow']+'$' + RESET)]:
            return 4
        if scenematrix[i][y + item.width - 1] in [(colors['Red']+'@' + RESET)]:
            return 2
        if scenematrix[i][y + item.width - 1] in ['+']:
            return 3
        if scenematrix[i][y + item.width - 1] in ['@']:
            return 5
        if scenematrix[i][y + item.width - 1] in ['~']:
            return 6
   
    for i in range(y, y + item.width):
        
        if scenematrix[x + item.length][i] in [(colors['Brown']+'#' + RESET)    ]:
            
            item.status = 0


   
    return 0



def clashcheck2(scene, item, x, y):
    
    scenematrix = scene.returnmatrix()

    for i in range(x, x + item.width):
        if scenematrix[i][y] in [(colors['Red']+'@'+RESET)]:
            return 5

    for i in range(x, x + item.width):
        if scenematrix[i][y + item.width - 1] in [(colors['Red']+'@'+RESET)]:
            return 5


    for i in range(y, y + item.length):
        if scenematrix[i][y + item.width - 1] in [(colors['Red']+'@'+RESET)]:
            return 5

    
    for i in range(y, y + item.length):
           if scenematrix[i][y + item.width - 1] in [(colors['Red']+'@'+RESET)]:
            return 5

    return 0




