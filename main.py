inpt = int(input("Enter number to end: "))
primes = [2, 3]

for numb in range(4, inpt + 1):
    is_prime = True
    for divisor in range(2, int(numb ** 0.5) + 1):
        if numb % divisor == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(numb)

print(primes)