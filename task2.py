mylist1 = [1,2,3,4,5]
mylist2 = [5,4,3,2,1]
print(zip(mylist1, mylist2))
sum = 0
for i in zip(mylist1, mylist2):
    sum += ((i[0] * i[1]))
print(sum)

