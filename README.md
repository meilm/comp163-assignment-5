# Loop Design Documentation
## Challenge 1: Number Sequence Generator
I used an if/else statement to do different things if the number was currently even or odd
This statement is nested in a while loop, that executes until the value is 1.

## Challenge 2: Prime number checker
I used a for/else loop with a nested if statement.
The for loop is to repeat for each number in between 2 and the input.
The if statement checks if the input is divisible by the current number, and exits the loop if it is.
If the for loop never finds anything the number is divisible by, the else loop runs, which prints the fact that the input is prime.

## Challenge 3: Multiplication Table Grid
I used a for loop nested inside another for loop.
The outer for loop runs once for each row in the table, and prints which row we are on.
The inner for loop runs once for each number 1 through 10 for each row, mutiplying the numbers by the row number we are on. 
