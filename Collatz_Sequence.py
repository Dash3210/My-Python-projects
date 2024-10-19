#Collatz Sequence by Dash321
import time

print('''Collatz sequence is the simplest problem in mathematics
      So if you give this program a positive natural number, it checks:
      if n is even then it diveds the number by 2.
      if n is odd then it multiples the number by three and adds 1.
      if n is 1, program stops.''')

while True:#Asking for a valid number.
    response = input('Enter a number greater than 0:')
    if not response.isdecimal() or int(response) < 1:
        continue #Repeat until valid response.
    else:
        break #Valid response.

n = int(response)
Sequence = [n]
while n != 1:
    if n % 2 == 0: #If n is even number.
        n = n//2
        Sequence.append(str(n))
    else: #Otherwise n is odd number.
        n = (3*n + 1)
        Sequence.append(str(n))

for i in Sequence: #Printing answer
    if i == '1': #Last digit
        print(i, flush = True)
        break
    else:
        print(i, end=', ', flush = True)

    time.sleep(0.05)

print(len(Sequence))
