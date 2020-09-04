""" Defining the base background scene """
# from config import *
from settings import *
import time

class Scene:
    """ Making a matrix to represent the game scene """

    def __init__(self, length, width, fullwidth):
        """ Initial matrix """
        self.start = 0
        self.length = length
        self.width = width
        self.fullwidth = fullwidth
        self.max_y = 0
        self.score = 0
        self.scenematrix = []
        # scenematrix is a matrix to display all elements
        for x in range(0, fullwidth):
            self.scenematrix.append([])
            for y in range(0, fullwidth):
                self.scenematrix[x].append(' ')
        for x in range(36, length):
            for y in range(0, fullwidth):
                # self.scenematrix[x][y] = 
                 self.scenematrix[x][y] = colors['Brown'] + '#' + RESET


    def displayScene(self, original_time, recent, pow_up , life, boss_lives):
        """ Print the screen to the terminal """
        #initial values
        inc=0

        is_boost_on=0
        time_boost_start=0
        if is_boost_on != pow_up:
            time_boost_start= time.time()
            is_boost_on= 1
        if time.time() - time_boost_start <4:
            inc=2
        else:
            is_boost_on=3
            inc = 1
        if(self.start>=350):
            inc=0

        # if(recent - original_time >= 1):
        self.start += inc
        sceneprint = ""
        sceneprint += colors['Purple'] +"JETPACK JOYRIDER "+"\n"+ RESET 
        sceneprint += colors['Blue']+"SCORE : " + RESET+str(self.score) + colors['Green']+ "      LIVES:" + str(life)+ colors['White']+"      BOSS ENEMY LIVES:" +str(boss_lives)+"\n"
        for i in range(3, self.length):
            for j in range(self.start, self.start + self.width):
                sceneprint += str(self.scenematrix[i][j])
            sceneprint += '\n'
        sceneprint +=  colors['Blue']+"Press Q to exit\n" +RESET
        return sceneprint

    # auxilary functions to return and update matrix
    def returnmatrix(self):
        return self.scenematrix

    def updatescene(self, updmatrix):
        self.scenematrix = updmatrix
