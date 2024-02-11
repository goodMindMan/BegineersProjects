def bagelsGame():
    '''
    list of the real digits is 7, 0, 1 in this order
    and the limit to the number of trials in 10
    '''
    lstDgts = ['7', '0', '1']
    # assigning each digit separately for later
    dgt01 = '7'
    dgt02 = '0'
    dgt03 = '1'
    # digits inputed as str
    IN01 = str(input('enter your guess for the first digit: '))
    IN02 = str(input('enter your guess for the second digit: '))
    IN03 = str(input('enter your guess for the third digit: '))
    #belongs-to-list variables
    '''
    those are variables that are assigned as False 
    as long as an input doesn't belong to the list of 
    right digits and a fourth variable that increments
    once a guess is found in the the kist
    '''
    blngs01 = False 
    blngs02 = False
    blngs03 = False
    blngsAllThree = 0
    # loop variables
    trials = 0
    trialsLmt = 10
    picoCount = 0
    # as long as trials arent used up and digits not guessed loop on the code
    while trials != trialsLmt and picoCount != 3:
        '''
        assign True to belongs-to-variables if an
        input belongs to the list regardless of position
        '''
        if IN01 in lstDgts:
            blngs01 = True
            blngsAllThree +=1
        elif IN02 in lstDgts:
            blngs02 = True
            blngsAllThree +=1
        elif IN03 in lstDgts:
            blngs03 = True
            blngsAllThree +=1
        elif blngsAllThree == 0:  # if none of the inputs belong to the list print bagels
            print( 'bagels!' )
        elif blngsAllThree == 3 and IN01 == dgt01 and IN02 == dgt02 and IN03 == dgt03:
            picoCount = 3
            print('pico, pico, pico!!!')
            print('u win')
        elif blngs01 == True and IN01 == dgt01:
            print('pico!')
            picoCount += 1
        elif blngs01 == True and IN01 != dgt01:
            print('fermi!')
        elif blngs02 == True and IN02 == dgt02:
            print('pico!')
            picoCount += 1
        elif blngs02 == True and IN02 != dgt02:
            print('fermi!')
        elif blngs03 == True and IN03 == dgt03:
            print('pico!')
            picoCount += 1
        elif blngs03 == True and IN03 != dgt03:
            print('fermi!')
        trials += 1
    if picoCount == 3:
        print('You win!!')
    elif trials == 10:
        print('Out of trials rerun to play again')
    else:
        print('We encountered an error please contact the adminstrator +201146824479')
