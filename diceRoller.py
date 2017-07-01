#!python
import random
answer = 'yes'
while answer == 'yes':
    number = random.randint(1,6)
    print"your lucky number is: %d "%number
    answer = raw_input("Do u want to roll again?")
    if answer =='no':
        break
    
    
