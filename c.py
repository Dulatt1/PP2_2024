# программа которая выводит
# только четные из списка с помощью генератора

def onlyEvens(list_of_nums):
    for i in list_of_nums:
        if(i % 2 == 0):
            yield i

mylist = [16,32,432,343,3,5,8768,4,23,45,6,7,8,1,3,4,35,6,6587,68]

for num in onlyEvens(mylist):
    print(num, end = " ")