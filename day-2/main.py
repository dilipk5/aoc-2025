# ids = ['11-22','95-115','998-1012','1188511880-1188511890','222220-222224','1698522-1698528','38593856-38593862','446443-446449']
invalidids = []

with open('inputs', 'r') as file:
    for line in file:
        print(line)
        ids = line.split(',')

def vaildIdChecker(fid,lid):
    # print(fid,lid)
    for i in range(int(fid),int(lid)):
        # print("fid and lid",fid,lid)
        i = str(i)
        if (len(i) % 2 == 0):
            for j in range(0,len(str(i))+1):
                if i[:int(len(i)/2)] == i[int(len(i)/2):len(i)]:
                    print('bingo', i)
                    if i not in invalidids:
                        invalidids.append(i)
                    break
                    
        i = int(i)
        i = + 1
                        

for id in ids:
    idarr = id.split('-')
    fid = idarr[0]
    lid = idarr[1]
    vaildIdChecker(fid,lid)

# print(invalidids)


sum = 0 
for i in invalidids:
    # print(i,sum)
    sum = sum + int(i)
    
print(sum)