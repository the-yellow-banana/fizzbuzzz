import numpy

firstnum= int(input("Put your first number to check for here:"))
secondnum= int(input("Put your second number to check for here:"))
randomnums= numpy.random.randint(1, 1000, 100)

def fizzbuzz(some_nums):
    for i in some_nums:
            if i%firstnum==0 and i%secondnum==0:
                print("fizzbuzz")
            elif i%firstnum==0:
                print("fizz")
            elif i%secondnum==0:
                print("buzz")
            else:
                print(i)
fizzbuzz(randomnums)
