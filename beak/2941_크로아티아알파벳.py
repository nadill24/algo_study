calpa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

b = input()
a = []
for i in range(len(b)):
    a.append(b[i])

for i in range(0, len(a)-1):
    if a[i] == 'c':
        if a[i+1] == '=' or a[i+1] == '-':
            a[i] ='1'


    elif a[i] == 's':
        if a[i+1] == '=':
            a[i] = '1'


    elif a[i] == 'z':
        if a[i+1] == '=':
            a[i] = '1'


    elif a[i] == 'l':
        if a[i+1] == 'j':
            a[i] = '1'


    elif a[i] == 'n':
        if a[i+1] == 'j':
            a[i] = '1'


    elif a[i] == 'd':
        if a[i+1] == '-':
            a[i] = '1'


        if i < len(a)-2:
            if a[i] == 'd':
                if a[i + 1] == 'z':
                    if a[i + 2] == '=':
                        a[i] = '1'
                        a[i+1] = '1'


sum = len(a)
for i in range(len(a)):
    if a[i] == '1':
        sum -= 1

# print(a)
print(sum)

# 엄청 간단하네
a=input()
print(len(a)-a.count("=")-a.count("dz=")-a.count("-")-a.count("lj")-a.count("nj"))