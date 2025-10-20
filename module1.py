#EX 1
num = int(input("Enter a number: "))
if (num % 2) == 0:
    print("{} is Even".format(num))
else:
    print("{} is Odd".format(num))

#EX 2
a = (0 == True)
b = (False == False)
c = (True + True)
d = (False + 9)

print("a is", a)
print("b is", b)
print("c:", c)
print("d:", d)

#EX 3
print('T')
print('a')

#EX 4
a = int(input("Enter the real part: "))
b = int(input("Enter the imaginary part: "))

x = complex(a, b)

print("Complex number:", x)
print("Real part:", x.real)
print("Imaginary part:", x.imag)

#EX 5
men_stepped_on_the_moon = input("Enter a string: ")
print(men_stepped_on_the_moon)