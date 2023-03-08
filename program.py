x = range (1, 33)
for numbers in x:

  if numbers % 3 == 0 and numbers % 5 == 0: 
    print(numbers,"Fizzbuzz")

  elif numbers % 3 == 0: 
    print(numbers, "Fizz") 

  elif numbers % 5 == 0: 
    print(numbers, "Buzz") 
  
  else:
    print(numbers)
