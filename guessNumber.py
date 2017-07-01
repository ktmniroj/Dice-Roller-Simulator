import random
     
def guess(randomNumber, number):
    if number > randomNumber:
        print "the number is too high "
    if number < randomNumber:
        print 'the number is too low'
    if number == randomNumber:
        print 'your guess is correct'


while True:      
    randomNumber = random.randint(1,10)
    number = input("pick up any number between 1 to 10")
    guess(randomNumber,number)
    answer = raw_input('want to check again ?')
    if answer == 'no':
        break
        
    

    
    
