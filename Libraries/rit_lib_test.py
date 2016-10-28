from rit_lib import *

class Coin(struct):
    _slots=((str,'coin_name'),(int,'denominator'))
    
    
quarter = Coin("quarter",25)
    
print(quarter)

quarter.denomination=35

print(quarter)

