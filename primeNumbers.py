pNumbers = {2:2, 3:3, 5:5, 7:7, 11:11}

for i in range(2, 101):
    isPrime = True
    
    for prime in pNumbers.values():
        if i % prime == 0:
            isPrime = False
    
    if isPrime == True or i == pNumbers.get(i):
        print(i, end=" ")