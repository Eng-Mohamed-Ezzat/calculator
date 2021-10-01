
operators = "operator (q to quit) [+, -, *, /]:"
result=op = ""

while (op!="q"):
    if (result == "div/0"): 
        inputnum2msg = "Enter a non-zero divisor:"
    else: 
        inputnum2msg = "Enter second number:"
        op = input(operators).strip()[0].lower()
        
        while(op not in \
            list(["+","-","*","/","q"]) ):
            op = input("Please input a valid %s" % \
                (operators)).strip()[0].lower()
                    
        if(op !="q"): 
            num1 = float(input("Enter first number:"))

    if(op !="q"):
        num2 = float(input(inputnum2msg))
        
        if      (op == "+"):                result = num1 + num2
        elif    (op == "-"):                result = num1 - num2
        elif    (op == "*"):                result = num1 * num2
        elif    (op == "/" and num2 !=0):   result = num1 / num2
        else:                               result = "div/0"
        
        if (result!="div/0"):
            resultmsg = "Result of calculation: %.2f %s %.2f = %.2f" \
                % (num1, op, num2, result)

        elif (op == "/" and num2 == 0):
            resultmsg = "Division by zero cannot be performed."
        
        print(resultmsg)

print("Thanks for using the program.")
