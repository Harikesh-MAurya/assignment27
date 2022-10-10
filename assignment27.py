# 1. Write a python script to create a ArithmeticError
# 2. Write a python script to create a ValueError
# 3. Write a python script to handle the ArithmeticError
# 4. Write a python script to handle a ValueError
# 5. Write a python script to handle multiple Exception in one try
# 6. Write a python script to create a calculator with 4 basic operations, and handle a
# maximum number of exceptions.
# 7. Write a python script to add a finally block for the above script
# 8. Write a python script to implement try except and else block for division
# 9. Write a python script to raise a ValueError.
# 10. Write a python script to implemented a nested Try Except block


# 1) .................................................... 
#def sum(a,b):
#     c=a/b
#     print(c)
# sum(10,0)

# 2) ................................
#
#def value(a):
#   x,y,z=(a)
#   print(x,y,z)

# value([1,2,3,4])

# 3) ....................................
# try:
#     def sum(a,b):
#         c=a/b
#         print(c)
# except ArithmeticError as e:
#     print("arthimatic error will occure",e)

# sum(10,0)

# 4) ......................................
# try:
#     def value(a):
#        x,y,z=(a)
#        print(x,y,z)
# except ArithmeticError as e:
#     print("arthimatic error will occure",e)

# value([1,2,3,4])

# 5) ..........................................
# try:
#     a=7
#     b=int(input("Enter b : "))
#     c=a/b
#     print(c)
       
# except ArithmeticError:
#     print("arthimatic error will occure")
# except ValueError:
#     print("valueerror error will occure")
# except TypeError:
#     print("typeerror error will occure")
# finally:
#     print("got final resoult")


# 6) .............................
# try:
#     def sum(a,b):
#         print(a+b)
 
#     def sub(a,b):
#         print(a-b)
    
#     def mul(a,b):
#         print(a*b)
    
#     def div(a,b):
#         print(a/b)   

# except ValueError:
#     print('value')
# except SyntaxError:
#     print('syntax')
# except ArithmeticError:
#     print('arithematic')
# finally:
#     print("got final")

# a,b=int(input('enter a : ')),int(input("enter b : "))
# sum(a,b)
# sub(a,b)
# mul(a,b)
# div(a,b)

