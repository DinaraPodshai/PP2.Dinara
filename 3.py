##Function

# def my_function():
#   print("Hello from a function")


# def my_function(fname):
#   print(fname + " Refsnes")
# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# def my_function(fname, lname):
#   print(fname + " " + lname)
# my_function("Emil", "Refsnes")

# def my_function(*kids):
#   print("The youngest child is " + kids[2])
# my_function("Emil", "Tobias", "Linus")

# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)
# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# def my_function(country = "Norway"):
#   print("I am from " + country)
# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# def my_function(food):
#   for x in food:
#     print(x)
# fruits = ["apple", "banana", "cherry"]
# my_function(fruits)

# def my_function(x):
#   return 5 * x
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

# def my_function(a, b, /, *, c, d):
#   print(a + b + c + d)
# my_function(5, 6, c = 7, d = 8)

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result
# print("Recursion Example Results:")
# tri_recursion(6)


##Python Lambda

# x = lambda a: a + 10
# print(x(5))

# x = lambda a, b: a * b
# print(x(5, 6))

# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))

# def myfunc(n):
#   return lambda a : a * n
# mydoubler = myfunc(2)
# print(mydoubler(11))

# def myfunc(n):
#   return lambda a : a * n
# mydoubler = myfunc(2)
# mytripler = myfunc(3)
# print(mydoubler(11))
# print(mytripler(11))


##Python Arrays

# cars = ["Ford", "Volvo", "BMW"]
# x = cars[0]
# print(x)
# cars[0] = "Toyota"
# print(cars)
# x = len(cars)
# print(x)
# for x in cars:
#   print(x)
# cars.append("Honda")
# print(cars)
# cars.pop(1) ##-2
# print(cars)
# cars.remove("Volvo") ##zab
# print(cars)

# append()	Добавляет элемент в конец списка
# clear()	Удаляет все элементы из списка
# copy()	Возвращает копию списка
# count()	Возвращает количество элементов с указанным значением
# extend()	Добавляет элементы другого списка (или итерируемого объекта) в конец текущего списка
# index()	Возвращает индекс (позицию) первого элемента с указанным значением
# insert()	Вставляет элемент в указанную позицию
# pop()	Удаляет элемент из списка по указанной позиции (по умолчанию — последний элемент)
# remove()	Удаляет первое вхождение элемента с указанным значением
# reverse()	Разворачивает порядок элементов списка (наоборот)
# sort()	Сортирует список по возрастанию (или с параметром reverse=True — по убыванию


#Object-Oriented Programming
# Class	   Objects
#Fruit	   Apple, Banana, Mango
#Car	       Volvo, Audi, Toyota

#Classes and Objects

# class MyClass:
#   x = 5
# p1 = MyClass()
# print(p1.x)

# class Person:
#   def __init__(self, name, age):  ##self — это ссылка на текущий объект. параметры
#     self.name = name
#     self.age = age
# p1 = Person("John", 36)
# print(p1.name)
# print(p1.age)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def myfunc(self):
#     print("Hello my name is " + self.name)
# p1 = Person("John", 36)
# p1.myfunc()

# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age
#   def myfunc(abc):
#     print("Hello my name is " + abc.name)
# p1 = Person("John", 36)
# p1.myfunc()


#Python Inheritance - унаследовать свойства и методы другого класса (родительского/базового)

class Person:
  def __init__(self, fname, lname): ##Позволяет задать начальные значения
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  pass
x = Student("Mike", "Olsen")
x.printname()


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
x = Student("Mike", "Olsen")
x.printname()


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
x = Student("Mike", "Olsen")
x.printname()


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
x = Student("Mike", "Olsen")
print(x.graduationyear)



class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
x = Student("Mike", "Olsen", 2024)
x.welcome()