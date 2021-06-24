# Python program to print positive Numbers in a list
list1 = [12 , -7 , 5 , 64 , -14]

# iterating each number in list
for num in list1:

    # checking condition
    if num >= 0:
       print(num, end = " ")

list1 = [12 , 14 ,-95 , 3]
num = 0

# using while loop
while (num < len(list1)):

    # checking condition
    if list1[num] >= 0:
        print(list1[num], end=" ")

    # increment num
    num += 1
