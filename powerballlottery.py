import random
from ssl import RAND_add
import pyfiglet
font = pyfiglet.figlet_format('Powerball Lottery')



print('''powerall lottery! Each powerball lottery ticket costs $2''')

# Let the player enter the first five numbers, 1 to 69:

while True:
    print('print 5 diffirent numbers from 1 to 69, with spaces between them.')
    print ('******************************************************************')
    print('each number: for example: 5 56 23 14 2 47')
    response = input('> ')
# Check that the player entered 5 things:

    numbers = response.split()
    if len(numbers) !=5:
        print(' Please enter 5 numbers, separated by spaces.')   
        continue
# Convert the strings into integers:
    try:
        for i in range(5):
            numbers[i] = int(numbers[i])
    except ValueError:
        print('Please enter numbers are between 1 and 69')
        continue
# Check that the numbers are between 1 and 69:
    for i in range (5):
        if not (1 <=numbers[i] <=69):
            print(' The numbers must be between 1 and 69')
            continue
# Check that the numbers are unique:
    if len(set(numbers)) !=5:
        print('you must enter 5 different numbers')
        continue
    break
# Let the player select the powerball, 1 to 26:
while True:
    print('Enter the powerball number 1 to 26.')
    response= input ('> ')
# Convert the strings into integers:
    try:
        powerball = int(response)
    except ValueError:
            print('Please enter a number 1 to 26; like 3,5 17 or 26')
            continue
# Check that the number is between 1 and 26:
    if not (1 <= 26):
        print('the powerball must be between 1 to 26')
        continue
    break

while True:
    print ('how many times you want to play')
    response = input('> ')
    try:
        numPlays = int(response)
    except ValueError:
        print('please enter a number like 3. 15 250000')
        continue
# Check that the number is between 1 and 1000000:
    if not ( 1 <= numPlays <=1000000):
        print(' You can play 1 and 10000000 times')    
        continue
    break
 # Run the simulation (dananın kuyruğunun koptuğu yer):

price = '$'+ str(2 * numPlays)
print('it costs', price, 'to play', numPlays, 'times, but don\'t')
print('worry. I\m sure you\'ll wint it all back')
input('Press enter to start...')

possibleNumbers = list(range(1,70))
for i in range(numPlays):
# Come up with lottery numbers:
    random.shuffle(possibleNumbers)
    winningNumbers =(possibleNumbers)
    winningNumbers = possibleNumbers[0:5]
    winningPowerball = random.randint(1, 26)
# Display winning numbers:
print (' The winngi numbers are :' , end='')
allWinnigNums =''
for i in range (5):
    allWinnigNums += str(winningNumbers[i])+ ''
    allWinnigNums +='and' + str(winningPowerball)
    print(allWinnigNums.ljust(21), end='')
# NOTE: Sets are not ordered, so it doesn't matter what order the
# integers in set(numbers) and set(winningNumbers) are.
    if(set(numbers)== set(winningNumbers)

    and powerball == winningPowerball):
        print()
        print(' You have won the powerball Lottery!Congs,')
        print('you would be a billionaire if this was real!')
        break
    else:
        print(' You lost.') # The leading space is required here.
        print('You have wasted', price)
        print('Thanks for playing!')
                        

