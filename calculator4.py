# GET user selection of arithmetic operation or quit option
op = input("operator (q to quit) [+, -, *, /]:")

# WHILE user does not quit
while (op!="q"):
# GET list of numbers
    inputnums = input("Enter space-separated numbers (min 2):")
    
# Convert numbers to float
    nums =  [float(n) for n in inputnums.split(" ")]

# WHILE list has less than 2 elements
    while(len(nums)<2):
        # GET list of numbers
        inputnums = input("Enter space-separated numbers (min 2):")
        # Convert numbers to float
        nums =  [float(n) for n in inputnums.split(" ")]

    # Initialize total with first number in list
    total = nums[0]

    # Remove first number from list
    nums.pop(0)

# IF addition
    if      (op == "+"):
        # FOR every number in list
        for n in nums:
            # Add to total      
            total+= n        
          
        # PUT total
        print("-> Result of addition:" ,total)

# ELSE IF subtraction
    elif     (op == "-"):
        # FOR every number in list
        for n in nums:
            # Subtract from total
            total-= n        
          
        # PUT total
        print("-> Result of subtraction:" ,total)

# ELSE IF multiplication
    elif     (op == "*"):
        # FOR every number in list
        for n in nums:
            # Multiply with total
            total*= n        
          
        # PUT total
        print("-> Result of multiplication:" ,total)

# ELSE IF division
    elif     (op == "/"):
        # IF a number in list is zero  
        if nums.count(0) > 0:
            # Print error message
            print("Division by zero cannot be performed.")
        # ELSE
        else:
            # FOR every number in list
            for n in nums:
                # Divide from total
                total/= n        
            
            # PUT total
            print("-> Result of division:" ,total)

# GET user selection of arithmetic operation or quit option
    op = input("operator (q to quit) [+, -, *, /]:")

# PUT closing message
print("Closing calculator.")