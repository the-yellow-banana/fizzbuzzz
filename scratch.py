import numpy
randomnums= numpy.random.randint(1, 1000, 100)
def fizzbuzz(some_nums):
    for i in some_nums:
            if i%3==0 and i%5==0:
                print("fizzbuzz")
            elif i%3==0:
                print("fizz")
            elif i%5==0:
                print("buzz")
            else:
                print(i)
fizzbuzz(randomnums)
