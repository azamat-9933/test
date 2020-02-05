# a = open("aaa.txt", "w")
#  b = a.read()
# a.write("hello")
# # print(b)
# a.close()


# a = open("aaa.txt", "r")
# b = a.read()
# a.write("hello")
# print(b)
# a.close()



a = open("aaa.txt", "r")
for i in a:
    print(i)
    break
d = int(input('d ni kiriting : '))
if d == 1:
    a = open('aaa.txt').read().split('\n')[1]
    print(a)
    

# a.close()

# a.write("hello")

# a = open('aaa.txt').read().split('\n')[1]
# print(a)