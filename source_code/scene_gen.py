from obstacles import *

def generatescene(scene):
   
    x = 8
    for y in range(10, 500, 30):
        cloud = background(8, 8)
        x =x %15
        cloud.setPos(scene, x, y)
        x+=7
    

    wall = Wall(4, 100)
    wall.setPos(scene, 36,0)
    


    Magnet.draw_magnet(scene, 35, 78)
    