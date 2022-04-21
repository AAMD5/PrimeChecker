def isPrime(num):
    
    lst = [] # list containing all the numbers <= num
    for i in range(1, num+1):
        lst.append(i)
    
    divisors = [] # list containing all numbers that divide into num without a remainder       
    for i in range(len(lst)):
        if num % lst[i] == 0:
            divisors.append(lst[i])
            
    if len(divisors) == 2: # A prime number will have only two divisors, 1 and itself
        print("The number " + str(num) + " is prime!")
    
    else:
        print("The number " + str(num) + " is not prime!")
    
    return ("The divisors of your number are ") + str(divisors)

print(isPrime(646)) 