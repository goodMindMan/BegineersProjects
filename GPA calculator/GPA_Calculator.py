import numpy as np

def gpa_calculator(): 
    
    # GPA scale (out of 4 or 5)
    ValidScl = False
    while not ValidScl: # As long as the scale is not valid prompt the user to re try 
        GPAScl = int(input('Do you use a scale of 5 or 4: --> ')) # GPA scale input 
        
        # input validity check
        if GPAScl not in [4, 5]: # Makes sure entries are only 4 or 5
            ValidScl = False # Invalid response 
            print('Invalid input! Please enter a scale of 4 or 5.')
        else:
            ValidScl = True # Valid response
    
    # Grading system
    ValidSys = False # Initialize validity check variable
    GrdSysNeg = None # Initialize Input variable
    while ValidSys == False: # Loop until input is valid
        # grading system input
        GrdSysNeg = str(input('Does your grading scale system have negative grades i.e. (A-, B-, C-) y/n : --> ' ))
        # input validity check
        if GrdSysNeg not in ['y', 'n']: # Makes sure input is ether y or n 
            ValidSys = False
            print('invalid inputs! please enter valid scale answer: y (yes their are neag grdes) or n (no their isnt)')
        else:
            ValidSys = True
    # Checks whether the grading system Has D- or D before F
    ValidSys02 = False # Initialize validity check variable
    GrdSysD = None # initializing Input variable
    while ValidSys02 == False: # Loop until input is valid
        # grading system input
        GrdSysD = str(input('Does your grading scale system have D- or D before F: --> ' ))
        # input validity check
        if GrdSysD not in ['D', 'D-']: # Makes sure input is ether D- or D
            ValidSys02 = False
            print('invalid inputs! please enter D- (yes their is D- before F) or D (no their is D before F)')
        else:
            ValidSys02 = True
    # Setting total number of inputs for each grading system 
    # Creating dictonaries for each case
    if GrdSysNeg == 'y' and GrdSysD == 'D-' :
        InGrdNegDMin = {'A+': None, 'A': None, 'A-': None, 'B+': None, 'B': None, 'B-': None, 'C+': None, 'C': None, 'C-': None, 'D+': None, 'D': None, 'D-': None, 'F': 0.0}
        GrdTtl = 12 # Total number of inputs possilble for this case
    elif GrdSysNeg == 'y' and GrdSysD == 'D' :
        InGrdNegD = {'A+': None, 'A': None, 'A-': None, 'B+': None, 'B': None, 'B-': None, 'C+': None, 'C': None, 'C-': None, 'D+': None, 'D': None, 'F': 0.0}
        GrdTtl = 12 # Total number of inputs possilble for this case
    else:
        InGrdPos = {'A+': None, 'A': None, 'B+': None, 'B': None, 'C+': None, 'C': None, 'D+': None, 'D': None, 'F': 0.0}
        GrdTtl = 8 # Total number of inputs possilble for this case
    
    # Grades input
    NoGrdIn = 0 # Intializie Counter
    InGrdLst = [] #Empty set to be populated
    while NoGrdIn < GrdTtl: # Loop as long as counter is less that total grades available
        try:
            InGrd = float(input('Enter GPA for each grade from A to D-( or D) Descending: --> ')) # Input float for each grade
            if 1 <= InGrd <= 5: # If the number is in that interval it is valid
                InGrdLst.append(InGrd) # Add each valid entry to the list left empty earlier
                NoGrdIn += 1 # Increment counter
            else:
                print(f'Invalid grade detected: {InGrd}. Make sure to enter numbers between 1 and 5.')
        except ValueError: # If there is an input error print error message and reprompt the user
            print('Please enter a valid number.')
    InGrdLst.append(0.0) # Add Fail (F) with Zero GPA
    # Filling previously empty dictonaries for each case
    if GrdSysNeg == 'y' and GrdSysD == 'D-' : # Grading system with Negative grades inluding D-
        for i, j in zip(InGrdNegDMin, InGrdLst):
            InGrdNegDMin[i] = j
        print('Your entries: ', InGrdNegDMin)
    elif GrdSysNeg == 'y' and GrdSysD == 'D' : # Grading system with Negative grades excluding D-
        for i, j in zip(InGrdNegD, InGrdLst):
            InGrdNegD[i] = j
        print('Your entries: ', InGrdNegD)
    else: 
        for i, j in zip(InGrdPos, InGrdLst):
            InGrdPos[i] = j
        print('Your entries: ', InGrdPos)
    
    # converting inputs into arrays
    InGrdArr = np.array(InGrdLst)
    
    # Number of subjects
    ValidSubjNo = False # Initialize validity check variable
    while not ValidSubjNo: # Loop until input is valid
        try: 
            SubjNo = int(input('How many subjects do you have: --> '))
            # Input validity check
            ValidSubjNo = True  # Valid response
            print(f'entry: {SubjNo}') #Display Input
        except ValueError:
            print( 'Input a number please')

    #Score input
    NoScrIn = 0 # Intializie Counter
    InScrLst = [] #Empty set to be populated
    while NoScrIn < SubjNo :  # Loop as long as counter is less that total subjects count 
        InScr = input(f'Enter score number {NoScrIn} e.g. (A-, C, etc.): --> ') # prompt 
        #input validity check
        if (len(InScr) > 2) or ( InScr not in ['A+', 'A', 'A-', 'A', 'B+', 'B', 'B-','C+', 'C', 'C-', 'D+', 'D', 'D-', 'F']): # Makes sure input is a two letter valid grade
            print('Score invalid! Make sure to enter maximum 2 letters')
        else:
            InScrLst.append(InScr) # Adds to empty list
            NoScrIn += 1 # Increments
    
    # Setting Grades for each score
    InScrGPA = np.array([]) # empty array to be populated
    if GrdSysNeg == 'y' and GrdSysD == 'D-' : #case
        for i in InScrLst: 
            for j in InGrdNegDMin:
                if i == j: # for every element in scores list that is equal to key in dictionary of grades 
                    InScrGPA = np.append(InScrGPA, InGrdNegDMin[j]) # Populate the array with the floating point values in the dictionary 
        print('Your entries: ', InScrGPA)
    elif GrdSysNeg == 'y' and GrdSysD == 'D' :
        for i in InScrLst:
            for j in InGrdNegD:
                if i == j: # for every element in scores list that is equal to key in dictionary of grades
                    InScrGPA = np.append(InScrGPA, InGrdNegD[j]) # Populate the array with the floating point values in the dictionary 
        print('Your entries: ', InScrGPA)
    else:
        for i in InScrLst:
            for j in InGrdPos:
                if i == j: # for every element in scores list that is equal to key in dictionary of grades
                    InScrGPA = np.append(InScrGPA, InGrdPos[j]) # Populate the array with the floating point values in the dictionary 
        print('Your entries: ', InScrGPA)

    # Subject weights input
    InWhtNo = 0 # Intializie Counter
    InWhtLst = [] #Empty set to be populated
    while InWhtNo < SubjNo: # Loop as long as counter is less that total subjects count
        try:
            InWht = int(input(f'Enter each subject weight { InWhtNo + 1}: --> ')) # Input weights
            InWhtLst.append(InWht) # Populated empty list
            InWhtNo += 1 # Increment
        except ValueError:
            print('Please enter a valid number.')

    # Saving input weights into an array
    InWhtArr = np.array(InWhtLst) # Create a aray of weights

    # Main GPA equation
    TtlCrHrs = np.sum(InWhtArr) # Total credit hours 
    WhtScr = (InWhtArr*InScrGPA) # Ceate an Array of weighted scores
    GPA = np.sum(WhtScr)/TtlCrHrs # Divide the sum of weighted scores by the total Credit hours
    print('Your GPA is: --> :'round(GPA, 2)) # Print the GPA rounded to two decimal places
