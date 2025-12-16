# ids = ['11-22','95-115','998-1012','1188511880-1188511890','222220-222224','1698522-1698528','38593856-38593862','446443-446449']


with open('inputs', 'r') as file:
    for line in file:
        print(line)
        ids = line.split(',')
        # ids.append(line.split(',')) 


print(ids)
# print(ids2)

# for id in ids:
#     idarr = id.split('-')
#     fid = idarr[0]
#     lid = idarr[1]
#     # print(fid,lid)