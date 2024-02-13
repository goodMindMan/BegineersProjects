def bagels_game():
'''
list of the real digits is 7, 0, 1 in this order
and the limit to the number of trials in 10
'''
    lstDgts = ['7', '0', '1']
# assigning each digit separately for later
    dgt01 = '7'
    dgt02 = '0'
    dgt03 = '1'
# loop variables
    trials = 0
    trialsLmt = 10
    PlyrWins = False
# as long as trials arent used up and digits not guessed loop on the code
    while trials < trialsLmt and PlyrWins == False:
# digits inputed as str
        gues01 = str(input('enter your guess for the first digit: '))
        gues02 = str(input('enter your guess for the second digit: '))
        gues03 = str(input('enter your guess for the third digit: '))
        LstGuesses = [gues01, gues02, gues03]
'''
examines whether the player's previous guess was correct; if so:
sets __PlyerWins__ as true and ends the while loop
'''    
        if LstGuesses == lstDgts:
            PlyrWins = True
#this block is run went the guess is not correct
        else: 
#first guess
            if gues01 == dgt01:
                print('pico')
            elif gues01 in lstDgts:
                print('fermi')
            else:
                print('bagels')
#second guess
            if gues02 == dgt02:
                print('pico')
            elif gues02 in lstDgts:
                print('fermi')
            else:
                print('bagels')
#third guess
            if gues03 == dgt03:
                print('pico')
            elif gues03 in lstDgts:
                print('fermi')
            else:
                print('bagels')
            trials += 1
# executs if Player wins or runs out of trials
    if PlyrWins == True:
        print('You win!!')
    elif trials == 10:
        print('Out of trials rerun to play again')
    else:
        print('We encountered an error please contact the adminstrator +201146824479')
