#2)
#i=1
#while i<=50: #цикл, который работает, пока условие `i <= 50` истинно
#    print(i)
#    i+=1

#1)
#i=2
#while i<=20:
#    print(i)
#    i+=2

#3)
#i = ""

#while i != "admin123":
 #   i = input("password: ")
 #   if i != "admin123":
  #      print("NO")

#print("YES")


#for i in range(1,10):  #Цикл for перебирает числа от 1 до 9.
#    print(f"{i}")

#for i in range(1, 11):
#    print(f"{i}*{i}={i*i}")

#fruits = ["apple", "banana", "cherry"]
#for x in fruits:
#    print(x)

#list=[1,2,3,4,5]
#maxi=max(list)
#mini=min(list)
#print(maxi,mini)

#list=['a','b','c']
#list[1]='n'  #Меняет элемент с индексом 1 ('b') на 'n'.
#print(list)

#list=['Aman','Ayana','Nur','Dana','Asem']
#for name in list:
#    if name.startswith("A"):  #Печатает имена, начинающиеся на "A".
#        print(name)


#Python Booleans:

#a = 200
#b = 33
#if b > a:
#  print("b is greater than a")
#else:
#  print("b is not greater than a")


#x = "Hello"
#y = 15
#print(bool(x))
#print(bool(y)) #Любая непустая строка или число → `True`


#def myFunction() :
#  return False
#if myFunction():
#  print("YES!")
#else:
#  print("NO!")

#x = 200
#print(isinstance(x, int)) #-определения, относится ли объект к определенному типу данных:


#Python Operators

#=	x = 5	x = 5	
#+=	x += 3	x = x + 3	
#-=	x -= 3	x = x - 3	
#*=	x *= 3	x = x * 3	
#/=	x /= 3	x = x / 3	
#%=	x %= 3	x = x % 3	- не хватает
#//=	x //= 3	x = x // 3	- калдык
#**=	x **= 3	x = x ** 3	- дареже
#&=	x &= 3	x = x & 3	-and
#|=	x |= 3	x = x | 3	-or
#^=	x ^= 3	x = x ^ 3	-xor
#>>=	x >>= 3	x = x >> 3	-not
#<<=	x <<= 3	x = x << 3	-	Zero fill left shift
#:=	print(x := 3)	x = 3 print(x) -Signed right shift

#print(100 + 5 * 3)


#Python Lists

#thislist = ["apple", "banana", "cherry"]
#print(thislist)

#thislist = ["apple", "banana", "cherry"]
#print(len(thislist)) #-сколько

#mylist = ["apple", "banana", "cherry"]
#print(type(mylist)) 

#thislist = ["apple", "banana", "cherry"]
#print(thislist[-1])

#thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#print(thislist[2:5]) #This will return the items from position 2 to 5.
#print(thislist[:4])
#print(thislist[2:])
#print(thislist[-4:-1])

#thislist = ["apple", "banana", "cherry"]
#if "apple" in thislist:
#  print("Yes, 'apple' is in the fruits list")
#thislist[1] = "blackcurrant"
#print(thislist)
#thislist[1:3] = ["blackcurrant", "watermelon"]
#print(thislist)
#thislist[1:2] = ["blackcurrant", "watermelon"]
#print(thislist)
#thislist[1:3] = ["watermelon"]
#print(thislist)
#thislist.insert(2, "watermelon")
#print(thislist) 
#thislist.append("orange")
#print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical) #-добав
# print(thislist)
# thislist.remove("banana") -удал
# print(thislist)
# thislist.pop() #che
# print(thislist)
# del thislist[0]
# print(thislist) #app
# thislist.clear()
# print(thislist) #[]


# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i]) #по порядку

# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1

# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

