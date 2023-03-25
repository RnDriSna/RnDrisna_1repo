try:
    file = open('data/app.conf', 'r')
    line = file.readline()
    linecheck = line.split(" ")
    linecheck[2] = linecheck[2].replace('\n', '')
except:
    flag = False

if 'linecheck' in vars():
    if len(linecheck) == 3:
        for num in linecheck:
            if num.isdigit():
                flag = True
            else:
                flag = False
                break
if flag == False:
    print('the file could not be opened')
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    with open('data/app.conf', 'w+') as conf:
        ast = str(a)
        bst = str(b)
        cst = str(c)
        conf.write(ast)
        conf.write(' ')
        conf.write(bst)
        conf.write(' ')
        conf.write(cst)

elif flag == True:
    a, b, c = line.split(" ")
    a, b, c = int(a), int(b), int(c)

print(a, b, c)
arr = []
for i in range(a):
    arr.append(b*i + c)

print(arr)
strrr = str(arr)
with open('data/result.dat', 'w+') as result:
    result.write(strrr)

