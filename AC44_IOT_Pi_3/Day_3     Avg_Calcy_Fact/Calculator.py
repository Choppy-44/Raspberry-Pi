print 'Welcome to the Calculator!'
print 'Select the Operation to be performed'
print "1.Addition \n2.Subtraction \n3.Multiplication \n4.Division"

opcode = input ('Opcode =')

if opcode == 1:
    a = input ('Enter first number')
    b = input ('Enter second number')
    print "The Addition is ",a+b

if opcode == 2:
    c = input ('Enter first number')
    d = input ('Enter second number')
    print "The Subtraction is ",c-d

if opcode == 3:
    e = input ('Enter first number')
    f = input ('Enter second number')
    print "The Multiplication is ",e*f

if opcode == 4:
    g = input ('Enter the Dividend')
    h = input ('Enter the Divisor')
    print "The Quotient is ",g/h
    print "The Remainder is ",g%h

if opcode > 4 and opcode < 1:
    print 'Invalid Selection'
