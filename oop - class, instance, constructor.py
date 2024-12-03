# class Car():
#     pass
#
# BMW = Car()
# BMW.xuatxu="Ger"
# BMW.nam="1990"
#
# print(f'Nationalitity is {BMW.xuatxu}, year is {BMW.nam}')
#
# #hàm __init__() được gọi bất cứ khi nào khởi tạo một đối tượng, một biến mới trong class và được gọi là constructor trong lập trình hướng đối tượng.
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# #self: nhận giá trị chính đối tượng đã gọi hàm đó
#
# # Creating an instance of the Person class
# person1 = Person("Alice", 30)
# print(person1.name)
# print(person1.age)
#
# class Country:
#     def __init__(self, continent, ranking):
#         self.continent = continent #khai báo biến
#         self.ranking = ranking
#     def continent(self):
#         return self.continent
#
# Asian=Country('Asia',2)
# print(Asian.continent, Asian.ranking)
#
# class House:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def name(self):
#         return self.name
#
# amn= House('Son',20)
# print(f'My name is {amn.name} and I am {amn.age}')