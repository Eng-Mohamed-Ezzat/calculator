op = ""
def displ_menu():
    print("Menu options:")
    print("  +: to add")
    print("  -: to subtract")
    print("  *: to multiply")
    print("  /: to divide")
    print()
    
def get_float(prompt):
    return float(input(prompt))

def add(num1, num2):
    #  Add the two operands 
    result = num1 + num2

    # PUT result
    return ("-> Result of calculation: " + str(num1) + " + " + str( num2 ) + " = " + str( result))

def subtract(num1, num2):
    #  Subtract the two operands
    result = num1 - num2
    
    # PUT result
    return ("-> Result of calculation: " + str(num1) + " - " + str( num2 ) + " = " + str( result))


def multiply(num1, num2):
    # Multiply the two operands
    result = num1 * num2

    # PUT result
    return ("-> Result of calculation: " + str(num1) + " * " + str( num2 ) + " = " + str( result))

def iszero(num2):
    return num2 == 0

def divide(num1, num2):
    
    if (iszero(num2)):
        print("Division by zero cannot be performed.")

        # WHILE divisor is zero
        while(num2==0):
            # GET divisor
            num2 = float(input("Enter a non-zero divisor:"))

    # Divide the two operands
    result = num1 / num2
    
    #  PUT result
    return ("-> Result of calculation: " + str(num1) + " / " + str( num2 ) + " = " + str( result))


def main():
    displ_menu()
    # GET operator or quit option 

    op = input("Enter operator (q to quit):")
    # WHILE operator not quit 
    while (op!="q"):
        # IF operator is addition
        if      (op == "+"): 
            num1 = get_float("Enter first number:")
            num2 = get_float("Enter second number:")
            results =  add(num1,num2) 
            print(results)

        # ELSE IF operator is subtraction
        elif    (op == "-"):
            num1 = get_float("Enter first number:")
            num2 = get_float("Enter second number:")
            results = subtract(num1,num2)
            print(results)

        # ELSE IF operator is multiplication
        elif    (op == "*"):
            num1 = get_float("Enter first number:")
            num2 = get_float("Enter second number:")
            results = multiply(num1,num2)
            print(results)

        # ELSE IF operator is division
        elif    (op == "/"):
            num1 = get_float("Enter first number:")
            num2 = get_float("Enter second number:")
            results = divide(num1, num2)
            print(results)
        
        op = input("Enter operator (q to quit):")

    # PUT closing message
    print("Thanks for using the program.")    

if __name__ == "__main__": main()