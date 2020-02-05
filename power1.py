a = [51,545,545,1,8,8,52,152]

def DeleteFromList(a):
    for i in a:
        if a[i] % 2 == 1:
            a.remove(a[i])
            print('List after removing : ', a)
        else:
            a[i] / 2
            print(a)
    return a

c = DeleteFromList(a)




