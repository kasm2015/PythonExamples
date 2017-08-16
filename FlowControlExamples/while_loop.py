#WHILE LOOP EXAMPLES
#For random numbers import module named random
print("Random numbers program initiated")
import random
x=1
nofoundafteriteration=0
while x!=23:
    print(x)
    nofoundafteriteration=nofoundafteriteration+1
    x=random.randrange(1,40)

print("Condition satisfied after ",nofoundafteriteration," no of iterations")