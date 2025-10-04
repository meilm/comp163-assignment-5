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
if step_count == 0:                         # stupid shit i have to do to match the zybooks whitespace
    print(int(n), 'Steps:', step_count) 
else:                                       # omit the newline before "Steps: " if the input is 1 because zybooks is stupid
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

print('\n=== Challenge 3: Multiplication Table ===')
print('Multiplication Table:')
row_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('   ', end='')
for item in row_values:
    if item < 10:                           # determine how many spaces to print to keep the table organized
        print('  ', item, end='') 
    else: print(' ', item, end='')
print()
for row in row_values:
    if row < 10:                            # same thing here
        print('', row, end=' ')
    else: print(row, end=' ') 
    for item in row_values: 
        current_value = item * row
        if current_value >= 100:            # and here, too
            print('', current_value, end='') 
        elif current_value >= 10:
            print(' ', current_value, end='')
        else: print('  ', current_value, end='') 
    print()