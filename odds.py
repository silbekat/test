//
This file holds the payout odds
payme = type_of_bet,payout)
//

def odds(bet,unit):
     payme = {
	 'PASSLINE':1
	 ,'DONTPASS':1
	 ,'BIG6':1
	 ,'BUY4':2
	 ,'COME':1
	 ,'DONTCOME':1
	 ,'FIELD':1
	 ,'BIG6':1
	 ,'BIG8':1
	 }
	 print(payme[bet]*unit)
	 return payme[bet]*unit
