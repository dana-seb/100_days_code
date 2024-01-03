# ask user for number from 1 to 100
# number = int(input("Enter a number 1 to 100 and see if it is a prime number? "))

# My version
# agg = []
# for x in range(1, 101):
#     if (number % x) == 0:
#        agg.append(x)
# # print(agg)
# if len(agg) > 2:
#     print(f"{number} is a not prime number.")
# else:
#     print(f"{number} is a prime number.")  

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"{number} is prime")
    else:
        print(f"{number} is not a prime")

prime_checker(4)