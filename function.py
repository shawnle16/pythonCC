# def hello():
#     print("hello")
#     print("good morning")
#
# hello()
#
#
# def hello(name,age):
#     print("hello", name, age)
#     print("good morning", name, age)
#
#
# hello("Son","24")
#
#
# #arguments: * for tuple, ** for dictionary
#
# def max(a,b,c):
#   if (a>b) and (a>c):
#       print("a max")
#   elif (b>a) and (b>c):
#       print("b max")
#   else:
#       print("c max")
# (a,b,c)=(1,2,0)
# max(a,b,c)
#
# def sm(a,b):
#     print(a+b)
#
# sm(2,3)
#
# def greet(a,b,c):
#     print(a,b,c)
# #positional arguements
# greet(3,4,5)
# #keyword arguements
# greet(b=10,c='Son',a='Good morning')
# #default arguements
# def greet(a,b,c='Hello'):
#     print(a,b,c)
#
# greet(0,8)
#
# def greet(a,b,c,*args):
#     print(a,b,c)
#     for a in args:
#         print(a)
#
# greet(9,9,7,'GM','to','Son')
#
# def greet(a,b,c,*args):
#     print(a,b,c)
#     for a in args:
#         print(args)
#
# greet(9,9,7,'GM','to','Son')
#
# def book(a,b,**kwargs):
#     print(a,b)
#     for a in kwargs.items():
#         print(a)
#
# book(6,9,d=299,x='Hello')
#
#
#
#
