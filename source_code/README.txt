REQUIREMENTS-
1. python3
2. colorama , time, os, sys


COMMAND TO RUN-
python3 main.py

MOVEMENT-
• A for left and D for right. W for activating the jetpack and jumping up. F for firing bullets at the enemies.
• When the Mandalorian moves upwards, the jet pack is activated as long as
the ‘W’ key is pressed. When ‘W’ is released, the jetpack deactivates and gravity comes into play.

BACKGROUND-
• Wall which is a horizontal surface on ehich Mando stands.
• Randomly generated background similar to the app.
• Lots of coins suspended which the Mandalorian can collect and increase his score.

OBSTACLES-
• Fire Beams: Beam like structures should appear (like in the figure above) as obstacles. There must be three kinds of beams: horizontal, vertical and some at 45 ◦ with the ground/platform. The Mandalorian must ensure to not collide with these beams, else he will lose a life. He can shoot at them and clear his way.
• Magnet: A magnet should randomly appear on the way, which will influence the motion of Mando. Constant force towards magnet when mando is in the range.



CHARACTERS-

• Boss enemy-(appears at the end)
The boss enemy is Viserion, the flying dragon that adjusts its position according to the player (with respect to the movement along the Y axis). It should throws aimed at the Mandalorian, which he must dodge. It has multiple lives,  decrease when the Mandalorian shoots bullets at it. Once the boss enemy is defeated, Baby Yoda can be rescued and the game is complete.
• Mando-
Stick fogure controlled by user


MOVEMENT

    Press 'w' to activate the jetpack(move up).
    Press 'a' to move left.
    Press 'd' to move right.
    Press 'q' at any time to quit.
    




OOPS CONCEPTS USED-
• Inheritance: Used in Person class which has Mando and Dragon as subclasses
• Polymorphism: Exhibited by setPos method being implemented differently for Person and Obstacles classes.
• Encapsulation: Exhibited by private variables in person class along with  private variables and methods in Obstacle class. 
• Abstraction: Functionality like move() for player, shoot() for player, check() for bullet, move() for dragon are methods within the class. So inner details are storerd away from end user.
