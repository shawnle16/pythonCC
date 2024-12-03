# # x=5
# # y=1
# #
# # try:
# #     print(x/y)
# # except NameError as e:
# #     print("e")
# # except ZeroDivisionError as e1:
# #     print(e1)
# # except:
# #     print("loi khac")
# # else:
# #     print("Success")
# # finally:
# #     print("finish")
#
# # x=input("Nhap vao so a:")
# # y=input("Nhap vao so b:")
#
# # x= {"ga":"2 chan", "cho": "4 chan"}
# # y= ["xuan","ha","thu","dong"]
# #
# # try:
# #     print(y[5])
# # except NameError as e:
# #     print("e")
# # except ZeroDivisionError as e1:
# #     print(e1)
# # except TypeError:
# #     print("loi khac")
# # except KeyError:
# #     print("khong co gia tri")
# # except IndexError:
# #     print("Sai chi so")
# # else:
# #     print("Success")
# # finally:
# #     print("finish")
#
#
# # x=-1
# # if x<0:
# #     raise Exception ("lỗi")
#
# # x = {"car": "4 wheels", "bike": "2 wheels", "man": "2 feet"}
#
# # try:
# #     print(x[4])
# # except NameError as nameE:
# #     print(nameE)
# # except ZeroDivisionError as zeroD:
# #     print(zeroD)
# # except TypeError as typeE:
# #     print(typeE)
# # except KeyError as keyE:
# #     print(keyE)
# # else:
# #     print("Success")
# # finally:
# #     print("close")
#
# # x=6
# # y='nha'
# #
# # try:
# #     print(x/y)
# # except ValueError:
# #     print("loi")
#
# def open_file(filename):
#     try:
#         with open('abc.py', 'r') as file:
#             contents = file.read()
#             print(f"Contents of {'abc.py'}:")
#             print(contents)
#     except FileNotFoundError:
#         print(f"Error: File '{'abc.py'}' not found.")