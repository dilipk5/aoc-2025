with open('input','r') as file:
    lines = [line.strip() for line in file]
    
blank = lines.index('')
freshIds = lines[:blank]
availIds = lines[blank + 1:] 
        
g = 0
for i in availIds:
    for j in freshIds:
        temp = j.split('-')
        if int(temp[0]) < int(i) < int(temp[1]):
            g = g + 1
            break    

print(g)