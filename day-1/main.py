with open('inputs', 'r') as file:
    inputs = [line.strip() for line in file]

currentDail = 50

def transformer(num):
    num = int(num)

def leftSide(num):
    if num > currentDail:
        diff = num - currentDail
        rtn = 100 - diff
        return rtn
    else:
        rtn = currentDail - num
        return rtn

def rightSide(num):
    tmp = currentDail + num
    if tmp > 99:
        diff = tmp - 100
        return diff
    else:
        return currentDail + num

# inputs = ['L68','L30','R48','L5','R60','L55','L1','L99','R14','L82']

# inputs=['L428']

ans = 0

for i in inputs:
    if i[0] == 'L':
        cnumber = i[1:len(i)]
        if int(cnumber) > 100:
            cnumber = cnumber[1:len(cnumber)]
            
        cnumber = int(cnumber)
        currentDail = leftSide(cnumber)
        if currentDail == 0:
            ans = ans + 1
        # print(currentDail)
    else:
        cnumber = i[1:len(i)]
        if int(cnumber) > 100:
            cnumber = cnumber[1:len(cnumber)]
            
        cnumber = int(cnumber)
        currentDail = rightSide(cnumber)
        if currentDail == 0:
            ans = ans + 1
        # print(currentDail)

print(ans)