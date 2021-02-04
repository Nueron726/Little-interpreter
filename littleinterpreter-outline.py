# This program interprets lines in a .little file and computes them.
# The little language is defined by the following BNF:
#
# digit ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
# int ::= <digit> | <int><digit>
# list_int ::= <int> <int> | <int> <list_int> 
# unary_op ::= double | triple | square | cube 
# binary_op ::= sub | div
# list_op ::= add | mult
# expression ::= <unary_op> <int> |
#                <binary_op> <int> <int> |
#                <list_op> <list_int>
# comment ::= #
#
# Original outline by Lisa Minogue, edited by Alexis Delgado 
# Student name goes here


# Returns true if the operation only takes one operand 
def isUnaryOp (op):
    if op == "double" or op == "triple" or op == "square" or op == "cube": 
        return True # added operand conditions and error messages
    else:
        return False
        print ":\tParsing eroor: unary operator requries one operand" 

# Returns true if the operation takes exactly two operands
def isBinaryOp (op): # added the operands defined as binary 
    if op == "sub" or op =="div": # added operand conditions and error message
        return True 
    else:
        return False
        print ":\tParsing error: binary operator rqruires two operands"

# Returns true if the operation takes 2 or more operands   
def isListOp (op):
    if op == "add" or op == "mult": # added operand conditions and error message
        return True
    else:
        return False
        print ":\tParsing error: multipe operands expected"
        
# Returns true if the operation is valid
def isValidOp (op):
    if isUnaryOP == True or isBinaryOp == True or isListOp == True:
        return isUnaryOp(op) or isBinaryOp(op) or isListOp(op)
        return True
    else:
        print line + ":\tParsing error: no such operation"


# Returns true if the string passed in is an integer
def isValidInt (num):
    try:
        int(num)
        return True
    except ValueError:
        return False

# Returns True if there is an error found in the expression
def found_errors (op, numOperands, expression, line):

    # if the operation is not valid
    if (isValidOp == False):
        print line + ":\tParsing error: no such operation"
        return True
    
    # if there are no operands
    if(numOperands == 0):
        print line + ":\tParsing error: no operands"
        return True
    
    # if operator is unary, then there should be one operand
    # TODO
    if(isUnaryOp(op) and not numOperands == 1):
        print line + ":\tParsing error: unary operator requires one operand"
        return True
        
    
    # if operator is binary, then there should be two operands
    if (isBinaryOp(op) and not numOperands == 2):
        print line + ":\tParsing error: binary operator requires two operands"
        return True

    # if operator is a list op, then there should be more than one operand
    # TODO
    if (isListOp (op) and not numOperands > 1):
        print line + ":\tParsing error: multiple operands expected"
        return True
    
    # Can't divide by zero
    # TODO
    
  
    
        
            
      
    # Check to make sure all the operands are numeric:
    i = 1
    while i <= numOperands:
        if (not isValidInt (expression[i])):
            print line + ":\tParsing error: integer expected"
            return True
        i = i + 1   
    return False    
        


########################################
###     main program starts here     ### 
########################################

# Ask the user for the name of the file:
filename = file(raw_input("Enter the filename:"), 'r')

filename = "TestAll.little.txt"


# Open the file:
print "Reading file: " + filename
infile = open (filename, "r")

# Loop through each line in the file and process it:
for i in infile:

    # Get rid of leading and trailing spaces, including the newline character
    line = i.strip()

    # Split line into a list
    expression = line.split()

    # Number of operands = the number of elements in the line -1 (the operand)
    numOperands = len (expression) - 1
    
    # check for whitespace or comments
    # If the line is a comment or is blank, we can skip it.
    # We could do this with an if...else block and indent all the rest of the code.
    # But in this case, continue will make the rest of the code easier to read.
    # That's not always the case with break and continue - which is why we need
    # to be careful when we choose to use them

    # This line checks for empty lines
    if numOperands == -1:
        continue

    # Check for comments - lines which start with a hashtag
    # TODO - For help, See Python Strings in Week 4
    if line[0] == "#":
        continue

    # find operator
    # Operator is the first element in the line. 
    op = expression[0]
    
    error_found = found_errors (op, numOperands, expression, line)
    if not error_found:
        
        
            

        # double operation has one operand and prints the value of the operand multiplied by 2
        if (op == "double"):
            print line + ":\t", int(expression[1]) * 2
        # add operation has many operands and prints the total of all of them
        if (op == "add"):
            total = 0
            i = 1
            while (i <= numOperands):
                total = total + int(expression[i])
                i = i + 1
            print line + ":\t", total

        # triple operation has one operand and prints the value of the operand mutilplied by 3
        if (op == "triple"):
            print line + ":\t", int(expression[1]) * 3

        # square operation has one operand and prints the value of the operand multtiplied by itself
        if (op == "square"):
            print line + ":\t",  (int(expression[1]) * int(expression[1]))
        # cube operation has one operand and prints the value of the operand mutliplied by
        if (op == "cube"):
            print line + ":\t\t", (int(expression[1]) * int(expression[1]) * int(expression[1]))
            
        #  sub operation has two operands, and prints the difference between the second and first respectively
        if (op == "sub"):
            print line + ":\t", (int(expression[1]) -  int(expression[2]))
        # div operation has two operands, and prints the divsion between of the second and first respectively
        if (op == "div" and not int(expression[2]) == 0):
             print line + ":\t", (int(expression[1]) / int(expression[2]))
              
        elif(op == "div" and int(expression[2]) == 0):
           
            print line + ":\t Divide by zero error"
            
            
            
       
        # mult operation has two or more operands and prints their function
        if (op == "mult"):
            total = 1
            i = 1
            while (i <= numOperands):
                total = total * (int(expression[i]))
                i = i + 1
            print line + ":\t", total 
                
        
        # TODO: Implement triple, square, cube, sub, div and mult
        
        
infile.close()

