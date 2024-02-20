def center_grav_location():
    import numpy as np
  
    # Total Number of Alternatives input
    ValidAltNo = False # Initialize validity check variable
    while not ValidAltNo: # Loop until input is valid
      try: 
          AltNo  = int(input('How many Locations alternatives: --> ')) # Entering number of locations alternatives
          # Input validity check
          if AltNo > 0: # Is it positive?
              ValidAltNo = True  # Valid response
              print(f'entry: {AltNo}') #Display Input
          else:
              print('Enter a positive number')
      except ValueError:
          print('Input a number please')
    
    # Creating a dictionary with the number of locations entered
    # X-Coords
    print('consider any place as the origin point and input vertical and horizontal distances')
    Inc_Var_InX = 0 # Initialize counter
    AltDictX = {} # Empty dictionary to be populated with X coordinates 
    while Inc_Var_InX < AltNo:
        try:
            InX = float(input(f'Enter X (horizontal) coordinate of Location {Inc_Var_InX +1}: --> ')) # Input x coordinate
            AltDictX.__setitem__(f'Location {Inc_Var_InX + 1} X coordinate', InX) # Populate empty Dict
            Inc_Var_InX += 1 # Increment 
        except ValueError:
            print('Enter a Whole or Decimal Number only')
    print(AltDictX)
    # Y-coords
    Inc_Var_InY = 0 # Initialize counter
    AltDictY = {} # Empty dictionary to be populated with X coordinates 
    while Inc_Var_InY < AltNo: # loop until Incremening __AltNo__ number of times
        try:
            InY = float(input(f'Enter y (vertical) coordinate of Location {Inc_Var_InY +1}: --> ')) # Input Y coordinate 
            AltDictY.__setitem__(f'Location {Inc_Var_InY + 1} Y coordinate', InY) # Populate empty Dict
            Inc_Var_InY += 1 # Increment
        except ValueError:
            print('Enter a Whole or Decimal Number only')
    print(AltDictY)

    # Create an array of x and y coordinates
    # X-coords
    Xcrds = np.array([]) # Empty array to be populated with coordinates for futhur processing
    for i in AltDictX.values(): # populate array with all values of the dictionary
        Xcrds = np.append(Xcrds, i)
    # Y-coords
    Ycrds = np.array([]) # // for Y axis
    for i in AltDictY.values(): # // for Y axis
        Ycrds = np.append(Ycrds, i)

    # weight or no weights
    Exit = False # Initalize Loop Variables 
    while Exit == False: # Loop only if there are weights or if all weights are entered
        NoWhtsIn = input('Do alternatives have weights? y/n: --> ') # Prompt user 
        #Input validity check
        if NoWhtsIn in ['y', 'n']: 
            if NoWhtsIn == 'y':
                IsWhts = True
                Exit = True
            else:
                IsWhts = False 
                Exit = True # Assign it true to exit loop 
        else:
            print('Please enter a valid response; No weights --> n, Has weights --> y') #

    # Input weights in array and calculating coordinates
    if IsWhts == True:
        Whts = np.array([]) # Empty array to be populated with Alternatives Weights if any
        Inc_Var_Wht = 0 # Initialize counter
        while Inc_Var_Wht < AltNo:
            try:
                # Inputs
                InWht = float(input(f'Please Enter Weights at the same order of Coordinates,,, weight {Inc_Var_Wht + 1}: --> ')) 
                Whts = np.append(Whts, InWht) # Populate weights array
                Inc_Var_Wht += 1 # increment
            except ValueError:
                print('Please Enter a Whole or Decimal Number!')
        # Compute average weighted coordinates
        AveX = np.average(Xcrds, None, Whts, 0)
        AveY = np.average(Ycrds, None, Whts, 0)
        print(f'center of gravity coordinates are ({AveX} , {AveY})')
    else:
        # Compute average coordinates  
        AveX = np.average(Xcrds, None, None, 0)
        AveY = np.average(Ycrds, None, None, 0)
        print(f'center of gravity coordinates are ({AveX} , {AveY})')
