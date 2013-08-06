import random
import player
import re
stake=1000
bet=1
unit=5
i=1
points=[]
def roll():
	dice1=[1,2,3,4,5,6]
	dice2=[1,2,3,4,5,6]
	random.seed()
	random.shuffle(dice2)
	random.shuffle(dice1)
	print(dice1[1])
	print(dice2[2])
	return dice1[1]+dice2[2]
	


while bet !='END':
        bet=input("Place bet...")
        result=roll()
        #print(result)
        odds(bet,unit)
        if result==bet:
            print("you win")
            #points=[]
        else:
                points.append(result)
                print(points)

        if points.index(result)!=0:
                points.remove(result)
