x1 = int(input('x1 ni kiriting : '))
y1 = int(input('y1 ni kiriting : '))
x2 = int(input('x2 ni kiriting : '))
y2 = int(input('y2 ni kiriting : '))


# (x1, y1) va (x2, y2) orsidagi masofa topilsin
# xy bu nuqtalar orasidagi masofa

xy = (((x2 - x1)** 2) + ((y2 - y1) ** 2)) ** 0.5

print(xy)