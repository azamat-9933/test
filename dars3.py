"""
a = 0
while 10 > a:
    b = int(input("sonni kiriting : "))
    print(a)
    a = a + b
    print(a)
    if a == 5:
        print(a)
        break
print(' вы вышли из кода ')
"""
a = 0

while 10 > a:
    b = int(input('sonni kiriting : '))
    print(a)
    a = a + b
    if a == 5:
        print(a)
        continue
    print('abc')
print(' вы вышли из кода ')