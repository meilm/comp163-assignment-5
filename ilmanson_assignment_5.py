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