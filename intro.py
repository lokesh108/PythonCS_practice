# Print Welcome Message
print('Hello World')

# WE learn how to print the sting and how does a command works

message='Hello Lokesh'

print(message)


# escape sequence

# Using ' 
# USing "
# Multiline string """ """

message="Hi this is lokesh's Macbook"
print(message)
message=' Really("")'
print(message)
message='Hi this is lokesh\'s Macbook'
print(message)
message="""This is
an example of
multiline comment"""
print(message)

#Function
 #Len function

print(len(message))
print(message[:39])
print(message[0:])
print(message[0:5])
print(message.upper())
print(message.lower())
print(message.title())
print(message.count("i"))
print(message.find('i'))
message=message.replace('comment','Statement')
print(message)

greeting='Hi'
name='Lokesh'
country='India'
print(f'Hi {name},How is everone at {country}')


# Numeric data in python
'''
Addition
Subtraction
Multiplication
Division
Floor Division
Exponent
Modulus
parathesis
'''
num_1=3
num_2=2

print(num_1+num_2)
print(num_1-num_2)
print(num_1*num_2)
print(num_1/num_2)
print(num_1//num_2)
print(num_1**num_2)
print(num_1%num_2)

print(3*2-3+4)
print((3*2)-3+4)

#Comparison Operator
'''
==
!=
>=
<=
>
<
'''
print(num_1==num_2)
print(num_1!=num_2)
print(num_1>=num_2)
print(num_1<=num_2)
print(num_1>num_2)
print(num_1<num_2)
