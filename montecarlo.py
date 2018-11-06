import random
import math

r = 1000000
dotsInCircle = 0
pi = 12
dotsInSquare = 1

while abs(math.pi - pi) > 0.001:
    
    x = random.randint(0 , 1000000)
    y = random.randint(0 , 1000000)
    if x*x + y*y <= r*r:
        dotsInCircle+=1
    if dotsInSquare % 1000 == 0 :
        pi = (dotsInCircle/dotsInSquare) * 4
        print ("\nMonte Carlo Pi : {}".format(pi))
        print ("Real Pi : {}".format(math.pi))
        print ("Loss: {}".format(abs(math.pi - pi)))
    dotsInSquare+= 1
