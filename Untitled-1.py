
import math
import string

first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")

print("Hello", first_name.upper(),last_name.lower())
print("")
print("")
name = str(first_name + " " + last_name)

slc = name[:]
print(slc)
slc = slc.replace(last_name,last_name + " Welsh College Student")
print(slc)

print(" \"Start by doing what's necessary; then do what's possible; and suddenly you are doing the impossible - Francis of Assisi \" ")

x = float(input("Enter a decmial number: "))
y = float(input("Enter a decmial number: "))
sub = x-y
add = x+y
div = x/y
mlt = x*y

print(x,"plus",y,"equals",add)
print(x,"minus" ,y ,"equals", sub)
print(f"{x} times {y} equals {mlt}")
print("%s divided by %s equals %s"%(x,y,div))

sqrt_root = round(math.sqrt(mlt),2)
print(sqrt_root)

month = str("october")
day = int(5)
print("")
print("\t\t Today is day of",day,"of the month of",month)