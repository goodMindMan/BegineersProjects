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
    #belongs-to-list variables
    '''
    those are variables that are assigned as False 
    as long as an input doesn't belong to the list of 
    right digits and a fourth variable that increments
    once a guess is found in the the kist
    '''
    Gues01InLst = False 
    Gues02InLst = False
    Gues03InLst = False
    AllGuessesInLst = 0
    # loop variables
    trials = 0
    trialsLmt = 10
    picoCount = 0
    # as long as trials arent used up and digits not guessed loop on the code
    while trials != trialsLmt and picoCount != 3:
        # digits inputed as str
        gues01 = str(input('enter your guess for the first digit: '))
        gues02 = str(input('enter your guess for the second digit: '))
        gues03 = str(input('enter your guess for the third digit: '))
        '''
        assign True to belongs-to-variables if an
        input belongs to the list regardless of position
        '''
        if gues01 in lstDgts:
            Gues01InLst = True
            AllGuessesInLst +=1
        elif gues02 in lstDgts:
            Gues02InList = True
            AllGuessesInLst +=1
        elif gues03 in lstDgts:
            Gues03InList = True
            AllGuessesInLst +=1
        elif AllGuessesInLst == 0:  # if none of the inputs belong to the list print bagels
            print( 'bagels!' )
        elif AllGuessesInLst == 3 and gues01 == dgt01 and gues02 == dgt02 and gues03 == dgt03:
            picoCount = 3
            print('pico, pico, pico!!!')
            print('u win')
        elif Gues01Inlst == False:
            print('bagels!')
        elif Gues01InLst == True and gues01 == dgt01:
            print('pico!')
            picoCount += 1
        elif Gues01InLst == True and gues01 != dgt01:
            print('fermi!')
        elif Gues02Inlst == False:
            print('bagels!')
        elif Gues02InLst == True and gues02 == dgt02:
            print('pico!')
            picoCount += 1
        elif Gues02InLst == True and gues02 != dgt02:
            print('fermi!')
        elif Gues03Inlst == False:
            print('bagels!')
        elif Gues03InLst == True and gues03 == dgt03:
            print('pico!')
            picoCount += 1
        elif Gues03InLst == True and gues03 != dgt03:
            print('fermi!')
        trials += 1
    if picoCount == 3:
        print('You win!!')
    elif trials == 10:
        print('Out of trials rerun to play again')
    else:
        print('We encountered an error please contact the adminstrator +201146824479')
