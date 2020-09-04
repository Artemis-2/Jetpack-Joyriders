from scene import *
from func import *
from obstacles import *
from settings import *
from colorama import Fore, Back, Style
import time

class Person:
    """ Base definition of people involved in the game"""

    def __init__(self, length, width):
        """ Giving initial standard values """
        self.length = length
        self.width = width
        # x and y are the values of the top left coordinate
        self.x = None
        self.y = None
        self.__matrix = []
        # defining how much the person moves at a time
        self.__step = None
        self.__jump = None


    def setPos(self, scene, x, y):
        """ Calls blitobject function and updates position """
        blitobject(scene, self, x, y)
        self.x = x
        self.y = y

    def returnmatrix(self):
        """ Return the person as a matrix """
        return self.matrix

    def moveright(self, scene):
        # print("cJKCB")
        newy=0
        chk=0
        if(self.in_range==1):
                newy =self.y + self.step+3
                chk = clashcheck(scene, self, self.x, newy)
                if chk == 0:
                    self.setPos(scene, self.x, newy)
                elif chk == 2:
                    if self.shield == 0:
                        self.lives-=1
                        self.setPos(scene, self.x, newy)
                elif chk == 3:
                    self.is_boost =1
                    self.setPos(scene, self.x, newy)
                elif chk == 4:
                    collect_coin(scene, self.y, Coins.coins)
                    self.setPos(scene, self.x, newy)
                elif chk == 6:
                    if self.shield == 0:
                        self.lives-=1
                    self.setPos(scene, self.x, newy)
        elif(self.in_range==2):
            newy=self.y + self.step -1
            if chk == 0:
                    self.setPos(scene, self.x, newy)
            elif chk == 2:
                    if self.shield == 0:
                        self.lives-=1
                        self.setPos(scene, self.x, newy)
            elif chk == 3:
                    self.is_boost =1
                    self.setPos(scene, self.x, newy)
            elif chk == 4:
                    collect_coin(scene, self.y, Coins.coins)
                    self.setPos(scene, self.x, newy)
            elif chk == 6:
                    if self.shield == 0:
                        self.lives-=1
                    self.setPos(scene, self.x, newy)
            
        else:

            newy = self.y + self.step
            chk = clashcheck(scene, self, self.x, newy)
            if chk == 0:
                    self.setPos(scene, self.x, newy)
            elif chk == 2:
                    if self.shield == 0:
                        self.lives-=1
                        self.setPos(scene, self.x, newy)
            elif chk == 3:
                    self.is_boost =1
                    self.setPos(scene, self.x, newy)
            elif chk == 4:
                    collect_coin(scene, self.y, Coins.coins)
                    self.setPos(scene, self.x, newy)
            elif chk == 6:
                    if self.shield == 0:
                        self.lives-=1
                    self.setPos(scene, self.x, newy)

    def moveleft(self, scene):
        chk=0
        if(self.in_range==2):
            newy =self.y -self.step +3
            chk = clashcheck(scene, self, self.x, newy)
            if chk == 0:
                    self.setPos(scene, self.x, newy)
            elif chk == 2:
                    if self.shield == 0:
                        self.lives-=1
                        self.setPos(scene, self.x, newy)
            elif chk == 3:
                    self.is_boost =1
                    self.setPos(scene, self.x, newy)
            elif chk == 4:
                    collect_coin(scene, self.y, Coins.coins)
                    self.setPos(scene, self.x, newy)
            elif chk == 6:
                    if self.shield == 0:
                        self.lives-=1
                    self.setPos(scene, self.x, newy)
        if(self.in_range==1):
            newy = self.y -self.step + 1
            chk = clashcheck(scene, self, self.x, newy)
            if chk == 0:
                    self.setPos(scene, self.x, newy)
            elif chk == 2:
                    if self.shield == 0:
                        self.lives-=1
                        self.setPos(scene, self.x, newy)
            elif chk == 3:
                    self.is_boost =1
                    self.setPos(scene, self.x, newy)
            elif chk == 4:
                    collect_coin(scene, self.y, Coins.coins)
                    self.setPos(scene, self.x, newy)
            elif chk == 6:
                    if self.shield == 0:
                        self.lives-=1
                    self.setPos(scene, self.x, newy)
        else:
            newy = self.y - self.step
            chk = clashcheck(scene, self, self.x, newy)
            if chk == 0:
                    self.setPos(scene, self.x, newy)
            elif chk == 2:
                    if self.shield == 0:
                        self.lives-=1
                        self.setPos(scene, self.x, newy)
            elif chk == 3:
                    self.is_boost =1
                    self.setPos(scene, self.x, newy)
            elif chk == 4:
                    collect_coin(scene, self.y, Coins.coins)
                    self.setPos(scene, self.x, newy)
            elif chk == 6:
                    if self.shield == 0:
                        self.lives-=1
                    self.setPos(scene, self.x, newy)
    def jumpup(self, scene):
        """ Make mario jump up """
        # has to be on the ground to be allowed to jump
        # if self.status == 0:
        #     xup = 0
        xup=0
        newx=0
        while(xup < (self.jump*2) ):
            if(clashcheck(scene, self, self.x - xup, self.y) in [0,4]):
                xup += 1
            else:
                break
        # if(self.x>7):
        #     if(clashcheck(scene, self, self.x - 1, self.y) in [0,4]):
        #         self.setPos(scene, (self.x-1), self.y)
            if(self.x -2>10):
                #self.setPos(scene, (self.x-2), self.y)
                newx=self.x-2
            else:
                # self.setPos(scene, (10), self.y)
                newx=10
                chk=0
            for h in range(newx, self.x):
                chk = clashcheck(scene, self, newx, self.y)
                if chk == 0:
                    # print("fdgdf")
                    self.setPos(scene, newx, self.y)
                elif chk == 2:
                    if self.shield == 0:
                        self.lives-=1
                    self.setPos(scene, newx,
                                self.y)
                elif chk == 3:
                    self.is_boost =1
                    # print("jfkjhf")
                    self.setPos(scene, newx,
                                self.y)
                elif chk == 4:
                    collect_coin(scene, self.y, Coins.coins)
                    self.setPos(scene, newx,
                                self.y)
                elif chk == 6:
                    if self.shield == 0:
                        self.lives-=1
                    self.setPos(scene, newx,
                                self.y)


        self.status = 1

    

            

class Mario(Person):
    """ Defining the classic hero """

    def __init__(self, length, width):
        """ Initialize Mario as a person and give initial structure"""
        Person.__init__(self, length, width)
        head = colors['Light Cyan'] + chr(213) + RESET
        mid = colors['Light Cyan'] + '|' + RESET
        left = colors['Purple'] + '/' + RESET
        right = colors['Purple'] + '\\' + RESET

         

        self.matrix = [[' ', head, ' '], [
            left, mid, right], [' ', mid, ' '], [left, ' ', right]]
        self.step = 2
        self.jump = 6
        self.x = 32
        self.y = 4
        self.in_range=0
        self.last_die=0
        # setting status to be equal to 0
        # 0-on ground, 1- in air going down
        self.status = 0
        self.gravity = 1
        self.shield=0
        self.lives = 6
        self.is_boost=0
        # self.setPos(Scenery, self.x + self.gravity, self.y)

    def move(self, keypress, scene):
        """ Functionality to move mario according to user input """
        # if keypress == 'w' or keypress == 'W' :
        #     self.jumpup(scene)
        # elif keypress == 'a' or keypress == 'A':
        #     self.moveleft(scene)
        if(self.shield==1):
            self.step = 4
        else:
            self.step=2


        if keypress == 'd' or keypress == 'D' :
            if self.y<400:
                self.moveright(scene)
        elif keypress == 'a' or keypress == 'A':
            self.moveleft(scene)
        elif keypress == 'w' or keypress == 'W':
            self.jumpup(scene)
        else:
            pj=999

        if ( self.y -scene.start<= 4 ):
            # print("SURPRISE!!!!")
            self.y = scene.start +4

    def shield_on(self,scene):
    # right = colors['Purple'] + '\\' + RESET
        head = colors['Light Cyan'] + chr(213) + RESET
        mid = colors['Light Cyan'] + '|' + RESET
        left = colors['Purple'] + '/' + RESET
        right = colors['Purple'] + '\\' + RESET
        q= colors['Light Green'] + '(' +RESET
        r= colors['Light Green'] + ')' +RESET
        self.matrix = [[' ', head, ' '], [
                left, mid, right], [q, mid, r], [left, ' ', right]]


    def shield_off(self, scene):
    # right = colors['Purple'] + '\\' + RESET
        head = colors['Light Cyan'] + chr(213) + RESET
        mid = colors['Light Cyan'] + '|' + RESET
        left = colors['Purple'] + '/' + RESET
        right = colors['Purple'] + '\\' + RESET
        q= colors['Light Green'] + '(' +RESET
        r= colors['Light Green'] + ')' +RESET
        self.matrix = [[' ', head, ' '], [
                left, mid, right], [' ', mid, ' '], [left, ' ', right]]


    def gravityfall(self, scene):
        """ Simple gravity fall if no input is provided and in air"""
        if(self.status==1):
            if self.x < 20:
                # print("hjdfkh")
                self.gravity=1
            elif self.x<30:
                # print("2222")
                self.gravity=2
            else:
                # print("ds")
                if(32-self.x>3):
                    self.gravity=3
                else:
                    self.gravity= 32-self.x
        else:
            self.gravity=1
        if self.status == 1:
            chk = clashcheck(scene, self, self.x+self.gravity, self.y)
            if chk == 0:
                # print("fdgdf")
                self.setPos(scene, self.x+self.gravity, self.y)
            elif chk == 2:
                if self.shield == 0:
                    self.lives-=1
                self.setPos(scene, self.x + self.gravity,
                            self.y)
            elif chk == 3:
                self.is_boost =1
                self.setPos(scene, self.x + self.gravity,
                            self.y)
            elif chk == 4:
                collect_coin(scene, self.y, Coins.coins)
                self.setPos(scene, self.x + self.gravity,
                            self.y)
            elif chk == 6:
                if self.shield == 0:
                    self.lives-=1
                self.setPos(scene, self.x + self.gravity,
                            self.y)



class Dragon(Person):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        # x and y are the values of the top left coordinate
        self.__step = None
        self.__jump = None
        self.matrix=[ 
               list("  ,===:'.,            `-._           "),
               list("    `:.`---.__         `-._          "),
               list("       `:.     `--.         `.       "),
               list("          \.        `.         `.    "),
               list("   (,,(,    \.         `.   ____,-`.,"),
               list("  (,'     `/   \.   ,--.___`.'       "),
               list(",  ,'  ,--.  `,   \.;'         `     "),
               list(" `{D, {    \  :    \;                "),
               list("   V,,'    /  /    //                "),
               list("   j;;    /  ,' ,-//.    ,---.      ,"),
               list("   \;'   /  ,' /  _  \  /  _  \   ,'/"),
               list("         \   `'  / \  `'  / \  `.' / "),
               list("          `.___,'   `.__,'   `.__,'  ")]
        self.x = 15
        self.y = 450
        self.to_shoot=1
        self.lives= 3
        icedaggers = []


    def move_drag(self, scene, dir):
        x2 = self.x
        # print("DIR:", dir)
        if(dir==1):
            if(self.x-5 < 5):
                x2=  5
            else:
                x2= self.x -5
        elif (dir==2):
            if(self.x+ 5 > 27):
                x2=  26
            else:
                x2 = self.x +5 
        self.posdrag( scene, x2, self.y )
        self.x = x2          
        # self.to_shoot+=1

    def posdrag(self, scene, x2 , y2 ):
        scenematrix = scene.returnmatrix()
        # print("DRAGONS MOVING!")
        for a in range(0, len(self.matrix)):
            for b in range(0, len(self.matrix[0])):
                # print("Hoiii")
                scenematrix[self.x+a][self.y+b]= "\033[37m" + "\033[40m"+ "\033[1m" + ' '
                

        for a in range(0, len(self.matrix)):
            for b in range(0, len(self.matrix[0])):
                scenematrix[x2 +a][self.y+b]= "\033[37m" + "\033[40m"+ "\033[1m" + self.matrix[a][b]

        scene.updatescene(scenematrix)
     


