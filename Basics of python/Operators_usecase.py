# This covers the bisic understanding and practical implementatio of inputs, operators, string formating and type casting   
print("hi!,parva")
a=int(input("A ="))
b=int(input("B ="))
 
# Arithemetic operator 
sum=a+b #addition 

mul=a*b #Multyiplication

sub=a-b #subtraction

dev=a/b #Division

Mod= a%b #Modlous

Ex= a**b #Exponetiation

FD= a//b #Floor division 

# usiing the print function to see the output
print("addition of a and b is ",sum)
print("multiply of a and b is ",mul)
print("subtraction  of a and b is ",sub)
print("devide of a and b is ",dev)
print("Modulous of a and b is ",Ex)
print("Exponentional of a&b is",Ex)
print("Floor division of a&b is",FD)

#####################################################

#Comperision Operators is used to compare the two values which returns TRUE or FLASE
A=a==b
B=a!=b
C=a>b
D=a<b
E=a>=b
F=a<=b
print("when two operator is equal then a&b is",A)
print("when two operator is not equal a&b",B)
print("when two operator is grater then a, a&bis ",C)
print("when two operator is less then a&b is ",D)
print("when two operator is grater the or equal",E)
print("when two operator is less the or equal",F)

###########################################################

#Logical operaor

a=5
b=10
c=15
print(a<b and b<c)
print(a<b or b>c)
print(not(a<b and b<c))

#Idetity operator
print(a<b is b<c)
print(a<b is not b>c)


print("type of a is ",type(a))

#############################################

#1 using assignement operator
x=5
print(x)
#2  adding  `10` with the use of operators
x=5
x+=10
print(x)
#3 subtracting `2` using operstors
x=5
x-=2
print(x)
#4 multiplication operators
x=5
x*=4
print(x)
#5 division op
x=5
x/=6
print(x)
#6 floor division op
x=5
x//=2
print(x)
#7 Modlous op
x=5
x%=6
print(x)
#8 Exponenational op
x=5
x**=8
print(x)
# using Bitwise operators.

#9 and (will return 1 if both are 1)op
x=5
x&=6
print(x)

#10 OR (Return 1 if either bit is 1 )op
x=5
x|=4
print(x)

#11 Return 1 if only one of the bit is 1 op
x=5
x^=12 
print(x)

# Inverts all the bits
x=5
~x= -12
print(x)

#12 Shift the bit to the left by n op
x=5
x<<=14
print(x)

#13 Shift the bit to the right by n op
x=5
x>>=10
print(x)
