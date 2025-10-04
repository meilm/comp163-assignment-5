print('=== Challenge 1: Collatz Conjecture ===')
n = int(input('Enter starting number: '))
print('Sequence: ', end='') 
step_count = 0
while n != 1:
    print(int(n), end=' ')
    if n % 2 == 0:
        n /= 2
    else:
        n *= 3
        n += 1
    step_count += 1
if step_count == 0: # stupid shit i have to do to match the zybooks whitespace
    print(int(n), 'Steps:', step_count) 
else: # omit the newline before "Steps:" if the input is 1 because zybooks is stupid
    print(int(n))
    print('Steps:', step_count)

print('\n=== Challenge 2: Prime Number Checker ===')
n = int(input('Enter a number: '))
print(f'Testing divisors from 2 to {n-1}...')
for divisor in range(2, n):
    if n % divisor == 0:
        print(f'{n} is not prime (divisible by {divisor})')
        break
else: print(n, 'is prime!')
