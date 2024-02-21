# primeInPython
prime numbers from 2 to 100 in python

## Program made in Python 3

this is the code, if you want to learn more of python go to their website [here](https://www.python.org/).

This is the code:

```
pNumbers = {2:2, 3:3, 5:5, 7:7, 11:11}

for i in range(2, 101):
    isPrime = True
    
    for prime in pNumbers.values():
        if i % prime == 0:
            isPrime = False
    
    if isPrime == True or i == pNumbers.get(i):
        print(i, end=" ")
        
print("\n\nEnd of the program.")
```
