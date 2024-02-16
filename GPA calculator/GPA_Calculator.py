import numpy as np

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
            ValidScl = True # Valid response
    
    # Grading system
    # Initialize the counter for valid response
    ValidSys = False
    GrdSysPos = None # Fix01(UnboundLocalError): initializing this variable to ensure it is defined for use outside the loop
    while ValidSys == False: 
        # grading system input
        GrdSysPos = str(input('Does your grading scale system have negative grades i.e. (A-, B-, C-) y/n': ))
        # input validity check
        if GrdSysPos not in ['y', 'n']:
            ValidSys = False
            print('invalid inputs! please enter a scale of y (yes their are neag grdes) or n (no their isnt)')
        else:
            ValidSys = True
    # Setting total number of inputs for each grading system
    if GrdSysPos == 'y':
        GrdTtl = 12 # Fix03(logicalError): User doesn't input F as it is assumed to be 1
    else:
        GrdTtl = 8 # Fix03
    
    # Grades input
    NoGrdIn = 0
    InGrdClean = {} # Fix02(logicalError): inputs to be add later in the loop
    for i in range(GrdTtl):
        InGrd = float(input(f'Enter GPA of every grade from A+ to D- (of D depending on Entered grading system) descendingly : '))
        if 1 <= grade <= 5:
            InGrdClean[f"grade{i+1}"] = InGrd  
            NoGrdIn += 1
            print('here are your enteries \n', InGrdClean)
        else:
            print(f'Invalid grade detected: {InGrd}. Make sure to enter numbers between {GrdScl} and 1')
    InGrdClean[f'grade{Grd}]= 1.0

    # converting inputs into arrays
    InGrdArray = np.array([])
    for i in my_dict:
        array = np.append(InGrdArray, my_dict[i])
    
    # Number of subjects
    while not ValidSubjNo:
        SubjNo = int(input('How many subjects do you have: '))
        # input validity check
        if type(SubjNo) is int:
            ValidSubjNo = False # Invalid response 
            print('Invalid input! Enter a number!')
        else:
            ValidSubjNo = True # Valis response
    
    #Score input
    NoScrIn = 0
    InScrLst = []
    while NoScrIn < ValidSubjNo :  # Adjusted the loop condition to ensure it runs 9 times
        InScr = str(input(f'Enter score number {NoScrIn} e.g. (A-, C, etc.): '))
        if type(InScr) :
            print('Score invalid! Make sure to enter letters')
        elif len(InScr) > 2:
            print('Please enter a valid score (A+, F, C, etc.))
        else:
            InScrLst.append(InScr)
            NoScrIn += 1
