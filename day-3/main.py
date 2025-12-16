# intInps = [987654321111111,811111111111119,234234234234278,818181911112111]
# intInps= ['1342732443442344263423337324424434443443334244433443443334415443115424254244777424433734347323332332']

with open('inputs', 'r') as file:
    inps = [line.strip() for line in file]

def maxJolts(num):
    numArr = []
    for i in num:
        numArr.append(i)
    lnum = numArr[0]
    lpos  = 0
    rnum = 1
    for i in range(len(numArr)):
        if numArr[i] > lnum and i != len(numArr)-1:
            lnum = numArr[i]
            lpos = i 
    for i in range(lpos+1,len(numArr)):
        if int(numArr[i]) > int(rnum):
            rnum = numArr[i]
    return lnum + rnum
            
sum = 0

for i in inps:
    sum = sum + int(maxJolts(i))
    
print(sum)