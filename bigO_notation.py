#Time complexity
def get_squared_Numbers(numbers):
    squared_numbers = []
    for n in numbers :
        squared_numbers.append(n * n)
    return squared_numbers

numbers = [2,5,7,9]
ans = get_squared_Numbers(numbers)
print(ans)    

# trying to find a duplicate number from a list

numb_1 = [3,6,2,3,8, 7, 2, 4]

for i in range(len(numb_1)):
    for j in range(i +1 , len(numb_1)):
        if(numb_1[i] == numb_1[j]):
            print(f"{numb_1[i]} is a duplicate")

for p in range( 0 +1,len(numb_1)):
 print (p)
                 
