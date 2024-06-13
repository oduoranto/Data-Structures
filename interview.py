print ("Welcome")

numbers = [1,3,5,0,9,9,8,20,200]

for num in numbers:
    if  num == 0:
      numbers.remove(num)
      numbers.append(num)


print(numbers)      



names = ["Antony", "John", "Davis"]

for name in names:
   if name == "John":
      names.remove(name)
      names.append(name)


print(names)      
