a = int(input('massani kiriting:'))
b = int(input('boyingizni kiriting:'))

c = a/ b ** 2

d = c * 10000
print(c)
print(d)

if d <= 18:
    print('below normal weight')
if d > 18 and d < 25:
    print('normal weight')
if d > 25:
    print('overweight')

