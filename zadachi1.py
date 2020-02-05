

"""
a = [51,545,545,1,8,8,52,152]
b = []
def DeleteFromList(a):
    for i in a:
        if i % 2 == 1:
            a.remove(i)
            print('List after removing : ',)
        else:
            d = i / 2
            b.append(d)
            print(b)
    return a

c = DeleteFromList(a)
"""

# Spisok beril lyuboy 3, 6, 9 , 12; shu spisokki har 3 ta elementini olib summasini boshqa beriladigan o'zgaruvchiga kopaytirib yeng ispisokka append qberishi kerede.
# spisokki spisok holatida ciqarib berishi kere.
# telebotapi da sonla kiritaman 0 kiritgandan keyin spisok holaida print qberish kere.

# a = []
# while True:
#     dd = int(input())
#     a.append(dd)
#     print(a)
# c = []
# def new_func(list, abc):
#     b = 0
#     a = 0
#     for el in list:
#         if a != 3:
#             b = b + el
#             a = a + 1
#         if a == 3:
#             a = 0
#             c.append(b)
#             b = 0
#     print(c)

# new_func(a, c)

# a = [51,545,545,1,8,8,52,152]

# dd = sum(a[3:])

# print(dd)

# a = [51,545,545,1,8,8,52,152]

# dd = sum(a[:3])

# print(dd)
p =[]
a = [51,545,545,1,8,8,52,152,143]
b = sum(a[:3])
print(b)
p.append(b)
print(p)

# c = sum(a[])
# print(c)
# p.append(b)


