bets = {}

#calculates payout on win 
def toWin(odds, bet):
    if odds > -1: 
        return "You make $" + str((bet *(odds / 100)))+ " on a win"
    else: 
        return "You make $" + str((bet/(-1*odds/100)))+ " on a win"

#calculates net profit from my log
def getTotal():
    total = 0
    for value in bets:
        total+=bets[value]
    if total < 0: 
        return "You are down $" + str(abs(total)) + " (" + str(total) + ")"
    else: 
        return "You are up $" + str(total)

#finds most money won on a bet from log
def biggestWin():
    high = -10000
    num = 0
    for value in bets:
        if bets[value] > high:
            high = bets[value]
            num = value
    return "Biggest win: $" + str(high)+ " from " + str(value)

#finds most money lost on a bet from log 
def biggestLoss():
    low = 10000
    num = 0
    for value in bets:
        if bets[value] < low:
            low = bets[value]
            num = value
    return "Biggest loss: $" + str(abs(low)) + " (" + str(low) +") from " + value
    
 


#bet log
bets['CLIPPERS vs Suns, 6/22'] = -10 
bets['Clippers vs SUNS, 6/24'] = -20 
bets['HAWKS vs Bucks, 6/25'] = -20
bets['CLIPPERS vs Suns, 6/28'] = 115
bets['Bucks vs HAWKS, 7/1'] = -30
bets['BUCKS vs Suns, 7/8'] = -50
bets['CONOR vs Porier 3, 7/11'] = -30 
bets['BUCKS vs Suns, 7/17'] = 75
bets['DILLASHAW vs Sandhagen'] = 85
bets['LEWIS vs Gane'] = -60
