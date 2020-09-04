
from func import *
from settings import *
from colorama import *



def make_bullet(scene , person):

    bullet = Bullets(1,5)
    Bullets.bullets.append(bullet)
    # print("!!!1")
    bullet.setPos(scene, person.x+1, person.y+2 )
    bullet.starty= bullet.y

def update_bullet(scene ,  bullets , beams, dragon):
    ''' Update all coins remaining in each game loop iteration '''
    # print("&&&&")


    scenematrix= scene.returnmatrix()
    
    for bullet in Bullets.bullets:

        if bullet.x in range(dragon.x, dragon.x + dragon.length) and bullet.y in range(dragon.y,
         dragon.y +dragon.width):
            dragon.lives-=1
            # print("YO PEEPS")
            del Bullets.bullets[q]

        if clashcheck2(scene, bullet, bullet.x, bullet.y ) == 5:
            # print("hsavxj")
            Bullets.collected+=1
            for i in range(bullet.x-15 , bullet.x +15):
                for j in range(bullet.y -15, bullet.y+15):
                    if scenematrix[i][j] in [colors['Red']+'@'+RESET]:
                        # print("gggg")
                        scenematrix[i][j]=' '+RESET
            # Bullets.bullets.remove(bullet)   
        bullet.setPos(scene, bullet.x, bullet.y + bullet.speed)
        
        scene.updatescene(scenematrix)



# def check_shot(scene, item):
#     for bullet in Bullets.bullets:
#             erase_beams(scene, bullet)
            
            #remove the beam now 
    #to do

def eliminate_bullets(scene, bullets):
    q=0
    scenematrix= scene.returnmatrix()
    for bullet in Bullets.bullets:
        if bullet.y- bullet.starty >= 25:
            #replace bullet position with whitespace
            for i in range(bullet.x, bullet.x + bullet.length):
                for j in range(bullet.y, bullet.y + bullet.width):
                    if scenematrix[i][j] in ['>']:
                        scenematrix[i][j]=' '

            Bullets.bullets.remove(bullet)
        
    for bullet in Bullets.bullets:
        bullet.setPos(scene, bullet.x, bullet.y )



def putbeams(scene, beams):
    ''' Put coins on the map according to the level '''
    i=0
    randx=17
    randy=40
    mod=1
    for i in range(0,15):
        if mod%3==1:
            beam = Hbeam(2,8)
        if mod%3==2:
            beam = Vbeam(8,4)
        if mod%3 ==0:
            beam = Dbeam(6,8)
        Beams.beams.append(beam)
        if (randx%27> 6):
            beam.setPos(scene, randx%27,randy)
        else:
            beam.setPos(scene, randx%27,randy+6)
        randy+=24
        randx+=13
        mod+=1


# def erase_beams(scene, bullet, beams):
#     ''' Delete the coin after collecting it '''
#     scenematrix = scene.returnmatrix()

#     if scenematrix[bullet.x][bullet.y ]=='@':
#         remove_beams(beams, bullet.x, bullet.y  )

def update_beams(scene,  beams):
    ''' Update all coins remaining in each game loop iteration '''
    for beam in Beams.beams:
        beam.setPos(scene, beam.x, beam.y)
   

def remove_beams(scene, beams, x1, y1 ):
    # print("im called!")
    scenematrix = scene.returnmatrix()
    for beam in Beams.beams:
        # print("hcdhvj")
        for i in range(beam.x , beam.x + beam.length):
            for j in range(beam.y , beam.y + beam.width):
                if i==x1 and j==y1:
                    Beams.beams.remove(beam)
                    Beams.collected += 1
                    # print("hjbdcj")
                    del beam
                    break
    scene.updatescene(scenematrix)





def putcoins(scene, coins):
    ''' Put coins on the map according to the level '''

    i=0
    randx=11
    randy=37
    mod=1
    for i in range(0,18):
        for j in range(0, mod):
            coin = Coins()
            Coins.coins.append(coin)
            coin.setPos(scene, randx%23 + 10 , randy%380)
            randy+=3

        randy+=29
        randx+=17
        mod+=1
        
   
    


def update_coins(scene,  coins):
    ''' Update all coins remaining in each game loop iteration '''
    for coin in Coins.coins:
        if coin.to_print==1:
            coin.setPos(scene, coin.x, coin.y)


def collect_coin(scene, y, coins):
    ''' Delete the coin after collecting it '''
    # print("hgjk")
    g=0
    scenematrix = scene.returnmatrix()
    for coin in Coins.coins:
        if coin.y in range(y-4, y):
            for i in range(coin.x, coin.x+coin.length):
                for j in range(coin.y, coin.y+coin.width):
                    scenematrix[i][j] = ' '
            Coins.collected += 1
            coin.to_print=0
        #Coins.coins.remove(coin)
        # del(Coins.coins[g])
        # Coins.collected += 1
        # coin.to_print=0
        # del coin
        g+=1
        
    scene.updatescene(scenematrix)




def putspeed(scene, speedboosts):
    ''' Put coins on the map according to the level '''
    speedboost = Speedboosts()
    Speedboosts.speedboosts.append(speedboost)
    speedboost.setPos(scene, 24,45 )


def update_speed(scene,  speedboosts):
    ''' Update all coins remaining in each game loop iteration '''
    for speedboost in Speedboosts.speedboosts:
        speedboost.setPos(scene, speedboost.x, speedboost.y)


def collect_speed(scene, y, speedboosts):
    ''' Delete the coin after collecting it '''
    scenematrix = scene.returnmatrix()
    for speedboost in Speedboosts.speedboosts:
        if speedboost.y in range(y-4, y):
            for i in range(speedboost.x, speedboost.x+speedboost.length):
                for j in range(speedboost.y, speedboost.y+speedboost.width):
                    scenematrix[i][j] = ' '
        Speedboosts.speedboosts.remove(speedboost)
        # is_use_boost=1
        del speedboost
        break
    scene.updatescene(scenematrix)


class Obstacle:
    ''' Base definition for any obstacle '''

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.x = None
        self.y = None
        self.matrix = []
        self.__is_ded=0

    def setPos(self, scene, x, y):
        ''' Take the item and blit it over the scene at position specified'''
        # self.x = x
        # self.y = y
        blitobject(scene, self, x, y)
        self.x = x
        self.y = y

    def returnmatrix(self):
        ''' Return the obstacle as a matrix '''
        return self.matrix


class Wall(Obstacle):
    ''' Walls that player has to jump '''

    def __init__(self, length, width):
        ''' Initialize as a type of obstacke '''
        Obstacle.__init__(self, length, width)
        self.x = 0
        self.y = 0
        # self.matrix = [[colors['Brown']+'#'+RESET for i in range(0, width)]
        #                for j in range(0, length)]
        self.matrix = [[(colors['Brown']+'#'+RESET) for i in range(0, width)]
                       for j in range(0, length)]


    def draw_wall(scene, length, width, y):
        wall = Wall(length, width)
        x = 36-wall.length
        wall.setPos(scene, x, y)

class Magnet(Obstacle):
    ''' Pits that player has to avoid '''

    def __init__(self, length, width):
        ''' Initialize as a type of obstacke '''
        Obstacle.__init__(self, length, width)
        self.x = 0
        self.y = 0
        self.matrix = [[ (colors['Cyan']+'0'+RESET)  for i in range(0, width)]
                       for j in range(0, length)]
        self.matrix[0] = [' ' for i in range(0, width)]

    def draw_magnet(scene, width, y):
        magnet = Magnet(3,3)
        magnet.setPos(scene, 20, y)


def update_mag(scene ,  mario):
    ''' Update all coins remaining in each game loop iteration '''
    # print("&&&&")
    if mario.in_range==1:
        mario.setPos(scene, mario.x, mario.y+1)
    if mario.in_range==2:
        mario.setPos(scene, mario.x, mario.y-1)
class Coins(Obstacle):
    ''' Coins that can be collected as the player moves over them'''
    coins = []
    collected = 0

    def __init__(self, length=3, width=3):
        Obstacle.__init__(self, length, width)
        self.x = 0
        self.y = 0
        p = colors['Yellow'] + '$' + RESET 
        self.matrix = [[' ', p, ' '],
                       [p, p, p],
                       [' ', p, ' ']]
        self.to_print=1

    # def put_coin(scene, x, y):
    #     coin = Coins()
    #     x=37
    #     y=6
    #     coin.setPos(scene, x, y)

class Beams(Obstacle):
    beams = []
    collected=0



class Vbeam(Beams):
    # coins = []

    def __init__(self, length, width):
        Obstacle.__init__(self, length, width)
        self.x = 0
        self.y = 0
        self.length= 8
        self.width= 4
        p= colors['Red'] + '@' + RESET
        self.matrix = [[p,p,p,p], [p,p,p,p],[p,p,p,p],[p,p,p,p],[p,p,p,p],[p,p,p,p],[p,p,p,p],[p,p,p,p]]

    def __draw_vbeam(scene, length, width):
        vbeam = Vbeam(length, width)
        x = 30
        # vbeam.setPos(scene, 30, 40)

class Dbeam(Beams):
    # coins = []

    def __init__(self, length, width):
        Obstacle.__init__(self, length, width)
        self.x = 0
        self.y = 0
        self.length= 6
        self.width= 8
        p= colors['Red'] + '@' + RESET
        q = ' '
        self.matrix = [[p,p,p,q,q,q,q,q],[q,p,p,p,q,q,q,q],[q,q,p,p,p,q,q,q],[q,q,q,p,p,p,q,q],[q,q,q,q,p,p,p,q],
        [q,q,q,q,q,p,p,p]]

    def draw_vbeam(scene, length, width):
        __dbeam = Dbeam(length, width)
        x = 30
        # vbeam.setPos(scene, 30, 40)




class Hbeam(Beams):
    # coins = []

    def __init__(self, length, width):
        Obstacle.__init__(self, length, width)
        self.x = 0
        self.y = 0
        self.length= 2
        self.width= 8
        p= colors['Red'] + '@' + RESET
        self.matrix = [[p,p,p,p,p,p,p,p],
                       [p,p,p,p,p,p,p,p]]

    def __draw_hbeam(scene, length, width):
        hbeam = Hbeam(length, width)
        x = 30
        hbeam.setPos(scene, 30, 60)


class Speedboosts(Obstacle):
    speedboosts = []
    def __init__(self, length=3, width=3):
        Obstacle.__init__(self, length, width)
        self.x = 0
        self.y = 0
        self.matrix=[['+','+','+'],['+','+','+'],['+','+','+']]

    def draw_speedboost(scene, length, width):
        boost = Speedboost(length, width)
        boost.setPos(scene, 24, 30)


class Bullets(Obstacle):
    bullets = []
    collected =0

    def __init__(self, length, width):
        Obstacle.__init__(self, length=1 , width=5)
        self.x = 0
        self.y = 0
        self.length=length
        self.width=width
        # self.matrix = [['>'],['>'],['>'],['>'],['>']]
        self.matrix = [['>','>','>','>','>']]
        self.speed=6
        self.starty=0


    def draw_bullet(scene, person):
        bullet = Bullet(1, 5)
        x = 30
        bullet.setPos(scene, person.x+1, person.y+2)
        bullet.starty = bullet.y


class Daggers(Obstacle):
    daggers = []

    def __init__(self, length, width):
        Obstacle.__init__(self, length=2 , width=4)
        self.x = 0
        self.y = 0
        self.length=length
        self.width=width
        # self.matrix = [['>'],['>'],['>'],['>'],['>']]
        self.matrix = [['~','~','~','~'],['~','~','~','~']]
        self.speed=6

    
def make_dagger(scene , dragon):
    dagger = Daggers(2,4)
    Daggers.daggers.append(dagger)
    # print("!!!1")
    dagger.setPos(scene, dragon.x+4, dragon.y-2)


def update_dagger(scene,  daggers):
    ''' Update all coins remaining in each game loop iteration '''
    for dagger in Daggers.daggers:
        dagger.setPos(scene, dagger.x, dagger.y - dagger.speed)
   

class background(Obstacle):
    '''Making clouds on top '''

    def __init__(self, length, width):
        ''' Initialize as a type of obstacke '''
        Obstacle.__init__(self, length, width)
        self.x = 0
        self.y = 0
        p = colors['Gray']+'.'+RESET
        q = ' '+RESET
        self.matrix = [[p,p,p,p,p,p,p,p],
                      [p,q,q,q,q,q,q,p],
                      [p,q,q,q,q,q,q,p],
                      [p,q,q,q,q,q,q,p],
                      [p,q,q,q,q,q,q,p],
                      [p,q,q,q,q,q,q,p],
                      [p,q,q,q,q,q,q,p],
                      [p,p,p,p,p,p,p,p]]
                              
        self.length= length
        self.width = width