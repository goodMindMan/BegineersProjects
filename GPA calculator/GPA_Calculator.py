def gpa_calculator(): 
    
    # GPA scale
    ValidScl = False
    while not ValidScl:  # GPA scale input
        GPAScl = int(input('Do you use a scale of 5 or 4: '))
        # input validity check
        if GPAScl not in [4, 5]:
            ValidScl = False # Invalid response 
            print('Invalid input! Please enter a scale of 4 or 5.')
        else:
            ValidScl = True # Valis response
    
    # Grading system
    # Initialize the counter for valid response
    ValidSys = False
    while ValidSys == False: 
        # grading system input
        GrdSysPos = str(input('Does your grading scale system have negative grades i.e. (A-, B-, C-) y/n'))
        # input validity check
        if GrdSysPos not in ['y', 'n']:
            ValidSys = False
            print('invalid inputs! please enter a scale of y (yes their are neag grdes) or n (no their isnt)')
        else:
            ValidSys = True
    # Setting total number of inputs for each grading system
    if GrdSysPos == 'y':
        GrdTtl = 13
    else:
        GrdTtl = 9
    
    # Grades input
    NoGrdIn = 0
    while NoGrdIn <= GrdTtl:
        InGrd = [float(input(f'Enter GPA of every grade from A+ to D- (of D depending on Entered grading system) descendingly {i + 1}' for i in range(GrdTtl)))]
        for i01 in InGrd:
            if (i01 < 1) or ( i01 > 5):
                print(f'grade in valid, make sure to enter numbers between {GPAScl} and 1')
            else:
                NoGrdIn += 1