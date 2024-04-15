def center_grav_location():
    import numpy as np
  
    # Total Number of Alternatives input
    valid_alt_no = False # Initialize validity check variable
    while not valid_alt_no: # Loop until input is valid
      try: 
          alt_no  = int(input('How many Locations alternatives: --> ')) # Entering number of locations alternatives
          # Input validity check
          if alt_no > 0: # Is it positive?
              valid_alt_no = True  # Valid response
              print(f'entry: {alt_no}') #Display Input
          else:
              print('Enter a positive number')
      except ValueError:
          print('Input a number please')
    
    # Creating a dictionary with the number of locations entered
    # X-Coords
    print('consider any place as the origin point and input vertical and horizontal distances')
    inc_var_inx = 0 # Initialize counter
    alt_dictx = {} # Empty dictionary to be populated with X coordinates 
    while inc_var_inx < alt_no:
        try:
            inx = float(input(f'Enter X (horizontal) coordinate of Location {inc_var_inx +1}: --> ')) # Input x coordinate
            alt_dictx.__setitem__(f'Location {inc_var_inx + 1} X coordinate', inx) # Populate empty Dict
            inc_var_inx += 1 # Increment 
        except ValueError:
            print('Enter a Whole or Decimal Number only')
    print(alt_dictx)
    # Y-coords
    inc_var_iny = 0 # Initialize counter
    alt_dicty = {} # Empty dictionary to be populated with X coordinates 
    while inc_var_iny < alt_no: # loop until Incremening __alt_no__ number of times
        try:
            InY = float(input(f'Enter y (vertical) coordinate of Location {inc_var_iny +1}: --> ')) # Input Y coordinate 
            alt_dicty.__setitem__(f'Location {inc_var_iny + 1} Y coordinate', InY) # Populate empty Dict
            inc_var_iny += 1 # Increment
        except ValueError:
            print('Enter a Whole or Decimal Number only')
    print(alt_dicty)

    # Create an array of x and y coordinates
    # X-coords
    xcrds = np.array([]) # Empty array to be populated with coordinates for futhur processing
    for i in alt_dictx.values(): # populate array with all values of the dictionary
        xcrds = np.append(xcrds, i)
    # Y-coords
    ycrds = np.array([]) # // for Y axis
    for i in alt_dicty.values(): # // for Y axis
        ycrds = np.append(ycrds, i)

    # weight or no weights
    exit_loop_var = False # Initalize Loop Variables 
    while exit_loop_var == False: # Loop only if there are weights or if all weights are entered
        no_whts_in = input('Do alternatives have weights? y/n: --> ') # Prompt user 
        #Input validity check
        if no_whts_in in ['y', 'n']: 
            if no_whts_in == 'y':
                is_whts = True
                exit_loop_var = True
            else:
                is_whts = False 
                exit_loop_var = True # Assign it true to exit_loop_var loop 
        else:
            print('Please enter a valid response; No weights --> n, Has weights --> y') #

    # Input weights in array and calculating coordinates
    if is_whts == True:
        Whts = np.array([]) # Empty array to be populated with Alternatives Weights if any
        inc_var_wht = 0 # Initialize counter
        while inc_var_wht < alt_no:
            try:
                # Inputs
                in_wht = float(input(f'Please Enter Weights at the same order of Coordinates,,, weight {inc_var_wht + 1}: --> ')) 
                Whts = np.append(Whts, in_wht) # Populate weights array
                inc_var_wht += 1 # increment
            except ValueError:
                print('Please Enter a Whole or Decimal Number!')
        # Compute average weighted coordinates
        avex = np.average(xcrds, None, Whts, 0)
        avey = np.average(ycrds, None, Whts, 0)
        print(f'center of gravity coordinates are ({avex} , {avey})')
    else:
        # Compute average coordinates  
        avex = np.average(xcrds, None, None, 0)
        avey = np.average(ycrds, None, None, 0)
        print(f'center of gravity coordinates are ({avex} , {avey})')
