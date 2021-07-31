"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

NOTE: this is done using file with primes from '7. 10001st prime'
"""
sum_of_primes = 0

with open('primes.txt') as file:
    data = file.readlines()

    for line in data:

        print(line)
        prime = int(line.split(',')[1])
        if prime > 2000000:
            break
        sum_of_primes += prime

    print(sum_of_primes)
