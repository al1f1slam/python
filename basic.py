print("Hello World!")

#Variable
a = 10
b = 5
c = a+b
print(c)

name = "Alif Islam Siam"
info = "Address: Dhaka, Edu: CSE"
print(name, info)

#take input from keyboard
firstNum = 10
secondNum = input("Enter a number")

print("Sum:",firstNum+ int(secondNum))

#Conditional statement
age = input("Enter your age: ")

if int(age) >= 30:
    print("Senior")
else:
    print("Junior")

#loop
for i in range(5):
  print(i)

for i in range(1, 6, 2): #odd number print
  print(i)

for i in range(0, 6, 2): #Even number print
  print(i)

sum = 0
for i in range(1, 100):
  sum = sum + 1
  print(sum)

#odd number add between 1 to 100
sum = 0
for i in range(1, 100):
  if i%2 == 0:
    continue
  else:
    sum = sum + i

print(sum)

#Even number add between 1 to 100
sum = 0
for i in range(1, 100):
  if i%2 != 0:
    continue
  else:
    sum = sum + i

print(sum)
