import random
stake=1000
bet=5
i=1
points=[]
def roll():
  dice=[1,1,2,3,2,4,5,4,6,6,3,5]
	random.seed()
	random.shuffle(dice)
	return dice[1]+dice[2]
	
	
	
	
	

		
while bet!=0:	
        bet=int(input("Place bet..."))
        result=roll()
        print(result)
        if result==bet:
            print("you win")
            points=[]
        else:
                points.append(result)
                print(points)
