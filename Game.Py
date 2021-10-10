test = "hello world"
print(test)

def exponent(Base_Number, Power_Number):
   Result = 1
   for index in range(Power_Number):
        Result = Result * Base_Number
   #return Result

#print(exponent(2, 5)) 

def calcbonus(Relays, Level):
    Bonus = 10
    if Relays > 0: 
        Bonus = exponent(Relays, Level)
    else:
        return Bonus
print(calcbonus(2, 3))

def levelfinished(Relays, Level, Score):
    Score = Score + calcbonus(Relays, Level)
    Highscore = 100
    if Score > Highscore: 
        Highscore = Score
    else:
        return Score

Totalscore = levelfinished(2, 5, 21)
print(Totalscore)