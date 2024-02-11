def bagelsGame( IN01 str, IN01 str, IN03 str):
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
    #belongs to list variables
    '''
    those are variables that are assigned as False 
    as long as an input doesn't belong to the list of 
    right digits
    '''
    blngs01 = False 
    blngs02 = False
    blngs03 = False
    # loop variables
    trials = 0
    trialsLmt = 10
    picoCount = 0
    # as long as trials arent used up and digits not guessed loop on the code
    while trials != trialsCount and picoCount != 3:
        # assign True to 
        if IN01 in lstDgts:
            blngs01 = True
        elif IN02 in lstDgts:
            blngs02 = True
        elif IN03 in lstDgts:
            blngs02 = True
        else:
            None
        
    if picoCount = 3:
        print('You win!!')
    elif trials = 10:
        print('Out of trials rerun to play again')
    else:
        print('We encountered an error please contact the adminstrator +201146824479')