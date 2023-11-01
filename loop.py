numbers=[1,2,3,4,5,6,7,8,9,10]
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)
for number in numbers:
    if number % 2==2:
        print("The numbers are even")
    elif number==3:
        print ("All are present")