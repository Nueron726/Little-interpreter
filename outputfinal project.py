Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:TestAll.little.txt
Reading file: TestAll.little.txt
double 5:	10
double 10:	20
triple 7:	21
triple 2:	6
square 2:	4
square 5:	25
cube 3:	27
cube 5:	125
sub 5 4:	1
sub 8 4:	4
add 2 3:	5
add 1 2 3:	6
add 1 2 3 4 5:	15
add 2 3 3:	8
add 4 5 6 7 8 9 10 2 3 4:	58
add 4 2 3 2 4 4 5:	24

Traceback (most recent call last):
  File "C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py", line 156, in <module>
    error_found = found_errors (op, numOperands, expression, line)
  File "C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py", line 93, in found_errors
    if (op == "div" and numOperand == 0):
NameError: global name 'numOperand' is not defined
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:TestAll.little.txt
Reading file: TestAll.little.txt
double 5:	10
double 10:	20
triple 7:	21
triple 2:	6
square 2:	4
square 5:	25
cube 3:	27
cube 5:	125
sub 5 4:	1
sub 8 4:	4
add 2 3:	5
add 1 2 3:	6
add 1 2 3 4 5:	15
add 2 3 3:	8
add 4 5 6 7 8 9 10 2 3 4:	58
add 4 2 3 2 4 4 5:	24
div 10 5:	2
div 8 2:	4
div 16 4:	4
mult 4 5:	20
mult 1 2 3:	6
mult 1 2 3 4 5:	120
mult 2 3 4 5:	120
mult 6 7 5 3 2 1 2 3 4 5:	151200
square 3:	9
double 6:	12
mult 5 2:	10
sub 9 3:	6
add 3 4 2:	9
sub 12 2:	10
cube 8:	512
add 5 6:	11
mult 8 2 1 2:	32
triple 4:	12
square 7:	49
add 3 2:	5
error:	Parsing error: no operands
null:	Parsing error: no operands
no_op:	Parsing error: no operands
add 4:	Parsing error: multiple operands expected
double 3 8:	Parsing error: unary operator requires one operand
sub 2:	Parsing error: binary operator requires two operands
sub 3 4 5:	Parsing error: binary operator requires two operands
sub:	Parsing error: no operands
mult 3:	Parsing error: multiple operands expected
hi:	Parsing error: no operands
triple:	Parsing error: no operands
cube:	Parsing error: no operands
cube 6 7:	Parsing error: unary operator requires one operand
square 4 5:	Parsing error: unary operator requires one operand
double trouble:	Parsing error: integer expected
add hello world:	Parsing error: integer expected
add 4 5 xyz:	Parsing error: integer expected
sub 3 abc:	Parsing error: integer expected
div 3 0:	
Traceback (most recent call last):
  File "C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py", line 190, in <module>
    print line + ":\t", (int(expression[1]) / int(expression[2]))
ZeroDivisionError: integer division or modulo by zero
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:TestAll.little.txt
Reading file: TestAll.little.txt
double 5:	10
double 10:	20
triple 7:	21
triple 2:	6
square 2:	4
square 5:	25
cube 3:	27
cube 5:	125
sub 5 4:	1
sub 8 4:	4
add 2 3:	5
add 1 2 3:	6
add 1 2 3 4 5:	15
add 2 3 3:	8
add 4 5 6 7 8 9 10 2 3 4:	58
add 4 2 3 2 4 4 5:	24
div 10 5:	 Divide by zero error
div 10 5:	2
div 8 2:	 Divide by zero error
div 8 2:	4
div 16 4:	 Divide by zero error
div 16 4:	4
mult 4 5:	20
mult 1 2 3:	6
mult 1 2 3 4 5:	120
mult 2 3 4 5:	120
mult 6 7 5 3 2 1 2 3 4 5:	151200
square 3:	9
double 6:	12
mult 5 2:	10
sub 9 3:	6
add 3 4 2:	9
sub 12 2:	10
cube 8:	512
add 5 6:	11
mult 8 2 1 2:	32
triple 4:	12
square 7:	49
add 3 2:	5
error:	Parsing error: no operands
null:	Parsing error: no operands
no_op:	Parsing error: no operands
add 4:	Parsing error: multiple operands expected
double 3 8:	Parsing error: unary operator requires one operand
sub 2:	Parsing error: binary operator requires two operands
sub 3 4 5:	Parsing error: binary operator requires two operands
sub:	Parsing error: no operands
mult 3:	Parsing error: multiple operands expected
hi:	Parsing error: no operands
triple:	Parsing error: no operands
cube:	Parsing error: no operands
cube 6 7:	Parsing error: unary operator requires one operand
square 4 5:	Parsing error: unary operator requires one operand
double trouble:	Parsing error: integer expected
add hello world:	Parsing error: integer expected
add 4 5 xyz:	Parsing error: integer expected
sub 3 abc:	Parsing error: integer expected
div 3 0:	 Divide by zero error
div 3 0:	
Traceback (most recent call last):
  File "C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py", line 190, in <module>
    print line + ":\t", (int(expression[1]) / int(expression[2]))
ZeroDivisionError: integer division or modulo by zero
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:TestAll.little.txt
Reading file: TestAll.little.txt
double 5:	10
double 10:	20
triple 7:	21
triple 2:	6
square 2:	4
square 5:	25
cube 3:	27
cube 5:	125
sub 5 4:	1
sub 8 4:	4
add 2 3:	5
add 1 2 3:	6
add 1 2 3 4 5:	15
add 2 3 3:	8
add 4 5 6 7 8 9 10 2 3 4:	58
add 4 2 3 2 4 4 5:	24
div 10 5:	2
div 8 2:	4
div 16 4:	4
mult 4 5:	20
mult 1 2 3:	6
mult 1 2 3 4 5:	120
mult 2 3 4 5:	120
mult 6 7 5 3 2 1 2 3 4 5:	151200
square 3:	9
double 6:	12
mult 5 2:	10
sub 9 3:	6
add 3 4 2:	9
sub 12 2:	10
cube 8:	512
add 5 6:	11
mult 8 2 1 2:	32
triple 4:	12
square 7:	49
add 3 2:	5
error:	Parsing error: no operands
null:	Parsing error: no operands
no_op:	Parsing error: no operands
add 4:	Parsing error: multiple operands expected
double 3 8:	Parsing error: unary operator requires one operand
sub 2:	Parsing error: binary operator requires two operands
sub 3 4 5:	Parsing error: binary operator requires two operands
sub:	Parsing error: no operands
mult 3:	Parsing error: multiple operands expected
hi:	Parsing error: no operands
triple:	Parsing error: no operands
cube:	Parsing error: no operands
cube 6 7:	Parsing error: unary operator requires one operand
square 4 5:	Parsing error: unary operator requires one operand
double trouble:	Parsing error: integer expected
add hello world:	Parsing error: integer expected
add 4 5 xyz:	Parsing error: integer expected
sub 3 abc:	Parsing error: integer expected
div 3 0:	
Traceback (most recent call last):
  File "C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py", line 190, in <module>
    print line + ":\t", (int(expression[1]) / int(expression[2]))
ZeroDivisionError: integer division or modulo by zero
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:TestAll.little.txt
Reading file: TestAll.little.txt
double 5:	10
double 10:	20
triple 7:	21
triple 2:	6
square 2:	4
square 5:	25
cube 3:	27
cube 5:	125
sub 5 4:	1
sub 8 4:	4
add 2 3:	5
add 1 2 3:	6
add 1 2 3 4 5:	15
add 2 3 3:	8
add 4 5 6 7 8 9 10 2 3 4:	58
add 4 2 3 2 4 4 5:	24
div 10 5:	2
div 8 2:	4
div 16 4:	4
mult 4 5:	20
mult 1 2 3:	6
mult 1 2 3 4 5:	120
mult 2 3 4 5:	120
mult 6 7 5 3 2 1 2 3 4 5:	151200
square 3:	9
double 6:	12
mult 5 2:	10
sub 9 3:	6
add 3 4 2:	9
sub 12 2:	10
cube 8:	512
add 5 6:	11
mult 8 2 1 2:	32
triple 4:	12
square 7:	49
add 3 2:	5
error:	Parsing error: no operands
null:	Parsing error: no operands
no_op:	Parsing error: no operands
add 4:	Parsing error: multiple operands expected
double 3 8:	Parsing error: unary operator requires one operand
sub 2:	Parsing error: binary operator requires two operands
sub 3 4 5:	Parsing error: binary operator requires two operands
sub:	Parsing error: no operands
mult 3:	Parsing error: multiple operands expected
hi:	Parsing error: no operands
triple:	Parsing error: no operands
cube:	Parsing error: no operands
cube 6 7:	Parsing error: unary operator requires one operand
square 4 5:	Parsing error: unary operator requires one operand
double trouble:	Parsing error: integer expected
add hello world:	Parsing error: integer expected
add 4 5 xyz:	Parsing error: integer expected
sub 3 abc:	Parsing error: integer expected
div 3 0:	
Traceback (most recent call last):
  File "C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py", line 191, in <module>
    print line + ":\t", (int(expression[1]) / int(expression[2]))
ZeroDivisionError: integer division or modulo by zero
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:TestAll.little.txt
Reading file: TestAll.little.txt
double 5:	10
double 10:	20
triple 7:	21
triple 2:	6
square 2:	4
square 5:	25
cube 3:	27
cube 5:	125
sub 5 4:	1
sub 8 4:	4
add 2 3:	5
add 1 2 3:	6
add 1 2 3 4 5:	15
add 2 3 3:	8
add 4 5 6 7 8 9 10 2 3 4:	58
add 4 2 3 2 4 4 5:	24
div 10 5:	 Divide by zero error
div 8 2:	 Divide by zero error
div 16 4:	 Divide by zero error
mult 4 5:	20
mult 1 2 3:	6
mult 1 2 3 4 5:	120
mult 2 3 4 5:	120
mult 6 7 5 3 2 1 2 3 4 5:	151200
square 3:	9
double 6:	12
mult 5 2:	10
sub 9 3:	6
add 3 4 2:	9
sub 12 2:	10
cube 8:	512
add 5 6:	11
mult 8 2 1 2:	32
triple 4:	12
square 7:	49
add 3 2:	5
error:	Parsing error: no operands
null:	Parsing error: no operands
no_op:	Parsing error: no operands
add 4:	Parsing error: multiple operands expected
double 3 8:	Parsing error: unary operator requires one operand
sub 2:	Parsing error: binary operator requires two operands
sub 3 4 5:	Parsing error: binary operator requires two operands
sub:	Parsing error: no operands
mult 3:	Parsing error: multiple operands expected
hi:	Parsing error: no operands
triple:	Parsing error: no operands
cube:	Parsing error: no operands
cube 6 7:	Parsing error: unary operator requires one operand
square 4 5:	Parsing error: unary operator requires one operand
double trouble:	Parsing error: integer expected
add hello world:	Parsing error: integer expected
add 4 5 xyz:	Parsing error: integer expected
sub 3 abc:	Parsing error: integer expected
div 3 0:	 Divide by zero error
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:TestAll.little.txt
Reading file: TestAll.little.txt
double 5:	10
double 10:	20
triple 7:	21
triple 2:	6
square 2:	4
square 5:	25
cube 3:	27
cube 5:	125
sub 5 4:	1
sub 8 4:	4
add 2 3:	5
add 1 2 3:	6
add 1 2 3 4 5:	15
add 2 3 3:	8
add 4 5 6 7 8 9 10 2 3 4:	58
add 4 2 3 2 4 4 5:	24
div 10 5:	 Divide by zero error
div 8 2:	 Divide by zero error
div 16 4:	 Divide by zero error
mult 4 5:	20
mult 1 2 3:	6
mult 1 2 3 4 5:	120
mult 2 3 4 5:	120
mult 6 7 5 3 2 1 2 3 4 5:	151200
square 3:	9
double 6:	12
mult 5 2:	10
sub 9 3:	6
add 3 4 2:	9
sub 12 2:	10
cube 8:	512
add 5 6:	11
mult 8 2 1 2:	32
triple 4:	12
square 7:	49
add 3 2:	5
error:	Parsing error: no operands
null:	Parsing error: no operands
no_op:	Parsing error: no operands
add 4:	Parsing error: multiple operands expected
double 3 8:	Parsing error: unary operator requires one operand
sub 2:	Parsing error: binary operator requires two operands
sub 3 4 5:	Parsing error: binary operator requires two operands
sub:	Parsing error: no operands
mult 3:	Parsing error: multiple operands expected
hi:	Parsing error: no operands
triple:	Parsing error: no operands
cube:	Parsing error: no operands
cube 6 7:	Parsing error: unary operator requires one operand
square 4 5:	Parsing error: unary operator requires one operand
double trouble:	
Traceback (most recent call last):
  File "C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py", line 167, in <module>
    print line + ":\t", int(expression[1]) * 2
ValueError: invalid literal for int() with base 10: 'trouble'
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:return True

Traceback (most recent call last):
  File "C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py", line 118, in <module>
    filename = file(raw_input("Enter the filename:"), 'r')
IOError: [Errno 2] No such file or directory: 'return True'
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:TestAll.little.txt
Reading file: TestAll.little.txt
double 5:	10
double 10:	20
triple 7:	21
triple 2:	6
square 2:	4
square 5:	25
cube 3:	27
cube 5:	125
sub 5 4:	1
sub 8 4:	4
add 2 3:	5
add 1 2 3:	6
add 1 2 3 4 5:	15
add 2 3 3:	8
add 4 5 6 7 8 9 10 2 3 4:	58
add 4 2 3 2 4 4 5:	24
mult 4 5:	20
mult 1 2 3:	6
mult 1 2 3 4 5:	120
mult 2 3 4 5:	120
mult 6 7 5 3 2 1 2 3 4 5:	151200
square 3:	9
double 6:	12
mult 5 2:	10
sub 9 3:	6
add 3 4 2:	9
sub 12 2:	10
cube 8:	512
add 5 6:	11
mult 8 2 1 2:	32
triple 4:	12
square 7:	49
add 3 2:	5
error:	Parsing error: no operands
null:	Parsing error: no operands
no_op:	Parsing error: no operands
add 4:	Parsing error: multiple operands expected
double 3 8:	Parsing error: unary operator requires one operand
sub 2:	Parsing error: binary operator requires two operands
sub 3 4 5:	Parsing error: binary operator requires two operands
sub:	Parsing error: no operands
mult 3:	Parsing error: multiple operands expected
hi:	Parsing error: no operands
triple:	Parsing error: no operands
cube:	Parsing error: no operands
cube 6 7:	Parsing error: unary operator requires one operand
square 4 5:	Parsing error: unary operator requires one operand
double trouble:	
Traceback (most recent call last):
  File "C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py", line 167, in <module>
    print line + ":\t", int(expression[1]) * 2
ValueError: invalid literal for int() with base 10: 'trouble'
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:TestAll.little.txt
Reading file: TestAll.little.txt
double 5:	10
double 10:	20
triple 7:	21
triple 2:	6
square 2:	4
square 5:	25
cube 3:	27
cube 5:	125
sub 5 4:	1
sub 8 4:	4
add 2 3:	5
add 1 2 3:	6
add 1 2 3 4 5:	15
add 2 3 3:	8
add 4 5 6 7 8 9 10 2 3 4:	58
add 4 2 3 2 4 4 5:	24
div 10 5:	 Divide by zero error
div 8 2:	 Divide by zero error
div 16 4:	 Divide by zero error
mult 4 5:	20
mult 1 2 3:	6
mult 1 2 3 4 5:	120
mult 2 3 4 5:	120
mult 6 7 5 3 2 1 2 3 4 5:	151200
square 3:	9
double 6:	12
mult 5 2:	10
sub 9 3:	6
add 3 4 2:	9
sub 12 2:	10
cube 8:	512
add 5 6:	11
mult 8 2 1 2:	32
triple 4:	12
square 7:	49
add 3 2:	5
error:	Parsing error: no operands
null:	Parsing error: no operands
no_op:	Parsing error: no operands
add 4:	Parsing error: multiple operands expected
double 3 8:	Parsing error: unary operator requires one operand
sub 2:	Parsing error: binary operator requires two operands
sub 3 4 5:	Parsing error: binary operator requires two operands
sub:	Parsing error: no operands
mult 3:	Parsing error: multiple operands expected
hi:	Parsing error: no operands
triple:	Parsing error: no operands
cube:	Parsing error: no operands
cube 6 7:	Parsing error: unary operator requires one operand
square 4 5:	Parsing error: unary operator requires one operand
double trouble:	Parsing error: integer expected
add hello world:	Parsing error: integer expected
add 4 5 xyz:	Parsing error: integer expected
sub 3 abc:	Parsing error: integer expected
div 3 0:	 Divide by zero error
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:TestAll.little.txt
Reading file: TestAll.little.txt
double 5:	10
double 10:	20
triple 7:	21
triple 2:	6
square 2:	4
square 5:	25
cube 3:	27
cube 5:	125
sub 5 4:	1
sub 8 4:	4
add 2 3:	5
add 1 2 3:	6
add 1 2 3 4 5:	15
add 2 3 3:	8
add 4 5 6 7 8 9 10 2 3 4:	58
add 4 2 3 2 4 4 5:	24
div 10 5:	2
div 8 2:	4
div 16 4:	4
mult 4 5:	20
mult 1 2 3:	6
mult 1 2 3 4 5:	120
mult 2 3 4 5:	120
mult 6 7 5 3 2 1 2 3 4 5:	151200
square 3:	9
double 6:	12
mult 5 2:	10
sub 9 3:	6
add 3 4 2:	9
sub 12 2:	10
cube 8:	512
add 5 6:	11
mult 8 2 1 2:	32
triple 4:	12
square 7:	49
add 3 2:	5
error:	Parsing error: no operands
null:	Parsing error: no operands
no_op:	Parsing error: no operands
add 4:	Parsing error: multiple operands expected
double 3 8:	Parsing error: unary operator requires one operand
sub 2:	Parsing error: binary operator requires two operands
sub 3 4 5:	Parsing error: binary operator requires two operands
sub:	Parsing error: no operands
mult 3:	Parsing error: multiple operands expected
hi:	Parsing error: no operands
triple:	Parsing error: no operands
cube:	Parsing error: no operands
cube 6 7:	Parsing error: unary operator requires one operand
square 4 5:	Parsing error: unary operator requires one operand
double trouble:	Parsing error: integer expected
add hello world:	Parsing error: integer expected
add 4 5 xyz:	Parsing error: integer expected
sub 3 abc:	Parsing error: integer expected
div 3 0:	
Traceback (most recent call last):
  File "C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py", line 192, in <module>
    print line + ":\t", (int(expression[1]) / int(expression[2]))
ZeroDivisionError: integer division or modulo by zero
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:TestAll.little.txt
Reading file: TestAll.little.txt
double 5:	10
double 10:	20
triple 7:	21
triple 2:	6
square 2:	4
square 5:	25
cube 3:	27
cube 5:	125
sub 5 4:	1
sub 8 4:	4
add 2 3:	5
add 1 2 3:	6
add 1 2 3 4 5:	15
add 2 3 3:	8
add 4 5 6 7 8 9 10 2 3 4:	58
add 4 2 3 2 4 4 5:	24
div 10 5:	 Divide by zero error
div 8 2:	 Divide by zero error
div 16 4:	 Divide by zero error
mult 4 5:	20
mult 1 2 3:	6
mult 1 2 3 4 5:	120
mult 2 3 4 5:	120
mult 6 7 5 3 2 1 2 3 4 5:	151200
square 3:	9
double 6:	12
mult 5 2:	10
sub 9 3:	6
add 3 4 2:	9
sub 12 2:	10
cube 8:	512
add 5 6:	11
mult 8 2 1 2:	32
triple 4:	12
square 7:	49
add 3 2:	5
error:	Parsing error: no operands
null:	Parsing error: no operands
no_op:	Parsing error: no operands
add 4:	Parsing error: multiple operands expected
double 3 8:	Parsing error: unary operator requires one operand
sub 2:	Parsing error: binary operator requires two operands
sub 3 4 5:	Parsing error: binary operator requires two operands
sub:	Parsing error: no operands
mult 3:	Parsing error: multiple operands expected
hi:	Parsing error: no operands
triple:	Parsing error: no operands
cube:	Parsing error: no operands
cube 6 7:	Parsing error: unary operator requires one operand
square 4 5:	Parsing error: unary operator requires one operand
double trouble:	Parsing error: integer expected
add hello world:	Parsing error: integer expected
add 4 5 xyz:	Parsing error: integer expected
sub 3 abc:	Parsing error: integer expected
div 3 0:	 Divide by zero error
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:TestAll.little.txt
Reading file: TestAll.little.txt
double 5:	10
double 10:	20
triple 7:	21
triple 2:	6
square 2:	4
square 5:	25
cube 3:	27
cube 5:	125
sub 5 4:	1
sub 8 4:	4
add 2 3:	5
add 1 2 3:	6
add 1 2 3 4 5:	15
add 2 3 3:	8
add 4 5 6 7 8 9 10 2 3 4:	58
add 4 2 3 2 4 4 5:	24
div 10 5:	 Divide by zero error
div 8 2:	 Divide by zero error
div 16 4:	 Divide by zero error
mult 4 5:	20
mult 1 2 3:	6
mult 1 2 3 4 5:	120
mult 2 3 4 5:	120
mult 6 7 5 3 2 1 2 3 4 5:	151200
square 3:	9
double 6:	12
mult 5 2:	10
sub 9 3:	6
add 3 4 2:	9
sub 12 2:	10
cube 8:	512
add 5 6:	11
mult 8 2 1 2:	32
triple 4:	12
square 7:	49
add 3 2:	5
error:	Parsing error: no operands
null:	Parsing error: no operands
no_op:	Parsing error: no operands
add 4:	Parsing error: multiple operands expected
double 3 8:	Parsing error: unary operator requires one operand
sub 2:	Parsing error: binary operator requires two operands
sub 3 4 5:	Parsing error: binary operator requires two operands
sub:	Parsing error: no operands
mult 3:	Parsing error: multiple operands expected
hi:	Parsing error: no operands
triple:	Parsing error: no operands
cube:	Parsing error: no operands
cube 6 7:	Parsing error: unary operator requires one operand
square 4 5:	Parsing error: unary operator requires one operand
double trouble:	Parsing error: integer expected
add hello world:	Parsing error: integer expected
add 4 5 xyz:	Parsing error: integer expected
sub 3 abc:	Parsing error: integer expected
div 3 0:	 Divide by zero error
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:TestAll.little.txt
Reading file: TestAll.little.txt
double 5:	10
double 10:	20
triple 7:	21
triple 2:	6
square 2:	4
square 5:	25
cube 3:	27
cube 5:	125
sub 5 4:	1
sub 8 4:	4
add 2 3:	5
add 1 2 3:	6
add 1 2 3 4 5:	15
add 2 3 3:	8
add 4 5 6 7 8 9 10 2 3 4:	58
add 4 2 3 2 4 4 5:	24
div 10 5:	 Divide by zero error
div 8 2:	 Divide by zero error
div 16 4:	 Divide by zero error
mult 4 5:	20
mult 1 2 3:	6
mult 1 2 3 4 5:	120
mult 2 3 4 5:	120
mult 6 7 5 3 2 1 2 3 4 5:	151200
square 3:	9
double 6:	12
mult 5 2:	10
sub 9 3:	6
add 3 4 2:	9
sub 12 2:	10
cube 8:	512
add 5 6:	11
mult 8 2 1 2:	32
triple 4:	12
square 7:	49
add 3 2:	5
error:	Parsing error: no operands
null:	Parsing error: no operands
no_op:	Parsing error: no operands
add 4:	Parsing error: multiple operands expected
double 3 8:	Parsing error: unary operator requires one operand
sub 2:	Parsing error: binary operator requires two operands
sub 3 4 5:	Parsing error: binary operator requires two operands
sub:	Parsing error: no operands
mult 3:	Parsing error: multiple operands expected
hi:	Parsing error: no operands
triple:	Parsing error: no operands
cube:	Parsing error: no operands
cube 6 7:	Parsing error: unary operator requires one operand
square 4 5:	Parsing error: unary operator requires one operand
double trouble:	Parsing error: integer expected
add hello world:	Parsing error: integer expected
add 4 5 xyz:	Parsing error: integer expected
sub 3 abc:	Parsing error: integer expected
div 3 0:	 Divide by zero error
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:TestAll.little.txt
Reading file: TestAll.little.txt
double 5:	10
double 10:	20
triple 7:	21
triple 2:	6
square 2:	4
square 5:	25
cube 3:	27
cube 5:	125
sub 5 4:	1
sub 8 4:	4
add 2 3:	5
add 1 2 3:	6
add 1 2 3 4 5:	15
add 2 3 3:	8
add 4 5 6 7 8 9 10 2 3 4:	58
add 4 2 3 2 4 4 5:	24
mult 4 5:	20
mult 1 2 3:	6
mult 1 2 3 4 5:	120
mult 2 3 4 5:	120
mult 6 7 5 3 2 1 2 3 4 5:	151200
square 3:	9
double 6:	12
mult 5 2:	10
sub 9 3:	6
add 3 4 2:	9
sub 12 2:	10
cube 8:	512
add 5 6:	11
mult 8 2 1 2:	32
triple 4:	12
square 7:	49
add 3 2:	5
error:	Parsing error: no operands
null:	Parsing error: no operands
no_op:	Parsing error: no operands
add 4:	Parsing error: multiple operands expected
double 3 8:	Parsing error: unary operator requires one operand
sub 2:	Parsing error: binary operator requires two operands
sub 3 4 5:	Parsing error: binary operator requires two operands
sub:	Parsing error: no operands
mult 3:	Parsing error: multiple operands expected
hi:	Parsing error: no operands
triple:	Parsing error: no operands
cube:	Parsing error: no operands
cube 6 7:	Parsing error: unary operator requires one operand
square 4 5:	Parsing error: unary operator requires one operand
double trouble:	Parsing error: integer expected
add hello world:	Parsing error: integer expected
add 4 5 xyz:	Parsing error: integer expected
sub 3 abc:	Parsing error: integer expected
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:

Traceback (most recent call last):
  File "C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py", line 115, in <module>
    filename = file(raw_input("Enter the filename:"), 'r')
  File "C:\Python27\lib\idlelib\PyShell.py", line 1398, in readline
    line = self._line_buffer or self.shell.readline()
KeyboardInterrupt
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:numOperands == 0

Traceback (most recent call last):
  File "C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py", line 115, in <module>
    filename = file(raw_input("Enter the filename:"), 'r')
IOError: [Errno 2] No such file or directory: 'numOperands == 0'
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:TestAll.little.txt
Reading file: TestAll.little.txt
double 5:	10
double 5:	 Divide by zero error
double 10:	20
double 10:	 Divide by zero error
triple 7:	21
triple 7:	 Divide by zero error
triple 2:	6
triple 2:	 Divide by zero error
square 2:	4
square 2:	 Divide by zero error
square 5:	25
square 5:	 Divide by zero error
cube 3:	27
cube 3:	 Divide by zero error
cube 5:	125
cube 5:	 Divide by zero error
sub 5 4:	1
sub 5 4:	 Divide by zero error
sub 8 4:	4
sub 8 4:	 Divide by zero error
add 2 3:	5
add 2 3:	 Divide by zero error
add 1 2 3:	6
add 1 2 3:	 Divide by zero error
add 1 2 3 4 5:	15
add 1 2 3 4 5:	 Divide by zero error
add 2 3 3:	8
add 2 3 3:	 Divide by zero error
add 4 5 6 7 8 9 10 2 3 4:	58
add 4 5 6 7 8 9 10 2 3 4:	 Divide by zero error
add 4 2 3 2 4 4 5:	24
add 4 2 3 2 4 4 5:	 Divide by zero error
div 10 5:	 Divide by zero error
div 8 2:	 Divide by zero error
div 16 4:	 Divide by zero error
mult 4 5:	 Divide by zero error
mult 4 5:	20
mult 1 2 3:	 Divide by zero error
mult 1 2 3:	6
mult 1 2 3 4 5:	 Divide by zero error
mult 1 2 3 4 5:	120
mult 2 3 4 5:	 Divide by zero error
mult 2 3 4 5:	120
mult 6 7 5 3 2 1 2 3 4 5:	 Divide by zero error
mult 6 7 5 3 2 1 2 3 4 5:	151200
square 3:	9
square 3:	 Divide by zero error
double 6:	12
double 6:	 Divide by zero error
mult 5 2:	 Divide by zero error
mult 5 2:	10
sub 9 3:	6
sub 9 3:	 Divide by zero error
add 3 4 2:	9
add 3 4 2:	 Divide by zero error
sub 12 2:	10
sub 12 2:	 Divide by zero error
cube 8:	512
cube 8:	 Divide by zero error
add 5 6:	11
add 5 6:	 Divide by zero error
mult 8 2 1 2:	 Divide by zero error
mult 8 2 1 2:	32
triple 4:	12
triple 4:	 Divide by zero error
square 7:	49
square 7:	 Divide by zero error
add 3 2:	5
add 3 2:	 Divide by zero error
error:	Parsing error: no operands
null:	Parsing error: no operands
no_op:	Parsing error: no operands
add 4:	Parsing error: multiple operands expected
double 3 8:	Parsing error: unary operator requires one operand
sub 2:	Parsing error: binary operator requires two operands
sub 3 4 5:	Parsing error: binary operator requires two operands
sub:	Parsing error: no operands
mult 3:	Parsing error: multiple operands expected
hi:	Parsing error: no operands
triple:	Parsing error: no operands
cube:	Parsing error: no operands
cube 6 7:	Parsing error: unary operator requires one operand
halve 8:	 Divide by zero error
square 4 5:	Parsing error: unary operator requires one operand
double trouble:	Parsing error: integer expected
add hello world:	Parsing error: integer expected
add 4 5 xyz:	Parsing error: integer expected
sub 3 abc:	Parsing error: integer expected
div 3 0:	 Divide by zero error
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:TestAll.little.txt
Reading file: TestAll.little.txt
double 5:	10
double 5:	 Divide by zero error
double 10:	20
double 10:	 Divide by zero error
triple 7:	21
triple 7:	 Divide by zero error
triple 2:	6
triple 2:	 Divide by zero error
square 2:	4
square 2:	 Divide by zero error
square 5:	25
square 5:	 Divide by zero error
cube 3:	27
cube 3:	 Divide by zero error
cube 5:	125
cube 5:	 Divide by zero error
sub 5 4:	1
sub 5 4:	 Divide by zero error
sub 8 4:	4
sub 8 4:	 Divide by zero error
add 2 3:	5
add 2 3:	 Divide by zero error
add 1 2 3:	6
add 1 2 3:	 Divide by zero error
add 1 2 3 4 5:	15
add 1 2 3 4 5:	 Divide by zero error
add 2 3 3:	8
add 2 3 3:	 Divide by zero error
add 4 5 6 7 8 9 10 2 3 4:	58
add 4 5 6 7 8 9 10 2 3 4:	 Divide by zero error
add 4 2 3 2 4 4 5:	24
add 4 2 3 2 4 4 5:	 Divide by zero error
div 10 5:	 Divide by zero error
div 8 2:	 Divide by zero error
div 16 4:	 Divide by zero error
mult 4 5:	 Divide by zero error
mult 4 5:	20
mult 1 2 3:	 Divide by zero error
mult 1 2 3:	6
mult 1 2 3 4 5:	 Divide by zero error
mult 1 2 3 4 5:	120
mult 2 3 4 5:	 Divide by zero error
mult 2 3 4 5:	120
mult 6 7 5 3 2 1 2 3 4 5:	 Divide by zero error
mult 6 7 5 3 2 1 2 3 4 5:	151200
square 3:	9
square 3:	 Divide by zero error
double 6:	12
double 6:	 Divide by zero error
mult 5 2:	 Divide by zero error
mult 5 2:	10
sub 9 3:	6
sub 9 3:	 Divide by zero error
add 3 4 2:	9
add 3 4 2:	 Divide by zero error
sub 12 2:	10
sub 12 2:	 Divide by zero error
cube 8:	512
cube 8:	 Divide by zero error
add 5 6:	11
add 5 6:	 Divide by zero error
mult 8 2 1 2:	 Divide by zero error
mult 8 2 1 2:	32
triple 4:	12
triple 4:	 Divide by zero error
square 7:	49
square 7:	 Divide by zero error
add 3 2:	5
add 3 2:	 Divide by zero error
error:	Parsing error: no operands
null:	Parsing error: no operands
no_op:	Parsing error: no operands
add 4:	Parsing error: multiple operands expected
double 3 8:	Parsing error: unary operator requires one operand
sub 2:	Parsing error: binary operator requires two operands
sub 3 4 5:	Parsing error: binary operator requires two operands
sub:	Parsing error: no operands
mult 3:	Parsing error: multiple operands expected
hi:	Parsing error: no operands
triple:	Parsing error: no operands
cube:	Parsing error: no operands
cube 6 7:	Parsing error: unary operator requires one operand
halve 8:	 Divide by zero error
square 4 5:	Parsing error: unary operator requires one operand
double trouble:	Parsing error: integer expected
add hello world:	Parsing error: integer expected
add 4 5 xyz:	Parsing error: integer expected
sub 3 abc:	Parsing error: integer expected
div 3 0:	 Divide by zero error
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:TestAll.little.txt
Reading file: TestAll.little.txt
double 5:	10
double 10:	20
triple 7:	21
triple 2:	6
square 2:	4
square 5:	25
cube 3:	27
cube 5:	125
sub 5 4:	1
sub 8 4:	4
add 2 3:	5
add 1 2 3:	6
add 1 2 3 4 5:	15
add 2 3 3:	8
add 4 5 6 7 8 9 10 2 3 4:	58
add 4 2 3 2 4 4 5:	24
mult 4 5:	20
mult 1 2 3:	6
mult 1 2 3 4 5:	120
mult 2 3 4 5:	120
mult 6 7 5 3 2 1 2 3 4 5:	151200
square 3:	9
double 6:	12
mult 5 2:	10
sub 9 3:	6
add 3 4 2:	9
sub 12 2:	10
cube 8:	512
add 5 6:	11
mult 8 2 1 2:	32
triple 4:	12
square 7:	49
add 3 2:	5
error:	Parsing error: no operands
null:	Parsing error: no operands
no_op:	Parsing error: no operands
add 4:	Parsing error: multiple operands expected
double 3 8:	Parsing error: unary operator requires one operand
sub 2:	Parsing error: binary operator requires two operands
sub 3 4 5:	Parsing error: binary operator requires two operands
sub:	Parsing error: no operands
mult 3:	Parsing error: multiple operands expected
hi:	Parsing error: no operands
triple:	Parsing error: no operands
cube:	Parsing error: no operands
cube 6 7:	Parsing error: unary operator requires one operand
square 4 5:	Parsing error: unary operator requires one operand
double trouble:	Parsing error: integer expected
add hello world:	Parsing error: integer expected
add 4 5 xyz:	Parsing error: integer expected
sub 3 abc:	Parsing error: integer expected
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:TestAll.little.txt
Reading file: TestAll.little.txt
double 5:	10
double 10:	20
triple 7:	21
triple 2:	6
square 2:	4
square 5:	25
cube 3:	27
cube 5:	125
sub 5 4:	1
sub 8 4:	4
add 2 3:	5
add 1 2 3:	6
add 1 2 3 4 5:	15
add 2 3 3:	8
add 4 5 6 7 8 9 10 2 3 4:	58
add 4 2 3 2 4 4 5:	24
mult 4 5:	20
mult 1 2 3:	6
mult 1 2 3 4 5:	120
mult 2 3 4 5:	120
mult 6 7 5 3 2 1 2 3 4 5:	151200
square 3:	9
double 6:	12
mult 5 2:	10
sub 9 3:	6
add 3 4 2:	9
sub 12 2:	10
cube 8:	512
add 5 6:	11
mult 8 2 1 2:	32
triple 4:	12
square 7:	49
add 3 2:	5
error:	Parsing error: no operands
null:	Parsing error: no operands
no_op:	Parsing error: no operands
add 4:	Parsing error: multiple operands expected
double 3 8:	Parsing error: unary operator requires one operand
sub 2:	Parsing error: binary operator requires two operands
sub 3 4 5:	Parsing error: binary operator requires two operands
sub:	Parsing error: no operands
mult 3:	Parsing error: multiple operands expected
hi:	Parsing error: no operands
triple:	Parsing error: no operands
cube:	Parsing error: no operands
cube 6 7:	Parsing error: unary operator requires one operand
square 4 5:	Parsing error: unary operator requires one operand
double trouble:	Parsing error: integer expected
add hello world:	Parsing error: integer expected
add 4 5 xyz:	Parsing error: integer expected
sub 3 abc:	Parsing error: integer expected
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:TestAll.little.txt
Reading file: TestAll.little.txt
double 5:	10
double 10:	20
triple 7:	21
triple 2:	6
square 2:	4
square 5:	25
cube 3:	27
cube 5:	125
sub 5 4:	1
sub 8 4:	4
add 2 3:	5
add 1 2 3:	6
add 1 2 3 4 5:	15
add 2 3 3:	8
add 4 5 6 7 8 9 10 2 3 4:	58
add 4 2 3 2 4 4 5:	24
div 10 5:	2
div 8 2:	4
div 16 4:	4
mult 4 5:	20
mult 1 2 3:	6
mult 1 2 3 4 5:	120
mult 2 3 4 5:	120
mult 6 7 5 3 2 1 2 3 4 5:	151200
square 3:	9
double 6:	12
mult 5 2:	10
sub 9 3:	6
add 3 4 2:	9
sub 12 2:	10
cube 8:	512
add 5 6:	11
mult 8 2 1 2:	32
triple 4:	12
square 7:	49
add 3 2:	5
error:	Parsing error: no operands
null:	Parsing error: no operands
no_op:	Parsing error: no operands
add 4:	Parsing error: multiple operands expected
double 3 8:	Parsing error: unary operator requires one operand
sub 2:	Parsing error: binary operator requires two operands
sub 3 4 5:	Parsing error: binary operator requires two operands
sub:	Parsing error: no operands
mult 3:	Parsing error: multiple operands expected
hi:	Parsing error: no operands
triple:	Parsing error: no operands
cube:	Parsing error: no operands
cube 6 7:	Parsing error: unary operator requires one operand
square 4 5:	Parsing error: unary operator requires one operand
double trouble:	Parsing error: integer expected
add hello world:	Parsing error: integer expected
add 4 5 xyz:	Parsing error: integer expected
sub 3 abc:	Parsing error: integer expected
div 3 0:	
Traceback (most recent call last):
  File "C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py", line 190, in <module>
    print line + ":\t", (int(expression[1]) / int(expression[2]))
ZeroDivisionError: integer division or modulo by zero
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:TestAll.little.txt
Reading file: TestAll.little.txt
double 5:	10
double 10:	20
triple 7:	21
triple 2:	6
square 2:	4
square 5:	25
cube 3:	27
cube 5:	125
sub 5 4:	1
sub 8 4:	4
add 2 3:	5
add 1 2 3:	6
add 1 2 3 4 5:	15
add 2 3 3:	8
add 4 5 6 7 8 9 10 2 3 4:	58
add 4 2 3 2 4 4 5:	24
div 10 5:	2
div 8 2:	4
div 16 4:	4
mult 4 5:	20
mult 1 2 3:	6
mult 1 2 3 4 5:	120
mult 2 3 4 5:	120
mult 6 7 5 3 2 1 2 3 4 5:	151200
square 3:	9
double 6:	12
mult 5 2:	10
sub 9 3:	6
add 3 4 2:	9
sub 12 2:	10
cube 8:	512
add 5 6:	11
mult 8 2 1 2:	32
triple 4:	12
square 7:	49
add 3 2:	5
error:	Parsing error: no operands
null:	Parsing error: no operands
no_op:	Parsing error: no operands
add 4:	Parsing error: multiple operands expected
double 3 8:	Parsing error: unary operator requires one operand
sub 2:	Parsing error: binary operator requires two operands
sub 3 4 5:	Parsing error: binary operator requires two operands
sub:	Parsing error: no operands
mult 3:	Parsing error: multiple operands expected
hi:	Parsing error: no operands
triple:	Parsing error: no operands
cube:	Parsing error: no operands
cube 6 7:	Parsing error: unary operator requires one operand
square 4 5:	Parsing error: unary operator requires one operand
double trouble:	Parsing error: integer expected
add hello world:	Parsing error: integer expected
add 4 5 xyz:	Parsing error: integer expected
sub 3 abc:	Parsing error: integer expected
div 3 0:	
Traceback (most recent call last):
  File "C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py", line 190, in <module>
    print line + ":\t", (int(expression[1]) / int(expression[2]))
ZeroDivisionError: integer division or modulo by zero
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:int(expression[2])

Traceback (most recent call last):
  File "C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py", line 115, in <module>
    filename = file(raw_input("Enter the filename:"), 'r')
IOError: [Errno 2] No such file or directory: 'int(expression[2])'
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:int(expression[2])

Traceback (most recent call last):
  File "C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py", line 115, in <module>
    filename = file(raw_input("Enter the filename:"), 'r')
IOError: [Errno 2] No such file or directory: 'int(expression[2])'
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:TestAll.little.txt
Reading file: TestAll.little.txt
double 5:	10

Traceback (most recent call last):
  File "C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py", line 191, in <module>
    elif(int(expression[2]) == 0):
IndexError: list index out of range
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:TestAll.little.txt
Reading file: TestAll.little.txt
double 5:	10
double 10:	20
triple 7:	21
triple 2:	6
square 2:	4
square 5:	25
cube 3:	27
cube 5:	125
sub 5 4:	1
sub 8 4:	4
add 2 3:	5
add 1 2 3:	6
add 1 2 3 4 5:	15
add 2 3 3:	8
add 4 5 6 7 8 9 10 2 3 4:	58
add 4 2 3 2 4 4 5:	24
div 10 5:	2
div 8 2:	4
div 16 4:	4
mult 4 5:	20
mult 1 2 3:	6
mult 1 2 3 4 5:	120
mult 2 3 4 5:	120
mult 6 7 5 3 2 1 2 3 4 5:	151200
square 3:	9
double 6:	12
mult 5 2:	10
sub 9 3:	6
add 3 4 2:	9
sub 12 2:	10
cube 8:	512
add 5 6:	11
mult 8 2 1 2:	32
triple 4:	12
square 7:	49
add 3 2:	5
error:	Parsing error: no operands
null:	Parsing error: no operands
no_op:	Parsing error: no operands
add 4:	Parsing error: multiple operands expected
double 3 8:	Parsing error: unary operator requires one operand
sub 2:	Parsing error: binary operator requires two operands
sub 3 4 5:	Parsing error: binary operator requires two operands
sub:	Parsing error: no operands
mult 3:	Parsing error: multiple operands expected
hi:	Parsing error: no operands
triple:	Parsing error: no operands
cube:	Parsing error: no operands
cube 6 7:	Parsing error: unary operator requires one operand
square 4 5:	Parsing error: unary operator requires one operand
double trouble:	Parsing error: integer expected
add hello world:	Parsing error: integer expected
add 4 5 xyz:	Parsing error: integer expected
sub 3 abc:	Parsing error: integer expected
div 3 0:	
Traceback (most recent call last):
  File "C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py", line 190, in <module>
    print line + ":\t", (int(expression[1]) / int(expression[2]))
ZeroDivisionError: integer division or modulo by zero
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:TestAll.little.txt
Reading file: TestAll.little.txt
double 5:	10
double 10:	20
triple 7:	21
triple 2:	6
square 2:	4
square 5:	25
cube 3:	27
cube 5:	125
sub 5 4:	1
sub 8 4:	4
add 2 3:	5
add 1 2 3:	6
add 1 2 3 4 5:	15
add 2 3 3:	8
add 4 5 6 7 8 9 10 2 3 4:	58
add 4 2 3 2 4 4 5:	24
div 10 5:	 Divide by zero error
div 8 2:	 Divide by zero error
div 16 4:	 Divide by zero error
mult 4 5:	20
mult 1 2 3:	6
mult 1 2 3 4 5:	120
mult 2 3 4 5:	120
mult 6 7 5 3 2 1 2 3 4 5:	151200
square 3:	9
double 6:	12
mult 5 2:	10
sub 9 3:	6
add 3 4 2:	9
sub 12 2:	10
cube 8:	512
add 5 6:	11
mult 8 2 1 2:	32
triple 4:	12
square 7:	49
add 3 2:	5
error:	Parsing error: no operands
null:	Parsing error: no operands
no_op:	Parsing error: no operands
add 4:	Parsing error: multiple operands expected
double 3 8:	Parsing error: unary operator requires one operand
sub 2:	Parsing error: binary operator requires two operands
sub 3 4 5:	Parsing error: binary operator requires two operands
sub:	Parsing error: no operands
mult 3:	Parsing error: multiple operands expected
hi:	Parsing error: no operands
triple:	Parsing error: no operands
cube:	Parsing error: no operands
cube 6 7:	Parsing error: unary operator requires one operand
square 4 5:	Parsing error: unary operator requires one operand
double trouble:	Parsing error: integer expected
add hello world:	Parsing error: integer expected
add 4 5 xyz:	Parsing error: integer expected
sub 3 abc:	Parsing error: integer expected
div 3 0:	 Divide by zero error
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:TestAll.little.txt
Reading file: TestAll.little.txt
double 5:	10
double 10:	20
triple 7:	21
triple 2:	6
square 2:	4
square 5:	25
cube 3:	27
cube 5:	125
sub 5 4:	1
sub 8 4:	4
add 2 3:	5
add 1 2 3:	6
add 1 2 3 4 5:	15
add 2 3 3:	8
add 4 5 6 7 8 9 10 2 3 4:	58
add 4 2 3 2 4 4 5:	24
mult 4 5:	20
mult 1 2 3:	6
mult 1 2 3 4 5:	120
mult 2 3 4 5:	120
mult 6 7 5 3 2 1 2 3 4 5:	151200
square 3:	9
double 6:	12
mult 5 2:	10
sub 9 3:	6
add 3 4 2:	9
sub 12 2:	10
cube 8:	512
add 5 6:	11
mult 8 2 1 2:	32
triple 4:	12
square 7:	49
add 3 2:	5
error:	Parsing error: no operands
null:	Parsing error: no operands
no_op:	Parsing error: no operands
add 4:	Parsing error: multiple operands expected
double 3 8:	Parsing error: unary operator requires one operand
sub 2:	Parsing error: binary operator requires two operands
sub 3 4 5:	Parsing error: binary operator requires two operands
sub:	Parsing error: no operands
mult 3:	Parsing error: multiple operands expected
hi:	Parsing error: no operands
triple:	Parsing error: no operands
cube:	Parsing error: no operands
cube 6 7:	Parsing error: unary operator requires one operand
square 4 5:	Parsing error: unary operator requires one operand
double trouble:	Parsing error: integer expected
add hello world:	Parsing error: integer expected
add 4 5 xyz:	Parsing error: integer expected
sub 3 abc:	Parsing error: integer expected
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:TestAll.little.txt
Reading file: TestAll.little.txt
double 5:	10
double 10:	20
triple 7:	21
triple 2:	6
square 2:	4
square 5:	25
cube 3:	27
cube 5:	125
sub 5 4:	1
sub 8 4:	4
add 2 3:	5
add 1 2 3:	6
add 1 2 3 4 5:	15
add 2 3 3:	8
add 4 5 6 7 8 9 10 2 3 4:	58
add 4 2 3 2 4 4 5:	24
div 10 5:	 Divide by zero error
div 8 2:	 Divide by zero error
div 16 4:	 Divide by zero error
mult 4 5:	20
mult 1 2 3:	6
mult 1 2 3 4 5:	120
mult 2 3 4 5:	120
mult 6 7 5 3 2 1 2 3 4 5:	151200
square 3:	9
double 6:	12
mult 5 2:	10
sub 9 3:	6
add 3 4 2:	9
sub 12 2:	10
cube 8:	512
add 5 6:	11
mult 8 2 1 2:	32
triple 4:	12
square 7:	49
add 3 2:	5
error:	Parsing error: no operands
null:	Parsing error: no operands
no_op:	Parsing error: no operands
add 4:	Parsing error: multiple operands expected
double 3 8:	Parsing error: unary operator requires one operand
sub 2:	Parsing error: binary operator requires two operands
sub 3 4 5:	Parsing error: binary operator requires two operands
sub:	Parsing error: no operands
mult 3:	Parsing error: multiple operands expected
hi:	Parsing error: no operands
triple:	Parsing error: no operands
cube:	Parsing error: no operands
cube 6 7:	Parsing error: unary operator requires one operand
square 4 5:	Parsing error: unary operator requires one operand
double trouble:	Parsing error: integer expected
add hello world:	Parsing error: integer expected
add 4 5 xyz:	Parsing error: integer expected
sub 3 abc:	Parsing error: integer expected
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:TestAll.little.txt
Reading file: TestAll.little.txt
double 5:	10
double 10:	20
triple 7:	21
triple 2:	6
square 2:	4
square 5:	25
cube 3:	27
cube 5:	125
sub 5 4:	1
sub 8 4:	4
add 2 3:	5
add 1 2 3:	6
add 1 2 3 4 5:	15
add 2 3 3:	8
add 4 5 6 7 8 9 10 2 3 4:	58
add 4 2 3 2 4 4 5:	24
mult 4 5:	20
mult 1 2 3:	6
mult 1 2 3 4 5:	120
mult 2 3 4 5:	120
mult 6 7 5 3 2 1 2 3 4 5:	151200
square 3:	9
double 6:	12
mult 5 2:	10
sub 9 3:	6
add 3 4 2:	9
sub 12 2:	10
cube 8:	512
add 5 6:	11
mult 8 2 1 2:	32
triple 4:	12
square 7:	49
add 3 2:	5
error:	Parsing error: no operands
null:	Parsing error: no operands
no_op:	Parsing error: no operands
add 4:	Parsing error: multiple operands expected
double 3 8:	Parsing error: unary operator requires one operand
sub 2:	Parsing error: binary operator requires two operands
sub 3 4 5:	Parsing error: binary operator requires two operands
sub:	Parsing error: no operands
mult 3:	Parsing error: multiple operands expected
hi:	Parsing error: no operands
triple:	Parsing error: no operands
cube:	Parsing error: no operands
cube 6 7:	Parsing error: unary operator requires one operand
square 4 5:	Parsing error: unary operator requires one operand
double trouble:	Parsing error: integer expected
add hello world:	Parsing error: integer expected
add 4 5 xyz:	Parsing error: integer expected
sub 3 abc:	Parsing error: integer expected
div 3 0:	 Divide by zero error
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:TestAll.little.txt
Reading file: TestAll.little.txt
double 5:	10
double 10:	20
triple 7:	21
triple 2:	6
square 2:	4
square 5:	25
cube 3:	27
cube 5:	125
sub 5 4:	1
sub 8 4:	4
add 2 3:	5
add 1 2 3:	6
add 1 2 3 4 5:	15
add 2 3 3:	8
add 4 5 6 7 8 9 10 2 3 4:	58
add 4 2 3 2 4 4 5:	24
div 10 5:	2
div 8 2:	4
div 16 4:	4
mult 4 5:	20
mult 1 2 3:	6
mult 1 2 3 4 5:	120
mult 2 3 4 5:	120
mult 6 7 5 3 2 1 2 3 4 5:	151200
square 3:	9
double 6:	12
mult 5 2:	10
sub 9 3:	6
add 3 4 2:	9
sub 12 2:	10
cube 8:	512
add 5 6:	11
mult 8 2 1 2:	32
triple 4:	12
square 7:	49
add 3 2:	5
error:	Parsing error: no operands
null:	Parsing error: no operands
no_op:	Parsing error: no operands
add 4:	Parsing error: multiple operands expected
double 3 8:	Parsing error: unary operator requires one operand
sub 2:	Parsing error: binary operator requires two operands
sub 3 4 5:	Parsing error: binary operator requires two operands
sub:	Parsing error: no operands
mult 3:	Parsing error: multiple operands expected
hi:	Parsing error: no operands
triple:	Parsing error: no operands
cube:	Parsing error: no operands
cube 6 7:	Parsing error: unary operator requires one operand
square 4 5:	Parsing error: unary operator requires one operand
double trouble:	Parsing error: integer expected
add hello world:	Parsing error: integer expected
add 4 5 xyz:	Parsing error: integer expected
sub 3 abc:	Parsing error: integer expected
>>> 
 RESTART: C:\Users\delga\OneDrive\Desktop\Spring 2018\Computer science\Lecture\CSC 160\Final project\littleinterpreter-outline.py 
Enter the filename:TestAll.little.txt
Reading file: TestAll.little.txt
double 5:	10
double 10:	20
triple 7:	21
triple 2:	6
square 2:	4
square 5:	25
cube 3:	27
cube 5:	125
sub 5 4:	1
sub 8 4:	4
add 2 3:	5
add 1 2 3:	6
add 1 2 3 4 5:	15
add 2 3 3:	8
add 4 5 6 7 8 9 10 2 3 4:	58
add 4 2 3 2 4 4 5:	24
div 10 5:	2
div 8 2:	4
div 16 4:	4
mult 4 5:	20
mult 1 2 3:	6
mult 1 2 3 4 5:	120
mult 2 3 4 5:	120
mult 6 7 5 3 2 1 2 3 4 5:	151200
square 3:	9
double 6:	12
mult 5 2:	10
sub 9 3:	6
add 3 4 2:	9
sub 12 2:	10
cube 8:	512
add 5 6:	11
mult 8 2 1 2:	32
triple 4:	12
square 7:	49
add 3 2:	5
error:	Parsing error: no operands
null:	Parsing error: no operands
no_op:	Parsing error: no operands
add 4:	Parsing error: multiple operands expected
double 3 8:	Parsing error: unary operator requires one operand
sub 2:	Parsing error: binary operator requires two operands
sub 3 4 5:	Parsing error: binary operator requires two operands
sub:	Parsing error: no operands
mult 3:	Parsing error: multiple operands expected
hi:	Parsing error: no operands
triple:	Parsing error: no operands
cube:	Parsing error: no operands
cube 6 7:	Parsing error: unary operator requires one operand
square 4 5:	Parsing error: unary operator requires one operand
double trouble:	Parsing error: integer expected
add hello world:	Parsing error: integer expected
add 4 5 xyz:	Parsing error: integer expected
sub 3 abc:	Parsing error: integer expected
div 3 0:	 Divide by zero error
>>> 
