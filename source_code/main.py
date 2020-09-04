
import os
from person import *
from scene import Scene
from func import *
from input import *
from obstacles import *
from scene_gen import *
from settings import *
import time
def print_home_page():
	os.system('clear')
	print(colors['White']+"WELCOME TO JETPACK JOYRIDER"+"\n"+RESET)
	name=input(colors['Purple']+"ENTER YOUR NAME:" +RESET)
	return name
def print_win_page():
    os.system('clear')
    print(colors['White']+name+" YOU WON"+"\n"+RESET)
    print(colors['Purple']+"FINAL SCORE:"+ str(scene.score)+"\n"+RESET)
    sys.exit()
def print_loss_page():
    os.system('clear')
    print(colors['White']+name+" YOU LOST"+"\n"+RESET)
    print(colors['Purple']+"FINAL SCORE:"+ str(scene.score+1000)+"\n"+RESET)
    sys.exit()
def print_time_over():
    os.system('clear')
    print(colors['White']+name+"TIME OVER"+"\n"+ RESET )
    print(colors['Purple']+"FINAL SCORE:"+ str(scene.score)+"\n"+RESET)
    sys.exit()

flag_boost = 0
start_game= time.time()

name=print_home_page()
scene = Scene(40, 140, 500)

generatescene(scene)
mario = Mario(4, 3)
dragon = Dragon(14, 38)
mario.setPos(scene, 32, 4)
dragon.posdrag(scene, 15, 530)
original_time=time.time()

putcoins(scene, Coins.coins)
putbeams(scene,Beams.beams)
putspeed(scene, Speedboosts.speedboosts)

getinp = Get()

print(scene.displayScene(original_time, 0, mario.is_boost, mario.lives , dragon.lives))

time_shield_off=0
time_shield_on=0



while True:


    recent =time.time()
    if(mario.shield ==1 ):
        if(recent- time_shield_on>=60):
            mario.shield=0
            mario.shield_off(scene)
            time_shield_off=recent

    input = input_to(getinp, 2)
    os.system('clear')
    
    update_coins(scene,  Coins.coins)
    eliminate_bullets(scene, Bullets.bullets)

    update_bullet(scene, Bullets.bullets, Beams.beams, dragon)
    update_dagger(scene, Daggers.daggers)
    # update_beams(scene, Beams.beams)
    if mario.x < dragon.x:
        dragon.move_drag(scene, 1)
    elif mario.x > dragon.x:
        dragon.move_drag(scene, 2)
    else:
        dragon.move_drag(scene, 0)
    if(dragon.to_shoot%2 == 0) and (dragon.y - mario.y) <= 60:
        make_dagger(scene , dragon)
    dragon.to_shoot+=1

    

    
    print(scene.displayScene(original_time, recent, mario.is_boost, mario.lives, dragon.lives))
    generatescene(scene)

    if input is not None:
        
        if input in ['a','d','w','A','D','W',' ','s','S','f','F']:
            if input in [' '] and time.time()- time_shield_off>=60:
                mario.shield =1
                time_shield_on= time.time()
                mario.shield_on(scene)
            elif input in ['f','F']:
                make_bullet(scene, mario)

            else:
                mario.move(input, scene)
        else:
            mario.move(input, scene)


        if input == 'q':
            os.system('clear')
            print(colors['White']+"YOU QUIT"+RESET)
            sys.exit()
        else:
            mario.gravityfall(scene)
            chk = clashcheck(scene, mario, mario.x, mario.y)
            if chk == 0:
                pass
            elif chk == 2:
                no_of_lives = no_of_lives-1
            elif chk == 4:
                collect_coin(scene, mario.y, Coins.coins)

    else:
        mario.gravityfall(scene)
        update_mag(scene, mario)
        chk = clashcheck(scene, mario, mario.x, mario.y)
        if chk == 0:
            pass
        elif chk == 4:
            collect_coin(scene, mario.y, Coins.coins)

    if mario.y > scene.max_y:
        scene.max_y = mario.y
    scene.score = scene.max_y*2  + Coins.collected*20 + Bullets.collected*30

    if( mario.lives<=0):
        print_loss_page()
    if(dragon.lives<=0):
        print_win_page()
    if(time.time()-start_game>=75):
        print_time_over()