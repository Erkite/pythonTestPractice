list = []
n =int(input("Enter the number of values: "))
for i in range(0,n):
    num = int(input("Enter a number: "))
    list.append(num)
print(list)
counter = 0
for x in list:
    if(x>list[0]):
        counter += 1
print(counter)