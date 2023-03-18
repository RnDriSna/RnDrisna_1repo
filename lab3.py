try:
    file = open('docs/app.conf', 'r')
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
elif flag == True:
    a, b, c = line.split(" ")
    a, b, c = int(a), int(b), int(c)

print(a, b, c)
arr = []
for i in range(a):
    arr.append(b*i + c)

print(arr)
strrr = str(arr)
with open('docs/result.dat', 'w') as result:
    result.write(strrr)

