import csv
list=[]
with open('ks-projects-201612.csv', 'r') as f:
    for index in f.__iter__():
        str = index.split(',')
        if len(str)== 13:
            list.append(str)

print(len(list))
list2 = []
for line in list:
    if len(line)!= 13:
        list2.append(line)
print(len(list2))


csvfile = open('kickclenaed.csv','w',newline='')
obj=csv.writer(csvfile)
for line in list:
    obj.writerow(line)
csvfile.close()
